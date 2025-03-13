from argparse import ArgumentParser
from pprint import pprint
import json, math, yaml
from datetime import datetime
from dateutil import rrule

# custom
from ..utils import api, util

# === *** === *** === BOILERPLATE WELCOME === *** === *** === #
parser = ArgumentParser(description='Generate psych sheet from existing WCIF.')
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
print('>> Welcome to CompWorkflow -> PreComp -> generatePsych.py <<')
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
# === *** === *** === LOAD WCIF === *** === *** === #
with open(f'CompWorkflow/output/{compID}/wcif_private.json') as file:
    wcif_private = json.load(file)

# === *** === *** === MODEL Registration / WorldRanks === *** === *** === #
registeredDict = {}
for p in wcif_private['persons']:
    if p['registration'] != None:
        if p['registration']['status'] == 'accepted' and p['registration']['isCompeting'] == True:
            wrForRegistered = {}
            for e in p['registration']['eventIds']:
                rankValues = [99999999,99999999]
                for pb in p['personalBests']:
                    if pb['eventId'] == e:
                        if pb['type'] == "single":
                            rankValues = [pb['worldRanking'], rankValues[1]]
                        elif pb['type'] == "average":
                            rankValues = [rankValues[0], pb['worldRanking']]
                wrForRegistered[e] = rankValues
            registeredDict[p['registrantId']] = wrForRegistered
print()
# === *** === *** === CALC PsychSheet === *** === *** === #
psych_dict = {}
for ev in wcif_private['events']:
    evId = ev['id']
    relevantPersonsDict = {}
    for r in registeredDict.keys():
        if evId in registeredDict[r].keys():
            # this person is competing in the current event
            relevantPersonsDict[r] = registeredDict[r][evId]
    if evId in util.sortBySingleOnly:
        print(f'>> Psych Sheet via World Ranks (Single Only) for {evId}')
        sortedRelevantPersonsList = (sorted(relevantPersonsDict.items(), key=lambda e: e[1][0]))
    elif evId in util.sortBySingleAverage:
        print(f'>> Psych Sheet via World Ranks (Single First, Then Average) for {evId}')
        sortedRelevantPersonsList = (sorted(relevantPersonsDict.items(), key=lambda e: (e[1][0], e[1][1])))
    else:
        print(f'>> Psych Sheet via World Ranks (Average First, Then Single) for {evId}')
        sortedRelevantPersonsList = (sorted(relevantPersonsDict.items(), key=lambda e: (e[1][1], e[1][0])))
    sortedRelevantPersonsDict = [{'registrantId' : items[0], 'worldRanks' : items[1]} for items in sortedRelevantPersonsList]
    psych_dict[evId] = sortedRelevantPersonsDict
# save result
util.writeOutputJSONForID(compID, f'psych_dict.json', psych_dict)
print()
print('>> Psych sheet for {} successfully created and saved to disk.'.format(compName))
