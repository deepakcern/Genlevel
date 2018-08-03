
import elementtree.ElementTree as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle,TLatex

#LHE coloumn informatiomn col1=pdgID, col2=status, col3=mother1, col4=mother2, col5=color, col6=col, col7-9=momentum, col10=energy
#Deepak dekumar

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(0)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
gStyle.SetHistFillStyle(2)
#gStyle.SetEndErrorSize(2)

# #For the axis labels:
# gStyle.SetLabelColor(1, "XYZ");
# gStyle.SetLabelFont(42, "XYZ");
# gStyle.SetLabelOffset(0.007, "XYZ");
# gStyle.SetLabelSize(0.05, "XYZ");
#
# # For the axis:
# gStyle.SetAxisColor(1, "XYZ");
# gStyle.SetStripDecimals(kTRUE);
# gStyle.SetTickLength(0.03, "XYZ");
# gStyle.SetNdivisions(510, "XYZ");
# gStyle.SetPadTickX(1);  // To get tick marks on the opposite side of the frame
# gStyle.SetPadTickY(1);
#
# # Change for log plots:
# gStyle.SetOptLogx(0);
# gStyle.SetOptLogy(0);
# gStyle.SetOptLogz(0);


cmsname = TCanvas()
cmsname=TLatex(0.15,0.95,'2HDM+a   bbDM ')
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)
legend=TLegend(.33,.69,.57,.89)
legend.SetTextSize(0.038)


tree = ET.parse('/afs/cern.ch/work/d/dekumar/public/forbbDM_lhe/test/events.lhe')
root=tree.getroot()
my_part_p4=[]

def getParticle(root,pdgid,status,mother1=None,mother2=None):
    for child in root:
        if (child.tag=='event'):
            lines=child.text.strip().split('\n')
            if not (mother1 and mother2):
                particle=[s for s in lines if (s.split()[0]==str(pdgid) and s.split()[1]==str(status))]
            else:
                mother1Cond=(s.split()[2]==(str(mother1) or str(mother2)) )
                mother2Cond=(s.split()[3]==(str(mother1) or str(mother2)) )
                particle=[s for s in lines if (s.split()[0]==str(pdgid) and s.split()[1]==str(status) and mother1Cond and mother2Cond )]
            if particle:
                px=float (particle[0].split()[6])
                py=float (particle[0].split()[7])
                pz=float (particle[0].split()[8])
                e=float (particle[0].split()[9])
                p4=TLorentzVector(px,py,pz,e)
                my_part_p4.append()

    return my_part_p4



def getPT(p4):
    pT=p4.Pt()
    return pT

def getEta(p4):
    eta=p4.Eta()
    return eta

def dR(p4_1,p4_2):
    deltaR=p4_1.DeltaR(p4_2)
    return deltaR

def getInvMass(p4_1,p4_2):
    mass=(p4_1+p4_2).M()
    return mass

def  getMET(p4_chi,p4_chibar):
    genmet=(p4_chi+p4_chibar).Pt()
    return genmet




def Hist(name,label,bins,lowx,highx):
    h_tep=TH1F(name,"",bins,lowx,highx)
    h_tep.SetXTitle(label)
    h_tep.SetYTitle("Events")
    h_tep.SetLineColor(2)
    h_tep.SetLineWidth(3)
    return h_tep

bbar_part=getParticle(root,-5,1)
b_part=getParticle(root,5,1)
chi_part=getParticle(root,52,1)
chibar_part=getParticle(root,-52,1)
# genmet=(chi_part+chibar_part).Pt()

for i in len(chi_part):
    gebMET=chi_part[i]+chibar_part[i]
    if gebMET > 200 and ( abs(bbar_part[i].Eta()) < 2.4 and abs(b_part[i].Eta()) < 2.4 ):
        genColl.append(gebMET)

print "efficiency", (len(genColl)/len(chi_part))
