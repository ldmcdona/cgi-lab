#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

import json
import os

#cgi.print_environ()

print("Content-Type: text/html\n")
print()
print("<!doctype html>")
print("<Head>")
print("<title>Hello</title>")
print("<style> pre {white-space: pre-wrap; word-wrap: break-word;}</style>")
print("</Head>")
print("<h2>Hello World</h2>")

#print(os.environ)
print("<pre>")
print(json.dumps(dict(os.environ)))
print("</pre>")

#Question 1, the cgi.print_environ() thing is the easier way
