#!/usr/bin/env python
import ROOT as ROOT
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle,TLatex,TFile,kBlack
import os
import glob



def AddHist(h1, h2):
     h3 = h1.Clone("h3")
     h3.SetLineColor(kBlack)
     h3.SetMarkerStyle(20)
     h3.SetTitle("")
     h3.SetMinimum(0.1)
     h3.SetMaximum(1.35)

     # Set up plot for markers and errors
     #h3.Sumw2()
     h3.SetStats(0)
     h3.Add(h2)
     return h3

def SetCanvas():

    # CMS inputs
    # -------------
    H_ref = 1000;
    W_ref = 1000;
    W = W_ref
    H  = H_ref

    T = 0.08*H_ref
    B = 0.21*H_ref
    L = 0.12*W_ref
    R = 0.08*W_ref
    # --------------

    c1 = TCanvas("c2","c2",0,0,2000,1500)
    c1.SetFillColor(0)
    c1.SetBorderMode(0)
    c1.SetFrameFillStyle(0)
    c1.SetFrameBorderMode(0)
    c1.SetLeftMargin( L/W )
    c1.SetRightMargin( R/W )
    c1.SetTopMargin( T/H )
    c1.SetBottomMargin( B/H )
    c1.SetTickx(0)
    c1.SetTicky(0)
    c1.SetTickx(1)
    c1.SetTicky(1)
    c1.SetGridy()
    c1.SetGridx()
    c1.SetLogy(1)
    return c1



def CreateLegend(x1, y1, x2, y2, header):

    leg = ROOT.TLegend(x1, x2, y1, y2)
    leg.SetFillColor(0)
    leg.SetFillStyle(3002)
    leg.SetBorderSize(0)
    leg.SetHeader(header)
    return leg


def AddText(txt):
    texcms = ROOT.TLatex(-20.0, 50.0, txt)
    texcms.SetNDC()
    texcms.SetTextAlign(12)
    texcms.SetX(0.1)
    texcms.SetY(0.94)
    texcms.SetTextSize(0.02)
    texcms.SetTextSizePixels(22)
    return texcms

def AddTextCat(cat):
    texCat = ROOT.TLatex(-20.0, 50.0, cat)
    texCat.SetNDC()
    texCat.SetTextAlign(12)
    texCat.SetX(0.85)
    texCat.SetY(0.94)
    texCat.SetTextFont(40)
    texCat.SetTextSize(0.025)
    texCat.SetTextSizePixels(22)
    return texCat

gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetErrorX(0.)
ROOT.gROOT.SetBatch(True)


'''gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(0)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
gStyle.SetHistFillStyle(2)

legend=TLegend(.63,.70,.80,.89)
legend.SetTextSize(0.038)
cmsname=TLatex(0.15,0.95,' 2HDM+a Model')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)'''

c      = SetCanvas()
legend = CreateLegend(0.60, 0.94, 0.75, 0.92, "")

#path ='/afs/cern.ch/work/d/dekumar/LHE_Plots/*'
path = '/afs/cern.ch/work/d/dekumar/LHE_Plots/bb_ggFCombined/BenidiktFiles/*.root'#'/afs/cern.ch/work/d/dekumar/LHE_Plots/bb_ggFCombined/rootFiles/*'#'/afs/cern.ch/work/d/dekumar/gridpacktest/CMSSW_9_3_8/src/bb_int_LHE/*'

MH4=['100','200','300','400','500']
sintheta=['0p3','0p4','0p6','0p7','0p8','0p9']
tanbeta =['0p5','1p5','10p0','20p0','40p0']

legSin=['sin#theta=0.3','sin#theta=0.4','sin#theta=0.6','sin#theta=0.7','sin#theta=0.8','sin#theta=0.9']
legTan=['tan#beta=0.5','tan#beta=1.5','tan#beta=10.0','tan#beta=20.0','tan#beta=40.0']
# mchi=['1','10','50','150','500','1000']
col=[1,2,4,6,7,8]
myhist=[]
CS=[0.0749,0.0009226]
files = sorted(glob.glob(path))
#for i in MH4:
#for i in sintheta:
normCS=True
proc=['bb','gg']
for i in proc:
    for file in files:
       # print "myfile",file
        #f=TFile.Open(file,'read')
        #if 'MH3_600_MH4_'+i+'_MH2_600_MHC' in file.split('/')[-1]:
        #if '_2HDMa_bb_sinp_'+i+'_tanb_1p0_mXd_10_MH3_' in file.split('/')[-1]:
        #if '2HDMa_'+i+'_sinp_0p35_tanb_20p0_mXd_10_MH3_600' in file.split('/')[-1]:
        if '2HDMa_'+i+'_tb' in file.split('/')[-1]:
		#print file
                exec("f"+i+"=TFile.Open(file,'read')")
                exec("print 'selected file'"+","+"f"+i)
    	        exec("hist_met=f"+i+".Get('getMET')")
                myhist.append(hist_met)
                #print ("integral",myhist[i].Integral())
                #print myhists
                #c.SaveAs('met.pdf')
                #f.Close()


print len(myhist)
#myhist[0].Draw('HIST')
for i in range(len(myhist)):
    if i==0:
        myhist[i].SetXTitle("genMET[GeV]")
        #myhist[i].SetYTitle("Events")
        myhist[i].SetLineColor(col[i])
        myhist[i].Rebin(2)
        myhist[i].SetLineWidth(3)
        #myhist[i].GetXaxis().SetRangeUser(0, 500)
        #myhist[i].SetMaximum(2)
        if not normCS:
        	myhist[i].Scale(1/myhist[i].Integral())
        	legend.AddEntry(myhist[i],legTan[i],"L")
        	myhist[i].SetMaximum(0.4)
        	myhist[i].Draw('HIST')
        if normCS:
		myhist[i].Scale(CS[i]/myhist[i].Integral())
                print "doing CS norm"
	#c.SaveAs('combinedHiggs_2HDMa'+legTan[i]+'.pdf')

    else:
        myhist[i].SetXTitle("MET[GeV]")
        #myhist[i].SetYTitle("Events")
        myhist[i].SetLineColor(col[i])
        myhist[i].Rebin(2)
        myhist[i].SetLineWidth(3)
        #myhist[i].SetMaximum(2)
        if not normCS:
        	myhist[i].Scale(1/myhist[i].Integral())
        	legend.AddEntry(myhist[i],legTan[i],"L")
        	myhist[i].SetMaximum(0.4)
        	myhist[i].Draw('HIST same')
        if normCS:
                print ("doing CS norm")
		myhist[i].Scale(CS[i]/myhist[i].Integral())
		#myhist[i].Add(myhist[i],myhist[i-1],1.0,1.0)
		#myhist[i].Draw('HIST')
                h3=AddHist(myhist[i],myhist[i-1])
h3.Draw('HIST')
	#c.SaveAs('combinedHiggs_2HDMa'+legTan[i]+'.pdf')

#cmsname.Draw()
legend.Draw()

txt = 'monoHbb'
texcms = AddText(txt)
texCat= AddTextCat("2HDM+a")
texcms.Draw("same")
texCat.Draw("same")
t = ROOT.TPaveLabel(0.1, 0.96, 0.95, 0.99, "genMET Comparison", "brNDC")
t.Draw('same')
c.Update()

c.SaveAs('combined_gg_bb.pdf')
c.SaveAs('combined_gg_bb.png')
