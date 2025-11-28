import time
import json
import requests  # type: ignore
import datetime
import os
import sys
import psutil  # For memory check

# Add parent directory to path to import nerves
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import yaml  # noqa: E402

# Configuration
CONFIG_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "blood/config/local_model_registry.yaml"
    )
)


def load_model_config():
    """Load the current champion from the registry."""
    try:
        with open(CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f)
            return config["current_champion"]["ollama_tag"]
    except Exception as e:
        print(f"⚠️ Config Load Failed: {e}. Fallback to gemma2:2b")
        return "gemma2:2b"


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = load_model_config()
PULSE_INTERVAL = 60  # Seconds
MIN_RAM_MB = 500  # Minimum free RAM required to pulse


def get_system_status():
    """Gather local context for the brain."""
    mem = psutil.virtual_memory()
    return {
        "time": datetime.datetime.now().isoformat(),
        "status": "nominal",
        "memory_available_mb": mem.available / (1024 * 1024),
        "message": "System running smoothly.",
    }


def check_safety():
    """Ensure we don't freeze the system."""
    mem = psutil.virtual_memory()
    available_mb = mem.available / (1024 * 1024)
    if available_mb < MIN_RAM_MB:
        print(
            f"⚠️ LOW MEMORY ({available_mb:.0f}MB). Skipping pulse to prevent freeze."
        )
        return False
    return True


def ask_gemma(context):
    """Send context to the LLM and get a decision."""
    if not check_safety():
        return {"status": "skipped", "action": "none"}

    prompt = f"""
    You are the HFO Heartbeat (Lvl 0).
    Current System Context: {json.dumps(context)}

    Your Job:
    1. Analyze the context.
    2. Decide if a Stigmergy Signal is needed.
    3. Output JSON ONLY.

    Format:
    {{
        "status": "nominal" | "alert",
        "action": "none" | "write_stigmergy",
        "payload": {{ ... }} (optional content for the signal)
    }}
    """

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "format": "json",  # Force JSON mode
            },
            timeout=30,
        )  # Add timeout
        response.raise_for_status()
        return json.loads(response.json()["response"])
    except Exception as e:
        print(f"❌ Brain Freeze: {e}")
        return {"status": "error", "action": "none"}


def execute_action(decision):
    """The Body executes the Brain's will."""
    if decision.get("action") == "write_stigmergy":
        print("⚡ ACTION: Writing to HOT Stigmergy (NATS)...")
        print(f"   Payload: {decision.get('payload')}")
        # Here we would call the NATS client to publish
        # from nerves.bus.nats_client import publish_signal
        # publish_signal("chronos", decision['payload'])
    else:
        print("💤 Pulse Nominal. No action taken.")


def heartbeat_loop(once=False):
    print(f"💓 HFO Heartbeat Online. Model: {MODEL}")
    while True:
        print(f"\n--- Pulse at {datetime.datetime.now().strftime('%H:%M:%S')} ---")

        # 1. Perceive (Senses)
        context = get_system_status()

        # 2. React (Brain)
        decision = ask_gemma(context)
        print(f"🧠 Thought: {decision}")

        # 3. Execute (Hands)
        execute_action(decision)

        if once:
            print("🛑 Test complete. Exiting.")
            break

        # 4. Yield (Wait)
        time.sleep(PULSE_INTERVAL)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="Run one pulse and exit")
    args = parser.parse_args()
    heartbeat_loop(once=args.once)
