import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            # replace 'myfile.root' with the source file you want to use
                            fileNames = cms.untracked.vstring(
        #'file:/hdfs/store/user/khurana/MonoH2DScanSamples/ZpBaryonic_MZp850_MChi575/GEN/180125_131917/0000/LHETOGEN_1.root'
        #'file:/hdfs/store/user/khurana/MonoH2DScanSamples/Zprime_A0h_A0chichi_MZp1650_MA0850/GEN/170626_162018/0000/LHETOGEN_1.root'
         'file:/afs/cern.ch/work/d/dekumar/VBF/GEN/CMSSW_8_3_0/src/MonoHGenTree/MonoHGenTree2DScans/python/PythiaH185bb_cfi_py_GEN.root'
        )
                            )

process.demo = cms.EDAnalyzer('MonoHGenTree2DScans'
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("GenInfoTree.root")
                                   )

process.p = cms.Path(process.demo)
