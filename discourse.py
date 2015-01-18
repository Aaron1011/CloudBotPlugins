from cloudbot import hook

import requests
import html

DEFAULT_BASE = "http://forums.spongepowered.org/"
DEFAULT_CATEGORY_SLUG = "announcements"

CATEGORY_URL = "c/{}/l/latest.json"

@hook.command("discourse", "dc")
def discourse(text, message):
    if len(text) == 0:
        data = requests.get(DEFAULT_BASE + (CATEGORY_URL.format(
                DEFAULT_CATEGORY_SLUG))).json()
        
        topics = data["topic_list"]["topics"]
        message(html.unescape(topics[0]["title"]))
        message(topics[0]["excerpt"])
