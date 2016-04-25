#!/bin/bash

CLUSTER=provisioning/envs/devops/USERNAME

cp -r ./provisioning/envs/feature/one $CLUSTER
ansible-vault decrypt --vault-password-file=~/.secrets/vault $CLUSTER/secrets.yml

python ~/workarea/stamp/token.py -i ~/workarea/stamp/template.json

ansible-vault encrypt --vault-password-file=~/.secrets/vault $CLUSTER/secrets.yml

