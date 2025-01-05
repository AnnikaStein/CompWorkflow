# PreComp

---

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

---

## Scheduling

---

## Private Competition WCIF
__Command__
```shell
python -m CompWorkflow.PreComp.loadPrivateWCIF -c rlp25.yml --debug
```

__Requirements__
- needs config/<compID>.yml to proceed
- oauth setup as described in main readme

__Outputs__  
inside /output/<compID> there will be
- wcif_private.json directly from the v0 WCA API for the competition described in the config

---

## Comp info (newcomers, foreigners, returners with little experience only, daily attendance)
- WIP: (and rename) wca-competition-orga / competition_info.ipynb

---

## Grouping cross-check

---

## Registration list (all / returners, sorted by registrationId / name)
__Command__
```shell
python -m CompWorkflow.PreComp.generateRegistrationList -c rlp25.yml --debug
```

__Requirements__
- needs config/<compID>.yml to proceed
- private comp WCIF step carried out already

__Outputs__  
inside /output/<compID> there will be
- four csv files with different registration lists (depending on inclusion of returners and sorting strategy)

__ToDo__
- write tex and later on compile as pdf to print out

---

## Nametag generation with front and back
__Command__
```shell
python -m CompWorkflow.PreComp.generateNametags -c rlp25.yml --debug
```

__Requirements__
- needs config/<compID>.yml to proceed
- private comp WCIF step carried out already

__Outputs__  
inside /output/<compID> there will be
- three tex files for frontsides, backsides, merged pdf to each be compiled (merger last)
