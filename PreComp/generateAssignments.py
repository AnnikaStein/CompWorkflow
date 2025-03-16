from argparse import ArgumentParser
from pprint import pprint
import json, math, yaml
from datetime import datetime
from dateutil import rrule, relativedelta
import sys

# custom
from ..utils import api, util

# === *** === *** === BOILERPLATE WELCOME === *** === *** === #
parser = ArgumentParser(description='Generate assignments from existing WCIF.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml (required argument)')
parser.add_argument('-r', '--round', default = 'allFirst',
                    help='Which round(s) to assign. Default: allFirst, alternative: type individual eventId-r')
parser.add_argument('-g', '--grant_type', default = 'password',
                    help='Choose grant_type for API request (optional flag). Default: password, alternative: authorization_code')
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts (optional flag)')
args = parser.parse_args()

print()
print('*='*80)
print()
print('>> Welcome to CompWorkflow -> PreComp -> generateAssignments.py <<')
print()
print('*='*80)
print()
print('>> Running with options:')
print('>>   debug =', args.debug)
print('>>   config =', args.config)
print('>>   grant_type =', args.grant_type)
print('>>   round =', args.round)

debug = args.debug
config_path = args.config
grant_type = args.grant_type
round = args.round

with open('CompWorkflow/config/'+config_path) as f:
    config = yaml.safe_load(f)
    if debug:
        print()
        print('>> This is the config file:')
        pprint(config)

with open('CompWorkflow/config/main.yml') as f:
    main_config = yaml.safe_load(f)
    if debug:
        print()
        print('>> This is the main_config file:')
        pprint(main_config)

compID = config['comp']['ID']
compName = config['comp']['name']

# === *** === *** === Main assignment config === *** === *** === #
minAgeS = main_config['minAgeS']
minAgeR = main_config['minAgeR']
minAgeJ = main_config['minAgeJ']

minPrevCompS = main_config['minPrevCompS']
minPrevCompThisEventS = main_config['minPrevCompThisEventS']
minPrevCompR = main_config['minPrevCompR']
minPrevCompThisEventR = main_config['minPrevCompThisEventR']
minPrevCompJ = main_config['minPrevCompJ']
minPrevCompThisEventJ = main_config['minPrevCompThisEventJ']

if main_config['neverS'] == None:
    neverS = []
else:
    if ',' in str(main_config['neverS']):
        neverS = main_config['neverS'].split(",")
    else:
        neverS = [main_config['neverS']]

if main_config['neverR'] == None:
    neverR = []
else:
    if ',' in str(main_config['neverR']):
        neverR = main_config['neverR'].split(",")
    else:
        neverR = [main_config['neverR']]

if main_config['neverJ'] == None:
    neverJ = []
else:
    if ',' in str(main_config['neverJ']):
        neverJ = main_config['neverJ'].split(",")
    else:
        neverJ = [main_config['neverJ']]

percentPodiumToPreserveInBestHeat = main_config['assignmentStrategies']['percentPodiumToPreserveInBestHeat']

# === *** === *** === Comp specific assignment config === *** === *** === #
if ',' in str(config['setup']['assignRoles']):
    assignRoles = config['setup']['assignRoles'].split(",")
else:
    assignRoles = [config['setup']['assignRoles']]

feedMbfJudgesFrom = config['setup']['feedMbfJudgesFrom']
feed444bfJudgesFrom = config['setup']['feed444bfJudgesFrom']
feed555bfJudgesFrom = config['setup']['feed555bfJudgesFrom']

# performs a check for the output destination
# such that further writing of files will work
util.checkOrCreateOutputFolderContainingID(compID)

# === *** === *** === ACTUAL SCRIPT STARTS === *** === *** === #
# === *** === *** === LOAD WCIF === *** === *** === #
with open(f'CompWorkflow/output/{compID}/wcif_private.json') as file:
    wcif_private = json.load(file)

# === *** === *** === LOAD psych_dict === *** === *** === #
with open(f'CompWorkflow/output/{compID}/psych_dict.json') as file:
    psych_dict = json.load(file)

# === *** === *** === LOAD evRound_dict === *** === *** === #
with open(f'CompWorkflow/output/{compID}/evRound_dict.json') as file:
    evRound_dict = json.load(file)

# === *** === *** === LOAD heatsDict === *** === *** === #
with open(f'CompWorkflow/output/{compID}/heatsDict.json') as file:
    heatsDict = json.load(file)

# === *** === *** === MODEL Rounds to assign === *** === *** === #
rounds = evRound_dict.keys()

events = [e['id'] for e in wcif_private['events']]

round_description = {}

nRoundsPerEvent = {key : 0 for key in events}
for ev in events:
    for r in rounds:
        if ev == r.split('-r')[0]:
            nRoundsPerEvent[ev] += 1

for r in rounds:
    roundNumber = 1 if '-r1' in r else (2 if ('-r2' in r) else (3 if ('-r3' in r) else 4))
    eve = r.split('-r')[0]
    if eve == '333fm' or eve == '333mbf':
        round_description[r] = 'unspecified'
    else:
        round_description[r] = 'roundFinal' if nRoundsPerEvent[eve] - roundNumber == 0 \
                           else ('roundBeforeFinal' if nRoundsPerEvent[eve] - roundNumber == 1 \
                           else 'otherRounds')
pprint(round_description)
sorted_events = sorted(events, key=lambda x: util.createAssignmentsEVENTORDER.index(x))

persons = wcif_private['persons']
# a dictionary of lists, that will contain dictionaries (one dict per assignment)
assignments = {pe['registrantId'] : [] for pe in persons}
person_properties = {pe['registrantId'] : {'age' : 0,
                                           'nComp': 0,
                                           'nVolunteer': 0,
                                           'nS': 0,
                                           'canS' : 0,
                                           'nR': 0,
                                           'canR' : 0,
                                           'nJ': 0,
                                           'canJ' : 0} for pe in persons}
now = datetime.now()
for pp in persons:
    birthdate = datetime.fromisoformat(pp['birthdate'])
    ageInYears = (relativedelta.relativedelta(now, birthdate)).years
    person_properties[pp['registrantId']]['age'] = ageInYears

    nRoles = len(pp['roles'])
    person_properties[pp['registrantId']]['canS'] = True if (nRoles == 0 and pp['wcaId'] != None and pp['wcaId'] not in neverS) else False
    person_properties[pp['registrantId']]['canR'] = True if (nRoles == 0 and pp['wcaId'] not in neverR) else False
    person_properties[pp['registrantId']]['canJ'] = True if (nRoles == 0 and pp['wcaId'] not in neverJ) else False

    nComp = len(pp['registration']['eventIds']) if pp['registration'] != None else 0
    person_properties[pp['registrantId']]['nComp'] = nComp

if round == 'allFirst':
    for se in sorted_events:
        # get all relevant people
        thisEventPsych = psych_dict[se]

        if '333fm' in se or '333mbf' in se:
            thisAssignmentStrategy = 'dump' # one heat, perhaps distributed over stages

            if se == '333mbf':
                relevantActivityIds = []
                for v in wcif_private['schedule']['venues']:
                    for r in v['rooms']:
                        for a in r['activities']:
                            if '333mbf' in a['activityCode']:
                                relevantActivityIds.append(a['id'])
                for psIndex, ps in enumerate(thisEventPsych):
                    nStagesAvailableThisAttempt = len(relevantActivityIds)
                    pickThisStage = (nStagesAvailableThisAttempt - 1 - psIndex) % nStagesAvailableThisAttempt
                    assignments[ps['registrantId']].append({
                        'activityId':relevantActivityIds[pickThisStage],
                        'assignmentCode':'competitor'
                    })
            else:
                # need assignments for 333fm-r1-a1, -a2, -a3 (if these three exist)
                # all attempts
                fmcAttempts = ['333fm-r1-a1']
                for potentialAttempt in ['333fm-r1-a2','333fm-r1-a3']:
                    if potentialAttempt in evRound_dict.keys():
                        fmcAttempts.append(potentialAttempt)
                relevantActivityIds = {f : [] for f in fmcAttempts}
                for v in wcif_private['schedule']['venues']:
                    for r in v['rooms']:
                        for a in r['activities']:
                            if a['activityCode'] in fmcAttempts:
                                relevantActivityIds[a['activityCode']].append(a['id'])
                for psIndex, ps in enumerate(thisEventPsych):
                    for fmc in fmcAttempts:
                        nStagesAvailableThisAttempt = len(relevantActivityIds[fmc])
                        pickThisStage = (nStagesAvailableThisAttempt - 1 - psIndex) % nStagesAvailableThisAttempt
                        assignments[ps['registrantId']].append({
                            'activityId':relevantActivityIds[fmc][pickThisStage],
                            'assignmentCode':'competitor'
                        })
        else:
            thisFirstRound = se + '-r1'
            thisRoundDescription = round_description[thisFirstRound]
            thisAssignmentStrategy = main_config['assignmentStrategies'][thisRoundDescription][se]
            nHeatsThisRound = heatsDict[thisFirstRound]
            if thisAssignmentStrategy == 'scramblerOptimizedPreservePodium':
                if nHeatsThisRound == 1:
                    chunkedPsychThisRound == [thisEventPsych]
                else:
                    nPodiumToPreserveInBestHeat = math.ceil(percentPodiumToPreserveInBestHeat / 100 * len(thisEventPsych))
                    mustBeLastHeat = thisEventPsych[:nPodiumToPreserveInBestHeat]
                    mustBeLastHeatRegIds = [m['registrantId'] for m in mustBeLastHeat]
                    chunkedPsychThisRound = []
                    for c in range(nHeatsThisRound):
                        chunkedPsychThisRound.append([thisEventPsych[i] for i in range(len(thisEventPsych)) if (i % nHeatsThisRound == (nHeatsThisRound - 1 - c))])

                    howManyToMoveFromLastToOtherChunks = 0
                    for c in range(nHeatsThisRound - 1):
                        modifiedChunk = []
                        for k in chunkedPsychThisRound[c]:
                            if k['registrantId'] not in mustBeLastHeatRegIds:
                                modifiedChunk.append(k)
                            else:
                                howManyToMoveFromLastToOtherChunks += 1
                                chunkedPsychThisRound[-1] = [k] + chunkedPsychThisRound[-1]
                        chunkedPsychThisRound[c] = modifiedChunk
                    removeFromLastHeatDistributeIntoOthers = chunkedPsychThisRound[-1][-howManyToMoveFromLastToOtherChunks:]
                    chunkedPsychThisRound[-1] = chunkedPsychThisRound[-1][:(len(chunkedPsychThisRound[-1]) - howManyToMoveFromLastToOtherChunks)]
                    for c in range(nHeatsThisRound - 1):
                        chunkedPsychThisRound[c].extend([removeFromLastHeatDistributeIntoOthers[i] for i in range(len(removeFromLastHeatDistributeIntoOthers)) if (i % (nHeatsThisRound - 1) == ((nHeatsThisRound - 1) - 1 - c))])

            else:
                if thisAssignmentStrategy == 'scramblerOptimized':
                    # alternate through residue classes
                    chunkedPsychThisRound = []
                    for c in range(nHeatsThisRound):
                        chunkedPsychThisRound.append([thisEventPsych[i] for i in range(len(thisEventPsych)) if (i % nHeatsThisRound == (nHeatsThisRound - 1 - c))])

                else: #elif thisAssignmentStrategy == 'psych':
                    # cut the full psych into equally-sized sets, to distribute into heats
                    # first chunk = worst heat, last chunk = best heat
                    chunkedPsychThisRound = util.chunks(thisEventPsych[::-1], nHeatsThisRound)

            for h in range(nHeatsThisRound):
                thisHeatChunk = chunkedPsychThisRound[h]
                # collect the group names for this heat
                groups = []
                for room in evRound_dict[thisFirstRound]:
                    for gIndex,g in enumerate(evRound_dict[thisFirstRound][room]):
                        if gIndex == h:
                            fullNameOfGroup = thisFirstRound + f'-g{g}'
                            groups.append(fullNameOfGroup)
                nAvailableStagesForHeat = len(groups)
                chunkedPsychThisHeat = util.chunks(thisHeatChunk, nAvailableStagesForHeat)
                for s in range(nAvailableStagesForHeat):
                    thisGroupChunk = chunkedPsychThisHeat[s]
                    thisGroupName = groups[s]
                    for v in wcif_private['schedule']['venues']:
                        for r in v['rooms']:
                            for a in r['activities']:
                                for chAc in a['childActivities']:
                                    if thisGroupName in chAc['activityCode']:
                                        relevantActivityId = chAc['id']
                    for groupMemberIndex, groupMember in enumerate(thisGroupChunk):
                        assignments[groupMember['registrantId']].append({
                            'activityId':relevantActivityId,
                            'assignmentCode':'competitor'
                        })
#pprint(assignments)
#sys.exit()

personListToPatch = []

for p in persons:
    currentAssignments = p['assignments']
    pDict = {
        'name': p['name'],
        'wcaUserId': p['wcaUserId'],
        'wcaId': p['wcaId'],
        'registrantId': p['registrantId'],
        'countryIso2': p['countryIso2'],
        'gender': p['gender'],
        'registration': p['registration'],
        'avatar': p['avatar'],
        'roles': p['roles'],
        'assignments': currentAssignments,
        'personalBests': p['personalBests'],
        'extensions': p['extensions'],
        'birthdate': p['birthdate'],
        'email': p['email'],
    }
    if p['registration'] != None:
        if p['registration']['status'] == 'accepted' and p['registration']['isCompeting'] == True:
            newactivityIds = [a['activityId'] for a in assignments[p['registrantId']]]
            assignmentsToKeep = []
            for ca in currentAssignments:
                if ca['activityId'] in newactivityIds:
                    assignmentsToKeep.append(ca)

            for thisPersonsAssignments in assignments[p['registrantId']]:
                thisAssignment = {
                    'activityId' : thisPersonsAssignments['activityId'],
                    'stationNumber' : None,
                    'assignmentCode' : thisPersonsAssignments['assignmentCode']
                }
                assignmentsToKeep.append(thisAssignment)
            currentAssignments = util.getUniqueListEntriesOfDicts(assignmentsToKeep, 'activityId')
            currentAssignments = []
        else:
            # if person has unregistered in the meantime, remove their assignments completely
            currentAssignments = []
    pDict['assignments'] = currentAssignments
    personListToPatch.append(pDict)

payload = {
    "persons": personListToPatch
}
#pprint(payload)
api.patch_information(compID, grant_type, payload)

print()
print('>> WCIF for {} successfully patched with Assignments.'.format(compName))
