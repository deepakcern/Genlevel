
import elementtree.ElementTree as ET
from ROOT import TLorentzVector, TCanvas, TH1F



tree = ET.parse('unweighted_events.lhe')
root=tree.getroot()

invisible_events1=[]
invisible_events2=[]
invisible_events3=[]
invisible_events4=[]
invisible_events5=[]


for child in root:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())



      
       chi=[s for s in lines if s.split()[0]=='52']



       px1=float (chi[0].split()[6])
       py1=float (chi[0].split()[7])
       pz1=float (chi[0].split()[8])
       e1=float (chi[0].split()[9])

       p1=TLorentzVector(px1,py1,pz1,e1)


       if(p1.Pt()>=100):
          i=1
          invisible_events1.append(i)
          i+=1

       if(p1.Pt()>=200):
          i=1
          invisible_events2.append(i)
          i+=1


       if(p1.Pt()>=250):
          i=1
          invisible_events3.append(i)
          i+=1


       if(p1.Pt()>=300):
          i=1
          invisible_events4.append(i)
          i+=1



       if(p1.Pt()>=350):
          i=1
          invisible_events5.append(i)
          i+=1

print "events and acceptance for pt=100" 
print (len(invisible_events1))

print len(invisible_events1)/5000.0

print "events and acceptance for pt=200" 
print (len(invisible_events2))

print len(invisible_events2)/5000.0

print "events and acceptance for pt=250" 
print (len(invisible_events3))

print len(invisible_events3)/5000.0

print "events and acceptance for pt=300" 
print (len(invisible_events4))

print len(invisible_events4)/5000.0

print "events and acceptance for pt=350" 
print (len(invisible_events5))

print len(invisible_events5)/5000.0










