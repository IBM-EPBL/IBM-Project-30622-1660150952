pfrom flask import Flask, render_template, request, redirect, url_for, session

import ibm_db
import bcrypt
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31929;UID=llk39962;PWD=zItMgmJHoIm42n82",'','')

app = Flask(__name__)
app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/home', methods=['POST','GET'])
def home():
    return render_template("home.html")

@app.route('/sigin', methods=['POST','GET'])
def signin():
    return render_template("signin.html")    




@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        print("entered into post")

        if not username or not password:
          return render_template('login.html', error='please fill all fields')
        sql = "select * from user where username=? and password=?"   
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt, 2, password)
        ibm_db.execute(stmt)
        dic = ibm_db.fetch_assoc(stmt)
        print(login)
        if login:
          return redirect(url_for('signin'))

            
        else:
            return redirect(url_for('login'))


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



        if not username or password or confirmpassword or gender or age or email or mobileno:
            return render_template('register.html', error = 'Please fill all the fields')
        hash=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        query = "SELECT * FROM user WHERE username=? OR password=?"
        stmt = ibm_db.prepare(conn,query)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        isuser=ibm_db.fetch_assoc(stmt)
        if not isuser:
            sql = "INSERT INTO user(username, password, confirmpassword, gender, age, email, mobileno) VALUES(?,?,?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn,sql)
            ibm_db.bind_param(prep_stmt,1,username)
            ibm_db.bind_param(prep_stmt,2,password)
            ibm_db.bind_param(prep_stmt,3,confirmpassword)
            ibm_db.bind_param(prep_stmt,4,gender)
            ibm_db.bind_param(prep_stmt,5,age)
            ibm_db.bind_param(prep_stmt,6, email)
            ibm_db.bind_param(prep_stmt,7, mobileno)
            ibm_db.execute(prep_stmt)
            return redirect(url_for('home'))
        else:
            return render_template('register.html',error='Invalid details')   
    return render_template('login.html', name='home')






@app.route('/registerfordonor',methods=['POST','GET'])
def registerfordonor():

    if request.method=='POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age1 = request.form['age1']
        bloodgroup = request.form['bloodgroup']
        gender1 = request.form['gender1']
        donatedbefore = request.form['donatedbefore']
        address1 = request.form['address1']
        anyhealthissues = request.form['anyhealthissues']
        sql1 = "insert into DONORDETAILS values(?,?,?,?,?,?,?,?)"
        prep_stmt1 = ibm_db.prepare(conn,sql1)
        ibm_db.bind_param(prep_stmt1,1,firstname)
        ibm_db.bind_param(prep_stmt1,2,lastname)
        ibm_db.bind_param(prep_stmt1,3,age1)
        ibm_db.bind_param(prep_stmt1,4,bloodgroup)
        ibm_db.bind_param(prep_stmt1,5,gender1)
        ibm_db.bind_param(prep_stmt1,6, donatedbefore)
        ibm_db.bind_param(prep_stmt1,7, address1)
        ibm_db.bind_param(prep_stmt1,8, anyhealthissues)
        ibm_db.execute(prep_stmt1)
        return redirect(url_for('home'))
    elif request.method=='GET':
        return render_template('register') 



@app.route('/requestfordonor',methods=['POST','GET'])
def requestfordonor():

    if request.method=='POST':
        username = request.form['username']
        gender1 = request.form['gender1']
        age1 = request.form['age1']
        bloodgroup = request.form['bloodgroup']
        email = request.form['email']
        mobileno = request.form['mobileno']


        if not username or gender1 or age1 or bloodgroup or email or mobileno:
            return render_template('request.html', error = 'Please fill all the fields')
        

        query = "select * from donordetails where username=? or bloodgroup=?"
        stmt = ibm_db.prepare(conn,query)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,bloodgroup)
        ibm_db.execute(stmt)
        isuser=ibm_db.fetch_assoc(stmt)
        if not isuser:
            return render_template('request.html', success='Request sent successfully.')
        else:
            return render_template('request.html',error='Invalid details')   
    return render_template('home.html', name='home')  












        
        
           
       
   


if (__name__)=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)