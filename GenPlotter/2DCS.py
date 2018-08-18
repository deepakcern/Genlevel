from ROOT import TFile, TGraph2D, TGraph, TTree, TH2F,  TCanvas, TChain, TMath, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend, TLatex
import os
import glob
from array import array
import ROOT as ROOT
import matplotlib.pyplot as plt

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
with open('bbDM_cross_section.txt') as f:
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

MA=['600.0','700.0','800.0','900.0','1000.0']
Ma=['100.0','200.0','300.0','400.0','500.0']
hist2=TH2F("hist2",'Cross section         tan #beta =1, sin#theta =0.35',len(Ma),0,len(Ma),len(MA),0,len(MA))
hist2.GetYaxis().SetTitle("M_{A} (GeV)")
hist2.GetXaxis().SetTitle("M_{a} (GeV)")
# hist2.SetStats(0)
hist2.SetTitle("Cross section         tan#beta =35, sin#theta =0.7")
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
c.SaveAs("bbDM_mchi_10_2DCross_withHist.pdf")
c.SaveAs("bbDM_mchi_10_2DCross_withHist.png")

cross1=[0.3217,0.2453,0.1758,0.1224,0.08198,0.0423,0.005887]
mass=[150,200,250,300,350,400,500]


plt.plot(mass,cross1,'-o',color='red',linewidth=2)

plt.xlabel(r'$\mathbf{M_{a}[GeV]}$')
plt.ylabel("Cross section",fontweight="bold")
plt.legend()#ncol=3,title=r"tan$\beta$")
plt.title(r"2HDM+a , h$\mathbf{\rightarrow b\bar{b}}$"+"        $\mathbf{M_{A}}$=600 GeV ",fontweight="bold")
plt.savefig(r'1D_xsec.pdf')
plt.savefig('1D_xsec.png')
plt.clf()
plt.cla()
plt.close('all')


from array import array
gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
c=TCanvas()

latex =  TLatex();
latex.SetNDC();
latex.SetTextSize(0.04);
latex.SetTextAlign(31);
latex.SetTextAlign(11);
x=array("d",mass)
y=array("d",cross1)
n=len(mass)
gr = TGraph( n, x, y )
#gr.SetTitle("Signal Efficiency Vs MH4")
gr.GetXaxis().SetTitle("M_{a}[GeV]")
gr.GetYaxis().SetTitle("Cross Section [pb]                          ")
gr.SetLineColor(2)
gr.Draw("AC*")
latex.DrawLatex(0.18, 0.93, "2HDM+a,   h #rightarrow b#bar{b}         M_{A}=600")#r"                             35.9 fb^{-1}(13 TeV)");

c.SaveAs("Xsec.pdf")
c.SaveAs("Xsec.png")
