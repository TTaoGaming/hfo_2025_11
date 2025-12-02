Feature: HFO Gen 63 Structure Registry & Enforcement
  As the Swarmlord
  I want a strict, declarative directory structure enforced by a Registry
  So that the system remains fractal, organized, and self-cleaning

  Scenario: The Registry defines the 8 Pillars
    Given the file "REGISTRY.yaml" exists in the root of the Bud
    Then it should define the following organs:
      | organ    | path       | description                     |
      | brain    | brain/     | Navigator: Intent & Strategy    |
      | eyes     | eyes/      | Observer: Sensors & Inputs      |
      | memory   | memory/    | Bridger: Knowledge & State      |
      | forge    | forge/     | Shaper: Tools & Actuators       |
      | pulse    | pulse/     | Injector: Heartbeat & Loops     |
      | venom    | venom/     | Disruptor: Tests & Chaos        |
      | carapace | carapace/  | Immunizer: Config & Security    |
      | digest   | digest/    | Assimilator: Ingestion & ETL    |

  Scenario: The Enforcer validates the File System
    Given the "REGISTRY.yaml" is valid
    When the "Structure Enforcer" runs
    Then it should ensure all Organ directories exist
    And it should flag any file in "src/" as a violation (Legacy Drift)
    And it should check that every ".py" file has a valid "holon" header linking to an Intent

  Scenario: The Enforcer creates missing Organs
    Given the directory "eyes/" does not exist
    When the "Structure Enforcer" runs
    Then it should create the directory "eyes/"
