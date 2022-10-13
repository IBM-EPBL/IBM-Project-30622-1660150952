"""----------------------------------------------------------------------------------------------------------------------------
-------------------- Done by Saran S [Team Leader] with [Team Members] Krishna Prasath , Ramasubramaniyan , Sathiya------------
-------------------------------------------------------------------------------------------------------------------------------"""

#Importing the Libraries 
from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3

#Creating a Flask App
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])

# Defining the Login Page using login() func

def login():
    if request.method == "POST":
        mail_id = request.form['mail']
        password = request.form["pass"]
        con = sqlite3.connect("assignment.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM signup WHERE mailid='"+mail_id+"'")
        res=cur.fetchone()
        if(len(res)>0):
         if(password==res[4]):
            con.commit()
            con.close()
            return render_template("home.html",name=res[2])
        else:
            return render_template("signup.html")
    else:
        return render_template("login.html")
@app.route("/signup",methods=['GET','POST'])

# Defining the signup Page using signup() func

def signup():
    if request.method == 'POST':
          con = sqlite3.connect("assignment.db")
          cur = con.cursor()
          mail_id=request.form['mail']
          name=request.form['name']
          ph=request.form['ph']
          passw=request.form['pass']
          cur.execute("SELECT * FROM signup WHERE mailid='" + mail_id + "'")
          if (len(cur.fetchall()) > 0):
                  return render_template("login.html")
          else:
              cur.execute(
                  "INSERT INTO signup (mailid,username,phno,password) values('"+mail_id+"','"+name+"','"+ph+"','"+passw+"');")
              con.commit()
              con.close()
              return render_template("login.html")

          return render_template("signup.html")
    else:
        return render_template("signup.html")

# Executing the Flask App

if __name__ == "__main__":
    app.run()

# Done by Saran S [Team Leader] with [Team Members] Krishna Prasath , Ramasubramaniyan , Sathiya 
# Git Repository IBM-Project-33476-1660221541