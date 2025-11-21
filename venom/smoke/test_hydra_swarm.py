import pytest
from body.hands.hydra_swarm import build_hydra_graph, HydraState

def test_hydra_swarm_smoke():
    print("\n🧪 SMOKE TEST: Hydra Scatter-Gather Pattern")
    
    try:
        app = build_hydra_graph()
        
        initial_state = {
            "mission": "Analyze the viability of a Dyson Sphere", 
            "results": []
        }
        
        print("   🚀 Launching Swarm...")
        final = app.invoke(initial_state)
        
        # Assertions
        assert final is not None
        assert "plan" in final
        assert len(final["plan"]) > 0
        assert "results" in final
        assert len(final["results"]) == len(final["plan"]) # Gathered all
        assert "final_output" in final
        assert final["final_output"].consensus_score > 0.0
        
        print(f"   ✅ Plan Generated: {len(final['plan'])} tasks")
        print(f"   ✅ Results Gathered: {len(final['results'])} outputs")
        print(f"   ✅ Synthesis: {final['final_output'].summary[:50]}...")
        
    except Exception as e:
        pytest.fail(f"Hydra Swarm failed: {e}")

if __name__ == "__main__":
    test_hydra_swarm_smoke()
