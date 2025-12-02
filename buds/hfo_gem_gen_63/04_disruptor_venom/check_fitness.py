import sys
import os
from buds.hfo_gem_gen_63.carapace.guard_knowledge_structure import KnowledgeStructureGuard

def main():
    brain_path = os.path.abspath("buds/hfo_gem_gen_63/brain")
    print(f"🛡️  Running Evo-Devo Fitness Function on: {brain_path}")
    
    guard = KnowledgeStructureGuard(brain_path)
    errors = guard.validate()
    
    if errors:
        print(f"❌ Fitness Check FAILED ({len(errors)} Violations):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("✅ Fitness Check PASSED (System is Healthy)")
        sys.exit(0)

if __name__ == "__main__":
    main()
