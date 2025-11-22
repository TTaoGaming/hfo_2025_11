Feature: Cognitive Loops (PREY & SWARM)
  As the Swarmlord
  I want to standardize the cognitive loops
  So that every agent and swarm operates with a consistent OODA rhythm.

  Scenario: PREY Loop (Atomic Agent)
    Given an individual agent
    When it is active
    Then it must cycle through:
      | Phase     | Action |
      | Perceive  | Read inputs, check memory |
      | React     | Plan next step, check tools |
      | Execute   | Run tools, generate code |
      | Yield     | Return result, sleep |

  Scenario: SWARM Loop (Holonic Node)
    Given a Swarm Controller (L1+)
    When it is managing a mission
    Then it must cycle through:
      | Phase   | Action |
      | Set     | Define mission, scatter tasks |
      | Watch   | Monitor progress (Stigmergy) |
      | Act     | Intervene, re-plan |
      | Review  | Synthesize results (Reduce) |
      | Mutate  | Evolve strategy (Optional) |
