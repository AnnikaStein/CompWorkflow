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
    echo ">> Running all PreComp python scripts now. Usually, this is not done all at once!"
    echo ">> These are generateWebsiteTabs / readWritePrivateWCIF / loadPrivateWCIF / patchGroupifierCompetitionConfigRoomConfigToPrivateWCIF / generateStats / generateGroups / generateRegistrationList / generateNametags"
    echo " "
    python -m CompWorkflow.PreComp.generateWebsiteTabs -c $2 --debug
    python -m CompWorkflow.PreComp.readWritePrivateWCIF -c $2 --debug
    python -m CompWorkflow.PreComp.loadPrivateWCIF -c $2 --debug
    python -m CompWorkflow.PreComp.patchGroupifierCompetitionConfigRoomConfigToPrivateWCIF -c $2 --debug
    python -m CompWorkflow.PreComp.generateStats -c $2 --debug
    python -m CompWorkflow.PreComp.generateGroups -c $2 --debug
    python -m CompWorkflow.PreComp.generateRegistrationList -c $2 --debug
    python -m CompWorkflow.PreComp.generateNametags -c $2 --debug
elif  [[ $1 == "PreAnnounced" ]]; then
    echo " "
    echo ">> Running PreAnnounced python scripts now. Do this when filling the website with information and test communication from/to WCIF."
    echo ">> This is generateWebsiteTabs / readWritePrivateWCIF"
    echo " "
    python -m CompWorkflow.PreComp.generateWebsiteTabs -c $2 --debug
    python -m CompWorkflow.PreComp.readWritePrivateWCIF -c $2 --debug
elif  [[ $1 == "PreAssigned" ]]; then
    echo " "
    echo ">> Running PreAssigned python scripts now. Do this after online registration started."
    echo ">> These are patchGroupifierCompetitionConfigRoomConfigToPrivateWCIF / generateStats / generateGroups"
    echo " "
    python -m CompWorkflow.PreComp.patchGroupifierCompetitionConfigRoomConfigToPrivateWCIF -c $2 --debug
    python -m CompWorkflow.PreComp.generateStats -c $2 --debug
    python -m CompWorkflow.PreComp.generateGroups -c $2 --debug
    python -m CompWorkflow.PreComp.generatePsych -c $2 --debug
elif  [[ $1 == "PrePrinted" ]]; then
    echo " "
    echo ">> Running PrePrinted python scripts now. Do this when grouping / assignments are done."
    echo ">> These are loadPrivateWCIF / generateStats / generateRegistrationList / generateNametags"
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
