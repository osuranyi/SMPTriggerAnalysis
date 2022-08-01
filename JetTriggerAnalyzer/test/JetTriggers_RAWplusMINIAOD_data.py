# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: HLT2 --step=L1REPACK:uGT,HLT:GRun_Data --data --conditions 124X_dataRun3_HLT_v4 --filein root://cms-xrd-global.cern.ch//store/data/Run2022C/ZeroBias/MINIAOD/PromptReco-v1/000/356/003/00000/b846c296-fc5c-4e3e-a1f1-3921a7163eb9.root --secondfilein root://cms-xrd-global.cern.ch//store/data/Run2022C/ZeroBias/RAW/v1/000/356/003/00000/92f5ad8d-54ec-4e6c-991b-1ae82b28f3e8.root,root://cms-xrd-global.cern.ch//store/data/Run2022C/ZeroBias/RAW/v1/000/356/003/00000/b2f5f909-d698-431f-bf23-a4cd68328bba.root,root://cms-xrd-global.cern.ch//store/data/Run2022C/ZeroBias/RAW/v1/000/356/003/00000/fd38b424-ff75-45d2-bdbc-b755b7c949aa.root --processName=HLT2 --python_filename=JetTriggers_RAWplusMINIAOD_data.py -n 10 --no_exec --era Run3
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('HLT2',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorRepack_uGT_cff')
process.load('HLTrigger.Configuration.HLT_GRun_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/data/Run2022C/ZeroBias/MINIAOD/PromptReco-v1/000/356/003/00000/b846c296-fc5c-4e3e-a1f1-3921a7163eb9.root'),
    secondaryFileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/data/Run2022C/ZeroBias/RAW/v1/000/356/003/00000/92f5ad8d-54ec-4e6c-991b-1ae82b28f3e8.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2022C/ZeroBias/RAW/v1/000/356/003/00000/b2f5f909-d698-431f-bf23-a4cd68328bba.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2022C/ZeroBias/RAW/v1/000/356/003/00000/fd38b424-ff75-45d2-bdbc-b755b7c949aa.root'
    )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('HLT2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('HLT2_L1REPACK_HLT.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '124X_dataRun3_HLT_v4', '')

# Path and EndPath definitions
process.L1RePack_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

process.TFileService = cms.Service("TFileService",
                                      fileName=cms.string("test.root"))

process.hltanalyzer = cms.EDAnalyzer('JetTriggerAnalyzer',
                 hltresults = cms.InputTag("TriggerResults","","HLT2"),
                 stageL1Trigger = cms.uint32(2),
                 jets = cms.InputTag("slimmedJets","","RECO"),
                 jets_ak8 = cms.InputTag("slimmedJetsAK8","","RECO"),
                 photons = cms.InputTag("slimmedPhotons","","RECO")
                 )

process.analyzer_step = cms.EndPath(process.hltanalyzer)



# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.insert(0, process.L1RePack_step)
process.schedule.extend([process.endjob_step,process.analyzer_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
