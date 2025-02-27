from argparse import ArgumentParser
from datetime import datetime
from pprint import pprint
import json, pycountry, yaml

# custom
from ..utils import util

# === *** === *** === BOILERPLATE WELCOME === *** === *** === #
parser = ArgumentParser(description='Generate registration list from existing WCIF.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml (required argument)')
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts (optional flag)')
args = parser.parse_args()

print()
print('*='*80)
print()
print('>> Welcome to CompWorkflow -> PreComp -> generateRegistrationList.py <<')
print()
print('*='*80)
print()
print('>> Running with options:')
print('>>   debug =', args.debug)
print('>>   config =', args.config)

debug = args.debug
config_path = args.config

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
# === *** === *** === LOAD WCIF === *** === *** === #
with open(f'CompWorkflow/output/{compID}/wcif_private.json') as file:
    wcif_private = json.load(file)

registration_list_ = []
registration_list_NewcomersOnly_ = []
registration_list_csvString = 'Name,Birthdate,Country,WCA ID,Checked?,Comment\n'
registration_list_NewcomersOnly_csvString = 'Name,Birthdate,Country,Checked?,Comment\n'
nPersons = len(wcif_private['persons'])
for p in range(nPersons):
    person = wcif_private['persons'][p]
    if person['registration'] != None:
        if wcif_private['registrationInfo']['openTime'] < str(datetime.now()):
            # reg open
            if person['registration']['status'] == 'accepted' and person['registration']['isCompeting'] == True:
                registration_list_.append([person["name"],person["birthdate"],pycountry.countries.get(alpha_2=person["countryIso2"]).name,person["wcaId"]])
                registration_list_csvString += f'"{person["name"]}",{person["birthdate"]},{pycountry.countries.get(alpha_2=person["countryIso2"]).name},{person["wcaId"]},,\n'
                if person["wcaId"] == None:
                    registration_list_NewcomersOnly_.append([person["name"],person["birthdate"],pycountry.countries.get(alpha_2=person["countryIso2"]).name])
                    registration_list_NewcomersOnly_csvString += f'"{person["name"]}",{person["birthdate"]},"{pycountry.countries.get(alpha_2=person["countryIso2"]).name}",,\n'
        else:
            # reg not open yet
            if person['registration']['isCompeting'] == True:
                registration_list_.append([person["name"],person["birthdate"],pycountry.countries.get(alpha_2=person["countryIso2"]).name,person["wcaId"]])
                registration_list_csvString += f'"{person["name"]}",{person["birthdate"]},{pycountry.countries.get(alpha_2=person["countryIso2"]).name},{person["wcaId"]},,\n'
                if person["wcaId"] == None:
                    registration_list_NewcomersOnly_.append([person["name"],person["birthdate"],pycountry.countries.get(alpha_2=person["countryIso2"]).name])
                    registration_list_NewcomersOnly_csvString += f'"{person["name"]}",{person["birthdate"]},"{pycountry.countries.get(alpha_2=person["countryIso2"]).name}",,\n'


registration_list_csvString_sorted = 'Name,Birthdate,Country,WCA ID,Checked?,Comment\n'
registration_list_NewcomersOnly_csvString_sorted = 'Name,Birthdate,Country,Checked?,Comment\n'
registration_list_sorted = util.getSortedListOfListsByNthColumn(registration_list_, 0)
registration_list_NewcomersOnly_sorted = util.getSortedListOfListsByNthColumn(registration_list_NewcomersOnly_, 0)
for comp in registration_list_sorted:
    registration_list_csvString_sorted += f'"{comp[0]}","{comp[1]}","{comp[2]}","{comp[3]}",,\n'
for newc in registration_list_NewcomersOnly_sorted:
    registration_list_NewcomersOnly_csvString_sorted += f'"{newc[0]}","{newc[1]}","{newc[2]}",,\n'


# === *** === *** === SAVE REGISTRATION LIST (csv) === *** === *** === #
util.writeOutputFileForID(compID, f'registration_list.csv', registration_list_csvString)
util.writeOutputFileForID(compID, f'registration_list_NewcomersOnly.csv', registration_list_NewcomersOnly_csvString)

util.writeOutputFileForID(compID, f'registration_list_sorted.csv', registration_list_csvString_sorted)
util.writeOutputFileForID(compID, f'registration_list_NewcomersOnly_sorted.csv', registration_list_NewcomersOnly_csvString_sorted)

# === *** === *** === SAVE REGISTRATION LIST (tex) === *** === *** === #
# ToDo
# === *** === *** === SAVE REGISTRATION LIST (pdf) === *** === *** === #
# ToDo
print(f'Registration list for {compName} successfully saved.')
