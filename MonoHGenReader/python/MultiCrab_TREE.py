import os

postfix="_2dScan_2HDM_LHE"

#datasetfile = open('allMCMonoHbb2016Legacy.txt','r')
#datasetfile = open('datsetsMonoHbb.txt','r')

def prepare(path_):
    outfile = open('allmonoHsamples.txt','w')
    for root_, dirs_, filenames_ in os.walk(path_):
        for ifile_ in filenames_:
            reqname_ = ifile_.replace('_tarball.tar.xz','')
            datasetname_ = reqname_
            inputpath_ = os.path.join(root_,ifile_)
            iline = reqname_ + ' [\\"tarball=' + inputpath_ + '\\"] ' + datasetname_ + '\n'
            outfile.write(iline)
        outfile.close()


def submit():
    print "submitting"
    f = open('GENSamples.txt','r')
    #f = open('GENSamples_ZPB.txt','r')
    for line in f:
        print line
        #a=[]
        #b=[]
        #c=[]
        #a,b,c = line.split()
        a = line.rstrip()
        b = a.split('/')[1]
        #c = b
        datasetdetail=[a,b]
        print datasetdetail
        os.system('cp -p crabConfig_stepTREE.py crabConfig.py')
        os.system ('crab submit General.requestName='+datasetdetail[1]+' Data.inputDataset='+datasetdetail[0])
        
        



def status(crabdirname):
    import os
    os.system ("./Statusall.sh "+crabdirname)


def resubmit(crabdirname):
    import os
    os.system ("./Resubmit.sh "+crabdirname)

    
    

## Add a help or usage function here 
def help() :
    print "this is under progress"

    


####################################################################################################################################################
####################################################################################################################################################
## this will control the functions   ##
## convert this to python main.      ##
####################################################################################################################################################
####################################################################################################################################################
import os
import sys
print sys.argv


## safety check
## improve this
if len(sys.argv) < 2 :
    print "insufficient options provided see help function "
    help()
    exit (1)


## submit jobs 
if len(sys.argv) == 2 :
    if sys.argv[1] == "submit" :
        submit()


if len(sys.argv) == 3 :
    if sys.argv[1] == "prepare" :
        path_ = sys.argv[2]
        prepare(path_)




## check status of jobs 
## send the crab directory 
if len(sys.argv) == 3 : 
    if sys.argv[1] == "status" :
        crabdir = sys.argv[2]
        status(crabdir)



if len(sys.argv) == 3 : 
    if sys.argv[1] == "resubmit" :
        crabdir = sys.argv[2]
        resubmit(crabdir)





#  LocalWords:  MonoHToBBarMZp
