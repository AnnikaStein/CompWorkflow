import os

def checkOrCreateOutputContainingID(comp_id):
    if not os.path.isdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}'):
         os.mkdir(f'{os.path.dirname(os.path.realpath(__file__))}/../output/{comp_id}')
