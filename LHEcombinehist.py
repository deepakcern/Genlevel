import elementtree.ElementTree as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle,TLatex
import os
import glob

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(0)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
gStyle.SetHistFillStyle(2)

path = '/home/deepak/Desktop/LHEFile/MH4scanequal_M_lamda0/'

runs=['01','02','03','04','05']

hists=[]
genMET=[]

for i in runs:
    h_genMET=TH1F('genMET'+i,"",100,0,1000)
    file=glob.glob(path+'run_'+i+'/*')
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
            genMET.append(pi.Pt())
    for met in genMET:
            h_genMET.Fill(met)
    hists.append(h_genMET)

legend=TLegend(.33,.69,.57,.89)
legend.SetTextSize(0.038)
leg_entry=['M_{H4}=50 GeV','M_{H4}=100 GeV','M_{H4}=350 GeV','M_{H4}=400 GeV','M_{H4}=500 GeV']


cmsname=TLatex(0.15,0.95,' 2HDM+a Model        bb+DM')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)

c = TCanvas()
c.SetLogy()

#print len(hists)

for hist in range(len(hists)):
    print hist
    if hist==0:
        hists[hist].SetXTitle("genMET[GeV]")
        hists[hist].SetYTitle("Events")
        hists[hist].SetLineColor(hist+1)
        hists[hist].Rebin(5)
        hists[hist].SetLineWidth(3)
        hists[hist].Scale(1/hists[hist].Integral())
        hists[hist].SetMaximum(2)
        legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists[hist].Draw('HIST')

    else:
        hists[hist].SetXTitle("genMET[GeV]")
        hists[hist].SetYTitle("Events")
        hists[hist].SetLineColor(hist+1)
        hists[hist].Rebin(5)
        hists[hist].SetLineWidth(3)
        hists[hist].Scale(1/hists[hist].Integral())
        hists[hist].SetMaximum(2)
        legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists[hist].Draw('HIST same')

cmsname.Draw()
legend.Draw()

c.SaveAs("test0.png")
