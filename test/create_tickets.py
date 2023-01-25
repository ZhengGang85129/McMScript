import sys
import os.path
import argparse
import time
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import * # Load class to access McM


f = open("./PrepId/ExtraYukawa_S0.txt","r")

tags = 'extrayukawa_runIISummer20'

mcm = McM(dev=False)
query_requests = mcm.get('requests',query='tags={tags}'.format(tags=tags))

ticket_requests = []

for request in  query_requests:
    print('prepid: {}'.format(request['prepid']))
    if "-RunIISummer20UL16wmLHEGEN-" in request['prepid']:
        ticket_requests.append(request['prepid'])
        print(request['prepid'])




new_mccm = {'pwg': 'TOP', 'prepid': 'TOP', 'requests': ticket_requests,'block':2}
ticket = mcm.put('mccms', new_mccm)
print(ticket['prepid'])
