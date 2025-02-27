echo " "
echo ">> Welcome to CompWorkflow!"

conda activate cubing

# Check if the location from where the script was called is equal to the location in which the script is contained
DIR=$(realpath "$(dirname "${BASH_SOURCE[0]}")")
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
if  [[ ${DIR} == ${dir} ]]; then
    # >> Already inside package directory. Run scripts there from one level up.
    cd ..
elif  [[ ${DIR} != ${dir} ]]; then
    # >> Not inside package directory. cd there first, run scripts there from one level up.
    cd ${dir}/..
fi

if  [[ $1 == "PreComp" ]]; then
    echo " "
    echo ">> Running all PreComp python scripts now."
    echo ">> These are generateWebsiteTabs / loadPrivateWCIF / generateRegistrationList / generateNametags / generateStats"
    echo " "
    python -m CompWorkflow.PreComp.generateWebsiteTabs -c $2 --debug
    python -m CompWorkflow.PreComp.loadPrivateWCIF -c $2 --debug
    python -m CompWorkflow.PreComp.patchGroupifierExtensionToPrivateWCIF -c $2 --debug
    python -m CompWorkflow.PreComp.generateStats -c $2 --debug
    python -m CompWorkflow.PreComp.generateRegistrationList -c $2 --debug
    python -m CompWorkflow.PreComp.generateNametags -c $2 --debug
elif  [[ $1 == "PreAnnounce" ]]; then
    echo " "
    echo ">> Running PreAnnounce python scripts now."
    echo ">> This is generateWebsiteTabs"
    echo " "
    python -m CompWorkflow.PreComp.generateWebsiteTabs -c $2 --debug
elif  [[ $1 == "PreAssign" ]]; then
    echo " "
    echo ">> Running PreAssign python scripts now."
    echo ">> This is patchGroupifierExtensionToPrivateWCIF"
    echo " "
    python -m CompWorkflow.PreComp.patchGroupifierExtensionToPrivateWCIF -c $2 --debug
    python -m CompWorkflow.PreComp.generateStats -c $2 --debug
    # create groups, per event and stage
    # fill groups with competitors and tasks
elif  [[ $1 == "PrePrint" ]]; then
    echo " "
    echo ">> Running PrePrint python scripts now."
    echo ">> These are loadPrivateWCIF / generateRegistrationList / generateNametags / generateStats"
    echo " "
    python -m CompWorkflow.PreComp.loadPrivateWCIF -c $2 --debug
    python -m CompWorkflow.PreComp.generateStats -c $2 --debug
    python -m CompWorkflow.PreComp.generateRegistrationList -c $2 --debug
    python -m CompWorkflow.PreComp.generateNametags -c $2 --debug
elif  [[ $1 == "DuringComp" ]]; then
    echo " "
    echo ">> Running all DuringComp python scripts now."
    echo ">> These are "
    echo " "
elif  [[ $1 == "PostComp" ]]; then
    echo " "
    echo ">> Running all PostComp python scripts now."
    echo ">> These are loadPrivateWCIF / aftercompMail"
    echo " "
    python -m CompWorkflow.PreComp.loadPrivateWCIF -c $2 --debug
    python -m CompWorkflow.PostComp.aftercompMail -c $2 --debug
fi

# Go back to original directory from which this runner was called
cd ${DIR}
