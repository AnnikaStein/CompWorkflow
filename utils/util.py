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
