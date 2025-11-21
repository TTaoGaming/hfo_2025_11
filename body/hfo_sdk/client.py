import ray
from temporalio.client import Client as TemporalClient


class HFOClient:
    """
    Main client for interacting with the Hive Fleet Obsidian swarm.
    """

    def __init__(self):
        self.temporal_client = None
        self.ray_initialized = False

    async def connect(self, temporal_addr="localhost:7235"):
        """Connects to the HFO infrastructure."""
        # Connect to Temporal
        try:
            self.temporal_client = await TemporalClient.connect(temporal_addr)
            print(f"✅ Connected to Temporal at {temporal_addr}")
        except Exception as e:
            print(f"❌ Failed to connect to Temporal: {e}")
            raise

        # Connect to Ray
        if not ray.is_initialized():
            try:
                ray.init(ignore_reinit_error=True, logging_level="ERROR")
                self.ray_initialized = True
                print("✅ Ray initialized")
            except Exception as e:
                print(f"❌ Failed to initialize Ray: {e}")
                raise
        else:
            print("ℹ️ Ray already initialized")

    def shutdown(self):
        """Clean shutdown of client resources."""
        if self.ray_initialized:
            ray.shutdown()
            print("🛑 Ray shutdown")
