"""
Multi-Model Law-to-Rules Swarm - Kimi + MiniMax Only
Supports Kimi K2 and MiniMax M2.5 (no Claude required)
"""

import os
from typing import Optional, Dict, Any
from langchain_openai import ChatOpenAI


class ModelRouter:
    """Routes agents to Kimi K2 and MiniMax M2.5 based on task requirements"""
    
    MODEL_CONFIGS = {
        "kimi-k2": {
            "provider": "moonshot",
            "model": "kimi-k2.5",
            "api_base": "https://api.moonshot.cn/v1",
            "strengths": ["long_context", "finnish_language", "document_analysis", "legal_reasoning"],
            "best_for": ["law_reader", "legal_analyst", "validator", "gap_analyzer"]
        },
        "minimax-m2.5": {
            "provider": "minimax",
            "model": "MiniMax-M2.5",
            "api_base": "https://api.minimax.chat/v1",
            "strengths": ["speed", "cost_efficiency", "pattern_matching", "structured_output"],
            "best_for": ["rule_extractor", "formatter"]
        }
    }
    
    def __init__(self, available_models: Optional[list] = None):
        """
        Initialize router with available models.
        
        Args:
            available_models: List of available model names. If None, uses all configured models.
        """
        self.llm_cache = {}
        self.available_models = available_models or list(self.MODEL_CONFIGS.keys())
        
        # Validate that all requested models are configured
        for model in self.available_models:
            if model not in self.MODEL_CONFIGS:
                raise ValueError(f"Unknown model: {model}. Available: {list(self.MODEL_CONFIGS.keys())}")
    
    def get_llm(self, model_name: str, temperature: float = 0.2) -> Any:
        """Get or create LLM instance"""
        if model_name not in self.available_models:
            raise ValueError(f"Model {model_name} not in available models: {self.available_models}")
        
        cache_key = f"{model_name}_{temperature}"
        
        if cache_key in self.llm_cache:
            return self.llm_cache[cache_key]
        
        config = self.MODEL_CONFIGS.get(model_name)
        llm = self._create_llm(config, temperature)
        self.llm_cache[cache_key] = llm
        return llm
    
    def _create_llm(self, config: Dict, temperature: float) -> Any:
        """Create LLM instance based on provider"""
        provider = config["provider"]
        
        if provider == "moonshot":
            # Kimi K2 via OpenAI-compatible API
            api_key = os.getenv("MOONSHOT_API_KEY")
            if not api_key:
                raise ValueError("MOONSHOT_API_KEY not set in environment")
            
            return ChatOpenAI(
                model=config["model"],
                temperature=temperature,
                api_key=api_key,
                base_url=config.get("api_base")
            )
        
        elif provider == "minimax":
            # MiniMax M2.5 via OpenAI-compatible API
            api_key = os.getenv("MINIMAX_API_KEY")
            if not api_key:
                raise ValueError("MINIMAX_API_KEY not set in environment")
            
            return ChatOpenAI(
                model=config["model"],
                temperature=temperature,
                api_key=api_key,
                base_url=config.get("api_base")
            )
        
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    def recommend_model(self, agent_role: str) -> str:
        """Recommend best model for agent role from available models"""
        # First try to find exact match in best_for
        for model_name in self.available_models:
            config = self.MODEL_CONFIGS[model_name]
            if agent_role.lower() in [r.lower() for r in config["best_for"]]:
                return model_name
        
        # Default to first available model (Kimi K2 preferred for complex tasks)
        if "kimi-k2" in self.available_models:
            return "kimi-k2"
        return self.available_models[0]
    
    def get_model_info(self, model_name: str) -> Dict:
        """Get information about a model"""
        return self.MODEL_CONFIGS.get(model_name, {})
    
    def list_available_models(self) -> list:
        """List all available models"""
        return self.available_models


# ============================================================================
# ENSEMBLE APPROACH - Kimi + MiniMax vote on critical decisions
# ============================================================================

class EnsembleValidator:
    """Uses Kimi and MiniMax to validate critical rules"""
    
    def __init__(self, router: ModelRouter):
        self.router = router
        # Only use available models
        self.models = [m for m in ["kimi-k2", "minimax-m2.5"] if m in router.available_models]
    
    def validate_rule(self, rule: Dict, section_text: str) -> Dict:
        """Get consensus from available models on rule validity"""
        import json
        
        votes = []
        
        for model_name in self.models:
            try:
                llm = self.router.get_llm(model_name, temperature=0.1)
                
                prompt = f"""Validate this business rule against the source law section.
                
                Rule: {json.dumps(rule, ensure_ascii=False)}
                
                Source Law: {section_text[:1000]}
                
                Respond with JSON:
                {{
                    "valid": true/false,
                    "confidence": 0-1,
                    "issues": ["list any issues"],
                    "suggestions": ["improvements if any"]
                }}
                """
                
                response = llm.invoke(prompt)
                votes.append({
                    "model": model_name,
                    "response": response.content
                })
                
            except Exception as e:
                votes.append({
                    "model": model_name,
                    "error": str(e)
                })
        
        return self._aggregate_votes(votes)
    
    def _aggregate_votes(self, votes: list) -> Dict:
        """Aggregate votes from multiple models"""
        valid_votes = [v for v in votes if "error" not in v]
        
        if not valid_votes:
            return {"consensus": "error", "votes": votes}
        
        # With 2 models, both must agree for consensus
        if len(valid_votes) >= 2:
            return {
                "consensus": "validated",
                "vote_count": len(valid_votes),
                "votes": votes
            }
        else:
            return {
                "consensus": "uncertain",
                "vote_count": len(valid_votes),
                "votes": votes
            }


# ============================================================================
# FALLBACK CHAIN - If primary model fails, try alternative
# ============================================================================

class FallbackChain:
    """Chain of models to try if primary fails (Kimi preferred, MiniMax fallback)"""
    
    def __init__(self, router: ModelRouter):
        self.router = router
        # Prefer Kimi for quality, fallback to MiniMax for speed/cost
        self.fallback_order = [m for m in ["kimi-k2", "minimax-m2.5"] 
                               if m in router.available_models]
    
    def invoke_with_fallback(self, prompt: str, temperature: float = 0.2) -> Dict:
        """Try models in order until one succeeds"""
        errors = []
        
        for model_name in self.fallback_order:
            try:
                llm = self.router.get_llm(model_name, temperature)
                response = llm.invoke(prompt)
                
                return {
                    "success": True,
                    "model_used": model_name,
                    "response": response.content,
                    "errors": errors
                }
                
            except Exception as e:
                errors.append({"model": model_name, "error": str(e)})
                continue
        
        return {
            "success": False,
            "errors": errors
        }


# ============================================================================
# COST-OPTIMIZED ROUTING - Use cheaper models where appropriate
# ============================================================================

class CostOptimizer:
    """Optimize model selection based on task complexity"""
    
    COST_PER_1K_TOKENS = {
        "kimi-k2": 0.002,      # $2/1M tokens (estimated)
        "minimax-m2.5": 0.001  # $1/1M tokens (estimated)
    }
    
    def __init__(self, router: ModelRouter):
        self.router = router
    
    def select_model(self, task_complexity: str, required_accuracy: float) -> str:
        """Select most cost-effective model for task from available models"""
        available = self.router.available_models
        
        if required_accuracy > 0.90 and "kimi-k2" in available:
            # High accuracy needed - use Kimi
            return "kimi-k2"
        
        elif task_complexity == "simple" and "minimax-m2.5" in available:
            # Simple task - use cheaper MiniMax
            return "minimax-m2.5"
        
        elif "kimi-k2" in available:
            # Default to Kimi for quality
            return "kimi-k2"
        
        else:
            # Fallback to whatever is available
            return available[0]
    
    def estimate_cost(self, model_name: str, input_tokens: int, output_tokens: int) -> float:
        """Estimate cost for a request"""
        cost_per_1k = self.COST_PER_1K_TOKENS.get(model_name, 0.002)
        total_tokens = input_tokens + output_tokens
        return (total_tokens / 1000) * cost_per_1k


# ============================================================================
# UPDATED AGENT CREATION - Kimi + MiniMax Only
# ============================================================================

def create_law_reader_agent_multi(router: ModelRouter) -> tuple:
    """Create Law Reader agent - uses Kimi K2"""
    from swarm import create_law_reader_agent
    
    # Kimi K2 for document analysis and Finnish language
    recommended = "kimi-k2" if "kimi-k2" in router.available_models else router.available_models[0]
    llm = router.get_llm(recommended, temperature=0.1)
    
    agent = create_law_reader_agent()
    agent.llm = llm
    
    return agent, recommended


def create_legal_analyst_agent_multi(router: ModelRouter) -> tuple:
    """Create Legal Analyst agent - uses Kimi K2"""
    from swarm import create_legal_analyst_agent
    
    # Kimi K2 for legal reasoning (replaces Claude)
    recommended = "kimi-k2" if "kimi-k2" in router.available_models else router.available_models[0]
    llm = router.get_llm(recommended, temperature=0.2)
    
    agent = create_legal_analyst_agent()
    agent.llm = llm
    
    return agent, recommended


def create_rule_extractor_agent_multi(router: ModelRouter) -> tuple:
    """Create Rule Extractor agent - uses MiniMax M2.5"""
    from swarm import create_rule_extractor_agent
    
    # MiniMax for fast pattern extraction
    recommended = "minimax-m2.5" if "minimax-m2.5" in router.available_models else router.available_models[0]
    llm = router.get_llm(recommended, temperature=0.2)
    
    agent = create_rule_extractor_agent()
    agent.llm = llm
    
    return agent, recommended


def create_validator_agent_multi(router: ModelRouter) -> tuple:
    """Create Validator agent - uses Kimi K2 (or ensemble if both available)"""
    from swarm import create_validator_agent
    
    # Use Kimi for validation (highest quality)
    recommended = "kimi-k2" if "kimi-k2" in router.available_models else router.available_models[0]
    llm = router.get_llm(recommended, temperature=0.1)
    
    agent = create_validator_agent()
    agent.llm = llm
    
    return agent, recommended


def create_dmn_formatter_agent_multi(router: ModelRouter) -> tuple:
    """Create DMN Formatter agent - uses MiniMax M2.5"""
    from swarm import create_dmn_formatter_agent
    
    # MiniMax for structured output
    recommended = "minimax-m2.5" if "minimax-m2.5" in router.available_models else router.available_models[0]
    llm = router.get_llm(recommended, temperature=0.2)
    
    agent = create_dmn_formatter_agent()
    agent.llm = llm
    
    return agent, recommended


def create_gap_analyzer_agent_multi(router: ModelRouter) -> tuple:
    """Create Gap Analyzer agent - uses Kimi K2"""
    from swarm import create_gap_analyzer_agent
    
    # Kimi for long context analysis
    recommended = "kimi-k2" if "kimi-k2" in router.available_models else router.available_models[0]
    llm = router.get_llm(recommended, temperature=0.2)
    
    agent = create_gap_analyzer_agent()
    agent.llm = llm
    
    return agent, recommended


# ============================================================================
# USAGE EXAMPLES - Kimi + MiniMax Only
# ============================================================================

if __name__ == "__main__":
    print("Kimi + MiniMax Router initialized")
    
    # Initialize with only Kimi and MiniMax
    router = ModelRouter(available_models=["kimi-k2", "minimax-m2.5"])
    
    print("\nAvailable Models:", router.list_available_models())
    
    # Show recommendations
    print("\nModel Recommendations:")
    for role in ["law_reader", "legal_analyst", "rule_extractor", "validator", "gap_analyzer"]:
        model = router.recommend_model(role)
        info = router.get_model_info(model)
        print(f"  {role}: {model} (strengths: {', '.join(info.get('strengths', []))})")
    
    # Cost estimation
    optimizer = CostOptimizer(router)
    print("\nCost Estimates (for 4K input + 2K output tokens):")
    for model in router.available_models:
        cost = optimizer.estimate_cost(model, 4000, 2000)
        print(f"  {model}: ${cost:.4f}")
    
    # Show ensemble setup
    print("\nEnsemble Validator:")
    ensemble = EnsembleValidator(router)
    print(f"  Models in ensemble: {ensemble.models}")
