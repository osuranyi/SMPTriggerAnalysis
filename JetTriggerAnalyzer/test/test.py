import FWCore.ParameterSet.Config as cms

process = cms.Process("Ana")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = '112X_mcRun3_2021_realistic_v16'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100000) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
          #'file:miniaodsim_2021.root'
          'file:HLT2_HLT.root'
          )
        )

process.TFileService = cms.Service("TFileService",
                                      fileName=cms.string("test.root"))

process.hltanalyzer = cms.EDAnalyzer('JetTriggerAnalyzer',
                 hltresults = cms.InputTag("TriggerResults","","HLT"),
                 #jets = cms.InputTag("ak4PFJetsCHS")
                 jets = cms.InputTag("slimmedJetsAK8","","RECO")
                 )

process.p = cms.Path(process.hltanalyzer)
