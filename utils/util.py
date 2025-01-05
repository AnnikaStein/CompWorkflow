import json, os

def checkOrCreateOutputFolderContainingID(comp_id):
    if not os.path.isdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}'):
         os.mkdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}')

def writeOutputFileForID(comp_id, fname, content):
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}/{fname}', 'w') as f:
        f.write(content)

def writeOutputJSONForID(comp_id, fname, content):
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}/{fname}', 'w') as f:
        json.dump(content, f)

def getSortedListOfListsByNthColumn(unsorted_list, column):
    sortList = unsorted_list.copy()
    sortList.sort(key=lambda x: x[column])
    return sortList

def numeric_order_assignments(a_string):
    if len(a_string) == 0 or a_string == ' ':
        return a_string
    x = a_string.split(',')
    x = [int(k) for k in x]
    x.sort()
    x = ', '.join(map(str, x)) 
    return x

def flatten(myList):
    return [x for sub in myList for x in sub]

def getUniqueListEntriesSorted(original_list):
    new_list = list(set(original_list))
    new_list.sort()
    return new_list

printAssignmentsEVENTORDER = ['333', '222', '444', '555', '666', '777', '333bf', '333fm', '333oh', 'clock', 'minx', 'pyram', 'skewb', 'sq1', '444bf', '555bf', '333mbf']