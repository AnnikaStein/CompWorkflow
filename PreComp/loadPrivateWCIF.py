from argparse import ArgumentParser
from pprint import pprint
import getpass, json, requests, yaml

# custom
from ..utils import util
from ..oauth import myOAuthApplication

parser = ArgumentParser(description='Load private competition WCIF json.')
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

# === *** === *** === API REQUEST FUNCTIONS === *** === *** === #
access_token_url = myOAuthApplication.access_token_url
competition_url = f'https://www.worldcubeassociation.org/api/v0/competitions/{compID}/wcif'

applicationDetails = myOAuthApplication.applicationDetails
applicationDetails['grant_type'] = (None, grant_type)
def get_access_token():
    if grant_type == 'password':
        wca_mail = input('Enter WCA mail address: ')
        wca_password = getpass.getpass('Enter WCA password: ')

        applicationDetails['grant_type'] = (None, grant_type)
        applicationDetails['scope'] = (None, 'public manage_competitions')
        applicationDetails['username'] = (None, wca_mail)
        applicationDetails['password'] = (None, wca_password)

    request1 = requests.post(access_token_url, files=applicationDetails)
    print(request1.text)
    return json.loads(request1.text)['access_token']

def fetch_information():
    access_token = get_access_token()
    authorization = 'Bearer ' + access_token
    headers2 = {'Authorization': authorization}

    # use access token to get competition information
    request2 = requests.get(competition_url, headers=headers2)

    return json.loads(request2.text)

competition_information = fetch_information()

# save result
util.writeOutputJSONForID(compID, f'wcif_private.json', competition_information)

print('Information about {} successfully saved.'.format(compName))
