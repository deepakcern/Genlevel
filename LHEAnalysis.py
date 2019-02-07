
#Not before running this script you need to follow below commands
#cd CMSSW_9_x/src
#wget http://madgraph.hep.uiuc.edu/Downloads/ExRootAnalysis/ExRootAnalysis_V1.0.10.tar.gz
#tar zxvf ExRootAnalysis_V1.0.10.tar.gz
#cd ExRootAnalysis/
#make

class cTerm:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'




 #External packages
import sys
import os
import math
import re
# Check if pyROOT is available
try:
    #from ROOT import *
    import ROOT
    print cTerm.GREEN+"ROOT module imported"+cTerm.END
except:
    print cTerm.RED+"\nError: Cannot load PYROOT, make sure you have setup ROOT in the path"
    print "and pyroot library is also defined in the variable PYTHONPATH, try:\n"+cTerm.END
    if (os.getenv("PYTHONPATH")):
        print " setenv PYTHONPATH ${PYTHONPATH}:$ROOTSYS/lib\n"
    else:
        print " setenv PYTHONPATH $ROOTSYS/lib\n"
    print "Exit now\n"
    sys.exit()

ROOT.PyConfig.IgnoreCommandLineOptions = True
from optparse import OptionParser

def main(argv = None):
    if argv == None:
        argv = sys.argv[1:]
    # OPTIONS
    usage = "usage: %prog [options]\n This script analyzes madgraph trees."
    parser = OptionParser(usage)
    parser.add_option("-b", "--batch",
                      action="store_true",
                      help="run ROOT in batch mode.")
    parser.add_option("-l", "--sample",
                      default="LHE",
                      help="input samples. The options are: madgraph or whizard [default: %default]")
    parser.add_option("-q","--quit",
                      action="store_true",
                      help="quit after reading tree otherwise prompt for keyboard to continue.")
    (options, args) = parser.parse_args(sys.argv[1:])
    #print options
    #print args
    return options



if __name__ == '__main__':

    LHE_file='/afs/cern.ch/work/d/dekumar/gridpacktest/CMSSW_9_3_8/src/New_tan_files/run_03/2HDMa_bb_sinp_0p35_tanb_40p0_mXd_10_MH3_600_MH4_100_MH2_600_MHC_600_cmsgrid_final.lhe'
    root_file=LHE_file.strip(LHE_file.split('.')[-1])+'root'
    os.system('rm -rf '+root_file)
    os.system('/afs/cern.ch/work/d/dekumar/LHE_Plots/releases/CMSSW_9_3_8/src/ExRootAnalysis/ExRootLHEFConverter '+LHE_file+' '+root_file)


    options = main()

    if options.batch:
        ROOT.gROOT.SetBatch()
        print cTerm.GREEN+"Run in batch mode."+cTerm.END

    # Load ROOT libraries
    ROOT.gSystem.Load('/afs/cern.ch/work/d/dekumar/LHE_Plots/releases/CMSSW_9_3_8/src/ExRootAnalysis/libExRootAnalysis.so')

    # Create output root file
    #root_file=''
    outname = "results_gen.root"
    if options.sample == "LHE":
        outname = 'Output_'+root_file.split('/')[-1]
    elif options.sample == "whizard":
        outname= "results_gen_whizard.root"
    else:
        print cTerm.RED+"Unknown sample name: "+options.sample+"\nOptions are \"madgraph\" or \"whizard\""+cTerm.RED
        #sys.exit()

    outFile = ROOT.TFile(outname,"RECREATE")

    # Create chain of root trees
    chain = ROOT.TChain("LHEF")
    maxEntries = -1
    # MG files
    print "Use dataset: "+options.sample

    if options.sample == "LHE":
        chain.Add(root_file)
        #chain.Add("/uscms_data/d2/maravin/TTG_MG5/Two2Seven/ROOT/ttgamma_27_part2.root")
    ##chain.Add("/uscms_data/d2/maravin/TTG_MG5/Two2Seven/ROOT/ttgamma_27_part3.root")
    ##chain.Add("/uscms_data/d2/maravin/TTG_MG5/Two2Seven/ROOT/ttgamma_27_part4.root")

    # Whizard files
    if options.sample == "whizard":
        chain.Add("/uscmst1b_scratch/lpc1/cmsroc/yumiceva/TTGamma/LHE/whizard/TTGamma_Whizard_2to7/ttgamma.root")
        maxEntries = 200000

    # setup ntuple object
    treeReader = ROOT.ExRootTreeReader(chain)
    # number of entries
    numberOfEntries = treeReader.GetEntries()
    print "Total number of entries to be processed: " + str(numberOfEntries)

    # Get pointers to branches used in this analysis
    Particles = treeReader.UseBranch("Particle")

    # Book histograms
    h_nocut = {}
    h_cut = {}

    h_nocut['getMET'] =ROOT.TH1F("getMET","getMET",100,0,500)
    h_nocut['higgsPT'] = ROOT.TH1F("higgsPT","higgsPT [GeV]",100,0,500)
    # h_nocut['q_eta'] = ROOT.TH1F("q_eta","b #eta",100,-5,5)
    # h_nocut['q_phi'] =ROOT.TH1F("q_phi","b #phi",80,-3.2,3.2)


    for key in h_nocut.keys():
        h_cut[key] = h_nocut[key].Clone(h_nocut[key].GetName())
        h_cut[key].Sumw2()
        h_nocut[key].Sumw2()
        h_cut[key].SetTitle( h_cut[key].GetTitle() )
        h_nocut[key].SetTitle( h_nocut[key].GetTitle() )

    # Loop over all events
    for entry in xrange(0, numberOfEntries):

        # Load selected branches with data from specified event
        treeReader.ReadEntry(entry)

        if entry%2000 == 0:
            print "entry=",entry
            ####
            if maxEntries!=-1 and maxEntries < entry:
                print cTerm.GREEN+"This sample has a maximum number of entries to process. Stop now."+cTerm.END
                break
        # Check ttbar production mechanism
        # TRootLHEFParticle
        index = 0
        chi = ROOT.TLorentzVector()
        chibar = ROOT.TLorentzVector()
        # p4Photon = ROOT.TLorentzVector()
        # p4Lepton = ROOT.TLorentzVector()
        # p4Nu = ROOT.TLorentzVector()
        #
        # numElectrons = 0
        # numMuons = 0
        # numTaus = 0
        # numPhotons =0


        # MG Status code: -1 initial, 2 intermediate, 1 final

        # Electrons

        for p in Particles:
            index += 1

            if p.PID == 18 and p.Status == 1:
#                if numElectrons == 0:
                chi.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)

            if p.PID == -18 and p.Status == 1:
#                if numElectrons == 0:
                chibar.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
            met = (chi+chibar)


            h_nocut['getMET'].Fill( met.Pt() )

    # END loop over entries
    h_nocut['getMET'].Draw()

    outFile.cd()
    for key in h_nocut.keys():

        if h_nocut[key].GetEntries() > 0:
            h_nocut[key].Write()
        if h_cut[key].GetEntries() > 0:
            h_cut[key].Write()

    outFile.Close()
    print cTerm.GREEN+"Output file name: "+outname+cTerm.END

    os.system('rm -rf '+root_file)

    print cTerm.GREEN+"done."+cTerm.END
