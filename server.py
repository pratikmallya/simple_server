from flask import Flask, request
from lib import utils
import json
import sys

app = Flask(__name__)


@app.route('/parse', methods=['POST'])
def parse_message():
    data = {}
    msg = request.get_json()["message"]
    mentions = utils.parse_mentions(msg)
    if mentions is not None:
        data["mentions"] = mentions
    emoticons = utils.parse_emoticons(msg)
    if emoticons is not None:
        data["emoticons"] = emoticons
    links = utils.parse_links(msg)
    if links is not None:
        data["links"] = links
    return json.dumps(data)


if __name__ == '__main__':
    app.run()
