from argparse import ArgumentParser
from pprint import pprint
import yaml

# custom
from ..utils import api, util

# NOTE: This is a basic test to check if reading and writing the same WCIF works
# Not for production purposes.

# === *** === *** === BOILERPLATE WELCOME === *** === *** === #
parser = ArgumentParser(description='Read/write private competition WCIF json.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml (required argument)')
parser.add_argument('-g', '--grant_type', default = 'password',
                    help='Choose grant_type for API request (optional flag). Default: password, alternative: authorization_code')
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts (optional flag)')
args = parser.parse_args()

print()
print('*='*80)
print()
print('>> Welcome to CompWorkflow -> PreComp -> loadPrivateWCIF.py <<')
print()
print('*='*80)
print()
print('>> Running with options:')
print('>>   debug =', args.debug)
print('>>   config =', args.config)
print('>>   grant_type =', args.grant_type)

debug = args.debug
config_path = args.config
grant_type = args.grant_type

with open('CompWorkflow/config/'+config_path) as f:
    config = yaml.safe_load(f)
    if debug:
        print()
        print('>> This is the config file:')
        pprint(config)

compID = config['comp']['ID']
compName = config['comp']['name']

# performs a check for the output destination
# such that further writing of files will work
util.checkOrCreateOutputFolderContainingID(compID)

# === *** === *** === ACTUAL SCRIPT STARTS === *** === *** === #
# === *** === *** === API REQUEST FUNCTIONS === *** === *** === #
competition_information = api.fetch_information(compID, grant_type)

# save result
util.writeOutputJSONForID(compID, f'wcif_private.json', competition_information)

print('Information about {} successfully saved.'.format(compName))

api.patch_information(compID, grant_type, competition_information)
