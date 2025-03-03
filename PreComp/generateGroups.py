from argparse import ArgumentParser
from pprint import pprint
import json, math, yaml

# custom
from ..utils import util

# === *** === *** === BOILERPLATE WELCOME === *** === *** === #
parser = ArgumentParser(description='Generate groups from existing WCIF.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml (required argument)')
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts (optional flag)')
args = parser.parse_args()

print()
print('*='*80)
print()
print('>> Welcome to CompWorkflow -> PreComp -> generateGroups.py <<')
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

if ',' in str(config['setup']['stationsPerStage']):
    stationsPerStage = config['setup']['stationsPerStage'].split(",")
else:
    stationsPerStage = [config['setup']['stationsPerStage']]

# performs a check for the output destination
# such that further writing of files will work
util.checkOrCreateOutputFolderContainingID(compID)

# === *** === *** === ACTUAL SCRIPT STARTS === *** === *** === #
# === *** === *** === LOAD WCIF === *** === *** === #
with open(f'CompWorkflow/output/{compID}/wcif_private.json') as file:
    wcif_private = json.load(file)

# === *** === *** === LOAD events_nComp === *** === *** === #
with open(f'CompWorkflow/output/{compID}/event_nComp.json') as file:
    event_nComp = json.load(file)

# === *** === *** === MODEL Schedule === *** === *** === #
eventsAtComp = event_nComp.keys()
evRound_dict = {}
evAct_dict = {ev : [] for ev in eventsAtComp}
for eve in wcif_private['events']:
    for rou in eve['rounds']:
        if eve['id'] in eventsAtComp and eve['id'] not in ['333fm']:
            evRound_dict[rou['id']] = []

for ven in wcif_private['schedule']['venues']:
    for rooInd, roo in enumerate(ven['rooms']):
        for act in roo['activities']:
            if act['activityCode'] in ['other', 'other-awards', 'other-checkin', 'other-lunch', 'other-misc', 'other-multi', 'other-tutorial']:
                continue
            #print(act)
            evRound = act['activityCode'].split('-r')[0] + '-r' + act['activityCode'].split('-r')[1][0]
            if act['activityCode'].split('-r')[0] == '333fm':
                evRound = act['activityCode']
                if not evRound in evRound_dict:
                    evRound_dict[evRound] = []
            evRound_dict[evRound].append(rooInd)
# maybe TODO: dump evRound_dict as json output

# === *** === *** === CALC Heats/Groups === *** === *** === #
print('eve, roundNumber, peopleInRound, heatsDecimal, heatsRounded')
for rou, rouValue in evRound_dict.items():
    if '-r1' in rou:
        # first round
        eve = rou.split('-r')[0]
        if eve not in util.nogroupsEvents:
            # how many heats needed?
            availStations = sum([int(stationsPerStage[staInd]) for staInd in rouValue])
            if eve in util.shortEvents:
                factor = 2.0
            else:
                factor = 1.5
            capacityInHeat = availStations * factor
            heatsDecimal = event_nComp[eve] / capacityInHeat
            heatsRounded = util.customRoundHeat(heatsDecimal)
            print(eve, 1, event_nComp[eve], heatsDecimal, heatsRounded)
            # distribute heats into stages
        else:
            continue
            # ToDo
            # needs no childActivities
            # force one group first stage
    elif ('-r2' in rou) or ('-r3' in rou) or ('-r4' in rou):
        # second, third or fourth round
        eve = rou.split('-r')[0]
        roundNumber = 2 if ('-r2' in rou) else (3 if ('-r3' in rou) else 4)
        previousRoundNumberZeroCounted = roundNumber - 2
        if eve not in util.nogroupsEvents:
            # how many heats needed?
            availStations = sum([int(stationsPerStage[staInd]) for staInd in rouValue])
            if eve in util.shortEvents:
                factor = 2.0
            else:
                factor = 1.5
            capacityInHeat = availStations * factor

            for ev in wcif_private['events']:
                if ev['id'] == eve:
                    ac = ev['rounds'][previousRoundNumberZeroCounted]['advancementCondition']
                    if ac['type'] == 'percent':
                        peopleInRound = math.floor(event_nComp[eve] * ac['level'] / 100)
                    elif ac['type'] == 'ranking':
                        peopleInRound = ac['level']
            heatsDecimal = peopleInRound / capacityInHeat
            heatsRounded = util.customRoundHeat(heatsDecimal)
            print(eve, roundNumber, peopleInRound, heatsDecimal, heatsRounded)
            # distribute heats into stages
        else:
            continue

print(evRound_dict)
#for ev in eventsAtComp:
    # walk through schedule from WCIF
