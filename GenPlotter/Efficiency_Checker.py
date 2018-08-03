import elementtree.ElementTree as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle,TLatex
import os
import glob
import matplotlib.pyplot as plt

path = '/afs/cern.ch/work/d/dekumar/public/forbbDM_lhe/lhefiles_tanbeta_35_mh3_600_mchi_10_2016/'
runs=['01','02','03','04','05']

eff=[]

for r in runs:
    genMET=[]
    selEvents=[]
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

            if (pi.Pt() > 200)and (p3.Pt() > 50) and (abs(p3.Eta()) < 2.4) and (p4.Pt() > 50) and (abs(p4.Eta()) < 2.4):
                # print ("Ent")
                selEvents.append(pi.Pt())
    print ("myEvet",len(selEvents))
    print("totalEvent",len(genMET))
    eff.append((float (len(selEvents)))/(float (len(genMET)) ))
    print ("Myeff",(float (len(selEvents)))/(float (len(genMET)) ))

fout=open('Efficiency.txt','w')
for i in eff:
    print ("eff",i)
    fout.write(str(i)+'\n')


n=len(genMET)

# print ("Total events", n)
# mass=[50,100,350,400,500]
#
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
