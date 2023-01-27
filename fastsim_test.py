import sys
import os
from rest import McM

sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
mcm = McM(dev = False)

request_preid_to_clone = '''
TOP-RunIISpring21UL18FSwmLHEGSPremix-00003 -> TOP-RunIISpring21UL18FSwmLHEGSPremix-00005
'''

multiple_requests = mcm.get_range_of_requests(request_preid_to_clone)


if os.path.isdir('PrepId'):
    pass
else:
    os.mkdir('PrepId')


File_Clone_request_list = 'PrepId/fastsim_clone.txt'
if os.path.isfile(File_Clone_request_list):
    raise ValueError('Duplicate File Names')



F_in = open(File_Clone_request_list, 'w')
Tags = 'UL18FASTSIM_10p6p30'
New_campaing_name = 'RunIISpring22UL18FSwmLHEGSPremix'
Cmssw_release = 'CMSSW_10_6_30'
def AddTags(prepid = '', tags = ''):

    reqs = mcm.get('requests', prepid)
    print(reqs['tags'])
    reqs['tags'] = [Tags]

    mcm.update('requests', reqs)

for request in multiple_requests:
    print('===========================================')
    print('--------- Reference request ---------------')
    print('PrepID: {}'.format(request.get('prepid',None)))
    print('CMSSW release: {}'.format(request.get('cmssw_release',None)))
    print('tags: {}'.format(request.get('tags',None))) 
    print('memeber of campaign: {}'.format(request.get('member_of_campaign',None)))
    
    
    """
    Update:
    """
    request['cmssw_release'] = Cmssw_release
    request['member_of_campaign'] = New_campaing_name
    

    print('--------- Cloned request ---------------')
    clone_request = mcm.clone_request(request)
    #mcm.update('requests',clone_request) 
    if clone_request.get('results'):
        AddTags(clone_request['prepid'], tags = Tags)
        print('Clone PrepID: {}'.format(clone_request['prepid']))
        print('Tags: {}'.format(Tags))
        F_in.write(clone_request['prepid']+'\n')
    else:
        print('Something is wrong while cloning a request.')
    print('===========================================')


F_in.close()
    




