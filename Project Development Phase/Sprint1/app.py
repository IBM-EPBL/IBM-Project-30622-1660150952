from flask import Flask, render_template, request, redirect, url_for, session , make_response

import ibm_db
import bcrypt
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=dkz79110;PWD=VnQyUFTQ0JNLLLGq",'','')

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        sql = "select * from user where username=? and password=?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt, 2, password)
        ibm_db.execute(stmt)
        dic = ibm_db.fetch_assoc(stmt)
        print(login)
        if login:
            return redirect(url_for('home.html'))
        else:
            return redirect(url_for('login.html'))
            return redirect(url_for('home.html'))
    elif request.method=='GET':
        return render_template('login.html')
    

@app.route('/register',methods=['POST','GET'])
def register():

    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        confirmpassword = request.form['confirm password']
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']
        mobileno = request.form['mobile no']
        address = request.form['address']
        sql = "insert into user values(?,?,?,?,?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(prep_stmt,1,username)
        ibm_db.bind_param(prep_stmt,2,password)
        ibm_db.bind_param(prep_stmt,3,confirmpassword)
        ibm_db.bind_param(prep_stmt,4,gender)
        ibm_db.bind_param(prep_stmt,5,age)
        ibm_db.bind_param(prep_stmt,6, email)
        ibm_db.bind_param(prep_stmt,7, mobileno)
        ibm_db.bind_param(prep_stmt,7, address)
        ibm_db.execute(prep_stmt)
        return redirect(url_for('home'))
    elif request.method=='GET':
        return render_template('register') 


@app.route('/registerfordonor',methods=['POST','GET'])
def registerfordonor():

    if request.method=='POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age1 = request.form['age1']
        bloodgroup = request.form['bloodgroup']
        gender1 = request.form['gender']
        donatedbefore = request.form['donatedbefore']
        address1 = request.form['address']
        anyhealthissues = request.form['anyhealthissues']
        sql = "insert into donordetails values(?,?,?,?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(prep_stmt,1,firstname)
        ibm_db.bind_param(prep_stmt,2,lastname)
        ibm_db.bind_param(prep_stmt,3,age1)
        ibm_db.bind_param(prep_stmt,4,bloodgroup)
        ibm_db.bind_param(prep_stmt,5,gender1)
        ibm_db.bind_param(prep_stmt,6, donatedbefore)
        ibm_db.bind_param(prep_stmt,7, address1)
        ibm_db.bind_param(prep_stmt,8, anyhealthissues)
        ibm_db.execute(prep_stmt)
        return redirect(url_for('home'))
    elif request.method=='GET':
        return render_template('register') 
       
   


if (__name__)=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)