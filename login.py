#!/usr/bin/env python3

import os
import cgi
import cgitb
cgitb.enable()
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password

form = cgi.FieldStorage()
f_username = form.getfirst("username")
f_password = form.getfirst("password")

request_type = os.environ.get("REQUEST_METHOD", "GET")

c_username = None
c_password = None

cookie_string = os.environ.get("HTTP_COOKIE")

cookie_kvs = cookie_string.split("; ")
if cookie_kvs:
    for kv in cookie_kvs:
        if kv:
            k, v = kv.split("=")
            if k == "username":
                c_username = v
            if k == "password":
                c_password = v

print("Content-Type: text/html")

if c_username and c_password:
    print()
    print(secret_page(c_username, c_password))

elif request_type == "POST":
    if f_username == username and f_password == password:
        #Login ok, set cookie
        print("Set-Cookie: username={}".format(f_username))
        print("Set-Cookie: password={}".format(f_password))
        print()
        print(secret_page(f_username, f_password))
    else:
        print()
        print(after_login_incorrect())
else:
    print()
    print(login_page())


#Question 4: cgi.FieldStorage()
#Question 5: "Set-Cookie: "
#Question 6: in the request header "Cookie:"
#Question 7: They are used to stored to save data between sessions.
