import json, math, os

# Operations with files, directories and os

def checkOrCreateOutputFolderContainingID(comp_id):
    if not os.path.isdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}'):
        os.mkdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}')
        os.mkdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}/participants')
    else:
        if not os.path.isdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}/participants'):
            os.mkdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}/participants')

def writeOutputFileForID(comp_id, fname, content):
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}/{fname}', 'w') as f:
        f.write(content)

def writeOutputJSONForID(comp_id, fname, content):
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}/{fname}', 'w') as f:
        json.dump(content, f)

def compilePdflatex(comp_id, fname, subFolder = '', cleanUp = False):
    mycwd = os.getcwd()
    os.chdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}{subFolder}')
    os.system(f'pdflatex -synctex=1 -interaction=batchmode --shell-escape "{fname}"')
    if cleanUp:
        os.remove(f'{fname[:-4]}.synctex.gz')
        os.remove(f'{fname[:-4]}.aux')
        os.remove(f'{fname[:-4]}.log')
        print('>> Cleaned up aux files.')
    os.chdir(mycwd)

# Operations with lists or dicts

def getSortedListOfListsByNthColumn(unsorted_list, column):
    sortList = unsorted_list.copy()
    sortList.sort(key=lambda x: x[column])
    return sortList

def flatten(myList):
    return [x for sub in myList for x in sub]

def getUniqueListEntriesSorted(original_list):
    new_list = list(set(original_list))
    new_list.sort()
    return new_list

def countOccurenceInListWithDict(original_list):
    new_list = getUniqueListEntriesSorted(original_list)
    count_dict = {uniqueEle : 0 for uniqueEle in new_list}
    for originalEle in original_list:
        for uniqueEle in new_list:
            if originalEle == uniqueEle:
                count_dict[uniqueEle] += 1
    return count_dict

# Operations with strings

def numeric_order_assignments(a_string):
    if len(a_string) == 0 or a_string == ' ':
        return a_string
    x = a_string.split(',')
    x = [int(k) for k in x]
    x.sort()
    x = ', '.join(map(str, x))
    return x

def getLatinNameFromFullName(full_name):
    latin_name = full_name.split(' (')[0]
    return latin_name

# Operations with numbers

def customRoundHeat(nHeat, decimals = 0, noShowPerHeat = 0.1):
    multiplier = 10 ** decimals
    noShowReducedHeat = nHeat - noShowPerHeat
    nRoundedHeat = math.ceil(noShowReducedHeat * multiplier) / multiplier
    return nRoundedHeat

def customRoundAssignees(nGroup, event, system, nStations, roleType):
    if roleType == 's':
        if event in shortEvents:
            targetPuzzlesPerAssignee = 6
        else:
            targetPuzzlesPerAssignee = 5
        nAssignees = min(5,max(2, math.ceil(nGroup / targetPuzzlesPerAssignee)))

    elif roleType == 'r':
        if event in shortEvents:
            targetPuzzlesPerAssignee = 6
        else:
            targetPuzzlesPerAssignee = 5
        nAssignees = max(2, math.ceil(nGroup / targetPuzzlesPerAssignee) - 1)

    else: # roleType == 'j'
        if system == ['s','r','j']:
            nAssignees = min(nStations, nGroup)
        elif system == ['s','j']:
            nAssignees = nGroup + 2

    return nAssignees

# Definitions

createAssignmentsEVENTORDER = ['333mbf', '444bf', '555bf', 'sq1', 'clock', '777', '666', '555', 'minx', '333bf', '444', '333oh', 'skewb', 'pyram', '333', '222']
printAssignmentsEVENTORDER = ['333', '222', '444', '555', '666', '777', '333bf', '333oh', 'clock', 'minx', 'pyram', 'skewb', 'sq1', '444bf', '555bf', '333mbf']
shortEvents = ['222','pyram','skewb']
nogroupsEvents = ['333fm', '333mbf']
noassignmentsEvents = ['333fm']
sortBySingleAverage = ['333bf', '444bf', '555bf']
sortBySingleOnly = ['333mbf']

# MaybeDo
# # Boilerplate code
#
# def welcome(args):
#     print()
#     print('*='*80)
#     print()
#     print('>> Welcome to CompWorkflow -> PreComp -> loadPrivateWCIF.py <<')
#     print()
#     print('*='*80)
#     print()
#     print('>> Running with options:')
#     for arg in vars(args):
#         print(f'>>   {arg} = {getattr(args, arg)}', getattr(args, arg))
#
#     debug = args.debug
#     config_path = args.config
#     grant_type = args.grant_type
#
#     with open('CompWorkflow/config/'+config_path) as f:
#         config = yaml.safe_load(f)
#         if debug:
#             print()
#             print('>> This is the config file:')
#             pprint(config)
#
#     compID = config['comp']['ID']
#     compName = config['comp']['name']
#
#     # performs a check for the output destination
#     # such that further writing of files will work
#     util.checkOrCreateOutputFolderContainingID(compID)
#
#     return config, compID, compName
