import getpass, json, requests
from ..oauth import myOAuthApplication
from pprint import pprint

# Interaction with the WCA REST API
# Requires oauth application, defined in oauth/myOAuthApplication.py

access_token_url = myOAuthApplication.access_token_url
applicationDetails = myOAuthApplication.applicationDetails
def get_access_token(grant_type):
    applicationDetails['grant_type'] = (None, grant_type)
    if grant_type == 'password':
        print()
        wca_mail = input('Enter WCA mail address: ')
        wca_password = getpass.getpass('Enter WCA password: ')

        applicationDetails['grant_type'] = (None, grant_type)
        applicationDetails['scope'] = (None, 'public manage_competitions')
        applicationDetails['username'] = (None, wca_mail)
        applicationDetails['password'] = (None, wca_password)

    request1 = requests.post(access_token_url, files=applicationDetails)
    print()
    print(request1.text)
    return json.loads(request1.text)['access_token']

def fetch_information(compID, grant_type):
    access_token = get_access_token(grant_type)
    authorization = 'Bearer ' + access_token
    headers2 = {'Authorization': authorization}

    # use access token to get competition information
    competition_url = f'https://www.worldcubeassociation.org/api/v0/competitions/{compID}/wcif'
    request2 = requests.get(competition_url, headers=headers2)

    return json.loads(request2.text)

def patch_information(compID, grant_type, payload):
    access_token = get_access_token(grant_type)
    authorization = 'Bearer ' + access_token
    headers3 = {'Authorization': authorization, 'content-type': 'application/json'}
    competition_url = f'https://www.worldcubeassociation.org/api/v0/competitions/{compID}/wcif'
    pprint(payload)
    response = requests.patch(competition_url, data=json.dumps(payload), headers=headers3)
    print('>> Patch response:', response.status_code, response.reason)
