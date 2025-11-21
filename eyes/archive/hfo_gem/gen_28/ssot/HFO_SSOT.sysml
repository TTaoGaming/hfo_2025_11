package G28_HFO_SSOT {

	/* Shared signal & artifact definitions */
	attribute def MissionSignal;
	attribute def ClarificationArtifact;
	attribute def MissionIntentArtifact;
	attribute def TaskSignal;
	attribute def MissionFeedback;
	attribute def TelemetryRecord;
	attribute def ProvenanceReference;
	attribute def MissionDigest;
	attribute def PresentArtifact;
	attribute def RiskProfile;
	attribute def CostProfile;
	attribute def ConfidenceScore;
	attribute def WorkflowSelection;
	attribute def KnowledgeInsight;
	attribute def PersonaIdentifier;
	attribute def PersistentMemoryFlag;
	attribute def ConcurrentAgentCapacity;
	attribute def WorkflowSupportIndicator;
	attribute def KnowledgeCapability;
	attribute def DeliveryReliability;
	attribute def FeaturePolicySupport;
	attribute def TelemetrySupport;
	attribute def ProvenanceSupport;
	attribute def QualityDiversitySupport;
	attribute def StigmergyEfficiencyMetric;
	attribute def HierarchicalScalingPattern;
	attribute def IDEVersionConstraint;
	attribute def ExtensionBaseline;
	attribute def MCPTrustProfile;
	attribute def DevContainerBlueprint;
	attribute def SmokeTestIndicator;
	attribute def WorkflowEngineBinding;
	attribute def TemporalNamespace;
	attribute def LangGraphProfile;
	attribute def EventSpineProfile;
	attribute def ParallelComputeProfile;
	attribute def ObservabilityProfile;
	attribute def FeatureFlagProfile;
	attribute def PersonaCatalog;
	attribute def WarChestArtifact;
	attribute def FundingTelemetry;
	attribute def ToolingRunbook;
	attribute def HourglassIntegrationStatus;

	requirement G28_REQ_001_PersistentSwarmlord {
		id = "G28-REQ-001";
		text = "Every USER is paired with a persistent Swarmlord persona that remains their only interface. The Swarmlord must coordinate up to 100 concurrent agents and deliver quorum-backed outcomes.";
	}

	requirement G28_REQ_002_HiveWorkflows {
		id = "G28-REQ-002";
		text = "The Swarmlord selects among HIVE, GROWTH, SWARM, PREY workflows based on user intent while keeping the user insulated from internal complexity.";
	}

	requirement G28_REQ_003_PersistentSwarm {
		id = "G28-REQ-003";
		text = "The Swarmlord maintains a persistent swarm of at least 100 concurrently active agents that can cycle through workflows without teardown between missions.";
	}

	requirement G28_REQ_004_HierarchicalScaling {
		id = "G28-REQ-004";
		text = "The orchestration stack must support hierarchical stigmergy so the Swarmlord can fan out mission intent across subordinate clusters, enabling 10^6+ agents without direct control calls.";
	}

	requirement G28_REQ_005_StigmergyEfficiency {
		id = "G28-REQ-005";
		text = "Stigmergic coordination shall reduce direct communication events by at least an order of magnitude compared to one-to-one agent polling, with results aggregated via a shared blackboard interface.";
	}

	requirement ClarificationSequence {
		/* Exactly three clarification passes are generated sequentially before a mission intent is issued. */
	}

	requirement StigmergicControl {
		/* Swarmlord interacts with AI swarms only through stigmergy; users interact only with the swarmlord facade. */
	}

	requirement G28_REQ_006_ToolingBaseline {
		id = "G28-REQ-006";
		text = "Before activating swarm orchestration the Generation 28 cockpit shall confirm a VS Code ≥1.105 stack with Copilot agent mode, Continue hybrid agents, and an auditable mcp.json trust profile via a repeatable smoke test (scripts/dev/check_tooling.sh).";
	}

	requirement G28_REQ_007_MCPTrustGuardrails {
		id = "G28-REQ-007";
		text = "Model Context Protocol servers must declare trust posture per PREY phase, gating high-impact tools and logging approvals so swarm automation stays bounded.";
	}

	requirement G28_REQ_008_HourglassWorkflowBridge {
		id = "G28-REQ-008";
		text = "Obsidian Horizon Hourglass outputs shall bind into Temporal workflows, LangGraph agent graphs, NATS JetStream subjects, Ray task pools, and Postgres/pgvector storage with OpenTelemetry and OpenFeature instrumentation.";
	}

	requirement G28_REQ_009_PersonaWarChest {
		id = "G28-REQ-009";
		text = "Hourglass briefs must map into the OBSIDIAN persona stack and mint war chest artifacts with funding telemetry for mission reinvestment.";
	}

	package G28_Structure {
		port def ClarificationExchangePort {
			attribute artifact: ClarificationArtifact;
		}

		port def MissionIntentPort {
			attribute artifact: MissionIntentArtifact;
		}

		port def TaskSignalPort {
			attribute signal: TaskSignal;
		}

		port def MissionFeedbackPort {
			attribute feedback: MissionFeedback;
		}

		port def TelemetryPort {
			attribute record: TelemetryRecord;
		}

		port def ProvenancePort {
			attribute reference: ProvenanceReference;
		}

		port def KnowledgeInsightPort {
			attribute insight: KnowledgeInsight;
		}

		part def User {
			attribute personaId: PersonaIdentifier;
			port clarificationOut: ClarificationExchangePort;
		}

		part def SwarmlordFacade {
			attribute personaName: PersonaIdentifier;
			attribute persistentMemory: PersistentMemoryFlag;
			attribute agentCapacity: ConcurrentAgentCapacity;
			port clarificationIn: ClarificationExchangePort;
			port missionIntentOut: MissionIntentPort;
			port missionFeedbackIn: MissionFeedbackPort;
			port telemetryIn: TelemetryPort;
			port provenanceIn: ProvenancePort;
			port insightsIn: KnowledgeInsightPort;
		}

		part def OrchestrationCore {
			attribute workflowSupport: WorkflowSupportIndicator;
			port missionIntentIn: MissionIntentPort;
			port taskSignalOut: TaskSignalPort;
		}

		part def SwarmExecutionFabric {
			attribute persistentAgentSpan: ConcurrentAgentCapacity;
			attribute hierarchyPattern: HierarchicalScalingPattern;
			attribute stigmergyEfficiency: StigmergyEfficiencyMetric;
			port taskSignalIn: TaskSignalPort;
			port missionFeedbackOut: MissionFeedbackPort;
			port telemetryOut: TelemetryPort;
			port provenanceOut: ProvenancePort;
			port insightsOut: KnowledgeInsightPort;
		}

		part def KnowledgeMemory {
			attribute knowledgeSupport: KnowledgeCapability;
			port insightsIn: KnowledgeInsightPort;
		}

		part def SignalEventSpine {
			attribute deliveryAssurance: DeliveryReliability;
			attribute stigmergyReadback: StigmergyEfficiencyMetric;
			port telemetryIn: TelemetryPort;
			port telemetryOut: TelemetryPort;
			port provenanceIn: ProvenancePort;
			port provenanceOut: ProvenancePort;
		}

		part def FeaturePolicyLayer {
			attribute featureSupport: FeaturePolicySupport;
		}

		part def ObservabilityGovernance {
			attribute telemetrySupport: TelemetrySupport;
			attribute provenanceSupport: ProvenanceSupport;
			port telemetryIn: TelemetryPort;
			port provenanceIn: ProvenancePort;
		}

		part def EvolutionOptimization {
			attribute qdSupport: QualityDiversitySupport;
		}

		part def SwarmlordAssembly {
			part user: User;
			part swarmlord: SwarmlordFacade;
			part orchestration: OrchestrationCore;
			part swarmFabric: SwarmExecutionFabric;
			part knowledgeStore: KnowledgeMemory;
			part signalSpine: SignalEventSpine;
			part policyLayer: FeaturePolicyLayer;
			part observability: ObservabilityGovernance;
			part evolution: EvolutionOptimization;

			// connect userIntentExchange user.clarificationOut -> swarmlord.clarificationIn
			// connect missionIntentFanout swarmlord.missionIntentOut -> orchestration.missionIntentIn
			// connect orchestrationDispatch orchestration.taskSignalOut -> swarmFabric.taskSignalIn
			// connect swarmFeedbackLoop swarmFabric.missionFeedbackOut -> swarmlord.missionFeedbackIn
			// connect swarmTelemetryFlow swarmFabric.telemetryOut -> signalSpine.telemetryIn
			// connect telemetryOversight signalSpine.telemetryOut -> observability.telemetryIn
			// connect swarmProvenanceFlow swarmFabric.provenanceOut -> signalSpine.provenanceIn
			// connect provenanceOversight signalSpine.provenanceOut -> observability.provenanceIn
			// connect insightBroadcast swarmFabric.insightsOut -> swarmlord.insightsIn
			// connect insightAbsorption swarmlord.insightsIn -> knowledgeStore.insightsIn
			// connect telemetryRelay signalSpine.telemetryOut -> swarmlord.telemetryIn
			// connect provenanceRelay signalSpine.provenanceOut -> swarmlord.provenanceIn
		}
	}

	package G28_Tooling {
		port def ToolingStatusPort {
			attribute smokeStatus: SmokeTestIndicator;
			attribute integrationStatus: HourglassIntegrationStatus;
		}

		port def MCPPolicyPort {
			attribute policy: MCPTrustProfile;
		}

		port def WorkflowBindingPort {
			attribute workflow: WorkflowEngineBinding;
			attribute temporalNs: TemporalNamespace;
			attribute langGraphProfile: LangGraphProfile;
			attribute eventSpine: EventSpineProfile;
			attribute parallelCompute: ParallelComputeProfile;
		}

		port def ObservabilityPort {
			attribute observability: ObservabilityProfile;
			attribute featureFlags: FeatureFlagProfile;
		}

		port def PersonaOutputPort {
			attribute personaSet: PersonaCatalog;
			attribute warChest: WarChestArtifact;
			attribute funding: FundingTelemetry;
		}

		part def IDEBaseline {
			attribute version: IDEVersionConstraint;
			attribute extensions: ExtensionBaseline;
			attribute runbook: ToolingRunbook;
			port statusOut: ToolingStatusPort;
		}

		part def MCPDeck {
			attribute trustProfile: MCPTrustProfile;
			port policyOut: MCPPolicyPort;
		}

		part def EnvironmentScaffold {
			attribute devContainer: DevContainerBlueprint;
			attribute workflowBinding: WorkflowEngineBinding;
			attribute temporal: TemporalNamespace;
			attribute langGraph: LangGraphProfile;
			attribute eventSpine: EventSpineProfile;
			attribute parallelCompute: ParallelComputeProfile;
			port workflowOut: WorkflowBindingPort;
		}

		part def AutomationRituals {
			attribute smokeIndicator: SmokeTestIndicator;
			attribute hourglassBinding: HourglassIntegrationStatus;
			port statusIn: ToolingStatusPort;
			port policyIn: MCPPolicyPort;
			port workflowIn: WorkflowBindingPort;
			port observabilityOut: ObservabilityPort;
			port statusOut: ToolingStatusPort;
		}

		part def PersonaForge {
			attribute catalog: PersonaCatalog;
			port observabilityIn: ObservabilityPort;
			port personaOut: PersonaOutputPort;
		}

		part def WarChestForge {
			attribute artifacts: WarChestArtifact;
			attribute fundingSignals: FundingTelemetry;
			port statusIn: ToolingStatusPort;
			port personaIn: PersonaOutputPort;
			port warChestOut: PersonaOutputPort;
		}

		part def ToolingAssembly {
			part ide: IDEBaseline;
			part mcp: MCPDeck;
			part environment: EnvironmentScaffold;
			part rituals: AutomationRituals;
			part persona: PersonaForge;
			part warChest: WarChestForge;

			// connect ideStatus ide.statusOut -> rituals.statusIn
			// connect mcpPolicy mcp.policyOut -> rituals.policyIn
			// connect workflowBinding environment.workflowOut -> rituals.workflowIn
			// connect ritualTelemetry rituals.observabilityOut -> persona.observabilityIn
			// connect personaCatalog persona.personaOut -> warChest.personaIn
			// connect ritualStatus rituals.statusOut -> warChest.statusIn
		}
	}

	// satisfy G28_REQ_001_PersistentSwarmlord by G28_Structure::SwarmlordAssembly::swarmlord
	// satisfy G28_REQ_002_HiveWorkflows by MissionLifecycle.SelectWorkflow
	// satisfy G28_REQ_003_PersistentSwarm by G28_Structure::SwarmExecutionFabric
	// satisfy G28_REQ_004_HierarchicalScaling by G28_Structure::SwarmExecutionFabric
	// satisfy G28_REQ_005_StigmergyEfficiency by G28_Structure::SignalEventSpine
	// satisfy ClarificationSequence by MissionLifecycle
	// satisfy StigmergicControl by G28_Structure::SwarmlordAssembly::signalSpine
	// satisfy G28_REQ_006_ToolingBaseline by G28_Tooling::ToolingAssembly
	// satisfy G28_REQ_007_MCPTrustGuardrails by G28_Tooling::MCPDeck
	// satisfy G28_REQ_008_HourglassWorkflowBridge by G28_Tooling::EnvironmentScaffold
	// satisfy G28_REQ_009_PersonaWarChest by G28_Tooling::PersonaForge
	// satisfy G28_REQ_008_HourglassWorkflowBridge by HourglassSwarmBridge
	// satisfy G28_REQ_009_PersonaWarChest by PersonaWarChestPipeline.ForgeWarChestArtifacts

	/* Mission orchestration pipeline for the persistent Swarmlord */
	action MissionLifecycle {
		action CaptureIntent {
			out clarification : ClarificationArtifact;
		}

		action ClarifyMission1 {
			in prior : ClarificationArtifact;
			out clarification : ClarificationArtifact;
		}

		action ClarifyMission2 {
			in prior : ClarificationArtifact;
			out clarification : ClarificationArtifact;
		}

		action SelectWorkflow {
			in clarification : ClarificationArtifact;
			out selection : WorkflowSelection;
		}

		action PublishMissionIntent {
			in selection : WorkflowSelection;
			out missionIntent : MissionIntentArtifact;
		}

		action DeployOrchestration {
			in missionIntent : MissionIntentArtifact;
			out taskSignal : TaskSignal;
		}

		action CoordinateSwarm {
			in taskSignal : TaskSignal;
			out missionFeedback : MissionFeedback;
			out telemetry : TelemetryRecord;
			out provenance : ProvenanceReference;
			out insights : KnowledgeInsight;
		}

		action ValidateResults {
			in missionFeedback : MissionFeedback;
			in telemetry : TelemetryRecord;
			in provenance : ProvenanceReference;
			out digest : MissionDigest;
		}

		action DeliverOutcome {
			in digest : MissionDigest;
		}

		action UpdateKnowledge {
			in insights : KnowledgeInsight;
		}

		succession flow intent_to_clarify1 from CaptureIntent.clarification to ClarifyMission1.prior;
		succession flow clarify1_to_clarify2 from ClarifyMission1.clarification to ClarifyMission2.prior;
		succession flow clarify2_to_select from ClarifyMission2.clarification to SelectWorkflow.clarification;
		succession flow select_to_publish from SelectWorkflow.selection to PublishMissionIntent.selection;
		succession flow publish_to_deploy from PublishMissionIntent.missionIntent to DeployOrchestration.missionIntent;
		succession flow deploy_to_coordinate from DeployOrchestration.taskSignal to CoordinateSwarm.taskSignal;
		succession flow coordinate_to_validate from CoordinateSwarm.missionFeedback to ValidateResults.missionFeedback;
		succession flow coordinate_telemetry_to_validate from CoordinateSwarm.telemetry to ValidateResults.telemetry;
		succession flow coordinate_provenance_to_validate from CoordinateSwarm.provenance to ValidateResults.provenance;
		succession flow validate_to_deliver from ValidateResults.digest to DeliverOutcome.digest;
		succession flow coordinate_to_update from CoordinateSwarm.insights to UpdateKnowledge.insights;
	}

	/* Workflow selection logic for the Swarmlord persona */
	action WorkflowSelectionStateMachine {
		action AssessContext {
			out selection : WorkflowSelection;
		}

		action ApplyHiveLoop {
			in selection : WorkflowSelection;
		}

		action ApplyGrowthLoop {
			in selection : WorkflowSelection;
		}

		action ApplySwarmLoop {
			in selection : WorkflowSelection;
		}

		action ApplyPreyLoop {
			in selection : WorkflowSelection;
		}

		succession flow assess_to_hive from AssessContext.selection to ApplyHiveLoop.selection;
		succession flow assess_to_growth from AssessContext.selection to ApplyGrowthLoop.selection;
		succession flow assess_to_swarm from AssessContext.selection to ApplySwarmLoop.selection;
		succession flow assess_to_prey from AssessContext.selection to ApplyPreyLoop.selection;
	}

	/* Tooling enablement aligned with the IDE modernization report */
	action ToolingEnablementLifecycle {
		action BaselineIDEStack {
			out status : SmokeTestIndicator;
			out runbook : ToolingRunbook;
		}

		action ConfigureMCPDeck {
			out policy : MCPTrustProfile;
		}

		action ScaffoldEnvironment {
			out workflowBinding : WorkflowEngineBinding;
			out temporalNs : TemporalNamespace;
			out langGraphProfile : LangGraphProfile;
			out eventSpineProfile : EventSpineProfile;
			out parallelProfile : ParallelComputeProfile;
		}

		action RunToolingSmokeTest {
			in status : SmokeTestIndicator;
			in policy : MCPTrustProfile;
			in workflowBinding : WorkflowEngineBinding;
			out verified : SmokeTestIndicator;
			out integration : HourglassIntegrationStatus;
		}

		action RegisterRituals {
			in verified : SmokeTestIndicator;
			in integration : HourglassIntegrationStatus;
			in runbook : ToolingRunbook;
			in policy : MCPTrustProfile;
			in temporalNs : TemporalNamespace;
			in langGraphProfile : LangGraphProfile;
			in eventSpineProfile : EventSpineProfile;
			in parallelProfile : ParallelComputeProfile;
		}

		succession flow baseline_to_smoke from BaselineIDEStack.status to RunToolingSmokeTest.status;
		succession flow baseline_runbook_to_register from BaselineIDEStack.runbook to RegisterRituals.runbook;
		succession flow mcp_to_smoke from ConfigureMCPDeck.policy to RunToolingSmokeTest.policy;
		succession flow mcp_to_register from ConfigureMCPDeck.policy to RegisterRituals.policy;
		succession flow environment_to_smoke from ScaffoldEnvironment.workflowBinding to RunToolingSmokeTest.workflowBinding;
		succession flow environment_temporal_to_register from ScaffoldEnvironment.temporalNs to RegisterRituals.temporalNs;
		succession flow environment_langgraph_to_register from ScaffoldEnvironment.langGraphProfile to RegisterRituals.langGraphProfile;
		succession flow environment_eventSpine_to_register from ScaffoldEnvironment.eventSpineProfile to RegisterRituals.eventSpineProfile;
		succession flow environment_parallel_to_register from ScaffoldEnvironment.parallelProfile to RegisterRituals.parallelProfile;
		succession flow smoke_to_register from RunToolingSmokeTest.verified to RegisterRituals.verified;
		succession flow integration_to_register from RunToolingSmokeTest.integration to RegisterRituals.integration;
	}

	/* Bridge hourglass briefs into swarm-ready workflows */
	action HourglassSwarmBridge {
		action CaptureHourglassBrief {
			out artifact : PresentArtifact;
			out risk : RiskProfile;
			out cost : CostProfile;
			out confidence : ConfidenceScore;
		}

		action BindWorkflowInterfaces {
			in artifact : PresentArtifact;
			out workflowBinding : WorkflowEngineBinding;
			out temporalNs : TemporalNamespace;
			out langGraphProfile : LangGraphProfile;
			out eventSpineProfile : EventSpineProfile;
			out parallelProfile : ParallelComputeProfile;
		}

		action ScheduleTemporalWorkflows {
			in workflowBinding : WorkflowEngineBinding;
			in temporalNs : TemporalNamespace;
			out missionSignal : MissionSignal;
		}

		action ActivateSwarmBridge {
			in missionSignal : MissionSignal;
			in langGraphProfile : LangGraphProfile;
			in eventSpineProfile : EventSpineProfile;
			in parallelProfile : ParallelComputeProfile;
			in risk : RiskProfile;
			in cost : CostProfile;
			in confidence : ConfidenceScore;
			out digest : MissionDigest;
		}

		action PublishPersonaBrief {
			in digest : MissionDigest;
			out personas : PersonaCatalog;
			out warChest : WarChestArtifact;
			out funding : FundingTelemetry;
		}

		succession flow brief_to_bind from CaptureHourglassBrief.artifact to BindWorkflowInterfaces.artifact;
		succession flow bind_to_schedule from BindWorkflowInterfaces.workflowBinding to ScheduleTemporalWorkflows.workflowBinding;
		succession flow bind_temporal_to_schedule from BindWorkflowInterfaces.temporalNs to ScheduleTemporalWorkflows.temporalNs;
		succession flow schedule_to_activate from ScheduleTemporalWorkflows.missionSignal to ActivateSwarmBridge.missionSignal;
		succession flow bind_langgraph_to_activate from BindWorkflowInterfaces.langGraphProfile to ActivateSwarmBridge.langGraphProfile;
		succession flow bind_eventSpine_to_activate from BindWorkflowInterfaces.eventSpineProfile to ActivateSwarmBridge.eventSpineProfile;
		succession flow bind_parallel_to_activate from BindWorkflowInterfaces.parallelProfile to ActivateSwarmBridge.parallelProfile;
		succession flow risk_to_activate from CaptureHourglassBrief.risk to ActivateSwarmBridge.risk;
		succession flow cost_to_activate from CaptureHourglassBrief.cost to ActivateSwarmBridge.cost;
		succession flow confidence_to_activate from CaptureHourglassBrief.confidence to ActivateSwarmBridge.confidence;
		succession flow digest_to_publish from ActivateSwarmBridge.digest to PublishPersonaBrief.digest;
	}

	/* Persona and war chest reinforcement */
	action PersonaWarChestPipeline {
		action HarvestPersonaInsights {
			in digest : MissionDigest;
			out personas : PersonaCatalog;
		}

		action ForgeWarChestArtifacts {
			in personas : PersonaCatalog;
			out warChest : WarChestArtifact;
			out funding : FundingTelemetry;
		}

		action ArchivePersonaRunbook {
			in personas : PersonaCatalog;
			in warChest : WarChestArtifact;
			in funding : FundingTelemetry;
		}

		succession flow insights_to_forge from HarvestPersonaInsights.personas to ForgeWarChestArtifacts.personas;
		succession flow insights_to_archive from HarvestPersonaInsights.personas to ArchivePersonaRunbook.personas;
		succession flow warChest_to_archive from ForgeWarChestArtifacts.warChest to ArchivePersonaRunbook.warChest;
		succession flow funding_to_archive from ForgeWarChestArtifacts.funding to ArchivePersonaRunbook.funding;
	}

}
