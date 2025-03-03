from argparse import ArgumentParser
import json
import pandas as pd
from pprint import pprint
import sys
import yaml

# custom
from ..utils import util
from ..templates import mail, participantsCertificates_tex

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
partCertLink = config['orga']['partCertLink']
systemJRSGerman = config['orga']['systemJRSGerman']
systemJRS = config['orga']['systemJRS']
backgroundImg_path = config['orga']['certificateBgPath']

# performs a check for the output destination
# such that further writing of files will work
util.checkOrCreateOutputFolderContainingID(compID)

# === *** === *** === ACTUAL SCRIPT STARTS === *** === *** === #
# === *** === *** === LOAD WCIF === *** === *** === #
with open(f'CompWorkflow/output/{compID}/wcif_private.json') as file:
    wcif_private = json.load(file)


# === *** === *** === CONTENT OF MAIL === *** === *** === #
content = mail.aftercomp(compID, contact, compName, shortName, LaF, LaFGerman, surveyLink, partCertLink, systemJRS, systemJRSGerman)
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
competedNames = []
competedRegistrantIds = []
for person in wcif_private['persons']:
    if person['registrantId'] in all_personIds_who_competed:
        competedMails.append(person['email'])
        competedNames.append(person['name'])
        competedRegistrantIds.append(person['registrantId'])

mailsSepBySemicolon = ''
for c in competedMails:
    mailsSepBySemicolon += c+';'
util.writeOutputFileForID(compID, 'mail_aftercomp_recipients.txt', mailsSepBySemicolon)

print()
print(f'>> Successfully wrote aftercomp mail content to txt file and found {len(competedMails)} relevant recipients. <<')

# === *** === *** === PARTICIPANT BEST RANKS === *** === *** === #
highestRank_strings = []
for regId in competedRegistrantIds:
    regId_best_rank = {eve : [99999, '-'] for eve in [e['id'] for e in events]}
    for ev in events:
        for ro in ev['rounds']:
            for competitor in ro['results']:
                if competitor['personId'] == regId:
                    regId_best_rank[ev['id']] = [int(competitor['ranking']), ro['id']]
    regId_overall_best_rank = 99999
    regId_overall_best_rank_meta = []
    for key, item in regId_best_rank.items():
        if item[0] < regId_overall_best_rank:
            # new best
            regId_overall_best_rank = item[0]
            regId_overall_best_rank_meta = [item[1]]
        elif item[0] == regId_overall_best_rank:
            # tie
            regId_overall_best_rank_meta.append(item[1])
    if len(regId_overall_best_rank_meta) > 1:
        multiple_events_str = ', '.join(map(str, regId_overall_best_rank_meta))
        highestRank_strings.append(f'{regId_overall_best_rank} ({multiple_events_str})')
    else:
        highestRank_strings.append(f'{regId_overall_best_rank} ({regId_overall_best_rank_meta[0]})')

# === *** === *** === PARTICIPANT CERTIFICATES === *** === *** === #
print()
print(f'>> Creating participant certificates.')
for ind, regId in enumerate(competedRegistrantIds):
    test_participant_cert = participantsCertificates_tex.participant(name_string = util.getLatinNameFromFullName(competedNames[ind]), compName = compName, highestRank_string = highestRank_strings[ind], backgroundImg_path = backgroundImg_path)
    util.writeOutputFileForID(compID, f'participants/participant_cert_{regId}.tex', test_participant_cert)
    print(f'>> Compiling pdf.')
    util.compilePdflatex(compID, f'participant_cert_{regId}.tex', subFolder = '/participants', cleanUp = True)

print()
print(f'>> Successfully wrote and compiled participant certificates. <<\n')
