""" In CRAB3 the configuration file is in Python language. It consists of creating a Configuration object imported from the WMCore library: """
from WMCore.Configuration import Configuration
config = Configuration()

## change workArea
## change pyCfgParams
## change outputPrimaryDataset

"""  Once the Configuration object is created, it is possible to add new sections into it with corresponding parameters."""

config.section_("General")
config.General.requestName = 'MonoHStepGEN'
config.General.workArea = 'crab_projects_MonoHStepTREE2HDM'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ConfFile_cfg.py'

#config.JobType.outputFiles = ['output.root']
#config.JobType.pyCfgParams = ['tarball=/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi/v2/Zprime_A0h_A0chichi_MZp3850_MA0850_tarball.tar.xz']


config.section_("Data")
config.Data.inputDataset = '/DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.outputPrimaryDataset = 'MonoH_2HDM_Zprime_A0hbb_MZp3850_MA0850'
config.Data.splitting = 'FileBased'
config.Data.inputDBS = 'phys03'

## Note, the number of events here need to match the variable NEventsPerJob in stepLHE.py
config.Data.unitsPerJob = 30000
NJOBS = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag  = 'GEN'
config.Data.outLFNDirBase = '/store/user/khurana/MonoH2DScanTrees/'


config.section_("Site")
config.Site.storageSite = "T2_US_Wisconsin"
config.Site.whitelist = ['T2_CH_CERN', 'T2_IT_Pisa', 'T2_RU_JINR', 'T2_DE_RWTH', 'T2_US_Wisconsin']
