from flask_app import app
from flask import Flask, redirect, session, request, render_template, url_for, flash

@app.route('/')
def index():
    
    return redirect ("/Form")
@app.route('/Form')
def survey():
    print('survey')
    return render_template ("form.html" )
@app.route('/result')
def NewResult():
    print('NewResult')
    return render_template ("result.html" )
@app.route('/add', methods=['POST'])
def AddContent():
    print("FORM DATA",request.form)
    print("AddContent DATA",request.form)
    session["FullName"] = request.form['Full_Name']
    session["Location"] = request.form['location']
    session["Language"] = request.form['language']
    session["Comments"] = request.form['message']
    
    
    print(session)
    return redirect ("/result")
