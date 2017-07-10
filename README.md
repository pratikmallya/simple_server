[![Build Status](https://travis-ci.org/pratikmallya/simple_server.svg?branch=master)](https://travis-ci.org/pratikmallya/simple_server)

Simple Test Server
==================

Simple server to parse messages into mentions, emoticons and links.

## Run
```bash
pip install -r requirements.txt
python server.py
```

## Test

```bash
curl -XPOST -H "Content-Type: application/json" -d '{"message":"@bob @john (success) such a cool feature; https://ttus/430511497475670016"}' http://127.0.0.1:5000/parse
```
