from argparse import ArgumentParser
import json
import pandas as pd
from pprint import pprint
import sys
import yaml

# custom
from ..utils import util
from ..templates import mail, participantsCertificates_tex

parser = ArgumentParser(description='Generate new precomp mail.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml (required argument)')
parser.add_argument('-m', '--mailType', required=True,
                    help='Type of precomp mail (firstNewsletterEveryone, finalNewsletterEveryone)')
parser.add_argument('-xDE', '--zeitBis', required=True,
                    help='Time until competition (in GERMAN)')
parser.add_argument('-xEN', '--timeUntil', required=True,
                    help='Time until competition (in ENGLISH)')
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts (optional flag)')

args = parser.parse_args()

print()
print('>> Welcome to CompWorkflow -> PreComp -> precompMail.py <<')
print()
print('>> Running with options:')
print('>>   debug =', args.debug)
print('>>   mailType =', args.mailType)
print('>>   config =', args.config)
print('>>   zeitBis =', args.zeitBis)
print('>>   timeUntil =', args.timeUntil)

debug = args.debug
config_path = args.config
mailType = args.mailType
zeitBis = args.zeitBis
timeUntil = args.timeUntil
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
fristStorno = config['orga']['fristStorno']
deadlineStorno = config['orga']['deadlineStorno']

systemJRSGerman = config['orga']['systemJRSGerman']
systemJRS = config['orga']['systemJRS']

# performs a check for the output destination
# such that further writing of files will work
util.checkOrCreateOutputFolderContainingID(compID)

# === *** === *** === ACTUAL SCRIPT STARTS === *** === *** === #
# === *** === *** === LOAD WCIF === *** === *** === #
with open(f'CompWorkflow/output/{compID}/wcif_private.json') as file:
    wcif_private = json.load(file)


# === *** === *** === CONTENT OF MAIL === *** === *** === #
if mailType == 'firstNewsletterEveryone':
    content = mail.firstNewsletterEveryone(compName, shortName, fristStorno, deadlineStorno, zeitBis, timeUntil)
elif mailType == 'finalNewsletterEveryone':
    content = mail.finalNewsletterEveryone(compID, contact, compName, shortName, fristStorno, deadlineStorno, zeitBis, timeUntil)

util.writeOutputFileForID(compID, f'mail_{mailType}.txt', content)


# === *** === *** === FIND MAIL RECIPIENTS === *** === *** === #
acceptedMails = []

for person in wcif_private['persons']:
    if person['registration']['status'] == 'accepted' and person['registration']['isCompeting'] == True:
        acceptedMails.append(person['email'])

mailsSepBySemicolon = ''
for c in acceptedMails:
    mailsSepBySemicolon += c+';'
util.writeOutputFileForID(compID, f'mail_{mailType}_recipients.txt', mailsSepBySemicolon)

print()
print(f'>> Successfully wrote {mailType} mail content to txt file and found {len(acceptedMails)} relevant recipients. <<')
