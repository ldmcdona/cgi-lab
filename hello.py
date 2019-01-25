#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
from urllib.parse import parse_qs

import json
import os

#cgi.print_environ()

print("Content-Type: text/html\n")
print()
print("<!doctype html>")
print("<head>")
print("<title>Hello</title>")
print("<style>pre {white-space: pre-wrap; word-wrap: break-word;}</style>")
print("</head>")
print("<h2>Hello World</h2>")

#Print qyery string
qs = os.environ.get("QUERY_STRING", None)
ua = os.environ.get("HTTP_USER_AGENT", None)
print("<dl>")
print("<dt>QUERY_STRING</dt>")
print("<dd>{}</dd>".format(parse_qs(qs)))
print("<dt>HTTP_USER_AGENT</dt>")
print("<dd>{}</dd>".format(ua))
print("</dl>")

#print(os.environ)
print("<pre>")
print(json.dumps(dict(os.environ)))
print("</pre>")

#Question 1, the cgi.print_environ() thing is the easier way
#Question 2, QUERY_STRING
#Question 3, HTTP_USER_AGENT
