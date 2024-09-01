# CompWorkflow

Tool to streamline typical tasks when organizing / delegating WCA competitions.

Different steps have their associated scripts in one of the directories
- `PreComp`
- `DuringComp`
- `PostComp`

and all scripts can be called individually as modules. Additionally, multiple steps can be merged and called at the same time, at the level of the steps outlined above.

Each competition has a corresponding YAML configuration file in the `config` directory.

## Examples
### Call a single module of a given step
```shell
python -m CompWorkflow.PreComp.generateWebsiteTabs -c rlp25.yml --debug
```
Mind the `-m` and the dot-notation to ensure things are run as a module (that sees the sibling modules).
