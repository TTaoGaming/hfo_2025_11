Feature: GitOps Automation Protocol
  As the Swarmlord
  I want a resilient, agentic GitOps workflow
  So that the codebase remains clean, semantic, and synchronized without manual toil

  Background:
    Given the Hive Fleet Obsidian workspace is active
    And the "GitOps Agent" is operational

  Scenario: Automated Commit Cycle
    Given I have uncommitted changes in the workspace
    When I trigger the "GitOps Cycle"
    Then the agent should first run "Hive Guards" to verify integrity
    And if guards pass, it should stage all changes
    And it should generate a "Conventional Commit" message using the LLM
    And it should commit the changes to the local repository

  Scenario: Resilient Push Strategy
    Given I have committed changes locally
    When the agent attempts to push to "origin main"
    And if the push fails due to a conflict
    Then the agent should perform a "git pull --rebase"
    And retry the push operation
    And if the retry fails, it should alert the Swarmlord

  Scenario: Slop Prevention
    Given a file is not registered in "brain/registry.yaml"
    When the GitOps Agent scans the workspace
    Then it should flag the file as "Potential Slop"
    And require explicit confirmation or registration before committing
