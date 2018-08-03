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


cmsname=TLatex(0.15,0.95,' 2HDM+a Model        bb+DM')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)

c = TCanvas()
c.SetLogy()


path1 = '/home/deepak/Desktop/LHEFile/MH4scanequal_M_lamda0/'
path2 = '/home/deepak/Desktop/LHEFile/MH4scanequal_M_lamda3/'

paths=[path1,path2]
MH4=['MH4_50','MH4_100','MH4_350','MH4_400','MH4_500']
runs=['01','02','03','04','05']
leg_entry=['M_{H4}=50 GeV,lam3=lamP1=lamP2=','M_{H4}=100 GeV,lam3=lamP1=lamP2=','M_{H4}=350 GeV,lam3=lamP1=lamP2=','M_{H4}=400 GeV,lam3=lamP1=lamP2=','M_{H4}=500 GeV,lam3=lamP1=lamP2=']


pathhists=[]

for path in paths:
    print "hi"
    hists=[]
    genMET=[]
    for r in runs:
            h_genMET=TH1F('genMET'+path+r,"",100,0,1000)
            file=glob.glob(str(path)+'run_'+r+'/*')
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
            
            #file.Close()
    pathhists.append(hists)
#print pathhists

#for ph in range(len(pathhists)):
#print "pathshist",len(pathhists)
#print "hists0",(len(pathhists[0]))
#print "hists1",(len(pathhists[1]))
for hist in range(len(pathhists[0])):
    legend=TLegend(.33,.69,.57,.89)
    legend.SetTextSize(0.038)
    (pathhists[0])[hist].SetXTitle("genMET[GeV]")
    (pathhists[0])[hist].SetYTitle("Events")
    (pathhists[0])[hist].SetLineColor(2)
    (pathhists[0])[hist].Rebin(5)
    (pathhists[0])[hist].SetLineWidth(3)
    (pathhists[0])[hist].Scale(1/(pathhists[0])[hist].Integral())
    (pathhists[0])[hist].SetMaximum(2)
    legend.AddEntry((pathhists[0])[hist],leg_entry[hist]+'0',"L")
    pathhists[0][hist].Draw('HIST')

    (pathhists[1])[hist].SetLineColor(1)
    (pathhists[1])[hist].Rebin(5)
    (pathhists[1])[hist].SetLineWidth(3)
    (pathhists[1])[hist].Scale(1/(pathhists[1])[hist].Integral())
    #(pathhists[1])[hist].SetMaximum(2)
    legend.AddEntry((pathhists[1])[hist],leg_entry[hist]+'3',"L")
    (pathhists[1])[hist].Draw('HIST same')
    cmsname.Draw()
    legend.Draw()

    c.SaveAs('compare'+MH4[hist]+'.pdf')
    
    c.SaveAs('compare'+MH4[hist]+'.png')



