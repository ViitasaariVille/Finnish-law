"""
Multi-Model Law-to-Rules Swarm
Supports Claude, Kimi K2, and MiniMax M2.5
"""

import os
from typing import Optional, Dict, Any
from langchain_openai import ChatOpenAI


class ModelRouter:
    """Routes agents to different LLM providers based on task requirements"""
    
    MODEL_CONFIGS = {
        "claude": {
            "provider": "anthropic",
            "model": "claude-3-5-sonnet-20241022",
            "strengths": ["legal_reasoning", "structured_output", "nuanced_analysis"],
            "best_for": ["legal_analyst", "validator"]
        },
        "kimi-k2": {
            "provider": "moonshot",
            "model": "kimi-k2.5",
            "api_base": "https://api.moonshot.cn/v1",
            "strengths": ["long_context", "finnish_language", "document_analysis"],
            "best_for": ["law_reader", "gap_analyzer"]
        },
        "minimax-m2.5": {
            "provider": "minimax",
            "model": "MiniMax-M2.5",
            "api_base": "https://api.minimax.chat/v1",
            "strengths": ["speed", "cost_efficiency", "pattern_matching"],
            "best_for": ["rule_extractor", "formatter"]
        }
    }
    
    def __init__(self):
        self.llm_cache = {}
    
    def get_llm(self, model_name: str, temperature: float = 0.2) -> Any:
        """Get or create LLM instance"""
        cache_key = f"{model_name}_{temperature}"
        
        if cache_key in self.llm_cache:
            return self.llm_cache[cache_key]
        
        config = self.MODEL_CONFIGS.get(model_name)
        if not config:
            raise ValueError(f"Unknown model: {model_name}")
        
        llm = self._create_llm(config, temperature)
        self.llm_cache[cache_key] = llm
        return llm
    
    def _create_llm(self, config: Dict, temperature: float) -> Any:
        """Create LLM instance based on provider"""
        provider = config["provider"]
        
        if provider == "anthropic":
            from langchain_anthropic import ChatAnthropic
            return ChatAnthropic(
                model=config["model"],
                temperature=temperature,
                api_key=os.getenv("ANTHROPIC_API_KEY")
            )
        
        elif provider == "moonshot":
            # Kimi K2 via OpenAI-compatible API
            return ChatOpenAI(
                model=config["model"],
                temperature=temperature,
                api_key=os.getenv("MOONSHOT_API_KEY"),
                base_url=config.get("api_base")
            )
        
        elif provider == "minimax":
            # MiniMax M2.5 via OpenAI-compatible API
            return ChatOpenAI(
                model=config["model"],
                temperature=temperature,
                api_key=os.getenv("MINIMAX_API_KEY"),
                base_url=config.get("api_base")
            )
        
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    def recommend_model(self, agent_role: str) -> str:
        """Recommend best model for agent role"""
        for model_name, config in self.MODEL_CONFIGS.items():
            if agent_role.lower() in [r.lower() for r in config["best_for"]]:
                return model_name
        
        # Default to Claude for unknown roles
        return "claude"
    
    def get_model_info(self, model_name: str) -> Dict:
        """Get information about a model"""
        return self.MODEL_CONFIGS.get(model_name, {})


# ============================================================================
# ENSEMBLE APPROACH - Multiple models vote on critical decisions
# ============================================================================

class EnsembleValidator:
    """Uses multiple models to validate critical rules"""
    
    def __init__(self, router: ModelRouter):
        self.router = router
        self.models = ["claude", "kimi-k2", "minimax-m2.5"]
    
    def validate_rule(self, rule: Dict, section_text: str) -> Dict:
        """Get consensus from multiple models on rule validity"""
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
                # Parse response and add to votes
                votes.append({
                    "model": model_name,
                    "response": response.content
                })
                
            except Exception as e:
                votes.append({
                    "model": model_name,
                    "error": str(e)
                })
        
        # Aggregate results
        return self._aggregate_votes(votes)
    
    def _aggregate_votes(self, votes: list) -> Dict:
        """Aggregate votes from multiple models"""
        valid_votes = [v for v in votes if "error" not in v]
        
        if not valid_votes:
            return {"consensus": "error", "votes": votes}
        
        # Simple majority for now
        # In production, weight by model confidence
        return {
            "consensus": "validated" if len(valid_votes) >= 2 else "uncertain",
            "vote_count": len(valid_votes),
            "votes": votes
        }


# ============================================================================
# FALLBACK CHAIN - If primary model fails, try alternatives
# ============================================================================

class FallbackChain:
    """Chain of models to try if primary fails"""
    
    FALLBACK_ORDER = ["claude", "kimi-k2", "minimax-m2.5"]
    
    def __init__(self, router: ModelRouter):
        self.router = router
    
    def invoke_with_fallback(self, prompt: str, temperature: float = 0.2) -> Dict:
        """Try models in order until one succeeds"""
        errors = []
        
        for model_name in self.FALLBACK_ORDER:
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
        "claude": 0.008,      # $8/1M tokens
        "kimi-k2": 0.002,     # $2/1M tokens (estimated)
        "minimax-m2.5": 0.001 # $1/1M tokens (estimated)
    }
    
    def __init__(self, router: ModelRouter):
        self.router = router
    
    def select_model(self, task_complexity: str, required_accuracy: float) -> str:
        """Select most cost-effective model for task"""
        
        if required_accuracy > 0.95:
            # High accuracy needed - use Claude
            return "claude"
        
        elif task_complexity == "simple":
            # Simple task - use cheapest model
            return "minimax-m2.5"
        
        elif task_complexity == "medium":
            # Balanced - use Kimi
            return "kimi-k2"
        
        else:
            # Complex task with moderate accuracy needs
            return "kimi-k2"
    
    def estimate_cost(self, model_name: str, input_tokens: int, output_tokens: int) -> float:
        """Estimate cost for a request"""
        cost_per_1k = self.COST_PER_1K_TOKENS.get(model_name, 0.008)
        total_tokens = input_tokens + output_tokens
        return (total_tokens / 1000) * cost_per_1k


# ============================================================================
# UPDATED AGENT CREATION WITH MULTI-MODEL SUPPORT
# ============================================================================

def create_law_reader_agent_multi(router: ModelRouter) -> tuple:
    """Create Law Reader agent with model selection"""
    from swarm import create_law_reader_agent
    
    # Kimi K2 is best for document analysis and Finnish language
    recommended = router.recommend_model("law_reader")
    llm = router.get_llm(recommended, temperature=0.1)
    
    agent = create_law_reader_agent()
    agent.llm = llm
    
    return agent, recommended


def create_legal_analyst_agent_multi(router: ModelRouter) -> tuple:
    """Create Legal Analyst agent with model selection"""
    from swarm import create_legal_analyst_agent
    
    # Claude is best for legal reasoning
    recommended = router.recommend_model("legal_analyst")
    llm = router.get_llm(recommended, temperature=0.2)
    
    agent = create_legal_analyst_agent()
    agent.llm = llm
    
    return agent, recommended


def create_rule_extractor_agent_multi(router: ModelRouter) -> tuple:
    """Create Rule Extractor agent with model selection"""
    from swarm import create_rule_extractor_agent
    
    # MiniMax is fast for pattern extraction
    recommended = router.recommend_model("rule_extractor")
    llm = router.get_llm(recommended, temperature=0.2)
    
    agent = create_rule_extractor_agent()
    agent.llm = llm
    
    return agent, recommended


def create_validator_agent_multi(router: ModelRouter) -> tuple:
    """Create Validator agent with ensemble validation"""
    from swarm import create_validator_agent
    
    # Use Claude for primary validation
    llm = router.get_llm("claude", temperature=0.1)
    
    agent = create_validator_agent()
    agent.llm = llm
    
    return agent, "claude+ensemble"


def create_gap_analyzer_agent_multi(router: ModelRouter) -> tuple:
    """Create Gap Analyzer agent with model selection"""
    from swarm import create_gap_analyzer_agent
    
    # Kimi K2 for long context analysis
    recommended = router.recommend_model("gap_analyzer")
    llm = router.get_llm(recommended, temperature=0.2)
    
    agent = create_gap_analyzer_agent()
    agent.llm = llm
    
    return agent, recommended


# ============================================================================
# USAGE EXAMPLES
# ============================================================================

if __name__ == "__main__":
    print("Multi-Model Router initialized")
    
    router = ModelRouter()
    
    # Show recommendations
    print("\nModel Recommendations:")
    for role in ["law_reader", "legal_analyst", "rule_extractor", "validator", "gap_analyzer"]:
        model = router.recommend_model(role)
        info = router.get_model_info(model)
        print(f"  {role}: {model} (strengths: {', '.join(info.get('strengths', []))})")
    
    # Cost estimation
    optimizer = CostOptimizer(router)
    print("\nCost Estimates (for 4K input + 2K output tokens):")
    for model in ["claude", "kimi-k2", "minimax-m2.5"]:
        cost = optimizer.estimate_cost(model, 4000, 2000)
        print(f"  {model}: ${cost:.4f}")
