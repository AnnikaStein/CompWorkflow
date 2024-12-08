from argparse import ArgumentParser
from pprint import pprint
import yaml

# custom
from ..utils import util
from ..templates import websiteTabs

parser = ArgumentParser(description='Generate new competition website tabs.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml (required argument)')
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts (optional flag)')

args = parser.parse_args()

print()
print('>> Welcome to CompWorkflow -> PreComp -> generateWebsiteTabs.py <<')
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
loc = config['comp']['loc']
ppURL = config['payment']['paypalURLuptoAmount']
EUR = config['payment']['amountEUR']
contact = config['mail']
logoExists = config['setup']['logo']

# performs a check for the output destination
# such that further writing of files will work
util.checkOrCreateOutputFolderContainingID(compID)

# === *** === *** === MAIN PAGE === *** === *** === #
tabtitles = '''
Informationen / Information

'''
content = websiteTabs.main_info(compID, contact, compName, logoExists)
util.writeOutputFileForID(compID, 'main_info.md', content)

tabtitles += '''
Zusätzliche Bedingungen für die Registrierung / Extra registration requirements

'''
content = websiteTabs.main_register(compID, contact, ppURL, EUR)
util.writeOutputFileForID(compID, 'main_register.md', content)


# === *** === *** === REGULAR TABS === *** === *** === #
tabtitles = '''
📷 Foto- und Videoaufnahmen / Photo and video recordings

'''
content = websiteTabs.dpoa(contact)
util.writeOutputFileForID(compID, 'tab_dpoa.md', content)

tabtitles += '''
⁉️ FAQ

'''
content = websiteTabs.faq(compID, contact)
util.writeOutputFileForID(compID, 'tab_faq.md', content)

tabtitles += '''
🍕 Verpflegung / Food

'''
content = websiteTabs.food(loc)
util.writeOutputFileForID(compID, 'tab_food.md', content)

tabtitles += '''
ℹ️ Wichtige Infos für alle / Important info for everyone

'''
content = websiteTabs.important(contact, compID)
util.writeOutputFileForID(compID, 'tab_important.md', content)

tabtitles += '''
👕 Logo & Merchandise

'''
content = websiteTabs.logo()
util.writeOutputFileForID(compID, 'tab_logo.md', content)

tabtitles += '''
🔥 Neuigkeiten / News

'''
content = websiteTabs.news(compID, contact)
util.writeOutputFileForID(compID, 'tab_news.md', content)

tabtitles += '''
🐣 Für Neulinge / For Newcomers

'''
content = websiteTabs.newcomer(compID, contact)
util.writeOutputFileForID(compID, 'tab_newcomer.md', content)

tabtitles += '''
🚎 Anreise & Unterkunft / Travel & Accomodation

'''
content = websiteTabs.travel(loc)
util.writeOutputFileForID(compID, 'tab_travel.md', content)

tabtitles += '''
📝 Warteliste / Waiting list

'''
content = websiteTabs.waitlist(compID)
util.writeOutputFileForID(compID, 'tab_waitlist.md', content)


# === *** === *** === PLACEHOLDER TAB === *** === *** === #
content = websiteTabs.tba()
util.writeOutputFileForID(compID, 'tab_tba.md', content)


# === *** === *** === SPECIAL TABS === *** === *** === #
if config['setup']['aftercomp']:
    tabtitles += '''
🌅 Aftercomp / Dinner

    '''
    content = websiteTabs.aftercomp()
    util.writeOutputFileForID(compID, 'tab_aftercomp.md', content)

if config['setup']['awards']:
    tabtitles += '''
🏆 Auszeichnungen / Awards

    '''
    content = websiteTabs.awards()
    util.writeOutputFileForID(compID, 'tab_awards.md', content)

if config['setup']['sponsor']:
    tabtitles += '''
🤝 Sponsor

    '''
    content = websiteTabs.sponsor(compName)
    util.writeOutputFileForID(compID, 'tab_sponsor.md', content)

if config['setup']['unofficial']:
    tabtitles += '''
🎲 Inoffizielle Events / Unofficial events

    '''
    content = websiteTabs.unofficial(compID)
    util.writeOutputFileForID(compID, 'tab_unofficial.md', content)

if config['setup']['gca']:
    tabtitles += '''
👋 German Cube Association (GCA)

    '''
    content = websiteTabs.gca()
    util.writeOutputFileForID(compID, 'tab_gca.md', content)

# === *** === *** === TITLE COLLECTION === *** === *** === #
util.writeOutputFileForID(compID, 'tab_titles.md', tabtitles)
