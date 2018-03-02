
import elementtree.ElementTree as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle



tree1 = ET.parse('NLO_cmsgrid_final.lhe')
root1=tree1.getroot()
pt_phi1=[]
#lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())

   

       phi=[s for s in lines if s.split()[0]=='55']
       chi=[s for s in lines if s.split()[0]=='18']
       chibar=[s for s in lines if s.split()[0]=='-18']
          
    
       if phi:
           
           px=float (phi[0].split()[6])
           py=float (phi[0].split()[7])
           pz=float (phi[0].split()[8])
           e=float (phi[0].split()[9])
           p=TLorentzVector(px,py,pz,e)          
           pt_phi1.append(p.Pt())


'''       px1=float (chi[0].split()[6])
       py1=float (chi[0].split()[7])
       pz1=float (chi[0].split()[8])
       e1=float (chi[0].split()[9])

       px2=float (chibar[0].split()[6])
       py2=float (chibar[0].split()[7])
       pz2=float (chibar[0].split()[8])
       e2=float (chibar[0].split()[9])

       p1=TLorentzVector(px1,py1,pz1,e1)
       p2=TLorentzVector(px2,py2,pz2,e2)

       p=p1+p2
      
       pt_chi_chibar1.append(p.Pt())'''

h1=TH1F("P_{T} of #phi for NLO","",100,0,1000)
for i in pt_phi1:
        h1.Fill(i)
        


tree2 = ET.parse('mchi_1_mphi_1000_cmsgrid_final.lhe')
root2=tree2.getroot()
pt_phi2=[]
#lhefdata=LHEFData(float(root.attrib['version']))
for child in root2:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())

   

       phi=[s for s in lines if s.split()[0]=='55']
       chi=[s for s in lines if s.split()[0]=='18']
       chibar=[s for s in lines if s.split()[0]=='-18']
          
    
       if phi:
           
           px=float (phi[0].split()[6])
           py=float (phi[0].split()[7])
           pz=float (phi[0].split()[8])
           e=float (phi[0].split()[9])
           p=TLorentzVector(px,py,pz,e)          
           pt_phi2.append(p.Pt())
       
'''       px1=float (chi[0].split()[6])
       py1=float (chi[0].split()[7])
       pz1=float (chi[0].split()[8])
       e1=float (chi[0].split()[9])

       px2=float (chibar[0].split()[6])
       py2=float (chibar[0].split()[7])
       pz2=float (chibar[0].split()[8])
       e2=float (chibar[0].split()[9])

       p1=TLorentzVector(px1,py1,pz1,e1)
       p2=TLorentzVector(px2,py2,pz2,e2)

       p=p1+p2
      
       pt_chi_chibar2.append(p.Pt())'''

h2=TH1F("P_{T} of #phi for LO","",100,0,1000)
for i in pt_phi2:
        h2.Fill(i)
        




        

gStyle.SetOptStat(0)

c=TCanvas()
c.SetLogy()
h1.SetXTitle("P_{T}(phi)")
h1.SetYTitle("#events")
h1.Scale(1/h1.Integral())

h1.SetXTitle("P_{T}")
h1.SetYTitle("#events")
h1.SetLineColor(2)
h1.Draw()

h2.Scale(1/h2.Integral())
h2.SetLineColor(3)
h2.Draw("same")



c.BuildLegend(0.3,0.7,0.58,0.9,"(M_{#chi}=1, M_{#phi}=1000)")

c.SaveAs("pT(phi).png")




