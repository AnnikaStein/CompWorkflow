from argparse import ArgumentParser
import json
import pandas as pd
from pprint import pprint
import sys
import yaml

# custom
from ..utils import util
from ..templates import mail

parser = ArgumentParser(description='Generate new aftercomp mail.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml (required argument)')
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts (optional flag)')

args = parser.parse_args()

print()
print('>> Welcome to CompWorkflow -> PreComp -> aftercompMail.py <<')
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
shortName = config['comp']['shortname']
contact = config['mail']

LaF = config['orga']['lostAndFound']
if LaF != None:
    LaF = LaF.split(",")
LaFGerman = config['orga']['lostAndFoundGerman']
if LaFGerman != None:
    LaFGerman = LaFGerman.split(",")
surveyLink = config['orga']['surveyLink']
systemJRSGerman = config['orga']['systemJRSGerman']
systemJRS = config['orga']['systemJRS']

# needs to exist in order to send aftercomp mail (and I was the delegate)
resultsJson = f'CompWorkflow/input/Results for {compID}.json'
# the same that was used to print nametags (I was orga)
registrationsCSV = f'CompWorkflow/input/{compID}-registration.csv'


# performs a check for the output destination
# such that further writing of files will work
util.checkOrCreateOutputFolderContainingID(compID)

try:
    with open(resultsJson) as f:
        resultsComp = json.load(f)
except:
    sys.exit(f"\n>> ERROR: CompWorkflow/input/Results for {compID}.json not found.\n\
    Results not uploaded yet or you did not place the results json into CompWorkflow/input/Results for {compID}.json.\n\
    Come back later to send aftercomp mail or paste the results json into the default directory. <<")

# === *** === *** === CONTENT OF MAIL === *** === *** === #
content = mail.aftercomp(compID, contact, compName, shortName, LaF, LaFGerman, surveyLink, systemJRS, systemJRSGerman)
util.writeOutputFileForID(compID, 'mail_aftercomp.txt', content)


# === *** === *** === FIND MAIL RECIPIENTS === *** === *** === #
potentialCompetitors = pd.read_csv(registrationsCSV)
registeredMails = list(potentialCompetitors['Email'].values)

competedNames = [resultsComp['persons'][i]['name'] for i in range(len(resultsComp['persons']))]
competedMails = list(potentialCompetitors['Email'][potentialCompetitors['Name'].isin(competedNames)].values)

mailsSepBySemicolon = ''
for c in competedMails:
    mailsSepBySemicolon += c+';'
util.writeOutputFileForID(compID, 'mail_aftercomp_recipients.txt', mailsSepBySemicolon)

print()
print(f'>> Successfully wrote aftercomp mail content to txt file and found {len(competedMails)} relevant recipients. <<\n')
