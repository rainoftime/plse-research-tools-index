#!/usr/bin/env python3

import json
import requests

metadata = json.loads(open('metadata.json', 'r').read())

GITHUB_PREFIX = "https://github.com/"

for entry in metadata:
    if not entry["repo"].startswith(GITHUB_PREFIX):
        continue
    owner_repo = entry["repo"][len(GITHUB_PREFIX):]
    response = json.loads(requests.get("https://api.github.com/repos/" + owner_repo).text)
    entry["language"] = response["language"]
    entry["stargazers_count"] = response["stargazers_count"]
    entry["last-commit"] = response["pushed_at"]

open("docs/data.json", "w").write(json.dumps(metadata))
