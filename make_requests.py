import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import json
mcm = McM(dev=False)

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-m','--mode',help='Mode of action on requests',choices=['clone','new','define','submit','validate','approval'],default='clone')
parser.add_argument('--outputfile',help='Txt file name to contain the list of prepid.',default='test1')

args = parser.parse_args()
# Script clones a request to other campaign.
# Fefine list of modifications
# If member_of_campaign is different, it will clone to other campaign

#request_prepid_to_clone = "SUS-RunIIWinter15wmLHE-00040"




# Get a request object which we want to clone
#request = mcm.get('requests', request_prepid_to_clone)



if args.mode =='clone':
    request_prepid_to_clone ='''
    TOP-RunIISummer20UL16wmLHEGENAPV-00401 -> TOP-RunIISummer20UL16wmLHEGENAPV-00412
    TOP-RunIISummer20UL16wmLHEGEN-00435 -> TOP-RunIISummer20UL16wmLHEGEN-00446
    TOP-RunIISummer20UL17wmLHEGEN-00409 -> TOP-RunIISummer20UL17wmLHEGEN-00420 
    TOP-RunIISummer20UL18wmLHEGEN-00402 -> TOP-RunIISummer20UL18wmLHEGEN-00413    
    '''
    mulitple_requests = mcm.get_range_of_requests(request_prepid_to_clone)
    print('Found %s requests' % (len(mulitple_requests)))

    f_in= open('./PrepId/{}.txt'.format(args.outputfile),"w")

    for request in mulitple_requests:
        print(request['prepid'])
        
        #for key in modifications:
        #    request[key] = modifications[key]

        clone_answer = mcm.clone_request(request)
        if clone_answer.get('results'):
            print('Clone PrepID: %s' % (clone_answer['prepid']))
            f_in.write(clone_answer['prepid']+'\n')
        else:
            print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))
    f_in.close()
        
    
else:
    f = open('{}'.format(args.outputfile),"r")
    multiple_requests = f.readlines() 

    for request in multiple_requests:
        request = mcm.get('requests', request)
        
        print("Single Request: {}".format(request['prepid']))



        if args.mode =='new':
            Answer = mcm.approve("requests", request['prepid'], 0)
        elif args.mode=='validate':
            Answer = mcm.approve("requests", request['prepid'], 1)
        elif args.mode=='define':
            Answer = mcm.approve("requests", request['prepid'], 2)
        elif args.mode=='approved':
            Answer = mcm.approve("requests", request['prepid'], 3)
        elif args.mode=='submit':
            Answer = mcm.approve("requests", request['prepid'], 4)

        else:raise ValueError("No such mode {}".format(args.mode))

        #if Answer.get('result'):
        #    print("PrepID: {}, Status: {}".format(request['prepid'], args.mode))
        #else:
        #    print('Something went wrong while in {} for request with PrepId: {}. {}'.format(args.mode,request['prepid'],dumps(Answer)))



# Make predefined modifications
'''
print(request)

    '''
