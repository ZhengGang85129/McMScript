import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
import json
from rest import McM
from json import dumps

mcm = McM(dev=False)
prepid = 'TOP-RunIISpring21UL18FSwmLHEGSPremix-00003'
#Get request (dictionary) from McM with "prepid" prepid
req = mcm.get('requests', prepid)
# Nicely print dictionary with four space indents
print(json.dumps(req, indent=4))
