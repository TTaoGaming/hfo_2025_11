import sys
import os
import logging

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_59.immune_system.hive_guards import HiveGuard

def test_hive_guards():
    print("🧪 Testing Hive Guards (Immunizer)...")
    
    if HiveGuard.run_static_diagnostics():
        print("\n✅ HIVE GUARDS OPERATIONAL")
        print("   - Level 0 Validation: ENFORCED (PREY + 8 Pillars)")
        print("   - Level 1 Validation: ENFORCED (8x Links)")
        print("   - Regression Protection: ACTIVE")
    else:
        print("\n❌ HIVE GUARDS FAILED")
        sys.exit(1)

if __name__ == "__main__":
    test_hive_guards()
