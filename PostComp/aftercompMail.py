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
print('>> Welcome to CompWorkflow -> PostComp -> aftercompMail.py <<')
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


# performs a check for the output destination
# such that further writing of files will work
util.checkOrCreateOutputFolderContainingID(compID)

# === *** === *** === LOAD WCIF === *** === *** === #
with open(f'CompWorkflow/output/{compID}/wcif_private.json') as file:
    wcif_private = json.load(file)


# === *** === *** === CONTENT OF MAIL === *** === *** === #
content = mail.aftercomp(compID, contact, compName, shortName, LaF, LaFGerman, surveyLink, systemJRS, systemJRSGerman)
util.writeOutputFileForID(compID, 'mail_aftercomp.txt', content)


# === *** === *** === FIND MAIL RECIPIENTS === *** === *** === #
all_personIds_who_competed = []
events = wcif_private['events']
for ev in events:
    first_round = ev['rounds'][0]
    for competitor in first_round['results']:
        personId = competitor['personId']
        all_personIds_who_competed.append(personId)
all_personIds_who_competed = util.getUniqueListEntriesSorted(all_personIds_who_competed)
competedMails = []
for person in wcif_private['persons']:
    if person['registrantId'] in all_personIds_who_competed:
        competedMails.append(person['email'])

mailsSepBySemicolon = ''
for c in competedMails:
    mailsSepBySemicolon += c+';'
util.writeOutputFileForID(compID, 'mail_aftercomp_recipients.txt', mailsSepBySemicolon)

print()
print(f'>> Successfully wrote aftercomp mail content to txt file and found {len(competedMails)} relevant recipients. <<\n')
