---
holon:
  id: 0f6b5cf8-e163-4e43-a68d-c49f8d9f5f92
  type: codex_entry
  quadrant: reference
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/adapters/nats_adapter.py
hexagon:
  ontos: hive_fleet
  logos: diataxis
---

# NatsAdapter Class Documentation

## Class: `NatsAdapter`

The `NatsAdapter` class serves as an adapter for the NATS JetStream messaging system. It extends the `EventBusPort` interface.

### Methods:

#### `__init__(self, url: str)`
- **Inputs:**  
  - `url`: A string that represents the NATS server URL.
- **Outputs:**  
  - Initializes the adapter with a URL and sets up the connection variables.

#### `async connect(self)`
- **Inputs:** None
- **Outputs:** Establishes a connection to the NATS server and initializes the JetStream context. Logs the connection status or an error if it fails.

#### `async publish(self, subject: str, payload: Dict[str, Any])` 
- **Inputs:**  
  - `subject`: A string indicating the subject to which the message should be published.  
  - `payload`: A dictionary containing the message data to be sent.  
- **Outputs:**  
  - Publishes a JSON-encoded message to the specified subject. Logs the published message or raises an error if not connected.

#### `async subscribe(self, subject: str, callback: Callable[[Dict[str, Any]], Awaitable[None]])`
- **Inputs:**  
  - `subject`: A string indicating the subject to subscribe to.  
  - `callback`: A callable that will be invoked when a message is received. The callback should accept a dictionary as an input.  
- **Outputs:**  
  - Subscribes to the specified subject and sets up the handling of incoming messages. Logs the subscription status or raises an error if not connected.

#### `async close(self)`
- **Inputs:** None
- **Outputs:** Closes the connection to the NATS server if connected and logs the closure status.