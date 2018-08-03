from ROOT import TFile, TGraph2D, TGraph, TTree, TH2F,  TCanvas, TChain, TMath, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend
import os
import glob
from array import array
import ROOT as ROOT

gStyle.SetFrameLineWidth(3)
# gStyle.SetOptTitle(1)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)


# cmsname=TLatex(0.15,0.95,'CMS Simulation Preliminary')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
# cmsname.SetTextSize(0.036)
# cmsname.SetTextAlign(12)
# cmsname.SetNDC(1)
# cmsname.SetTextFont(61)

c=TCanvas()
c.SetLogz()

MH3 = []
MH4=[]
Cross=[]
with open('cross_section.txt') as f:
    for line in f:
        if line.split()[2]=='10':
            mA=float (line.split()[0])
            ma=float (line.split()[1])
            cs=float (line.split()[6])
            MH3.append(float (mA))
            MH4.append(float (ma))
            Cross.append(float (cs))



# X=map(float, MH3)
# Y=map(float,MH4)
# Z=map(float,Cross)
# x=array("d",MH3)
# y=array("d",MH4)
# z=array("d",Cross)
# n=len(z)
# gr = TGraph2D( n, x, y, z)
# gr.SetTitle("Cross section               tan(#beta)=1, sin(#theta)=0.35; M_{A}; M_{a}")
# #gr.GetXaxis().SetTitle("MH4")
# #gr.GetYaxis().SetTitle("tan(#beta)")
# #gr.GetHistogram().SetMaximum(10000.)
# #gr.GetHistogram().SetMinimum(0.)
# #gr.SetLineColor(2)
# gr.GetXaxis().SetTitleSize(.05)
# gr.Draw("colz")
# # gr.Draw("TEXT colz")
# #cmsname.Draw()
# c.SaveAs("MH3_vs_MH4.pdf")
# c.SaveAs("MH3_vs_MH4.png")

#plotting usinf 2d histogram

MA=['600.0','800.0','1000.0','1200.0']
Ma=['100.0','150.0','200.0','250.0','300.0','350.0','400.0','500.0']
hist2=TH2F("hist2",'Cross section         tan #beta =1, sin#theta =0.35',len(Ma),0,len(Ma),len(MA),0,len(MA))
hist2.GetYaxis().SetTitle("M_{A} (GeV)")
hist2.GetXaxis().SetTitle("M_{a} (GeV)")
# hist2.SetStats(0)
hist2.SetTitle("Cross section         tan#beta =1, sin#theta =0.35")
# hist2.SetMaximum(0.05)
# hist2.SetMinimum(2e-3)

for xsc in range(len(Cross)):
    for i in Ma:
        if i==str((MH4)[xsc]):
            # print ("enter1")
            for j in MA:
                if j==str((MH3)[xsc]):
                    # print ("enter2")
                    for numx in range(len(Ma)):
                        for numy in range(len(MA)):
                            if Ma[numx]==i and MA[numy]==j:
                                print ("numx",numx,'numy',numy)
                                hist2.GetXaxis().SetBinLabel(numx+1,i)
                                hist2.GetYaxis().SetBinLabel(numy+1,j)
                                hist2.SetBinContent(numx+1,numy+1,Cross[xsc])


hist2.Draw("COLZ TEXT")
# cmsname.Draw()
# cmsname.Draw()
c.SaveAs("2DCross_withHist.pdf")
