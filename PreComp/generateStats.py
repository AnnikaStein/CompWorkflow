from argparse import ArgumentParser
from collections import OrderedDict
from datetime import datetime
import numpy as np
import pandas as pd
from pprint import pprint
import urllib.request as libreq
import getpass, json, math, pycountry, re, requests, yaml

# custom
from ..utils import util

parser = ArgumentParser(description='Generate nametags for competition.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml (required argument)')
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts (optional flag)')
args = parser.parse_args()

print()
print('*='*80)
print()
print('>> Welcome to CompWorkflow -> PreComp -> generateStats.py <<')
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

# === *** === *** === LOAD WCIF === *** === *** === #
with open(f'CompWorkflow/output/{compID}/wcif_private.json') as file:
    wcif_private = json.load(file)

writeStatsString = ''
# ======================== Persons and Competitors ========================
# get info about which events a person is competing in,
# from that on which days they come,
# how many guests they bring,
# how experienced the competitor is
persons = wcif_private['persons']
competitors = []
gender = []
for person in persons:
    if person['registrantId'] != None:
        if person['registration']['status'] == 'accepted' and person['registration']['isCompeting'] == True:
            competitors.append(person)
            gender.append(person['gender'])
            
# basic demography for media
writeStatsString += '>> gender distribution\n\n'
genderHistogram = util.countOccurenceInListWithDict(gender)
writeStatsString += '>> genderHistogram ' + str(genderHistogram) + '\n\n'
util.writeOutputJSONForID(compID, f'genderHistogram.json', genderHistogram)

competitors_birthdaySorted = sorted(competitors, key=lambda competitors: competitors['birthdate'], reverse=True)
youngestCompetitor = competitors_birthdaySorted[:3]
oldestCompetitor = competitors_birthdaySorted[-3:]
writeStatsString += '>> youngestCompetitor (youngest first)\n\n'
for c in youngestCompetitor:
    writeStatsString += str(c) + '\n\n'
writeStatsString += '>> oldestCompetitor (oldest last)\n\n'
for c in oldestCompetitor:
    writeStatsString += str(c) + '\n\n'

# ======================== Events and Schedule ========================
# get info about which events are offered,
# assuming that each offered event has at least a r1
events = [ev['id'] for ev in wcif_private['events']]
# at the beginning it's unknown on which day an event starts
event_startsOn = {ev : ' ' for ev in events}
# at the beginning it's unknown how many competitors compete in the event
event_nComp = {ev : 0 for ev in events}
# get info about when each round takes place (on which day)
schedule = wcif_private['schedule']

startDate = schedule['startDate']
numberOfDays = schedule['numberOfDays']

for v in schedule['venues']:
    for r in v['rooms']:
        for a in r['activities']:
            for ev in events:
                if (f'{ev}-r1' in a['activityCode']):
                    # found an activity corresponding to first round of the event
                    # grab the day it starts
                    # each day has YYYY-MM-DD, so in total 10 chars
                    startingDayOfEvent = a['startTime'][:10]
                    if event_startsOn[ev] == ' ':
                        # first match found, write to dict
                        event_startsOn[ev] = startingDayOfEvent
                    else:
                        # there already was a day written, check if the new one is earlier
                        if startingDayOfEvent < event_startsOn[ev]:
                            event_startsOn[ev] = startingDayOfEvent

#print('event_startsOn', event_startsOn)
allDays = []
for ev in event_startsOn.keys():
    allDays.append(event_startsOn[ev])
allDays = util.getUniqueListEntriesSorted(allDays)

# ======================== Join Competitor and Schedule Info ========================
# find the first day on which a competitor is competing
# find all days on which a competitor is present
competitor_arrivalDay = {competitor['registrantId'] : ' ' for competitor in competitors}
competitor_presentDays = {competitor['registrantId'] : [] for competitor in competitors}

for competitor in competitors:
    registrantId = competitor['registrantId']
    for evId in competitor['registration']['eventIds']:
        # we found competitor for the given event and increase its counter
        event_nComp[evId] = event_nComp[evId] + 1
        # lookup the first day on which the registered-for event is held
        startingDayOfEvent = event_startsOn[evId]
        competitor_presentDays[registrantId].append(startingDayOfEvent)
        if competitor_arrivalDay[registrantId] == ' ':
            # first match found, write to dict
            competitor_arrivalDay[registrantId] = startingDayOfEvent
        else:
            # there already was a day written, check if the new one is earlier
            if startingDayOfEvent < competitor_arrivalDay[registrantId]:
                competitor_arrivalDay[registrantId] = startingDayOfEvent
    competitor_presentDays[registrantId] = util.getUniqueListEntriesSorted(competitor_presentDays[registrantId])

is_attending_all_days = []
dailyAttendance = {d : {'total_people' : 0,
                        'nGuests' : 0,
                        'competitors' : [],
                        'nCompetitors' : 0,
                        'newcomers' : [],
                        'nNewcomers' : 0,
                        'returners' : [],
                        'nReturners' : 0,
                        'inexperienced_returners' : [],
                        'nInexperienced_returners' : 0,
                        'foreign_newcomers' : [],
                        'nForeign_newcomers' : 0,
                        'foreign_returners' : [],
                        'nForeign_returners' : 0,
                        'foreign_inexperienced_returners' : [],
                        'nForeign_inexperienced_returners' : 0,
                       } for d in allDays}

for regId in competitor_presentDays.keys():
    competitor_Index = list(competitor_presentDays.keys()).index(regId)
    if len(competitor_presentDays[regId]) == numberOfDays:
        is_attending_all_days.append(regId)
    for d in dailyAttendance.keys():
        if d in competitor_presentDays[regId]:
            # this competitor is present on this day
            dailyAttendance[d]['total_people'] += 1
            dailyAttendance[d]['competitors'].append(regId)
            dailyAttendance[d]['nCompetitors'] += 1
            dailyAttendance[d]['nGuests'] += competitors[competitor_Index]['registration']['guests']
            dailyAttendance[d]['total_people'] += competitors[competitor_Index]['registration']['guests']
            if competitors[competitor_Index]['wcaId'] == None:
                dailyAttendance[d]['newcomers'].append(regId)
                dailyAttendance[d]['nNewcomers'] += 1
                if competitors[competitor_Index]['countryIso2'] != 'DE':
                    dailyAttendance[d]['foreign_newcomers'].append(regId)
                    dailyAttendance[d]['nForeign_newcomers'] += 1
            else:
                returner_wcaID = competitors[competitor_Index]['wcaId']
                with libreq.urlopen(f'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/persons/{returner_wcaID}.json') as file:
                    returner_Json = json.load(file)
                dailyAttendance[d]['returners'].append(regId)
                dailyAttendance[d]['nReturners'] += 1
                returner_isInexperienced = int(returner_Json['numberOfCompetitions']) <= 2
                if returner_isInexperienced:
                    dailyAttendance[d]['inexperienced_returners'].append(regId)
                    dailyAttendance[d]['nInexperienced_returners'] += 1
                if competitors[competitor_Index]['countryIso2'] != 'DE':
                    dailyAttendance[d]['foreign_returners'].append(regId)
                    dailyAttendance[d]['nForeign_returners'] += 1
                    if returner_isInexperienced:
                        dailyAttendance[d]['foreign_inexperienced_returners'].append(regId)
                        dailyAttendance[d]['nForeign_inexperienced_returners'] += 1
                

writeStatsString += '>> is_attending_all_days ' + str(len(is_attending_all_days)) + '\n\n'

writeStatsString += '>> event_nComp ' + str(event_nComp) + '\n\n'
util.writeOutputJSONForID(compID, f'event_nComp.json', event_nComp)

writeStatsString += '>> dailyAttendance ' + str(dailyAttendance) + '\n\n'
util.writeOutputJSONForID(compID, f'dailyAttendance.json', dailyAttendance)


util.writeOutputFileForID(compID, f'statistics.txt', writeStatsString)
print()
print()
print(f'>> Stats for {compName} successfully saved.')
print()
print()
