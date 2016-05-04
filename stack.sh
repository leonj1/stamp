#!/bin/bash

ATLAS_BASE=~/src/atlas/provisioning/envs
SRC_CLUSTER=$ATLAS_BASE/feature/one
TARGET_CLUSTER=$ATLAS_BASE/devops/jleon

STAMP_PATH=~/workarea/stamp
VAULT_FILE=~/.secrets/vault

if [ ! -r $VAULT_FILE ]; then
    echo "Vault file does not exist. Terminating."
    exit 1
fi

cp -r $SRC_CLUSTER $TARGET_CLUSTER
ansible-vault decrypt --vault-password-file=$VAULT_FILE $TARGET_CLUSTER/secrets.yml

python $STAMP_PATH/token.py -i $STAMP_PATH/template.json

ansible-vault encrypt --vault-password-file=$VAULT_FILE $TARGET_CLUSTER/secrets.yml

