from flask import Flask,render_template, request
from connect import *
import ibm_db

app= Flask(__name__,template_folder='templates', static_folder='static')
@app.route("/")
def index():
    return render_template("ui.html")

@app.route("/register",methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username=request.form['username']
        mail=request.form['email']
        password=request.form['password']
        query="insert into user values('"+username+"','"+password+"','"+mail+"')"
        stmt=ibm_db.exec_immediate(conn,query)
        rowcount=ibm_db.num_rows(stmt)
        print(rowcount)

    return  render_template("ui.html")

@app.route("/login",methods=('GET','POST'))
def loginpage():
    if request.method == 'GET':
        return  render_template("ui.html")
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        query = "select COUNT(*) from user where email='"+email+"' and password='"+password+"'"
        stmt5 = ibm_db.exec_immediate(conn,query)
        row = ibm_db.fetch_tuple(stmt5)
        if(row[0] ==1 ):
            return render_template("news.html")
    return render_template("ui.html")

def navigation():
    if request.method=="GET":
        home=request.form['home']
    return render_template("ui.html")

if(__name__=='__main__'):
     app.run('0.0.0.0',port=5000,debug=True)