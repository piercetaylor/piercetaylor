"""Refresh the generated blocks in README.md from the GitHub API.

Two blocks are rewritten in place, each delimited by HTML comments:
`recent_releases` lists the newest release of each public repository that has
one, and `recent_activity` lists the repositories pushed to most recently. The
script is idempotent; if nothing has changed the file is left untouched and the
workflow makes no commit.
"""

import json
import os
import pathlib
import re
import urllib.error
import urllib.request

USER = "piercetaylor"
ROOT = pathlib.Path(__file__).parent.resolve()
README = ROOT / "README.md"
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def api(path):
    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-profile-readme",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise


def replace_block(text, name, body):
    pattern = re.compile(
        rf"(<!-- {name} starts -->).*?(<!-- {name} ends -->)", re.DOTALL
    )
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(2)}", text)


def main():
    repos = [
        repo
        for repo in api(f"/users/{USER}/repos?sort=pushed&per_page=100&type=owner")
        if not repo["fork"] and not repo["archived"]
    ]

    releases = []
    for repo in repos:
        latest = api(f"/repos/{USER}/{repo['name']}/releases/latest")
        if latest:
            releases.append((latest["published_at"], repo["name"], latest))
    releases.sort(reverse=True)

    if releases:
        release_lines = [
            f"[{repo} {r['tag_name']}]({r['html_url']}) - {published[:10]}"
            for published, repo, r in releases[:6]
        ]
    else:
        release_lines = ["No tagged releases yet."]

    activity_lines = [
        f"[{repo['name']}](https://github.com/{USER}/{repo['name']}) - "
        f"{repo['pushed_at'][:10]}"
        for repo in repos[:6]
    ]

    text = README.read_text(encoding="utf-8")
    updated = replace_block(text, "recent_releases", "\n\n".join(release_lines))
    updated = replace_block(updated, "recent_activity", "\n\n".join(activity_lines))

    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print("README.md updated")
    else:
        print("README.md unchanged")


if __name__ == "__main__":
    main()
