from cloudbot import hook

import requests

GITHUB_URL = "https://api.github.com/repos/{}/{}/branches/{}"

DEFAULT_OWNER = "SpongePowered"
DEFAULT_REPO = "SpongeAPI"
DEFAULT_BRANCH = "master"

@hook.command("latest", "l")
def latest(text, message):
    data = None
    owner = DEFAULT_OWNER
    repo = DEFAULT_REPO
    branch = DEFAULT_BRANCH

    if len(text) == 0:
        data = requests.get(GITHUB_URL.format(DEFAULT_OWNER, DEFAULT_REPO,
            DEFAULT_BRANCH)).json()
    else:
        text = text.split(' ')
        if len(text) == 1:
            branch = text[0]

            data = requests.get(GITHUB_URL.format(DEFAULT_OWNER, DEFAULT_REPO,
                branch)).json()
        elif len(text) == 2:
            repo = text[0]
            branch = text[1]

            data = requests.get(GITHUB_URL.format(DEFAULT_OWNER, repo,
                branch)).json()

    if data != None:
        slug = "{}/{}".format(repo, branch)
        sha = data["commit"]["sha"][0:7]
        print(data["commit"])
        commit_message = data["commit"]["commit"]["message"].split("\n")[0]
        author = data["commit"]["commit"]["author"]["name"]

        message("{} {}: {} (by {})".format(slug, sha, commit_message, author))
