from ROOT import TGraph, TFile, TGraphAsymmErrors
from array import array
import os
import glob,math
import matplotlib.pyplot as plt

file1='/Users/dekumar/cernbox/monoH_lhefiles/2HDM_sintheta_scan_tan_1_mh3_600_mh4_100/Events/scan_run_[03-12].txt'
file2='/Users/dekumar/cernbox/monoH_lhefiles/monoH_tanbetascan_Ma_100_MA_600_sintheta_7/Events/scan_run_[01-11].txt'
f=open(file1,'r')

sin=[]
cross=[]

for line in f:
    if 'run_' in line:
        # print (line.split()[1],"    ",line.split()[2])
        sp=line.split()[1]
        CS=line.split()[2]
        # print (CS)
        sin.append(float(sp))
        cross.append(float(CS))

f.close()

print (sin)
print (cross)
plt.plot(sin,cross,'-o',label='$M_{A}=600, M_{a}=100,M_{\chi}=10, $'+r'$tan{\beta}$=1 ',color='red')

# plt.rc('axes', labelsize=20)
plt.xlabel(r'$Sin{\theta}$')
plt.ylabel("Cross section(pb)")
# plt.xticks([.1, .2, .3, .35, .4, .5,.6,.7,.8,.9])
plt.legend()#ncol=3,title=r"tan$\beta$")
plt.title(r"monoH+DM       2HDM+a")
plt.savefig('sintheta_scan.pdf')
plt.savefig('sintheta_scan.png')
plt.close('all')


f=open(file2,'r')

tan=[]
cross2=[]

for line in f:
    if 'run_' in line:
        # print (line.split()[1],"    ",line.split()[2])
        sp=line.split()[1]
        CS=line.split()[2]
        # print (CS)
        tan.append(float(sp))
        cross2.append(float(CS))

f.close()

print (tan)
print (cross2)
plt.plot(tan,cross2,'-o',label='$M_{A}=600, M_{a}=100,M_{\chi}=10, $'+r'$Sin{\theta}$=0.7 ',color='red')

plt.rc('axes', labelsize=20)
plt.xlabel(r'$Tan{\beta}$')
plt.ylabel("Cross section(pb)")
# plt.xticks([.1, .2, .3, .35, .4, .5,.6,.7,.8,.9])
plt.legend()#ncol=3,title=r"tan$\beta$")
plt.title(r"monoH+DM       2HDM+a")
plt.savefig('tan_scan.pdf')
plt.savefig('tan_scan.png')
plt.close('all')
