# PreComp

## Generation of Tabs depending on config
__Command__
```shell
python -m CompWorkflow.PreComp.generateWebsiteTabs -c rlp25.yml --debug
```

__Requirements__
- needs config/<compID>.yml to proceed
- if new venue / location, modification (addition) of further blocks inside /templates/websiteTabs.py is recommended

__Outputs__  
inside /output/<compID> there will be
- main_info.md and main_register.md (to fill into main page / registration steps)
- many tab_<...>.md files (content to fill in various tabs)
- tab_titles.md (titles of the tabs to appear on the navigation bar)

## Scheduling

## Comp info (newcomers, foreigners, returners with little experience only, daily attendance)
- WIP: (and rename) wca-competition-orga / competition_info.ipynb

## Grouping cross-check

## Nametag generation with front and back
- Just need to automate: TagTex
