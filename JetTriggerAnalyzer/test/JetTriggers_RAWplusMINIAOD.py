# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: HLT2 --step=HLT:JetTriggersNewTracking --era=Run3 --mc --conditions auto:phase1_2021_realistic --filein root://cms-xrd-global.cern.ch///store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/MINIAODSIM/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/1fb87340-34b4-4c8a-a049-33192b21d54b.root --secondfilein root://cms-xrd-global.cern.ch///store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/003cee26-b0ed-4491-a301-f3261420b157.root --processName=HLT2 --python_filename=JetTriggers_RAWplusMINIAOD.py -n 100 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('HLT2',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('HLTrigger.Configuration.HLT_JetTriggersNewTracking_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/MINIAODSIM/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/1fb87340-34b4-4c8a-a049-33192b21d54b.root'),
    secondaryFileNames = cms.untracked.vstring('/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/003cee26-b0ed-4491-a301-f3261420b157.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/08f9d5ad-7a1c-4440-ac2f-f71c84d6f525.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/0bd11d4d-1967-4973-80ad-0b962d2669c5.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/0e0481b5-1c39-4eda-a1de-0e2254f52a9c.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/2045ffa9-fbd3-4153-bc38-207b607304cb.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/236704cf-462c-47ec-a8b3-6147ff0f4be9.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/23dc9f4b-488c-4f9b-82dd-9c982a7cd449.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/2c2c1b8c-3378-44da-87e5-bd3b4f948d22.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/4fea1664-d8db-43bd-bfad-cd94126424d3.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/5556d434-1dd5-434a-bccd-a0bc5f277152.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/5561b0cb-fe04-4c02-881f-295e558c5444.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/5f8f1d6d-6210-42ab-b8ee-0b00aacdd8e1.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/600ff5f5-716d-49b5-b728-f8376f84ceb0.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/6742997d-3d24-4deb-8365-61b6abc87ca4.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/6cbfb800-3d15-488a-954f-0feb585d37a5.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/755bff65-36b9-4172-ac83-f4e2685b53b4.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/87b78df9-1cf3-4ab7-806e-58f748112d2f.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/991c0347-412d-43eb-b219-b28af01e067f.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/ac7addf7-cbd6-434b-b8b3-8f56407deecd.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/ae75c926-22a1-4d3e-b0b0-7fc2a67c9fb5.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/b259fb57-968d-4aef-b27d-c2fc03aaea27.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/b5799868-5a40-48f3-83ca-b6f59d666565.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/c0640f64-da4d-49b0-87f5-e25f02277eef.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/c1ae0140-d077-4d40-a895-87852244210f.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/ce4c3976-70d7-4d77-aa43-dfeb2eb32f4f.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/ce6ebc04-d829-42d8-88f6-9a7259809f79.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/cf182551-397e-424f-aa9b-190e1003ec38.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/d34ff4b3-ce41-47f7-8f83-9ddcd95122c3.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/d428f27f-2d2f-4e46-a005-92a7f4199fd7.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/d6f2e27b-c502-4fcd-812d-a96280814cca.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/f2bf3602-f0d9-4ddc-9503-e1deefa9a8d8.root' ,
      '/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/120000/fff0e03b-c95e-41b9-b72e-fa6f163d6308.root' )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
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
    annotation = cms.untracked.string('HLT2 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('HLT2_HLT.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

########################
# ADDING ANALYZER HERE #
########################

process.TFileService = cms.Service("TFileService",
                                      fileName=cms.string("test.root"))

process.hltanalyzer = cms.EDAnalyzer('JetTriggerAnalyzer',
                 hltresults = cms.InputTag("TriggerResults","","HLT2"),
                 #hltresults_rerun = cms.InputTag("TriggerResults","","HLT2"),
                 #jets = cms.InputTag("ak4PFJetsCHS")
                 jets = cms.InputTag("slimmedJetsAK8","","RECO")
                 )

process.analyzer_step = cms.Path(process.hltanalyzer)

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.extend([process.endjob_step,process.RECOSIMoutput_step])
#process.schedule.extend([process.endjob_step,process.RECOSIMoutput_step,process.analyzer_step])
#process.schedule.extend([process.analyzer_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
