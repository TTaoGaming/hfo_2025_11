package G28_ObsidianHourglass {

	/* Plain-language attribute definitions */
	attribute def MissionIntent;
	attribute def PrecedentBundle;
	attribute def SimulationConfig;
	attribute def SimulationReport;
	attribute def PresentArtifact;
	attribute def RiskProfile;
	attribute def CostProfile;
	attribute def ConfidenceScore;
	attribute def FlipDecision;
	attribute def KnowledgeReference;
	attribute def StatusEvent;

	requirement G28_OH_REQ_001_PastSweep {
		id = "G28-OH-REQ-001";
		text = "The hourglass must gather precedents from local archives, institutional knowledge, and open internet sources with priority on Cynefin framing and case-based reasoning.";
	}

	requirement G28_OH_REQ_002_FutureSimulation {
		id = "G28-OH-REQ-002";
		text = "The hourglass must support running future simulations with interchangeable algorithms (Monte Carlo, tree search, Bayesian planners, heuristic probes) and capture their outcomes.";
	}

	requirement G28_OH_REQ_003_PresentArtifact {
		id = "G28-OH-REQ-003";
		text = "Each hourglass flip must produce a present-day artifact that humans or swarm agents can execute without extra translation.";
	}

	requirement G28_OH_REQ_004_AgencyNeutrality {
		id = "G28-OH-REQ-004";
		text = "The hourglass must run with either a solo operator or an orchestrated crew while keeping the same interfaces and data contracts.";
	}

	requirement G28_OH_REQ_005_ProbabilityTracking {
		id = "G28-OH-REQ-005";
		text = "The hourglass must update probability, risk, and cost views after every flip so the mission owner can stop when satisfied.";
	}

	requirement G28_OH_REQ_006_ToolAgnostic {
		id = "G28-OH-REQ-006";
		text = "The hourglass must remain tool agnostic: storage, workflow engine, and simulation tooling can be swapped without breaking the loop.";
	}

	package G28_OH_Structure {
		port def MissionIntentPort {
			attribute intent: MissionIntent;
		}

		port def PrecedentPort {
			attribute bundle: PrecedentBundle;
		}

		port def SimulationPort {
			attribute config: SimulationConfig;
			attribute report: SimulationReport;
		}

		port def ArtifactPort {
			attribute deliverable: PresentArtifact;
		}

		port def RiskTelemetryPort {
			attribute risk: RiskProfile;
			attribute cost: CostProfile;
			attribute confidence: ConfidenceScore;
		}

		port def FlipStatusPort {
			attribute decision: FlipDecision;
			attribute flipEvent: StatusEvent;
		}

		part def HourglassConductor {
			attribute canBeHuman: AgencyNeutralityFlag;
			port missionIn: MissionIntentPort;
			port precedentsOut: PrecedentPort;
			port simulationOut: SimulationPort;
			port artifactOut: ArtifactPort;
			port riskOut: RiskTelemetryPort;
			port flipOut: FlipStatusPort;
		}

		attribute def AgencyNeutralityFlag;

		part def PrecedentHunter {
			attribute knowledgeSources: KnowledgeReference;
			port missionIn: MissionIntentPort;
			port precedentsOut: PrecedentPort;
			port statusOut: FlipStatusPort;
		}

		part def SimulationEngine {
			attribute algorithmCatalog: SimulationConfig;
			port precedentsIn: PrecedentPort;
			port missionIn: MissionIntentPort;
			port simulationOut: SimulationPort;
			port riskOut: RiskTelemetryPort;
			port statusOut: FlipStatusPort;
		}

		part def ArtifactForge {
			attribute deliverableTypes: PresentArtifact;
			port missionIn: MissionIntentPort;
			port precedentsIn: PrecedentPort;
			port simulationIn: SimulationPort;
			port artifactOut: ArtifactPort;
			port riskIn: RiskTelemetryPort;
			port statusOut: FlipStatusPort;
		}

		part def ArchiveUpdater {
			port precedentsIn: PrecedentPort;
			port simulationIn: SimulationPort;
			port artifactIn: ArtifactPort;
			port riskIn: RiskTelemetryPort;
			port statusOut: FlipStatusPort;
		}

		part def ObsidianHourglassAssembly {
			part conductor: HourglassConductor;
			part hunter: PrecedentHunter;
			part simulator: SimulationEngine;
			part forge: ArtifactForge;
			part archive: ArchiveUpdater;

			// connect missionIntentFlow conductor.missionIn -> hunter.missionIn
			// connect hunterToConductor hunter.precedentsOut -> conductor.precedentsOut
			// connect hunterToSimulator hunter.precedentsOut -> simulator.precedentsIn
			// connect missionToSimulator conductor.missionIn -> simulator.missionIn
			// connect simulatorToConductor simulator.simulationOut -> conductor.simulationOut
			// connect simulatorToForge simulator.simulationOut -> forge.simulationIn
			// connect missionToForge conductor.missionIn -> forge.missionIn
			// connect precedentsToForge hunter.precedentsOut -> forge.precedentsIn
			// connect forgeToConductor forge.artifactOut -> conductor.artifactOut
			// connect forgeToArchive forge.artifactOut -> archive.artifactIn
			// connect simulatorRisk simulator.riskOut -> conductor.riskOut
			// connect forgeRisk forge.riskIn -> conductor.riskOut
			// connect archiveUpdate archive.statusOut -> conductor.flipOut
			// connect statusFanout hunter.statusOut -> conductor.flipOut
			// connect statusFanoutSim simulator.statusOut -> conductor.flipOut
			// connect statusFanoutForge forge.statusOut -> conductor.flipOut
		}
	}

	// satisfy G28_OH_REQ_001_PastSweep by G28_OH_Structure::PrecedentHunter
	// satisfy G28_OH_REQ_002_FutureSimulation by G28_OH_Structure::SimulationEngine
	// satisfy G28_OH_REQ_003_PresentArtifact by G28_OH_Structure::ArtifactForge
	// satisfy G28_OH_REQ_004_AgencyNeutrality by G28_OH_Structure::HourglassConductor
	// satisfy G28_OH_REQ_005_ProbabilityTracking by ObsidianHourglassLoop.UpdateDecisionSurface
	// satisfy G28_OH_REQ_006_ToolAgnostic by G28_OH_Structure::ObsidianHourglassAssembly

	/* Hourglass workflow in SysML v2 actions */
	action ObsidianHourglassLoop {
		action IntakeMissionIntent {
			out mission : MissionIntent;
		}

		action HuntPrecedents {
			in mission : MissionIntent;
			out precedents : PrecedentBundle;
			out status : StatusEvent;
		}

		action ConfigureSimulations {
			in mission : MissionIntent;
			in precedents : PrecedentBundle;
			out config : SimulationConfig;
		}

		action RunSimulations {
			in config : SimulationConfig;
			out report : SimulationReport;
			out risk : RiskProfile;
			out cost : CostProfile;
			out confidence : ConfidenceScore;
		}

		action RetroflipPrecedents {
			in precedents : PrecedentBundle;
			in report : SimulationReport;
			out updatedPrecedents : PrecedentBundle;
		}

		action PublishArtifact {
			in mission : MissionIntent;
			in report : SimulationReport;
			in risk : RiskProfile;
			in cost : CostProfile;
			in confidence : ConfidenceScore;
			out artifact : PresentArtifact;
		}

		action UpdateDecisionSurface {
			in report : SimulationReport;
			in risk : RiskProfile;
			in cost : CostProfile;
			in confidence : ConfidenceScore;
			out decision : FlipDecision;
		}

		action DecideNextFlip {
			in decision : FlipDecision;
		}

		action ArchiveCycle {
			in updatedPrecedents : PrecedentBundle;
			in artifact : PresentArtifact;
			in report : SimulationReport;
		}

		succession flow intent_to_hunt from IntakeMissionIntent.mission to HuntPrecedents.mission;
		succession flow hunt_to_config from HuntPrecedents.precedents to ConfigureSimulations.precedents;
		succession flow intent_to_config from IntakeMissionIntent.mission to ConfigureSimulations.mission;
		succession flow config_to_run from ConfigureSimulations.config to RunSimulations.config;
		succession flow run_to_retro from RunSimulations.report to RetroflipPrecedents.report;
		succession flow hunt_to_retro from HuntPrecedents.precedents to RetroflipPrecedents.precedents;
		succession flow retro_to_archive from RetroflipPrecedents.updatedPrecedents to ArchiveCycle.updatedPrecedents;
		succession flow run_to_publish from RunSimulations.report to PublishArtifact.report;
		succession flow run_risk_to_publish from RunSimulations.risk to PublishArtifact.risk;
		succession flow run_cost_to_publish from RunSimulations.cost to PublishArtifact.cost;
		succession flow run_conf_to_publish from RunSimulations.confidence to PublishArtifact.confidence;
		succession flow publish_to_archive from PublishArtifact.artifact to ArchiveCycle.artifact;
		succession flow run_to_decision from RunSimulations.report to UpdateDecisionSurface.report;
		succession flow run_risk_to_decision from RunSimulations.risk to UpdateDecisionSurface.risk;
		succession flow run_cost_to_decision from RunSimulations.cost to UpdateDecisionSurface.cost;
		succession flow run_conf_to_decision from RunSimulations.confidence to UpdateDecisionSurface.confidence;
		succession flow decision_to_next from UpdateDecisionSurface.decision to DecideNextFlip.decision;
	}
}
