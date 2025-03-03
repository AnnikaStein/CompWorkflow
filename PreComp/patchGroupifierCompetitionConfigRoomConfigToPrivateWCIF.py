from argparse import ArgumentParser
from pprint import pprint
import yaml

# custom
from ..utils import api, util

# === *** === *** === BOILERPLATE WELCOME === *** === *** === #
parser = ArgumentParser(description='Patch private competition WCIF json with Groupifier extension.')
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
print('>> Welcome to CompWorkflow -> PreComp -> patchGroupifierExtensionToPrivateWCIF.py <<')
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
if ',' in str(config['setup']['stationsPerStage']):
    stationsPerStage = config['setup']['stationsPerStage'].split(",")
else:
    stationsPerStage = [config['setup']['stationsPerStage']]

# === *** === *** === API REQUEST FUNCTIONS === *** === *** === #
competition_information = api.fetch_information(compID, grant_type)

# save result
util.writeOutputJSONForID(compID, f'wcif_private.json', competition_information)

print()
print('>> Information about {} successfully saved.'.format(compName))

payloadConfig = {"extensions": [
            {
              "id": "groupifier.CompetitionConfig",
              "specUrl": "https://groupifier.jonatanklosko.com/wcif-extensions/CompetitionConfig.json",
              "data": {
                "localNamesFirst": False,
                "printOneName": False,
                "scorecardsBackgroundUrl": "",
                "competitorsSortingRule": "balanced",
                "noTasksForNewcomers": False,
                "tasksForOwnEventsOnly": True,
                "noRunningForForeigners": False,
                "printStations": False,
                "scorecardPaperSize": "a4",
                "scorecardOrder": "natural",
                "printScorecardsCoverSheets": False}
            }
        ]
    }

api.patch_information(compID, grant_type, payloadConfig)

print()
print('>> WCIF for {} successfully patched with Groupifier Config.'.format(compName))


venuesListForPayloadStations = []
for v in competition_information['schedule']['venues']:
    vDict = {
        "id": v['id'],
        "name": v['name'],
        "latitudeMicrodegrees": v['latitudeMicrodegrees'],
        "longitudeMicrodegrees": v['longitudeMicrodegrees'],
        "countryIso2": v['countryIso2'],
        "timezone": v['timezone'],
        "rooms": [],
        "extensions": []
    }
    for iR,r in enumerate(v['rooms']):
        rDict = {
            "id": r['id'],
            "name": r['name'],
            "color": r['color'],
            "activities": [],
            "extensions": [
              {
                "id": "groupifier.RoomConfig",
                "specUrl": "https://groupifier.jonatanklosko.com/wcif-extensions/RoomConfig.json",
                "data": {
                  "stations": stationsPerStage[iR]
                }
              }
            ]
        }
        for a in r['activities']:
            # at the beginning, each activity is only built up to round level
            aDict = {
                "id": a['id'],
                "name": a['name'],
                "activityCode": a['activityCode'],
                "startTime": a['startTime'],
                "endTime": a['endTime'],
                "childActivities": [],
                "extensions": []
            }
            # no childActivities yet
            # extensions to activities yet, i.e. no grouping config
            rDict['activities'].append(aDict)
        vDict['rooms'].append(rDict)
    venuesListForPayloadStations.append(vDict)

payloadStations = {"schedule": {
    "startDate": competition_information['schedule']['startDate'],
    "numberOfDays": competition_information['schedule']['numberOfDays'],
    "venues": venuesListForPayloadStations
  }
}
if compID == 'Template2025':
    api.patch_information(compID, grant_type, payloadStations)

    print()
    print('>> WCIF for {} successfully patched with Groupifier Stations.'.format(compName))


competition_information = api.fetch_information(compID, grant_type)
util.writeOutputJSONForID(compID, f'wcif_private.json', competition_information)
