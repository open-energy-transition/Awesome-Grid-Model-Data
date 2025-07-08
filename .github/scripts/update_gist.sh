#!/bin/bash

# SPDX-FileCopyrightText: 2025 Open Energy Transition (OET)
#
# SPDX-License-Identifier: MIT

# Update a GitHub Gist with the latest Shields.io badge JSON

# Usage:
#   GIST_ID=<your-gist-id> GIST_TOKEN=<your-token> ./update_gist.sh

set -e

if [ -z "$GIST_ID" ] || [ -z "$GIST_TOKEN" ]; then
  echo "❌ GIST_ID and GIST_TOKEN must be set in the environment."
  exit 1
fi

# Escape JSON content
CONTENT=$(jq -Rs . < link-status.json)

curl -s -X PATCH "https://api.github.com/gists/${GIST_ID}" \
  -H "Authorization: token ${GIST_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{
    \"files\": {
      \"link-status.json\": {
        \"content\": ${CONTENT}
      }
    }
  }"

echo "✅ Gist updated successfully."
