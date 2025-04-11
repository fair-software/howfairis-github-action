#!/bin/bash

set -e

howfairis \
    --branch ${INPUT_BRANCH-main} \
    ${INPUT_MY_REPO_URL}
    # --json-output${INPUT_JSON} \
