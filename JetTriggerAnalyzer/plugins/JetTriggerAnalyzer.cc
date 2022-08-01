// -*- C++ -*-
//
// Package:    FSQ/JetTriggerAnalyzer
// Class:      JetTriggerAnalyzer
// 
/**\class JetTriggerAnalyzer JetTriggerAnalyzer.cc FSQ/JetTriggerAnalyzer/plugins/JetTriggerAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Oliver Suranyi
//         Created:  Wed, 06 Dec 2017 17:12:48 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"

#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Photon.h"

#include "TTree.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

const static int Max = 200;
const static int TrigMax = 1000;

const static int nJetTrig = 9;

const static int caloJetThresholds[9] = {40,50,110,170,210,270,350,400,450};

class JetTriggerAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources, edm::one::WatchRuns> {
   public:
      explicit JetTriggerAnalyzer(const edm::ParameterSet&);
      ~JetTriggerAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void beginRun(const edm::Run&, const edm::EventSetup&) override;
      virtual void endRun(const edm::Run&, const edm::EventSetup&) override {}
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------

      HLTPrescaleProvider hltPrescaleProvider_;
      std::string trgResultsProcess_;
      edm::InputTag trigResultsTag_;

      edm::EDGetTokenT<edm::TriggerResults> token_hlt;
      edm::EDGetTokenT<edm::TriggerResults> token_hlt_rerun;

      edm::EDGetTokenT<std::vector<pat::Jet>> token_jets;
      edm::EDGetTokenT<std::vector<pat::Jet>> token_jets_ak8;

      edm::EDGetTokenT<std::vector<pat::Photon>> token_photons;

      std::vector<edm::EDGetTokenT<std::vector<pat::Jet>>> token_hltjets;

      TTree* Events;

      int evt, run, lumi;
      bool firstEvent;
      int* trigflag;
      int* hlt_prsc;
      int* l1_prsc;

      int jetmult;
      float pt[Max];
      float eta[Max];
      float phi[Max];

      int jetmult_ak8;
      float pt_ak8[Max];
      float eta_ak8[Max];
      float phi_ak8[Max];

      int phomult;
      float et_pho[Max];
      float e_pho[Max];
      float eta_pho[Max];
      float phi_pho[Max];

      float hOverE_pho[Max];

      float iso_ChargedHadron_pho[Max];
      float iso_NeutralHadron_pho[Max];
      float iso_Photon_pho[Max];

      /*int hltjetmult[nJetTrig];
      float pt_hlt[nJetTrig][Max];
      float eta_hlt[nJetTrig][Max];
      float phi_hlt[nJetTrig][Max];*/
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
JetTriggerAnalyzer::JetTriggerAnalyzer(const edm::ParameterSet& iConfig) : hltPrescaleProvider_(iConfig, consumesCollector(), *this){
  //now do what ever initialization is needed
  usesResource("TFileService");

  trigResultsTag_ = iConfig.getParameter<edm::InputTag>("hltresults");
  token_hlt = consumes<edm::TriggerResults>(trigResultsTag_);
  token_jets = consumes<std::vector<pat::Jet>>(iConfig.getParameter<edm::InputTag>("jets"));
  token_jets_ak8 = consumes<std::vector<pat::Jet>>(iConfig.getParameter<edm::InputTag>("jets_ak8")); 
  token_photons = consumes<std::vector<pat::Photon>>(iConfig.getParameter<edm::InputTag>("photons"));

  /*for(int i = 0; i < nJetTrig; i++){
    token_hltjets.push_back(consumes<std::vector<pat::Jet>>(iConfig.getParameter<edm::InputTag>("hltjets_"+std::to_string(caloJetThresholds[i]) ) ));
    std::cout << "hltjets_"+std::to_string(caloJetThresholds[i]) << std::endl;
  }*/
}


JetTriggerAnalyzer::~JetTriggerAnalyzer(){}


//
// member functions
//

void JetTriggerAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup){
  bool changed=false;
  hltPrescaleProvider_.init(iRun,iSetup,trigResultsTag_.process(),changed);
  std::cout << "beginRun called" << std::endl;
}


// ------------ method called for each event  ------------
void
JetTriggerAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){


  using namespace edm;

  evt = iEvent.id().event();
  run = iEvent.id().run();
  lumi = iEvent.luminosityBlock();


  ///////////////////////////////////////
  // Checking original trigger results //
  ///////////////////////////////////////

  edm::Handle<edm::TriggerResults> hltresults;
  iEvent.getByToken(token_hlt,hltresults);

  if(!hltresults.isValid())
    return;

  edm::TriggerNames const& triggerNames = iEvent.triggerNames(*hltresults);

 // bool cfg_changed = true;
 // hltPrescaleProvider_.init(iEvent.getRun(), iSetup, trgResultsProcess_, cfg_changed);
  //HLTConfigProvider const&  hltCfg = hltPrescaleProvider_.hltConfigProvider();

  int ntrigs = hltresults->size();
  //std::set<int> indices;

  //std::cout << "a" << std::endl;

  if(firstEvent){
    int n = 0;
    for(int itrig = 0; itrig != ntrigs; ++itrig) {
      TString trigName = triggerNames.triggerName(itrig);
      //if(trigName.BeginsWith("HLT_DiPFJet") || trigName.BeginsWith("HLT_AK8PFJet")  || trigName.BeginsWith("HLT_PFJet") || trigName.BeginsWith("HLT_Photon")){
        Events->Branch(trigName+"_acc", trigflag+n, trigName+"_acc/I");
        Events->Branch(trigName+"_hltpsc", hlt_prsc+n, trigName+"_hltpsc/I");
        Events->Branch(trigName+"_l1psc", l1_prsc+n, trigName+"_l1psc/I");
        n++;
      //}
    }
    firstEvent = false;
    std::cout << n << std::endl;
  }

  int n = 0;
  for(int itrig = 0; itrig != ntrigs; ++itrig){
    TString trigName = triggerNames.triggerName(itrig);
    //if(trigName.BeginsWith("HLT_DiPFJet") || trigName.BeginsWith("HLT_AK8PFJet")  || trigName.BeginsWith("HLT_PFJet") || trigName.BeginsWith("HLT_Photon")){
      trigflag[n] = (hltresults->accept(itrig)) ? 1 : 0;
      int l1_prescale = hltPrescaleProvider_.prescaleValues(iEvent,iSetup,trigName.Data()).first;
      int hlt_prescale = hltPrescaleProvider_.prescaleValues(iEvent,iSetup,trigName.Data()).second; 
      hlt_prsc[n] = hlt_prescale;
      l1_prsc[n] = l1_prescale;
      n++;
    //}
  }


  // Get jets
  jetmult = 0; 
  
  edm::Handle<std::vector<pat::Jet>> jets;
  iEvent.getByToken(token_jets,jets);

  for(auto jet = jets->begin(); jet != jets->end(); ++jet){
    pt[jetmult] = jet->pt();
    eta[jetmult] = jet->eta();
    phi[jetmult] = jet->phi();

    jetmult++;
  } 

  // Get AK8 jets
  jetmult_ak8 = 0; 
  
  edm::Handle<std::vector<pat::Jet>> jets_ak8;
  iEvent.getByToken(token_jets_ak8,jets_ak8);

  for(auto jet = jets_ak8->begin(); jet != jets_ak8->end(); ++jet){
    pt_ak8[jetmult_ak8] = jet->pt();
    eta_ak8[jetmult_ak8] = jet->eta();
    phi_ak8[jetmult_ak8] = jet->phi();

    jetmult_ak8++;
  }

  // Get Photons
  phomult = 0;

  edm::Handle<std::vector<pat::Photon>> photons;
  iEvent.getByToken(token_photons,photons);

  for(auto photon = photons->begin(); photon != photons->end(); ++photon){
    et_pho[phomult] = photon->energy();
    e_pho[phomult] = photon->et();
    eta_pho[phomult] = photon->eta();
    phi_pho[phomult] = photon->phi();

    hOverE_pho[phomult] = photon->hadTowOverEm();

    iso_ChargedHadron_pho[phomult] = photon->chargedHadronIso();
    iso_NeutralHadron_pho[phomult] = photon->neutralHadronIso();
    iso_Photon_pho[phomult]        = photon->photonIso();
  
    phomult++;
  }

  //std::cout << "c" << std::endl;
  if(jetmult >= 1 || jetmult_ak8 >= 1 || phomult >= 1)
    Events->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void 
JetTriggerAnalyzer::beginJob(){
  edm::Service<TFileService> fs;
  Events = fs->make<TTree>("Events", "");
  Events->Branch("evt",&evt,"evt/I");
  Events->Branch("run",&run,"run/I");
  Events->Branch("lumi",&lumi,"lumi/I");

  Events->Branch("jetmult",&jetmult,"jetmult/I");
  Events->Branch("pt",pt,"pt[jetmult]/F");
  Events->Branch("eta",eta,"eta[jetmult]/F");
  Events->Branch("phi",phi,"phi[jetmult]/F");

  Events->Branch("jetmult_ak8",&jetmult_ak8,"jetmult_ak8/I");
  Events->Branch("pt_ak8",pt_ak8,"pt_ak8[jetmult_ak8]/F");
  Events->Branch("eta_ak8",eta_ak8,"eta_ak8[jetmult_ak8]/F");
  Events->Branch("phi_ak8",phi_ak8,"phi_ak8[jetmult_ak8]/F");

  Events->Branch("phomult",&phomult,"phomult/I");
  Events->Branch("et_pho",et_pho,"et_pho[phomult]/F");
  Events->Branch("e_pho",e_pho,"e_pho[phomult]/F");
  Events->Branch("eta_pho",eta_pho,"eta_pho[phomult]/F");
  Events->Branch("phi_pho",phi_pho,"phi_pho[phomult]/F");

  Events->Branch("hOverE_pho",hOverE_pho,"hOverE_pho[phomult]/F");
  Events->Branch("iso_ChargedHadron_pho",iso_ChargedHadron_pho,"iso_ChargedHadron_pho[phomult]/F");
  Events->Branch("iso_NeutralHadron_pho",iso_NeutralHadron_pho,"iso_NeutralHadron_pho[phomult]/F");
  Events->Branch("iso_Photon_pho",iso_Photon_pho,"iso_Photon_pho[phomult]/F");

  /*for(int i = 0; i < 9; i++){
    Events->Branch(("hltjetmult_"+std::to_string(caloJetThresholds[i])).c_str(),&(hltjetmult[i]),("hltjetmult_"+std::to_string(caloJetThresholds[i])+"/I").c_str());
    Events->Branch(("pt_hlt_"+std::to_string(caloJetThresholds[i])).c_str(),pt_hlt[i],("pt_hlt_"+std::to_string(caloJetThresholds[i])+"[hltjetmult_"+std::to_string(caloJetThresholds[i])+"]/F").c_str());
    Events->Branch(("eta_hlt_"+std::to_string(caloJetThresholds[i])).c_str(),eta_hlt[i],("eta_hlt_"+std::to_string(caloJetThresholds[i])+"[hltjetmult_"+std::to_string(caloJetThresholds[i])+"]/F").c_str());
    Events->Branch(("phi_hlt_"+std::to_string(caloJetThresholds[i])).c_str(),phi_hlt[i],("phi_hlt_"+std::to_string(caloJetThresholds[i])+"[hltjetmult_"+std::to_string(caloJetThresholds[i])+"]/F").c_str());
  }*/

  firstEvent = true;

  //const int Max = 200;
  trigflag = new int[TrigMax];
  hlt_prsc = new int[TrigMax];
  l1_prsc = new int[TrigMax];
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetTriggerAnalyzer::endJob(){
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetTriggerAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetTriggerAnalyzer);
