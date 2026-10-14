"""Skip repositories without published releases in the CI working copy of source.json."""

import argparse
import json
import os
from pathlib import Path
import re
from urllib.request import Request, urlopen


def releases_for(repository):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError(f"Invalid GitHub repository: {repository}")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "Azipa-Tools-VPM"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    request = Request(f"https://api.github.com/repos/{repository}/releases?per_page=1", headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def ready_source(source, fetch=releases_for):
    ready = []
    for repository in source.get("githubRepos", []):
        # Published GitHub pre-releases are valid here as well as regular releases.
        if fetch(repository):
            ready.append(repository)
        else:
            print(f"Waiting for first published release: {repository}")
    result = dict(source)
    result["githubRepos"] = ready
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("source.json"))
    args = parser.parse_args()
    source = json.loads(args.source.read_text(encoding="utf-8-sig"))
    args.source.write_text(json.dumps(ready_source(source), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
