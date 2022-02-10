#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, redirect, render_template, make_response, request, session
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
from config import DevelopentConfig, HostConfig, TOKEN, CLIENT_SECRET, OAUTH_URL, REDIREC_URI
from zenora import APIClient


load_dotenv()

DBC = DevelopentConfig
HSC = HostConfig

app=Flask(__name__)
app.config.from_object(DBC)

client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

app.config["secret_key"] = "XD"
csrf = CSRFProtect()

@app.route('/')
def index():   
    response = make_response( render_template("index.html", oauth_uri=OAUTH_URL) )
    response.set_cookie('log_user', 'True')
    log_user = request.cookies.get('log_user')
    print(log_user)
    return response

@app.route('/commands')
def commands():
    return render_template("commands.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/faq')
def faq():
    return render_template("team.html")

@app.route('/license')
def license():
    return render_template("license.html")

@app.route('/login')
def login():
    code = request.args['code']
    access_token = client.oauth.get_access_token(code, REDIREC_URI).access_token
    session["token"] = access_token
    
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template("profile.html", current_user=current_user)
        
    elif 'token' in session:
        return redirect("/")

def page_not_found(error):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.register_error_handler(404, page_not_found)
    csrf.init_app(app)
    app.run(host="0.0.0.0", port=8101)