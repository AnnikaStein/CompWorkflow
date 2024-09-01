from argparse import ArgumentParser
from pprint import pprint
import yaml

# custom
from ..utils import util

parser = ArgumentParser(description='Generate new competition website tabs.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml')
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts True/False')

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

util.checkOrCreateOutputContainingID(config['comp']['ID'])

def generate_readme():
    md_str = f'''# WCA German State Ranks
[![WCA German State Ranks Automation](https://github.com/AnnikaStein/WCA-German-State-Ranks/actions/workflows/automate.yml/badge.svg)](https://github.com/AnnikaStein/WCA-German-State-Ranks/actions/workflows/automate.yml)
[![pages-build-deployment](https://github.com/AnnikaStein/WCA-German-State-Ranks/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/AnnikaStein/WCA-German-State-Ranks/actions/workflows/pages/pages-build-deployment)

Displaying the PRs of people who have given *explicit consent* (opt-in) to appear in German WCA state rankings. PRs taken from the WCA database via the [unofficial API](https://github.com/robiningelbrecht/wca-rest-api).

## How to appear in these rankings?
Fill out the form here: [link to enter the ranks](https://docs.google.com/forms/d/e/1FAIpQLSdoLLgBLfTxZIwKJx9QC5XywuMRBreKU4ElbLTvMEZqxRHFcw/viewform).

## You want to participate in the state cup?
Fill out the form here: [link](https://docs.google.com/forms/d/e/1FAIpQLSdqA8dWufte8_KMMjQVvB0JpeQgKIzr1FH1Dk2-MgjFVEZjdw/viewform).

## Data statement
> This information is based on competition results owned and maintained by the
> World Cube Assocation, published at https://worldcubeassociation.org/results
> as of {updated}.

## Support
Enjoy what you see? Feel free to support my projects here: [at my Cuboss-Affiliate page](https://cuboss.com/affiliate/?affiliate=hugacuba&r=hugacuba) and save 5% off your order! Direct donations can be made to: [your developer](https://www.paypal.com/paypalme/hugacuba).

'''

    with open('../README.md', 'w') as f:
        f.write(md_str)
