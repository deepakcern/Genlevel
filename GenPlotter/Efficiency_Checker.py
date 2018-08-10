import elementtree.ElementTree as ET
from ROOT import TFile, kGreen,TLatex, TGraph, TTree, TH1F, TH2F, TCanvas, TChain, TMath, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend
import os
import glob
import matplotlib.pyplot as plt


gStyle.SetFrameLineWidth(3)
# gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)

path = '/afs/cern.ch/work/d/dekumar/public/forbbDM_lhe/lhefiles_tanbeta_35_mh3_600_mchi_10_2016/'
runs=['01','02','03','04','05']

c=TCanvas()
c.SetLogz()

#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")

eff=[]

sel1_masspoint=[]
sel2_masspoint=[]
sel3_masspoint=[]

for r in runs:
    genMET=[]
    selEvents=[]
    selEvents1=[]
    selEvents2=[]
    selEvents3=[]
    file=glob.glob(str(path)+'run_'+r+'/*.lhe')
    tree=ET.parse(str(file[0]))
    root=tree.getroot()
    for child in root:
        if (child.tag=='event'):
            lines=child.text.strip().split('\n')
            event_header=lines[0].strip()
            num_part=int(event_header.split()[0].strip())

            phi=[s for s in lines if s.split()[0]=='55']
            chi=[s for s in lines if s.split()[0]=='52']
            chibar=[s for s in lines if s.split()[0]=='-52']
            b=[s for s in lines if s.split()[0]=='5']
            bbar=[s for s in lines if s.split()[0]=='-5']

            if phi:
                px=float (phi[0].split()[6])
                py=float (phi[0].split()[7])
                pz=float (phi[0].split()[8])
                e=float (phi[0].split()[9])
                p=TLorentzVector(px,py,pz,e)

            px1=float (chi[0].split()[6])
            py1=float (chi[0].split()[7])
            pz1=float (chi[0].split()[8])
            e1=float (chi[0].split()[9])

            px2=float (chibar[0].split()[6])
            py2=float (chibar[0].split()[7])
            pz2=float (chibar[0].split()[8])
            e2=float (chibar[0].split()[9])

            p1=TLorentzVector(px1,py1,pz1,e1)
            p2=TLorentzVector(px2,py2,pz2,e2)

            pi=p1+p2
            # genMET.append(pi.Pt())
            if pi.Pt() > 170:
                genMET.append(pi.Pt())

                px3=float (b[0].split()[6])
                py3=float (b[0].split()[7])
                pz3=float (b[0].split()[8])
                e3=float (b[0].split()[9])

                px4=float (bbar[0].split()[6])
                py4=float (bbar[0].split()[7])
                pz4=float (bbar[0].split()[8])
                e4=float (bbar[0].split()[9])

                p3=TLorentzVector(px3,py3,pz3,e3)
                p4=TLorentzVector(px4,py4,pz4,e4)

                if (pi.Pt() > 200):
                    selEvents1.append(pi.Pt())

                if (pi.Pt() > 200) and (p3.Pt() > 50) and (p4.Pt() > 50):
                    selEvents2.append(pi.Pt())

                if (pi.Pt() > 200) and (p3.Pt() > 50) and (p4.Pt() > 50) and (abs(p3.Eta()) < 2.5)  and (abs(p4.Eta()) < 2.5):
                    selEvents3.append(pi.Pt())
                    selEvents.append(pi.Pt())


    print ("myEvet",len(selEvents))
    print("totalEvent",len(genMET))
    eff.append((float (len(selEvents)))/(float (len(genMET)) ))
    print ("Myeff",(float (len(selEvents)))/(float (len(genMET)) ))
    sel1_masspoint.append(selEvents1)
    sel2_masspoint.append(selEvents2)
    sel3_masspoint.append(selEvents3)

fout=open('Efficiency_cut.txt','w')
for i in eff:
    print ("eff",i)
    fout.write(str(i)+'\n')

allsel=[]
allsel.append(sel1_masspoint)
allsel.append(sel2_masspoint)
allsel.append(sel3_masspoint)

legend=TLegend(.53,.59,.87,.89)
legend.SetTextSize(0.05)
legend.SetBorderSize(0)


leg_entry=['M_{a}=50 GeV','M_{a}=100 GeV','M_{a}=350 GeV','M_{a}=400 GeV','M_{a}=500 GeV']
n=len(genMET)
mass_label=['50','100','350','400','500']
Hists=['m_50','m_100','m_350','m_400','m_500']


color=[1,2,3,4,6]
for mass in range(len(mass_label)):
    cutflowEvents=[len(sel1_masspoint[mass]), len(sel2_masspoint[mass]), len(sel3_masspoint[mass])]
    label=['genMETcond','p_{T}cond','EtaCond']
    h_cutflow=TH1F('cutflow','cutflow',4,0,4)
    Hists[mass]=TH1F('cutflow','cutflow',4,0,4)

    for i in range(len(cutflowEvents)):
        h_cutflow.GetXaxis().SetBinLabel(i+1,label[i])
        h_cutflow.SetBinContent(i+1,cutflowEvents[i])
        h_cutflow.GetXaxis().SetTitleOffset(1.05)
        h_cutflow.GetXaxis().SetTitleFont(42)
        h_cutflow.GetXaxis().SetLabelFont(42)
        h_cutflow.GetXaxis().SetLabelSize(.03)
        h_cutflow.SetYTitle("Events")
        h_cutflow.GetYaxis().SetTitleSize(0.12)
        h_cutflow.GetYaxis().SetTitleOffset(1.5)
        h_cutflow.GetYaxis().SetTitleFont(42)
        h_cutflow.GetYaxis().SetLabelFont(42)
        h_cutflow.GetYaxis().SetLabelSize(0.05)

    # h_cutflow.SetTextAngle(90)
    h_cutflow.SetFillColor(kGreen+1)
    h_cutflow.SetTitle('Cutflow'+'       M_{a}='+mass_label[mass]+'GeV'+'      TotalEvents='+str(n))
    h_cutflow.Draw()
    # cmsname.Draw()
    c.SaveAs("genLevel_cutflow_170cut"+mass_label[mass]+".pdf")
    c.SaveAs("genLevel_cutflow_170cut"+mass_label[mass]+".png")


for mass in range(len(mass_label)):
    cutflowEvents=[len(sel1_masspoint[mass]), len(sel2_masspoint[mass]), len(sel3_masspoint[mass])]
    label=['genMETcond','p_{T}cond','EtaCond']
    h_cutflow=TH1F('cutflow','cutflow',4,0,4)
    Hists[mass]=TH1F('cutflow','cutflow',4,0,4)
    legend.AddEntry(Hists[mass],leg_entry[mass],"L")

    for i in range(len(cutflowEvents)):
        h_cutflow.GetXaxis().SetBinLabel(i+1,label[i])
        h_cutflow.SetBinContent(i+1,cutflowEvents[i])


        if mass==0:
            Hists[mass].GetXaxis().SetTitleOffset(1.05)
            Hists[mass].GetXaxis().SetTitleFont(42)
            Hists[mass].GetXaxis().SetLabelFont(42)
            Hists[mass].GetXaxis().SetLabelSize(.03)
            Hists[mass].SetYTitle("Events")
            Hists[mass].GetYaxis().SetTitleSize(0.12)
            Hists[mass].GetYaxis().SetTitleOffset(1.5)
            Hists[mass].GetYaxis().SetTitleFont(42)
            Hists[mass].GetYaxis().SetLabelFont(42)
            Hists[mass].GetYaxis().SetLabelSize(0.05)
            Hists[mass].SetLineWidth(3)
            Hists[mass].SetMaximum(1200)
            Hists[mass].GetXaxis().SetBinLabel(i+1,label[i])
            Hists[mass].SetBinContent(i+1,cutflowEvents[i])

            Hists[mass].SetTitle('Cutflow'+'           TotalEvents='+str(n))
            Hists[mass].SetLineColor(color[mass])
            Hists[mass].Draw()
        else:
            Hists[mass].GetXaxis().SetTitleOffset(1.05)
            Hists[mass].GetXaxis().SetTitleFont(42)
            Hists[mass].GetXaxis().SetLabelFont(42)
            Hists[mass].GetXaxis().SetLabelSize(.05)
            Hists[mass].SetYTitle("Events")
            Hists[mass].GetYaxis().SetTitleSize(0.12)
            Hists[mass].GetYaxis().SetTitleOffset(1.5)
            Hists[mass].GetYaxis().SetTitleFont(42)
            Hists[mass].GetYaxis().SetLabelFont(42)
            Hists[mass].GetYaxis().SetLabelSize(0.05)
            Hists[mass].GetXaxis().SetBinLabel(i+1,label[i])
            Hists[mass].SetBinContent(i+1,cutflowEvents[i])
            Hists[mass].SetLineColor(color[mass])
            Hists[mass].SetLineWidth(3)
            Hists[mass].Draw('same')
legend.Draw()
c.SaveAs("genLevel_cutflow_all_170cut.pdf")



# print ("Total events", n)
# mass=[50,100,350,400,500]
#
# plt.plot(mass,eff,'-o',label='-',color='red')
#
# plt.rc('axes', labelsize=20)
# plt.xlabel(r'M_{a} (GeV)')
# plt.ylabel("Signal Efficiency")
# # plt.xticks([.1, .2, .3, .35, .4, .5,.6,.7,.8,.9])
# plt.legend()#ncol=3,title=r"tan$\beta$")
# plt.title(r"Signal efficiency    monoH+DM")
# plt.savefig('Eff.pdf')
# plt.savefig('Eff.png')
# plt.close('all')
