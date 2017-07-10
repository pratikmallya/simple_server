import re
import requests
from lxml import html

PAT_EMOTICONS = re.compile(r'\([a-zA-Z]{1,15}\)')
PAT_MENTIONS = re.compile(r'\@\w+')
PAT_URLS = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')


def parse_mentions(in_str):
    mentions = PAT_MENTIONS.findall(in_str)
    if mentions is None or len(mentions) == 0:
        return None
    # use map to remove the `@` prefix from matched string
    return map(lambda x: x[1:], mentions)


def parse_emoticons(in_str):
    emoticons = PAT_EMOTICONS.findall(in_str)
    if emoticons is None or len(emoticons) == 0:
        return None
    # use map to strip parenthesis from matched string
    return map(lambda x: x[1:-1], emoticons)


# Assumptions:
# Only HTTP/HTTPS urls parsed
# Only webpages visible publicly with titles defined in html returned
def parse_links(in_str):
    urls = PAT_URLS.findall(in_str)
    if urls is None or len(urls) == 0:
        return None
    # the following should be done concurrently, since HTTP requests can take
    # time but request can be initiated at the same time

    links = []
    for url in urls:
        res = requests.get(url)
        if res.status_code != 200:
            continue
        tree = html.fromstring(res.content)
        title = tree.findtext('.//title')
        if title is None:
            continue
        links.append({
            "url": url,
            "title": title,
        })
    if len(links) == 0:
        return None
    return links
