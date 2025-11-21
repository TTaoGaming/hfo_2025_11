# HFO Gen 42.1 Research Lineage

A. The Philosophy (Why)

Mosaic Warfare (JADC2):

Source: DARPA / US DoD.

Application: "Hexagonal Tiles." We do not build monolithic apps; we compose temporary kill-chains from modular capabilities.

The Cognitive Exoskeleton:

Source: Engelbart (Augmenting Human Intellect) / Licklider (Symbiosis).

Application: The system is a "Symbiote," not a tool. It co-evolves with the user.

B. The Architecture (Structure)

Fractal Holarchy:

Source: Arthur Koestler ("The Ghost in the Machine").

Application: The PREY/SWARM/GROWTH loops are self-similar structures at different time scales.

Stigmergy:

Source: Pierre-Paul Grassé (1959, Termite construction).

Application: Indirect coordination via NATS. Agents watch the environment, not each other.

Hexagonal Architecture (Ports & Adapters):

Source: Alistair Cockburn.

Application: Decoupling "Intent" (SysML) from "Implementation" (Python).

C. The Logic (Algorithms)

Byzantine Fault Tolerance (BFT):

Source: Lamport, Shostak, Pease (1982).

Application: V²C-SPIRAL-QUORUM. We assume 1/3 of agents are hallucinating (Byzantine).

MAP-Elites (Quality Diversity):

Source: Mouret & Clune (2015).

Application: Evolution. We don't just optimize; we search for diverse, high-quality solutions to populate the "Future" bulb.

OODA Loop:

Source: Col. John Boyd.

Application: The PREY Loop (Perceive-React-Execute-Yield).

D. The Engineering (Stack)

Durable Execution: Temporal.io (Proven by Uber/Netflix). Solves "Drift."

Vector Search: pgvector (Proven Standard). Solves "Amnesia."

Event Streaming: NATS JetStream (Proven by Synadia). Solves "Coupling."
