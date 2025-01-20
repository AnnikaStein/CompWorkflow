from argparse import ArgumentParser
from collections import OrderedDict
from datetime import datetime
import numpy as np
import pandas as pd
from pprint import pprint
import urllib.request as libreq
import getpass, json, math, os, pycountry, re, requests, yaml

# custom
from ..utils import util
from ..templates import nametags_tex

parser = ArgumentParser(description='Generate nametags for competition.')
parser.add_argument('-c', '--config', required=True,
                    help='Name of config file, e.g. rlp25.yml (required argument)')
parser.add_argument('-o',"--order_by", default='name',
                    help="Order of nametags for printing, options: id, name, default: name")
parser.add_argument('-l',"--huge_logo", action='store_true', default = True,
                    help="Put huge logo in center (optional flag)")
parser.add_argument('-a',"--alternating", action='store_true', default = True,
                    help="Order the PDFs as front side / back side alternatingly (optional flag)")
parser.add_argument('-n',"--add_non_competing", action='store_true', default = True,
                    help="Print nametags for non-competing orga people as well (optional flag)")
parser.add_argument('-d', '--debug', action='store_true', default = False,
                    help='Get detailed printouts (optional flag)')
args = parser.parse_args()

print()
print('*='*80)
print()
print('>> Welcome to CompWorkflow -> PreComp -> generateNametags.py <<')
print()
print('*='*80)
print()
print('>> Running with options:')
print('>>   debug =', args.debug)
print('>>   config =', args.config)
print('>>   order_by =', args.order_by)
print('>>   huge_logo =', args.huge_logo)
print('>>   alternating =', args.alternating)
print('>>   non_competing =', args.add_non_competing)

debug = args.debug
config_path = args.config
order_by = args.order_by
huge_logo = args.huge_logo
alternating = args.alternating
add_non_competing = args.add_non_competing

with open('CompWorkflow/config/main.yml') as f:
    mainConfig = yaml.safe_load(f)
    if debug:
        print()
        print('>> This is the > main < config file:')
        pprint(mainConfig)

svgs_path = mainConfig['graphics']['svgsPath']
qrcode_path = mainConfig['graphics']['qrcodePath']

with open('CompWorkflow/config/'+config_path) as f:
    config = yaml.safe_load(f)
    if debug:
        print()
        print('>> This is the config file:')
        pprint(config)

compID = config['comp']['ID']
compName = config['comp']['name']
logo_path = config['setup']['logoPath']

# performs a check for the output destination
# such that further writing of files will work
util.checkOrCreateOutputFolderContainingID(compID)

# === *** === *** === LOAD WCIF === *** === *** === #
with open(f'CompWorkflow/output/{compID}/wcif_private.json') as file:
    wcif_private = json.load(file)

activities = []
for x in range(len(wcif_private['schedule']['venues'][0]['rooms'])):
    activities += wcif_private['schedule']['venues'][0]['rooms'][x]['activities']

activityIdMap = dict()
for activity in activities:
    activityIdMap[activity['id']] = activity['activityCode']
    for child in activity['childActivities']:
        activityIdMap[child['id']] = child['activityCode']

persons = wcif_private['persons']
if order_by == 'name':
    persons = sorted(persons, key=lambda persons: persons['name'])

actual_competitors = []
non_competing = []
registrantIds = []
for i,item in enumerate(persons):
    if item['registrantId'] == None:
        # this is the my-mom-is-an-organizer-fix ;-)
        is_orga = True if 'organizer' in item['roles'] else False
        if is_orga:
            non_competing.append(item)
    else:
        if item['registration']['status'] == 'accepted' and item['registration']['isCompeting'] == True:
            actual_competitors.append(item)
            registrantIds.append(item['registrantId'])
persons = actual_competitors

frontside_tex_all = ''
for i in range(len(persons)):
    person = persons[i]
    if person['registration']['status'] != 'accepted' or person['registration']['isCompeting'] != True:
        pass
    else:
        if huge_logo == True:
            frontside_tex_inside = '\\addresslabel{\\centering{\\vspace{-0.7em}\\selectlanguage{english} ' + compName + '\\\\ \\vspace{0.5em}\\raisebox{-1.75\\baselineskip}{\\includegraphics[height=4\\baselineskip]{' + logo_path + '}} \\vspace{0.5em} \Huge \\\\ '
        else:
            frontside_tex_inside = '\\addresslabel{\\centering{\\vspace{-1em}\\selectlanguage{english} \\hspace{1em} ' + compName + '\\qquad \\raisebox{-1.75\\baselineskip}{\\includegraphics[height=4\\baselineskip]{' + logo_path + '}} \\vspace{0.5em} \Huge \\\\ '
        country_string = f'{pycountry.countries.get(alpha_2=person["countryIso2"]).name}'
        if person["wcaId"] == None:
            wca_id_string = '\\textcolor{ForestGreen}{Newcomer}'
        else:
            wca_id_string = f'{person["wcaId"]}'

        competitor_id_string = registrantIds[i]

        is_del = True if ('delegate' in person['roles']) or ('trainee-delegate' in person["roles"]) else False
        is_orga = True if 'organizer' in person['roles'] else False

        optional_role_string = ''
        if is_del and is_orga:
            optional_role_string = 'Delegate, Organizer'
        else:
            if is_del:
                optional_role_string = 'Delegate'
            elif is_orga:
                optional_role_string = 'Organizer'

        name_string = f'{person["name"]}'
        multi_row_name = False
        if '(' in name_string and ')' in name_string:
            multi_row_name = True
            # this is a name with additional local string with other characters
            # would require a linebreak most likely, so the string is split into two
            # and later the second part is written with a smaller fontsize
            name_string_a, name_string_b = name_string.split('(')
            name_string_a = name_string_a[:-1]
            name_string_b = name_string_b[:-1]
            long_name_smaller_font_start = '{\LARGE '
            long_name_smaller_font_end = '} '
            frontside_tex_inside += '\\textbf{\\centering \\begin{minipage}{86mm}\\centering ' + long_name_smaller_font_start + name_string_a + long_name_smaller_font_end + '\\end{minipage}\\vspace{1.5mm}}'
            frontside_tex_inside += '}'
            frontside_tex_inside += '\\\\'
            if (bool((re.compile(r'[\u0400-\u04FF]+')).search(name_string)) == True):
                frontside_tex_inside += ' \\selectlanguage{russian} '
            if (bool((re.compile(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')).search(name_string)) == True):
                frontside_tex_inside += ' \\begin{CJK*}{UTF8}{gbsn} '
                frontside_tex_inside += '(' + name_string_b + ')'
                frontside_tex_inside += ' \\end{CJK*}'
            else:
                frontside_tex_inside += '(' + name_string_b + ')'
                frontside_tex_inside += '\\vspace{-0.5em} '
        else:
            long_name_smaller_font_start = '{\LARGE ' if (len(name_string) > 19 or len(optional_role_string) > 0) else ''
            long_name_smaller_font_end = '} ' if (len(name_string) > 19 or len(optional_role_string) > 0) else ''
            frontside_tex_inside += '\\textbf{\\centering \\begin{minipage}{86mm}\\centering '+ long_name_smaller_font_start + name_string + long_name_smaller_font_end + '\\end{minipage}}}'
        frontside_tex_inside += '\\\\ '

        if optional_role_string != '':
            if multi_row_name:
                frontside_tex_inside += '\\vspace{-1em} \\selectlanguage{english} \\ \\\\ ' + '\\textcolor{Red}{' + optional_role_string + '} \\\\ '
                frontside_tex_inside += '\\vspace{-0.5em} '
            else:
                frontside_tex_inside += '\\vspace{-0.5em} \\selectlanguage{english} \\ \\\\ ' + '\\textcolor{Red}{' + optional_role_string + '} \\\\ '

        frontside_tex_inside += '\\vspace{-0.5em} \\selectlanguage{english} \\begin{tabular}{lcr}	\\qquad &  \\qquad & \\qquad  \\\\' + wca_id_string + '&' + country_string + '& ID: ' + f'{competitor_id_string}' + '\\\\ \\end{tabular}'
        #frontside_tex_inside += '\\selectlanguage{english} \\begin{tabular}{lr}	\\qquad &  \\qquad  \\\\' + wca_id_string + '&' + country_string + '\\\\ \\end{tabular}'

        frontside_tex_inside += '}'

        frontside_tex_all += frontside_tex_inside + '\n'

if add_non_competing:
    for i in range(len(non_competing)):
        person = non_competing[i]
        if huge_logo == True:
            frontside_tex_inside = '\\addresslabel{\\centering{\\vspace{-0.7em}\\selectlanguage{english} ' + compName + '\\\\ \\vspace{0.5em}\\raisebox{-1.75\\baselineskip}{\\includegraphics[height=4\\baselineskip]{' + logo_path + '}} \\vspace{0.5em} \Huge \\\\ '
        else:
            frontside_tex_inside = '\\addresslabel{\\centering{\\vspace{-1em}\\selectlanguage{english} \\hspace{1em} ' + compName + '\\qquad \\raisebox{-1.75\\baselineskip}{\\includegraphics[height=4\\baselineskip]{' + logo_path + '}} \\vspace{0.5em} \Huge \\\\ '
        country_string = f'{pycountry.countries.get(alpha_2=person["countryIso2"]).name}'

        optional_role_string = 'Organizer'

        name_string = f'{person["name"]}'
        multi_row_name = False
        if '(' in name_string and ')' in name_string:
            multi_row_name = True
            # this is a name with additional local string with other characters
            # would require a linebreak most likely, so the string is split into two
            # and later the second part is written with a smaller fontsize
            name_string_a, name_string_b = name_string.split('(')
            name_string_a = name_string_a[:-1]
            name_string_b = name_string_b[:-1]
            long_name_smaller_font_start = '{\LARGE '
            long_name_smaller_font_end = '} '
            frontside_tex_inside += '\\textbf{\\centering \\begin{minipage}{86mm}\\centering ' + long_name_smaller_font_start + name_string_a + long_name_smaller_font_end + '\\end{minipage}\\vspace{1.5mm}}'
            frontside_tex_inside += '}'
            frontside_tex_inside += '\\\\'
            if (bool((re.compile(r'[\u0400-\u04FF]+')).search(name_string)) == True):
                frontside_tex_inside += ' \\selectlanguage{russian} '
            if (bool((re.compile(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')).search(name_string)) == True):
                frontside_tex_inside += ' \\begin{CJK*}{UTF8}{gbsn} '
                frontside_tex_inside += '(' + name_string_b + ')'
                frontside_tex_inside += ' \\end{CJK*}'
            else:
                frontside_tex_inside += '(' + name_string_b + ')'
                frontside_tex_inside += '\\vspace{-0.5em} '
        else:
            long_name_smaller_font_start = '{\LARGE ' if (len(name_string) > 19 or len(optional_role_string) > 0) else ''
            long_name_smaller_font_end = '} ' if (len(name_string) > 19 or len(optional_role_string) > 0) else ''
            frontside_tex_inside += '\\textbf{\\centering \\begin{minipage}{86mm}\\centering '+ long_name_smaller_font_start + name_string + long_name_smaller_font_end + '\\end{minipage}}}'
        frontside_tex_inside += '\\\\ '

        if optional_role_string != '':
            frontside_tex_inside += '\\vspace{-0.5em} \\selectlanguage{english} \\ \\\\ ' + '\\textcolor{Red}{' + optional_role_string + '} \\\\ '
            if multi_row_name:
                frontside_tex_inside += '\\vspace{-0.5em} '

        frontside_tex_inside += '\\vspace{-0.5em} \\selectlanguage{english} \\begin{tabular}{lcr}	\\qquad &  \\qquad & \\qquad  \\\\' + ' ' + '&' + country_string + '&  ' + f' ' + '\\\\ \\end{tabular}'
        #frontside_tex_inside += '\\selectlanguage{english} \\begin{tabular}{lr}	\\qquad &  \\qquad  \\\\' + wca_id_string + '&' + country_string + '\\\\ \\end{tabular}'

        frontside_tex_inside += '}'

        frontside_tex_all += frontside_tex_inside + '\n'

frontside_tex = nametags_tex.front_nametags(frontside_tex_all)
# === *** === *** === SAVE NAMETAGS FRONT (tex) === *** === *** === #
util.writeOutputFileForID(compID, f'labels-{compID}-frontsides.tex', frontside_tex)

print()
print()
print('>> Statistics:')
n_persons = 0
for i,item in enumerate(persons):
    if item['registration']['status'] == 'accepted' and item['registration']['isCompeting'] == True:
        n_persons += 1

print('>>   Number of actual competitors:', n_persons)

if add_non_competing:
    n_persons += len(non_competing)
    print('>>   Number of additional non-competing organizers to be added:', len(non_competing))

print('>>   Number of name tags:', n_persons)
print()
print()
print('>> Back side follows...')
print()
print()

if n_persons % 2 == 0:
    # no empty filling label needed
    person_slicing = util.flatten([[2*k+1,2*k] for k in range(n_persons//2)])
else:
    # needs an empty filling label on the second to last position
    person_slicing = util.flatten([[2*k+1,2*k] for k in range(n_persons//2)]) + [-1, n_persons-1]

backside_tex_all = ''
for p in person_slicing:
    if p == -1:
        # empty label!
        print('>> Adding empty label for even-odd backside adjustment','\\addresslabel{\\emptylabel}')
        backside_tex_all += '\\addresslabel{\\emptylabel}' + '\n'
    else:
        if p >= len(persons):
            print('>> Adding empty label for non-competing organizer','\\addresslabel{\\emptylabel}')
            backside_tex_all += '\\addresslabel{\\emptylabel}' + '\n'
            continue
        person = persons[p]
        if person['registration']['status'] != 'accepted' or person['registration']['isCompeting'] != True:
            pass
        else:
            tmpName = person["name"]
            assignments = dict()
            for assignment in person['assignments']:
                assignment['activityId'] = activityIdMap[assignment['activityId']]
                if ((assignment['activityId'].startswith("333fm"))):
                    pass
                else:
                    activity = assignment['activityId'].split('-')
                    if not(activity[0] in assignments):
                        assignments[activity[0]] = [' ',' ',' ',' ']
                    if assignment['assignmentCode'] == 'competitor':
                        assignments[activity[0]][0] += ((activity[2])[1:], (',' + (activity[2])[1:]))[assignments[activity[0]][0] != ' ']
                    elif assignment['assignmentCode'] == 'staff-scrambler':
                        assignments[activity[0]][1] += ((activity[2])[1:], (',' + (activity[2])[1:]))[assignments[activity[0]][1] != ' ']
                    elif assignment['assignmentCode'] == 'staff-judge':
                        assignments[activity[0]][3] += ((activity[2])[1:], (',' + (activity[2])[1:]))[assignments[activity[0]][3] != ' ']
                    elif assignment['assignmentCode'] == 'staff-runner':
                        assignments[activity[0]][2] += ((activity[2])[1:], (',' + (activity[2])[1:]))[assignments[activity[0]][2] != ' ']

            # sorting
            assignmentsSorted = OrderedDict((k, assignments[k]) for k in util.printAssignmentsEVENTORDER if k in assignments)


            backside_tex_inside = '\\addresslabel{\\vspace{-1.7em}\\selectlanguage{english}{\\begin{table}[H]\\footnotesize\\hspace{1.1em}\\renewcommand{\\arraystretch}{1.35}'
            if len(assignmentsSorted) > 8:
                # dual-column format
                pass
                backside_tex_inside += '\\begin{tabular}{|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|}\\hline\\rowcolor[HTML]{DAE8FC}{\color[HTML]{000000} Event} & {\color[HTML]{000000} C} & {\color[HTML]{000000} S} &	{\color[HTML]{000000} R} & {\color[HTML]{000000} J} & {\color[HTML]{000000} Event} & {\color[HTML]{000000} C} &	{\color[HTML]{000000} S} & {\color[HTML]{000000} R} & {\color[HTML]{000000} J} \\\\ \\hline'
                n_double = len(assignmentsSorted) - 8
                table_row_counter = 1
                for d in range(n_double):
                    if table_row_counter % 2 == 1:
                        # odd row white
                        backside_tex_inside += '\\rowcolor[HTML]{FFFFFF}'
                    else:
                        # even row light grey
                        backside_tex_inside += '\\rowcolor[HTML]{EFEFEF}'
                    backside_tex_inside += '\\includesvg[height=1em]{' + svgs_path + list(assignmentsSorted.keys())[d] + '.svg}' + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d]][0])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d]][1])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d]][2])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d]][3])) + '&' + '\\includesvg[height=1em]{' + svgs_path + list(assignmentsSorted.keys())[d+8] + '.svg}' + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d+8]][0])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d+8]][1])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d+8]][2])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d+8]][3])) + '\\\\ \\hline'
                    table_row_counter += 1
                for d in range(n_double,8):
                    if table_row_counter % 2 == 1:
                        # odd row white
                        backside_tex_inside += '\\rowcolor[HTML]{FFFFFF}'
                    else:
                        # even row light grey
                        backside_tex_inside += '\\rowcolor[HTML]{EFEFEF}'
                    backside_tex_inside += '\\includesvg[height=1em]{' + svgs_path + list(assignmentsSorted.keys())[d] + '.svg}' + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d]][0])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d]][1])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d]][2])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[list(assignmentsSorted.keys())[d]][3])) + '& & & & & \\\\ \\hline'
                    table_row_counter += 1
            else:
                # one-column format
                backside_tex_inside += '\\begin{tabular}{|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|>{\\hspace{-0.2em}}c<{\\hspace{-0.2em}}|}\\hline\\rowcolor[HTML]{DAE8FC}{\color[HTML]{000000} Event} & {\color[HTML]{000000} C} & {\color[HTML]{000000} S} &	{\color[HTML]{000000} R} & {\color[HTML]{000000} J} \\\\ \\hline'
                table_row_counter = 1
                for k in assignmentsSorted:
                    if table_row_counter % 2 == 1:
                        # odd row white
                        backside_tex_inside += '\\rowcolor[HTML]{FFFFFF}'
                    else:
                        # even row light grey
                        backside_tex_inside += '\\rowcolor[HTML]{EFEFEF}'
                    backside_tex_inside += '\\includesvg[height=1em]{' + svgs_path + k + '.svg}' + '&' + util.numeric_order_assignments(str(assignmentsSorted[k][0])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[k][1])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[k][2])) + '&' + util.numeric_order_assignments(str(assignmentsSorted[k][3])) + '\\\\ \\hline'
                    table_row_counter += 1


            backside_tex_inside += '\\end{tabular}\\end{table}}\\vspace{-1.4em}\\selectlanguage{english}\\hspace{1.1em}\\footnotesize\\parbox{27em}{C = Competitor, S = Scrambler, R = Runner, J = Judge.\\\\ The table above shows first rounds only. \\\\ \\ \\\\Please check WCA Live and competitiongroups.com for information about next rounds. Your following assignments will appear there. Your ID: ' + str(person['registrantId']) + '.} \\raisebox{-3.65\\baselineskip}{\\includegraphics[height=7.2\\baselineskip]{' + qrcode_path + '}}}'

            backside_tex_all += backside_tex_inside + '\n'

backside_tex = nametags_tex.back_nametags(backside_tex_all)
# === *** === *** === SAVE NAMETAGS (tex) === *** === *** === #
util.writeOutputFileForID(compID, f'labels-{compID}-backsides.tex', backside_tex)


npages = math.ceil(n_persons / 10.0)
merged_tex_inside = ''
if alternating:
    for k in range(npages):
        merged_tex_inside += '\\includepdf[pages={' + str(k+1) + '}]{labels-' + compID + '-frontsides.pdf}\n'
        merged_tex_inside += '\\includepdf[pages={' + str(k+1) + '}]{labels-' + compID + '-backsides.pdf}\n'

else:
    merged_tex_inside += '\\includepdf{labels-' + compID + '-frontsides.pdf}\n'
    merged_tex_inside += '\\includepdf{labels-' + compID + '-backsides.pdf}\n'

merged_tex = nametags_tex.merged_nametags(merged_tex_inside)
# === *** === *** === SAVE NAMETAGS (tex) === *** === *** === #
util.writeOutputFileForID(compID, f'labels-{compID}-merged.tex', merged_tex)
print()
print()
print(f'>> Nametag tex files for {compName} successfully saved.')
print()
print()
print(f'>> Going ahead by compiling the following files from .tex to .pdf with pdflatex.')
print(f'    labels-{compID}-frontsides.tex')
print(f'    labels-{compID}-backsides.tex')
print(f'    labels-{compID}-merged.tex')
print()
print()
print(f'>> Compiling front sides.')
util.compilePdflatex(compID, f'labels-{compID}-frontsides.tex')
print(f'>> Compiling back sides.')
util.compilePdflatex(compID, f'labels-{compID}-backsides.tex')
print(f'>> Compiling merged pdf.')
util.compilePdflatex(compID, f'labels-{compID}-merged.tex')
print()
print()
print(f'>> Nametag tex files for {compName} successfully saved.')
print()
