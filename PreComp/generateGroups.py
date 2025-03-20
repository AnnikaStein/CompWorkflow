from argparse import ArgumentParser
from pprint import pprint
import json, math, yaml
from datetime import datetime
from dateutil import rrule

# custom
from ..utils import api, util

# === *** === *** === BOILERPLATE WELCOME === *** === *** === #
parser = ArgumentParser(description='Generate groups from existing WCIF.')
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
print('>> Welcome to CompWorkflow -> PreComp -> generateGroups.py <<')
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

if ',' in str(config['setup']['stationsPerStage']):
    stationsPerStage = config['setup']['stationsPerStage'].split(",")
else:
    stationsPerStage = [config['setup']['stationsPerStage']]

if ',' in str(config['setup']['assignRoles']):
    assignRoles = config['setup']['assignRoles'].split(",")
else:
    assignRoles = [config['setup']['assignRoles']]

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
            evRound_dict[rou['id']] = {}

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
                    evRound_dict[evRound] = {}
            evRound_dict[evRound] |= {rooInd : []}

# === *** === *** === FIND Number of Existing Activities === *** === *** === #
maxCurrentNumberOfDeepActivities = 0
for ven in wcif_private['schedule']['venues']:
    for rooInd, roo in enumerate(ven['rooms']):
        for act in roo['activities']:
            if act['id'] > maxCurrentNumberOfDeepActivities:
                maxCurrentNumberOfDeepActivities = act['id']
            for chiAct in act['childActivities']:
                if chiAct['id'] > maxCurrentNumberOfDeepActivities:
                    maxCurrentNumberOfDeepActivities = chiAct['id']
print()
print(f'>> maxCurrentNumberOfDeepActivities = {maxCurrentNumberOfDeepActivities}')


# === *** === *** === CALC Heats/Groups === *** === *** === #
print()
print('eve, roundNumber, peopleInRound, heatsDecimal, heatsRounded')
heatsDict = {}
rolesDict = {}
for rou, rouValue in evRound_dict.items():
    eve = rou.split('-r')[0]
    if eve not in util.nogroupsEvents:
        roundNumber = 1 if '-r1' in rou else (2 if ('-r2' in rou) else (3 if ('-r3' in rou) else 4))
        if roundNumber == 2:
            previousRoundNumberZeroCounted = 0
            for ev in wcif_private['events']:
                if ev['id'] == eve:
                    ac = ev['rounds'][previousRoundNumberZeroCounted]['advancementCondition']
                    if ac['type'] == 'percent':
                        peopleInSecondRound = math.floor(event_nComp[eve] * ac['level'] / 100)
                    elif ac['type'] == 'ranking':
                        peopleInSecondRound = ac['level']
            peopleInRound = peopleInSecondRound
        elif roundNumber == 3:
            previousRoundNumberZeroCounted = 1
            for ev in wcif_private['events']:
                if ev['id'] == eve:
                    ac = ev['rounds'][0]['advancementCondition']
                    if ac['type'] == 'percent':
                        peopleInSecondRound = math.floor(event_nComp[eve] * ac['level'] / 100)
                    elif ac['type'] == 'ranking':
                        peopleInSecondRound = ac['level']
                    ac_ = ev['rounds'][previousRoundNumberZeroCounted]['advancementCondition']
                    if ac_['type'] == 'percent':
                        peopleInThirdRound = math.floor(peopleInSecondRound * ac_['level'] / 100)
                    elif ac_['type'] == 'ranking':
                        peopleInThirdRound = ac_['level']
            peopleInRound = peopleInThirdRound
        elif roundNumber == 4:
            previousRoundNumberZeroCounted = 2
            for ev in wcif_private['events']:
                if ev['id'] == eve:
                    ac = ev['rounds'][0]['advancementCondition']
                    if ac['type'] == 'percent':
                        peopleInSecondRound = math.floor(event_nComp[eve] * ac['level'] / 100)
                    elif ac['type'] == 'ranking':
                        peopleInSecondRound = ac['level']

                    ac_ = ev['rounds'][1]['advancementCondition']
                    if ac_['type'] == 'percent':
                        peopleInThirdRound = math.floor(peopleInSecondRound * ac_['level'] / 100)
                    elif ac_['type'] == 'ranking':
                        peopleInThirdRound = ac_['level']

                    ac__ = ev['rounds'][previousRoundNumberZeroCounted]['advancementCondition']
                    if ac__['type'] == 'percent':
                        peopleInFourthRound = math.floor(peopleInThirdRound * ac__['level'] / 100)
                    elif ac__['type'] == 'ranking':
                        peopleInFourthRound = ac_['level']
            peopleInRound = peopleInFourthRound
        else:
            peopleInRound = event_nComp[eve]
        # how many heats needed?
        availStations = sum([int(stationsPerStage[staInd]) for staInd in rouValue])
        if eve in util.shortEvents:
            factor = 2.0
            if eve != '333bf':
                minHeatsFirstRound = 2 if roundNumber < len([1 for k in evRound_dict.keys() if eve in k]) else 1
            else:
                minHeatsFirstRound = 2 if roundNumber == 1 else 1
        elif eve in ['666', '777']:
            factor = 1.5
            minHeatsFirstRound = 2 if roundNumber < len([1 for k in evRound_dict.keys() if eve in k]) else 1
        else:
            factor = 1.5
            minHeatsFirstRound = 1
        capacityInHeat = availStations * factor
        heatsDecimal = peopleInRound / capacityInHeat
        heatsRounded = max(minHeatsFirstRound, int(util.customRoundHeat(heatsDecimal)))
        print(eve, roundNumber, peopleInRound, heatsDecimal, heatsRounded)
        roundForHeatsDict = eve + f'-r{roundNumber}'
        heatsDict[roundForHeatsDict] = heatsRounded
        # distribute heats into stages
        for staIndInd, staInd in enumerate(rouValue):
            evRound_dict[rou][staInd] = [(staIndInd + 1) + h * len(rouValue) for h in range(heatsRounded)]

        peopleInGroup = math.ceil(peopleInRound / (heatsRounded * len(rouValue)))

        capacityForGroupifierConfig = 1 / heatsRounded

        nScramblers = 0
        if 's' in assignRoles:
            nScramblers = util.customRoundAssignees(peopleInGroup, eve, assignRoles, int(stationsPerStage[0]), roleType = 's')

        nRunners = 0
        if 'r' in assignRoles:
            nRunners = util.customRoundAssignees(peopleInGroup, eve, assignRoles, int(stationsPerStage[0]), roleType = 'r')

        assignJudges = False
        nJudges = 0
        if 'j' in assignRoles:
            assignJudges = True
            nJudges = util.customRoundAssignees(peopleInGroup, eve, assignRoles, int(stationsPerStage[0]), roleType = 'j')

        rolesDict[rou] = {
            'capacity' : capacityForGroupifierConfig,
            'groups' : heatsRounded,
            'scramblers' : nScramblers,
            'runners' : nRunners,
            'assignJudges' : assignJudges,
            'judges' : nJudges
        }
    else:
        continue

has_existing_evRound_dict = True
try:
    with open(f'CompWorkflow/output/{compID}/evRound_dict.json') as file:
        existing_evRound_dict = json.load(file)
    # print('Existing evRound_dict')
    # pprint(existing_evRound_dict)
    # print('New evRound_dict')
    # pprint(evRound_dict)
    util.writeOutputJSONForID(compID, f'evRound_dict.json', evRound_dict)
    with open(f'CompWorkflow/output/{compID}/evRound_dict.json') as file:
        current_evRound_dict = json.load(file)
except:
    existing_evRound_dict = None
    has_existing_evRound_dict = False

updatedRounds = {}
if has_existing_evRound_dict:
    # check if there is sth to do, i.e. is there a round with new nHeats
    if existing_evRound_dict != current_evRound_dict:
        print('>> Existing != current')
        updatedRounds = {k: current_evRound_dict[k] for k in current_evRound_dict if k in existing_evRound_dict and current_evRound_dict[k] != existing_evRound_dict[k]}

# save result
util.writeOutputJSONForID(compID, f'evRound_dict.json', evRound_dict)
util.writeOutputJSONForID(compID, f'heatsDict.json', heatsDict)


# === *** === *** === PATCH ScrambleSetCount for every round === *** === *** === #
eventsListForPayloadScrambleSets = []
for e in wcif_private['events']:
    eDict = {
        "id": e['id'],
        "rounds": [],
        "extensions": e['extensions'],
        "qualification": e['qualification'],
    }
    for iR,r in enumerate(e['rounds']):
        rDict = {
            "id": r['id'],
            "format": r['format'],
            "timeLimit": r['timeLimit'],
            "cutoff": r['cutoff'],
            "advancementCondition": r['advancementCondition'],
            "scrambleSetCount": 1 if ('mbf' in r['id'] or 'fm' in r['id']) else heatsDict[r['id']],
            "results": r['results'],
            "extensions": r['extensions']
        }
        eDict['rounds'].append(rDict)
    eventsListForPayloadScrambleSets.append(eDict)

# === *** === *** === PATCH ActivityConfig for every round === *** === *** === #
activitiesWithRoles = rolesDict.keys()
venuesListForPayloadActivityConfig = []
for v in wcif_private['schedule']['venues']:
    vDict = {
        "id": v['id'],
        "name": v['name'],
        "latitudeMicrodegrees": v['latitudeMicrodegrees'],
        "longitudeMicrodegrees": v['longitudeMicrodegrees'],
        "countryIso2": v['countryIso2'],
        "timezone": v['timezone'],
        "rooms": [],
        "extensions": v['extensions']
    }
    for iR,r in enumerate(v['rooms']):
        rDict = {
            "id": r['id'],
            "name": r['name'],
            "color": r['color'],
            "activities": [],
            "extensions": r['extensions']
        }
        for a in r['activities']:
            thisActivityCode = a['activityCode']
            if thisActivityCode in activitiesWithRoles:
                print('has_existing_evRound_dict',has_existing_evRound_dict)
                print('thisActivityCode',thisActivityCode)
                print('updatedRounds.keys()',updatedRounds.keys())
                if has_existing_evRound_dict == False or thisActivityCode in updatedRounds.keys():
                    print(f'>> has_existing_evRound_dict = {has_existing_evRound_dict}, thisActivityCode = {thisActivityCode}, updatedRounds = {updatedRounds}')
                    groupsInThisRoom = evRound_dict[thisActivityCode][r['id'] - 1]
                    endDate = datetime.strptime(a['endTime'], '%Y-%m-%dT%H:%M:%SZ')
                    startDate = datetime.strptime(a['startTime'], '%Y-%m-%dT%H:%M:%SZ')
                    activityDurationInSeconds = (endDate - startDate).total_seconds()
                    heatDurationInSeconds = activityDurationInSeconds / len(groupsInThisRoom)
                    heatPartitionDates = list(rrule.rrule(rrule.SECONDLY, interval = int(heatDurationInSeconds), dtstart = startDate, until = endDate))
                    thisChildActivities = []
                    for groupInd, group in enumerate(groupsInThisRoom):
                        # this iterates through this room's+act childActivities,
                        # which is the same as the number of heats & groups in this room (at this stage)
                        maxCurrentNumberOfDeepActivities += 1
                        stT = heatPartitionDates[groupInd].strftime('%Y-%m-%dT%H:%M:%SZ')
                        enT = heatPartitionDates[groupInd + 1].strftime('%Y-%m-%dT%H:%M:%SZ')
                        chDict = {
                            "id": maxCurrentNumberOfDeepActivities,
                            "name": a['name'] + f', Group {group}',
                            "activityCode": a['activityCode'] + f'-g{group}',
                            "startTime": stT,
                            "endTime": enT,
                            "childActivities": [],
                            "extensions": []
                        }
                        thisChildActivities.append(chDict)

                    aDict = {
                        "id": a['id'],
                        "name": a['name'],
                        "activityCode": thisActivityCode,
                        "startTime": a['startTime'],
                        "endTime": a['endTime'],
                        "childActivities": thisChildActivities,
                        "extensions": [
                          {
                            "id": "groupifier.ActivityConfig",
                            "specUrl": "https://groupifier.jonatanklosko.com/wcif-extensions/ActivityConfig.json",
                            "data": {
                              "capacity": rolesDict[thisActivityCode]['capacity'],
                              "groups": rolesDict[thisActivityCode]['groups'],
                              "scramblers": rolesDict[thisActivityCode]['scramblers'],
                              "runners": rolesDict[thisActivityCode]['runners'],
                              "assignJudges": rolesDict[thisActivityCode]['assignJudges']
                            }
                          }
                        ]
                    }
                else:
                    aDict = {
                        "id": a['id'],
                        "name": a['name'],
                        "activityCode": thisActivityCode,
                        "startTime": a['startTime'],
                        "endTime": a['endTime'],
                        "childActivities": a['childActivities'],
                        "extensions": a['extensions']
                    }
            else:
                aDict = {
                    "id": a['id'],
                    "name": a['name'],
                    "activityCode": thisActivityCode,
                    "startTime": a['startTime'],
                    "endTime": a['endTime'],
                    "childActivities": a['childActivities'],
                    "extensions": a['extensions']
                }
            rDict['activities'].append(aDict)
        vDict['rooms'].append(rDict)
    venuesListForPayloadActivityConfig.append(vDict)

payload = {
    "events": eventsListForPayloadScrambleSets,
    "schedule": {
        "startDate": wcif_private['schedule']['startDate'],
        "numberOfDays": wcif_private['schedule']['numberOfDays'],
        "venues": venuesListForPayloadActivityConfig
    }
}
api.patch_information(compID, grant_type, payload)

print()
print('>> WCIF for {} successfully patched with ScrambleSets & ActivityConfig.'.format(compName))
