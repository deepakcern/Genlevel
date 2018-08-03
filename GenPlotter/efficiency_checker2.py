import matplotlib.pyplot as plt



f=open('Efficiency.txt','r')
eff=[]
for line in f:
    print (float (line.split()[0]))
    eff.append(float (line.split()[0]))


# print ("Total events", n)
mass=[50,100,350,400,500]


plt.plot(mass,eff,'-o',color='red')

plt.rc('axes', labelsize=20)
plt.xlabel(r'$M_{a}$ (GeV)')
plt.ylabel("Efficiency*Acceptance")
# plt.xticks([.1, .2, .3, .35, .4, .5,.6,.7,.8,.9])
plt.legend(title=r"$M_{A}=600GeV,M_{\chi}=10GeV, Tan{\beta}=35$"+"\n"+r"genMET > 200 GeV, $p_{T}(b,\bar{b})>50 GeV,$"+"\n"+r"$ {\eta}(b,\bar{b})$ < 2.4)")
plt.title(r"bb+DM                    2HDM+a")
plt.savefig('Eff.pdf')
plt.savefig('Eff.png')
plt.close('all')
