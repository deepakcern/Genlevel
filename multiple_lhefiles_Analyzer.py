
import elementtree.ElementTree as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle



tree1 = ET.parse('mchi_1_mphi_100_cmsgrid_final.lhe')
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

h1=TH1F("P_{T}for M_{#phi}=100","",100,100,1000)
for i in pt_phi1:
        h1.Fill(i)
        


tree2 = ET.parse('mchi_1_mphi_350_cmsgrid_final.lhe')
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

h2=TH1F("P_{T}for M_{#phi}=350","",100,100,1000)
for i in pt_phi2:
        h2.Fill(i)
        




tree3 = ET.parse('mchi_1_mphi_400_cmsgrid_final.lhe')
root3=tree3.getroot()
pt_phi3=[]
#lhefdata=LHEFData(float(root.attrib['version']))
for child in root3:
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
           pt_phi3.append(p.Pt())


       
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
      
       pt_chi_chibar3.append(p.Pt())'''

h3=TH1F("P_{T}for M_{#phi}=400","",100,100,1000)
for i in pt_phi3:
        h3.Fill(i)

#########################################################################################

tree4 = ET.parse('mchi_1_mphi_500_cmsgrid_final.lhe')
root4=tree4.getroot()
pt_phi4=[]
#lhefdata=LHEFData(float(root.attrib['version']))
for child in root4:
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
           pt_phi4.append(p.Pt())   

       
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
      
       pt_phi3.append(p.Pt())'''

h4=TH1F("P_{T}for M_{#phi}=500","",100,100,1000)
for i in pt_phi4:
        h4.Fill(i)
############################################################################

tree5 = ET.parse('mchi_1_mphi_1000_cmsgrid_final.lhe')
root5=tree5.getroot()
pt_phi5=[]
#lhefdata=LHEFData(float(root.attrib['version']))
for child in root5:
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
           pt_phi5.append(p.Pt())
       
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
      
       pt_chi_chibar3.append(p.Pt())'''

h5=TH1F("P_{T}for M_{#phi}=1000","",100,100,1000)
for i in pt_phi5:
        h5.Fill(i)
########################################################################

        

gStyle.SetOptStat(0)

c=TCanvas()
c.SetLogy()
h1.SetXTitle("P_{T}(#phi)")
h1.SetYTitle("#events")
h1.Scale(1/h1.Integral())

h1.SetXTitle("P_{T}")
h1.SetYTitle("#events")
h1.SetLineColor(2)
h1.Draw()

h2.Scale(1/h2.Integral())
h2.SetLineColor(3)
h2.Draw("same")

h3.Scale(1/h3.Integral())
h3.SetLineColor(4)
h3.Draw("same")

h4.Scale(1/h4.Integral())
h4.SetLineColor(6)
h4.Draw("same")

h5.Scale(1/h5.Integral())
h5.SetLineColor(1)
h5.Draw("same")

c.BuildLegend(0.2,0.7,0.48,0.9,"M_{#chi}=1")

c.SaveAs("pT(phi).png")




