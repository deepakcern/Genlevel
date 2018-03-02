// -*- C++ -*-
//
// Package:    MonoHGenTree/MonoHGenTree2DScans
// Class:      MonoHGenTree2DScans
// 
/**\class MonoHGenTree2DScans MonoHGenTree2DScans.cc MonoHGenTree/MonoHGenTree2DScans/plugins/MonoHGenTree2DScans.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Raman Khurana (CMS Tau; Saha Institute of Nuclear Physics
//         Created:  Wed, 28 Jun 2017 15:56:22 GMT
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
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "TH2.h"
#include "TH1.h"
#include "TFile.h"
#include "TTree.h"
#include "TLorentzVector.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class MonoHGenTree2DScans : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
public:
  explicit MonoHGenTree2DScans(const edm::ParameterSet&);
  ~MonoHGenTree2DScans();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  edm::EDGetTokenT<reco::GenParticleCollection>     genParticleToken;
  edm::EDGetTokenT<LHEEventProduct>                 lheEventToken;
  //TFile* file;
  //TTree* tree;
  TH1D *h_bpt;
  TH1D *h_beta;
  TH1D *h_bphi;
  TH1D *h_bbarpt;
  TH1D *h_bbareta;
  TH1D *h_higgsphi;
  TH1D *h_higgsmass;
  TH1D *h_higgsinvm;
  TH1D *h_deta;
  TH1D *h_dphi;
  TH1D *h_DR;
  TH1D *h_higgseta;
  TH1D *h_higgspt;
  TH1D *h_bbarphi;
  TH1D *h_eta1eta2;
  TH2D *h_DR_vs_Higgspt;
  




  TTree* tree_;
  double n_h_deta;
  double n_deltaR; 
  float HiggsMass;
  float jet1eta;
  float jet2eta;
  float jet1pt;
  float jet2pt;
  float Higgs_invMass;
  float HiggsPt;
  float trueMET;
  float HiggsEta;
   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

    
  // ----------member data ---------------------------
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
MonoHGenTree2DScans::MonoHGenTree2DScans(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   usesResource("TFileService");
   lheEventToken            = consumes<LHEEventProduct>(edm::InputTag("externalLHEProducer"));
   genParticleToken         = consumes<reco::GenParticleCollection>(edm::InputTag("genParticles"));
   
   edm::Service<TFileService> fs;
   tree_ = fs->make<TTree>("tree_","tree");
   h_bpt = fs->make<TH1D>("bjet_pt", "bjet_pt", 1000, 0, 1000);
   h_beta = fs->make<TH1D>("bjet_eta", "bjet_eta", 60,-3.5,3.5 );
   h_bphi = fs->make<TH1D>("bjet_phi", "bjet_phi", 60, -4, 4);
   h_bbarpt = fs->make<TH1D>("bbarjet_pt", "bbarjet_pt", 1000, 0, 1000);
   h_bbareta = fs->make<TH1D>("bbarjet_eta", "bbbarjet_eta", 60, -3.5, 3.5);
   h_bbarphi = fs->make<TH1D>("bbarjet_phi", "bbarjet_phi", 60, -3.5, 3.5);
   h_higgspt = fs->make<TH1D>("higgs_pt", "higgs_pt", 1000, 0, 1000);
   h_higgseta = fs->make<TH1D>("higgs_eta", "higgs_eta", 100, -5, 5);
   h_higgsphi = fs->make<TH1D>("higgs_phi", "higgs_phi", 50, -4, 4);
   h_higgsmass = fs->make<TH1D>("higgs_mass", "higgs_mass", 1000, 0, 500);
   h_higgsinvm = fs->make<TH1D>("higgs_invmass", "higgs_invmass", 1000, 0, 500);
   h_deta = fs->make<TH1D>("delta_eta", "delta_eta", 100,-3.5 , 3.5);
   h_dphi = fs->make<TH1D>("delta_phi", "delta_phi", 60,-4 , 4);
   h_DR = fs->make<TH1D>("DR", "DR", 50, 0, 7);
   h_eta1eta2 = fs->make<TH1D>("eta1*eta2", "eta1eta2", 100, -25, 25); 
   h_DR_vs_Higgspt = fs->make<TH2D>("DR_Vs_Higgspt","DR_Vs_Higgspt",1000,0,1000,100,0,7);  
   
}


MonoHGenTree2DScans::~MonoHGenTree2DScans()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
MonoHGenTree2DScans::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
   using namespace edm;
   edm::Handle<reco::GenParticleCollection> genParticleHandle;
   if(not iEvent.getByToken(genParticleToken, genParticleHandle))
     {
       std::cout<<
	 "GenAnalyzer: Generator Level Information not found\n"
	        <<std::endl;
     }
   
   //auto Higgs=0;
   //auto vV=0;
   TLorentzVector Higgs;
   TLorentzVector vV;
   TLorentzVector  bjet;
   TLorentzVector  bbarjet;   

   std::vector<TLorentzVector> jets;

   bool found_VBFjet1 = false;
   bool found_VBFjet2 = false;
   bool found_b = false;
   bool found_bbar = false; 
   bool found_higgs = false;
   bool found_a0 = false;
   
   std::vector<const reco::Candidate*> cands;
   std::vector<std::vector<reco::GenParticle>::const_iterator> myParticles;
   int idm = 0;
   HiggsMass=-99.;
   jet1eta=-99.;
   jet2eta=-99.;
   jet1pt=-99.;
   jet2pt=-99.;
  // double a=-99.;
   //Higgs_invMass=;
   HiggsPt = -99.;
   trueMET = -99.;
   HiggsEta = -99.; 
   for( std::vector<reco::GenParticle>::const_iterator it_gen = genParticleHandle->begin(); it_gen != genParticleHandle->end(); it_gen++ )    {
     reco::GenParticle gen = *it_gen;
     //std::cout << gen.size() <<"this is no of particles size" << std::endl; 
    // std::cout << "mother:   " << gen.mother(1)  <<std::endl; 
     //  std::cout<<" px = "<<gen.px()<<std::endl;
     //std::cout << "status: "<<gen.status() <<std::endl;
     /*if (gen.status()==21){
             //    std::cout << "hellow" << std::endl;
              //   std::cout <<"pdgId:  "<<gen.pdgId()<<std::endl;
                 
            //    bjet.SetPxPyPzE(gen.px(), gen.py(), gen.pz(), gen.energy());
              //  jets.push_back(bjet);
                 }

     if (gen.status()==23){

      std::cout<<"pdgId: " << gen.pdgId() << std::endl;
      VBFjets.SetPxPyPzE(gen.px(), gen.py(), gen.pz(), gen.energy());
      jets.push_back(VBFjets);
    

        }*/

     //if (found_b && found_bbar)  break;  
     if ( found_higgs && found_b && found_bbar)    break;
     
     if (abs(gen.pdgId())==25){
       if (!found_higgs){
	 Higgs.SetPxPyPzE(gen.px(), gen.py(), gen.pz(), gen.energy());
        /* std::cout << "phi of higgs: " << Higgs.Phi()<<std::endl;
         std::cout << "px of higgs: " << Higgs.Px()<<std::endl;
         std::cout << "pt of higgs: " << Higgs.Pt()<<std::endl;
         std::cout << "Eta of higgs: " << Higgs.Eta()<<std::endl;
         std::cout << "status of higgs: " <<gen.status() <<std::endl;
         std::cout << "mother:   " << gen.mother(0) <<"and" <<gen.mother(1) <<std::endl;
         std::cout << "daughter:   " << gen.daughter(0) << "and" <<gen.daughter(1) <<std::endl;*/
	 found_higgs = true;
       }
     }






     
    /* if (abs(gen.pdgId())==18){
       if (!found_a0){
	 if (idm < 3){
	   TLorentzVector tmp_;
	   tmp_.SetPxPyPzE(gen.px(), gen.py(), gen.pz(), gen.energy());
	   vV += tmp_;
	   //vV.SetPxPyPzE(gen.px(), gen.py(), gen.pz(), gen.energy());
	   std::cout<<" inside dm"<<gen.pt()
	   <<" " <<gen.status()<<std::endl;
	 }
	 idm++;
       }
       if (idm == 2) found_a0 = true;
       
	 else{
	 TLorentzVector tmp_;
	 tmp_.SetPxPyPzE(gen.px(), gen.py(), gen.pz(), gen.energy());
	 vV += tmp_;
	 found_a0 = true;
       }
       
     }*/

     if (gen.pdgId()==5){
        if (!found_b){
             bjet.SetPxPyPzE(gen.px(), gen.py(), gen.pz(), gen.energy());
            /* std::cout << "phi of b: " << bjet.Phi()<<std::endl;
             std::cout << "px of b: " << bjet.Px()<<std::endl;
             std::cout << "pt of b: " << bjet.Pt()<<std::endl;
             std::cout << "Eta of b: " << bjet.Eta()<<std::endl;
             std::cout << "status of b: " <<gen.status() <<std::endl;
             std::cout << "mother:   " << gen.mother(0) <<"and" <<gen.mother(1) <<std::endl;
             std::cout << "daughter:   " << gen.daughter(0) << "and" <<gen.daughter(1) <<std::endl;*/

             found_b = true;
          }
         
    }
     if (gen.pdgId()==-5){
        if (!found_bbar){
            bbarjet.SetPxPyPzE(gen.px(), gen.py(), gen.pz(), gen.energy());
          /*  std::cout << "phi of bbar: " << bbarjet.Phi()<<std::endl;
            std::cout << "px of bbar: " << bbarjet.Px()<<std::endl;
            std::cout << "pt of bbar: " << bbarjet.Pt()<<std::endl;
            std::cout << "Eta of bbar: " << bbarjet.Eta()<<std::endl;
            std::cout << "status of b: " <<gen.status() <<std::endl;
            std::cout << "mother:   " << gen.mother(0) <<"and" <<gen.mother(1) <<std::endl;
            std::cout << "daughter:   " << gen.daughter(0) << "and" <<gen.daughter(1) <<std::endl;*/

            found_bbar = true; 
        }
        
     }



   }

      if (abs(bjet.Eta()) < 3.5 && abs(bbarjet.Eta()) < 3.5 ){
       // if(Higgs.Pt() > 150.0 && deltaR(bjet.Eta(),bjet.Phi(),bbarjet.Eta(),bbarjet.Phi()) < 0.8 ){
       
       //newjets=jets[0]+jets[1];
        /* std::cout << "bjet Eta: "<< bjet.Eta() <<"  bjet phi: " <<bjet.Phi() <<"  bjet px: "<<bjet.Px() << std::endl;
         std::cout << "bbarjet Eta: "<< bbarjet.Eta() <<"  bbarjet phi: " <<bbarjet.Phi() <<"  bbarjet px: "<<bbarjet.Px() << std::endl;
         std::cout << "bjet Eta: "<< bjet.Eta() <<"  bjet phi: " <<bjet.Phi() <<"  bjet px: "<<bjet.Px() << std::endl;
         std::cout << "higgsEta: " <<Higgs.Eta() <<" Higgs phi: "<<Higgs.Phi() <<" Higgs px: "<<Higgs.Px() << std::endl;
         std::cout << "Mass:  " << (bjet+bbarjet).M() << std::endl;*/
      //   jet1eta=bjet.Eta();
        // jet2eta=bbarjet.Eta();
         //h3->Fill((bbarjet+bjet).M());   

         //n_deltaR=deltaR(bjet.Eta(),bjet.Phi(),bbarjet.Eta(),bbarjet.Phi());
         std::cout << "deltaR:  " << deltaR(bjet.Eta(),bjet.Phi(),bbarjet.Eta(),bbarjet.Phi()) << std::endl;
         std::cout << "delphiPhi: " << deltaPhi(bjet.Phi(),bbarjet.Phi()) << std::endl;
     //    std::cout << "deltaEta:  " << n_h_delta << std::endl;
     

         h_bpt->Fill(bjet.Pt());
         h_beta->Fill(bjet.Eta());
         h_bphi->Fill(bjet.Phi());
         h_bbarpt->Fill(bbarjet.Pt());
         h_bbareta->Fill(bbarjet.Eta());
         h_bbarphi->Fill(bbarjet.Phi());
         h_higgseta->Fill(Higgs.Eta());
         h_higgsmass->Fill(Higgs.M());
         h_higgsinvm->Fill((bjet+bbarjet).M());
         h_higgspt->Fill(Higgs.Pt());
         h_higgsphi->Fill(Higgs.Phi());

         n_deltaR = deltaR(bjet.Eta(),bjet.Phi(),bbarjet.Eta(),bbarjet.Phi());
      //   n_h_deta=(bjet.Eta()-bbarjet.Eta());  

         h_dphi->Fill(deltaPhi(bjet.Phi(),bbarjet.Phi()));
         h_DR->Fill(deltaR(bjet.Eta(),bjet.Phi(),bbarjet.Eta(),bbarjet.Phi()));
         h_eta1eta2->Fill((bjet.Eta())*(bbarjet.Eta()));
         h_deta->Fill(n_h_deta);
         h_DR_vs_Higgspt->Fill(Higgs.Pt(),n_deltaR);
          
        /* int i=0;
         if (jets[i].pdgId()==21,i++){
            if (jets[0].pdgId()==21){
                 jets[1]=jet1;
                 jets[2]=jet2;   
                   }
           
            if (jets[1].pdgId()==21){
                 jets[0]=jet1;
                 jets[2]=jet2;
                   }
            if (jets[2].pdgId()==21){
                 jets[1]=jet1;
                 jets[2]=jet2;
                   }

   

                 }*/




            
         //     }
        }
      




   HiggsMass=Higgs.M();
   jet1eta=bjet.Eta();
   jet2eta=bbarjet.Eta();
   jet1pt=bjet.Pt();
   jet2pt=bbarjet.Pt();  
   Higgs_invMass=(bjet+bbarjet).M();  
   HiggsPt = Higgs.Pt();
   trueMET = vV.Pt();
   HiggsEta = Higgs.Eta();
   //}
       //std::cout << "higgs mass" << newjets.M() <<std::endl;

  /* std::cout<<" higgs pt = "<<HiggsPt
	    <<" trueMET = "<<trueMET
            <<"HiggsMass = "<<Higgs.M()
	    <<std::endl;*/
   
   
   edm::Handle<LHEEventProduct> evt;
   if(iEvent.getByToken( lheEventToken, evt )){
     float sysLHEweight = evt->weights()[0].wgt/evt->weights()[0].wgt; 
     std::cout<< " sysLHEweight = "<<sysLHEweight<<std::endl;
   }
   
   tree_->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void 
MonoHGenTree2DScans::beginJob()
{
  
  //file = new TFile("output.root","RECREATE");
  //tree_ = new TTree("T","Signal Region");
  tree_->Branch("HiggsMass",&HiggsMass, "HiggsMass/f");
  tree_->Branch("jet1eta",&jet1eta, "jet1eta/f");
  tree_->Branch("jet2eta",&jet2eta, "jet2eta/f");
  tree_->Branch("jet1pt",&jet1pt, "jet1pt/f");
  tree_->Branch("jet2pt",&jet2pt, "jet2pt/f");
  tree_->Branch("Higgs_invMass",&Higgs_invMass, "Higgs_invMass/f");
  tree_->Branch("HiggsPt",&HiggsPt, "HiggsPt/f");
  tree_->Branch("HiggsEta",&HiggsEta, "HiggsEta/f");
  tree_->Branch("trueMET",&trueMET, "trueMET/f");
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MonoHGenTree2DScans::endJob() 
{
  //  file->Write();
  //  file->Close();

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MonoHGenTree2DScans::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MonoHGenTree2DScans);
