import sys
import os.path
import argparse
import time
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import * # Load class to access McM

mcm = McM(dev=False)

f = open("./PrepId/ExtraYukawa_S0.txt","r")

tags = 'UL18FASTSIM_10p6p30'
prepids_reqs = f.readlines()

#updateA

for prepid_reqs in  prepids_reqs:
   
    reqs = mcm.get('requests', query='prepid={prepid}'.format(prepid=prepid_reqs))[0] 
    reqs['tags'] = [tags]
    
    mcm.update('requests',reqs)
    print('prepid: {}'.format(prepid_reqs))


f.close()
