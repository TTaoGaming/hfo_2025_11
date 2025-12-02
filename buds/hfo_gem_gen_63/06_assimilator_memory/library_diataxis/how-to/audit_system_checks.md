---
holon:
  id: 4e1fb49b-b051-4f9e-8728-7c104c646736
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/audit_gen63.py
hexagon:
  ontos: <owner>
  logos: diataxis
---

# How to Perform the Gen 63 System Audit

This document outlines the steps necessary to perform the Gen 63 system audit using the provided Python script.

## Explanation

The `audit_system` function verifies the operational status of different components within the Hydra system, which include configuration settings, memory storage, NATS messaging system, swarm intelligence, and heartbeat verification. It is crucial to ensure that all components are functioning correctly before deployment.

## Step-by-Step Instructions

1. **Import Necessary Packages**: Ensure you have the required libraries installed in your environment. Import necessary modules such as `asyncio`, `logging`, `sys`, `os`, and `time`.

2. **Set Up Logging**: The logging configuration is set up to display messages in a standardized format. Add the following to the top of your script:
   ```python
   logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
   logger = logging.getLogger("AuditGen63")
   ```

3. **Define the Audit Function**: Implement the `audit_system` function where the actual checks will be performed. Start the function with logging to indicate the audit is beginning:
   ```python
   logger.info("🔍 STARTING GEN 63 SYSTEM AUDIT...")
   ```

4. **Check Configuration**: Verify the configuration settings are loaded correctly.
   ```python
   if settings.ENV and settings.NATS_URL:
       logger.info("✅ [CONFIG] Environment loaded.")
       report["config"] = True
   else:
       logger.error("❌ [CONFIG] Settings missing.")
   ```

5. **Check Memory**: Use the `Bridger` class to test memory functionalities by storing and retrieving a test message.
   ```python
   bridger = Bridger()
   test_mem = f"Audit Timestamp {time.time()}"
   bridger.memorize(test_mem, source="audit", category="test")
   results = bridger.ask(test_mem, limit=1)
   ```

6. **Check NATS Connectivity**: Establish a connection to the NATS system to verify the messaging capabilities:
   ```python
   bus = NatsAdapter(settings.NATS_URL)
   await bus.connect()
   logger.info("✅ [NERVES] NATS JetStream connected.")
   ```

7. **Check Brain**: Execute a test query using the Hydra Swarm to verify the response.
   ```python
   swarm = HydraSwarm()
   res = swarm.researcher.research("Are you online?")
   if res and "❌" not in res:
       logger.info("✅ [BRAIN] Hydra Swarm (OpenRouter) is thinking.")
   ```

8. **Check Heartbeat**: Verify the existence of a specific file, which indicates the system is operational:
   ```python
   if os.path.exists("buds/hfo_gem_gen_63/sandbox/hello_stigmergy.txt"):
       logger.info("✅ [HEARTBEAT] Stigmergy artifact found.")
   ```

9. **Final Verdict**: Log the success or failure message based on the results of the checks performed and return the result:
   ```python
   if all(report.values()):
       logger.info("🏆 AUDIT PASSED: Gen 63 is READY for Deployment.")
       return True
   else:
       logger.error(f"🚫 AUDIT FAILED: {report}")
       return False
   ```

10. **Run the Audit**: Finally, run the `audit_system()` function in your main block and handle the exit code accordingly:
    ```python
    if __name__ == "__main__":
        success = asyncio.run(audit_system())
        sys.exit(0 if success else 1)
    ```

Following these steps ensures a thorough audit of the Gen 63 system, allowing for the early identification of components that may require attention before deployment.