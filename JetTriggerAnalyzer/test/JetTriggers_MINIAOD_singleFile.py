# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('Ana',Run3)

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '124X_dataRun3_Prompt_v4', '')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2022C/ZeroBias/MINIAOD/PromptReco-v1/000/356/003/00000/3aa41dcd-8182-4761-bee9-4a149605f352.root')
      #'root://cmsxrootd.fnal.gov//store/data/Run2022B/ZeroBias/MINIAOD/PromptReco-v1/000/355/680/00000/17090530-d453-4e5c-9349-29f0f8b0631e.root'),
)

########################
# ADDING ANALYZER HERE #
########################

process.TFileService = cms.Service("TFileService",
                                      fileName=cms.string("test.root"))

process.hltanalyzer = cms.EDAnalyzer('JetTriggerAnalyzer',
                 hltresults = cms.InputTag("TriggerResults","","HLT"),
                 stageL1Trigger = cms.uint32(2),
                 jets = cms.InputTag("slimmedJets","","RECO"),
                 jets_ak8 = cms.InputTag("slimmedJetsAK8","","RECO"),
                 photons = cms.InputTag("slimmedPhotons","","RECO")
                 )

process.analyzer_step = cms.Path(process.hltanalyzer)



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
#from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
#process = customiseEarlyDelete(process)
# End adding early deletion
