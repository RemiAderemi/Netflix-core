#!C:\Python\python.exe
print("Content-type: text/html\n\n")
import sys
import os
import cgi
import cgitb
import model
import json
from datetime import datetime
cgitb.enable()

form=cgi.FieldStorage()
up_name=form.getvalue("up_name")
up_email=form.getvalue("up_email")
up_passwd=form.getvalue("up_password")
conf_pass=form.getvalue("password_confirm")
in_email= form.getvalue("in_email")
in_passwd=form.getvalue("in_password")
dateTime = datetime.utcnow().strftime('%Y-%m-%d %H:%H:%S')

if conf_pass:
    sign_up={'name':up_name,'email':up_email,'passwd':up_passwd,'date':dateTime}
    insertSignUp=model.sign_up(sign_up)
    twitterResponse = json.loads(insertSignUp)#json.dumps conver the jason.loads to readable for Serialization
    if twitterResponse['status'] == 200:
    # print "Location:http://localhost/neflix/index.py"
        redirect = """<script>window.location.replace('http://localhost/neflix/movie_list.py')</script>"""
        print(redirect)
    else:
        print(twitterResponse['message'])
        
else:
    sign_in={'email':in_email,'passwd': in_passwd}
    insertSignUp=model.sign_in(sign_in)
    twitterResponse = json.loads(insertSignUp)#json.dumps conver the jason.loads to readable for Serialization
    if twitterResponse['status'] == 200:
    # print "Location:http://localhost/neflix/index.py"
        redirect = """<script>window.location.replace('http://localhost/neflix/movie_detail.py')</script>"""
        print(redirect)
    else:
        print(twitterResponse['message'])

# twitterResponse = json.loads(insertSignUp)#json.dumps conver the jason.loads to readable for Serialization
# if twitterResponse['status'] == 200:
#    # print "Location:http://localhost/neflix/index.py"
#    redirect = """<script>window.location.replace('http://localhost/neflix/movie_list.py')</script>"""
#    print(redirect)
# else:
#    print(twitterResponse['message'])