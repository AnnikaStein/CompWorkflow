# CompWorkflow

Tool to streamline typical tasks when organizing / delegating WCA competitions.

Comes with an ISSUE_TEMPLATE for each new competition to be covered by CompWorkflow, with a project management view to track the individual steps (Preparation / Announced / Done).

## Setup
To use the OAuth functionality, create an [WCA OAuth application](https://www.worldcubeassociation.org/oauth/applications/new) with redirect URI `urn:ietf:wg:oauth:2.0:oob` and with the scopes `public manage_competitions`. Authorize the application, note down the code.

Put the three custom parameters Application ID, Secret and the code mentioned above that you see after the redirect in a python script in the `oauth` directory. You may use the entered `redirect_uri` as recommended by the WST. To make sure it does not get pushed to github by accident, the gitignore file excludes all `.py` files inside `oauth`. Stick to this pattern and replace the defaults:

```python
access_token_url = 'https://www.worldcubeassociation.org/oauth/token'

applicationDetails = {
    'client_id': (None, 'YOUR-CLIENT-ID'),
    'client_secret': (None, 'YOUR-CLIENT-SECRET'),
    'code': (None, 'YOUR-CODE'),
    'redirect_uri': (None, 'urn:ietf:wg:oauth:2.0:oob'),
}
```

Put this snippet with your own modifications into `oauth/myOAuthApplication.py`. Depending scripts will search for this file.

The WCA OAuth via the v0 API is documented on [this page](https://docs.worldcubeassociation.org/knowledge_base/v0_api.html) and to simplify implementing POST requests in Python 3, [curlconverter](https://curlconverter.com/python/) was used.

## Usage for new competitions

Different steps have their associated scripts in one of the directories
- `PreComp`
- `DuringComp`
- `PostComp`

and all scripts can be called individually as modules. Additionally, multiple steps can be merged and called at the same time, at the level of the steps outlined above and with diverse combinations.

Each competition has a corresponding YAML configuration file in the `config` directory.

## Examples
### Call a combination of modules to do multiple related steps at once
You can perform multiple tasks with one call to a runner script, from anywhere on your machine. It's quick, but it always uses the default arguments per python module.

General command:
```shell
source <some-path-to-the-script>/runWorkflow.sh <combination-name> <yaml-config-file>
```
Example command:
```shell
source CompWorkflow/runWorkflow.sh PrePrint rlp25.yml
```

Currently implemented combinations:

- `PreComp`: `generateWebsiteTabs / loadPrivateWCIF / generateRegistrationList / generateNametags / generateStats`
    - `PreAnnounce`: `generateWebsiteTabs`
    - `PrePrint`: `loadPrivateWCIF / generateRegistrationList / generateNametags / generateStats`

### Call a single module of a given step
This only works from the parent directory of `CompWorkflow`. This offers most flexibility to customize the parameters of each step.
```shell
python -m CompWorkflow.PreComp.generateWebsiteTabs -c rlp25.yml --debug
```

```shell
python -m CompWorkflow.PreComp.loadPrivateWCIF -c rlp25.yml --debug
```
(this will ask for your WCA account username (email) and password - if you want to use the authorization_code variant, put `-g authorization_code` and make sure to do a fresh authorization on the website and copy the latest code into your setup file, see above)

```shell
python -m CompWorkflow.PostComp.aftercompMail -c mzc25.yml --debug
```

Mind the `-m` and the dot-notation to ensure things are run as a module (that sees the sibling modules).

## Extras
### Certificates
Texts to fill into goosly's website "wca-certificates" are placed in `templates/certificates.md`.
