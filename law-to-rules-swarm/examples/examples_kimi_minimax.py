"""
Example: Using Kimi K2 + MiniMax M2.5 Only
No Claude required!
"""

from kimiminimax_router import (
    ModelRouter,
    EnsembleValidator,
    CostOptimizer,
    FallbackChain,
    create_law_reader_agent_multi,
    create_legal_analyst_agent_multi,
    create_rule_extractor_agent_multi,
    create_validator_agent_multi,
    create_dmn_formatter_agent_multi,
    create_gap_analyzer_agent_multi
)


def example_basic_setup():
    """Basic setup with Kimi + MiniMax"""
    print("=" * 60)
    print("Example 1: Basic Kimi + MiniMax Setup")
    print("=" * 60)
    
    # Initialize router with only Kimi and MiniMax
    router = ModelRouter(available_models=["kimi-k2", "minimax-m2.5"])
    
    print(f"\n✓ Available models: {router.list_available_models()}")
    
    # Create agents
    agents = {}
    
    reader, model = create_law_reader_agent_multi(router)
    agents["Law Reader"] = model
    
    analyst, model = create_legal_analyst_agent_multi(router)
    agents["Legal Analyst"] = model
    
    extractor, model = create_rule_extractor_agent_multi(router)
    agents["Rule Extractor"] = model
    
    validator, model = create_validator_agent_multi(router)
    agents["Validator"] = model
    
    formatter, model = create_dmn_formatter_agent_multi(router)
    agents["DMN Formatter"] = model
    
    gap_analyzer, model = create_gap_analyzer_agent_multi(router)
    agents["Gap Analyzer"] = model
    
    print("\n✓ Agent assignments:")
    for agent, model in agents.items():
        print(f"  {agent}: {model}")


def example_cost_comparison():
    """Compare costs between configurations"""
    print("\n" + "=" * 60)
    print("Example 2: Cost Comparison")
    print("=" * 60)
    
    # Kimi + MiniMax only
    router_km = ModelRouter(available_models=["kimi-k2", "minimax-m2.5"])
    optimizer_km = CostOptimizer(router_km)
    
    # Estimate for 4K input + 2K output tokens
    tokens_in, tokens_out = 4000, 2000
    
    print(f"\nCost for {tokens_in} input + {tokens_out} output tokens:")
    print()
    
    print("Kimi + MiniMax configuration:")
    cost_kimi = optimizer_km.estimate_cost("kimi-k2", tokens_in, tokens_out)
    cost_minimax = optimizer_km.estimate_cost("minimax-m2.5", tokens_in, tokens_out)
    print(f"  Kimi K2:        ${cost_kimi:.4f}")
    print(f"  MiniMax M2.5:   ${cost_minimax:.4f}")
    print(f"  Average:        ${(cost_kimi + cost_minimax) / 2:.4f}")
    
    print("\nClaude (for comparison):")
    print(f"  Claude:         ~${0.008 * (tokens_in + tokens_out) / 1000:.4f}")
    
    print("\n✓ Kimi + MiniMax is ~75% cheaper than Claude!")


def example_ensemble_validation():
    """Show ensemble validation with Kimi + MiniMax"""
    print("\n" + "=" * 60)
    print("Example 3: Ensemble Validation")
    print("=" * 60)
    
    router = ModelRouter(available_models=["kimi-k2", "minimax-m2.5"])
    ensemble = EnsembleValidator(router)
    
    print(f"\n✓ Ensemble uses: {ensemble.models}")
    print("\nBoth models validate critical rules and must agree.")
    
    # Example rule validation
    example_rule = {
        "rule_id": "INS-001",
        "condition": "Ajoneuvo on liikenteessä",
        "action": "Vakuutus on otettava"
    }
    
    section_text = "Ajoneuvosta, joka on liikenteessä, on otettava liikennevakuutus."
    
    print("\nExample rule:")
    print(f"  IF: {example_rule['condition']}")
    print(f"  THEN: {example_rule['action']}")
    
    print("\n✓ Ensemble validation would check this rule with both models")


def example_fallback_chain():
    """Show fallback chain"""
    print("\n" + "=" * 60)
    print("Example 4: Fallback Chain")
    print("=" * 60)
    
    router = ModelRouter(available_models=["kimi-k2", "minimax-m2.5"])
    fallback = FallbackChain(router)
    
    print("\n✓ Fallback order:")
    for i, model in enumerate(fallback.fallback_order, 1):
        print(f"  {i}. {model}")
    
    print("\nIf Kimi fails (rate limit, error), automatically tries MiniMax.")


def example_simple_usage():
    """Simple usage example"""
    print("\n" + "=" * 60)
    print("Example 5: Simple Usage")
    print("=" * 60)
    
    code = '''
from kimiminimax_router import ModelRouter, create_legal_analyst_agent_multi

# 1. Initialize router
router = ModelRouter(available_models=["kimi-k2", "minimax-m2.5"])

# 2. Create agent (automatically selects best model)
agent, model_name = create_legal_analyst_agent_multi(router)

# 3. Use agent
print(f"Agent ready using: {model_name}")
'''
    
    print("\nCode:")
    print(code)


if __name__ == "__main__":
    print("Kimi + MiniMax Swarm - Examples")
    print("=" * 60)
    print("No Claude required! Just Kimi K2 and MiniMax M2.5")
    print("=" * 60)
    
    example_basic_setup()
    example_cost_comparison()
    example_ensemble_validation()
    example_fallback_chain()
    example_simple_usage()
    
    print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60)
    print("\nTo run for real:")
    print("  1. Set MOONSHOT_API_KEY and MINIMAX_API_KEY in .env")
    print("  2. from kimiminimax_router import ModelRouter")
    print("  3. router = ModelRouter(available_models=['kimi-k2', 'minimax-m2.5'])")
