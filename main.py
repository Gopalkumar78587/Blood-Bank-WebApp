from flask import Flask
from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
import os
import base64
from PIL import Image
from datetime import datetime
from datetime import date
import datetime
import random
import cv2
import PIL.Image
from PIL import Image
from random import seed
from random import randint
from werkzeug.utils import secure_filename
from flask import send_file
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import threading
import time
import shutil
import hashlib
import urllib.request
import urllib.parse
from urllib.request import urlopen
import webbrowser

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  charset="utf8",
  database="blood_bank"
)


app = Flask(__name__)
##session key
app.secret_key = 'abcdef'
UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#####

@app.route('/',methods=['POST','GET'])
def index():
    cnt=0
    act=""
    msg=""

    '''fn="aa.jpg"
    image = cv2.imread('static/img/c1.jpg',cv2.IMREAD_UNCHANGED)

    name="Raj"
    bgrp="A+ve"
    ddate="08-03-2023"
    position = (530,390)
    cv2.putText(image, name, position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1) 
    cv2.imwrite("static/upload/"+fn, image)

    position = (550,435)
    cv2.putText(image, bgrp, position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1) 
    cv2.imwrite("static/upload/"+fn, image)

    position = (720,520)
    cv2.putText(image, ddate, position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1) 
    cv2.imwrite("static/upload/"+fn, image)'''
        
    return render_template('index.html',msg=msg,act=act)

@app.route('/login',methods=['POST','GET'])
def login():
    cnt=0
    act=""
    msg=""
    if request.method == 'POST':
        
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM admin where username=%s && password=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            session['username'] = username1
            #result=" Your Logged in sucessfully**"
            return redirect(url_for('admin')) 
        else:
            msg="Your logged in fail!!!"
            act="wrong"

    return render_template('login.html',msg=msg,act=act)

@app.route('/login_hos',methods=['POST','GET'])
def login_hos():
    cnt=0
    act=""
    msg=""

    
    
    if request.method == 'POST':
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM bb_register where uname=%s && pass=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            session['username'] = username1
            result=" Your Logged in sucessfully**"
            return redirect(url_for('hos_home')) 
        else:
            msg="Invalid Username or Password!"
            act="wrong"
        

    return render_template('login_hos.html',msg=msg,act=act)

@app.route('/login_donor',methods=['POST','GET'])
def login_donor():
    cnt=0
    act=""
    msg=""

    if request.method == 'POST':
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM bb_donor where donor=%s && pass=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            session['username'] = username1
            result=" Your Logged in sucessfully**"
            return redirect(url_for('donor_home')) 
        else:
            msg="Invalid Username or Password!"
            act="wrong"
        

    return render_template('login_donor.html',msg=msg,act=act)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg=""
    act=request.args.get("act")
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT max(id)+1 FROM bb_register")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1
    
    uid="BBH"+str(maxid)
    if request.method=='POST':

        name=request.form['name']
        location=request.form['location']
        city=request.form['city']
        mobile=request.form['mobile']
        email=request.form['email']
        uname=request.form['uname']
        pass1=request.form['password']
        utype=request.form['utype']

        now = date.today() #datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
        
        sql = "INSERT INTO bb_register(id,name,mobile,email,location,city,uname,pass,utype) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (maxid,name,mobile,email,location,city,uname,pass1,utype)
        mycursor.execute(sql, val)
        mydb.commit()

        
        print(mycursor.rowcount, "Registered Success")
        msg="success"
            
    return render_template('register.html', msg=msg,uid=uid)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    msg=""
    act=request.args.get("act")
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM bb_register")
    data = mycursor.fetchall()

    if act=="yes":
        sid=request.args.get("sid")
        mycursor.execute("update bb_register set status=1 where id=%s",(sid,))
        mydb.commit()
        act="success"
    if act=="no":
        sid=request.args.get("sid")
        mycursor.execute("update bb_register set status=2 where id=%s",(sid,))
        mydb.commit()
        act="no"
    
    return render_template('admin.html',msg=msg,act=act,data=data)

@app.route('/view_donor', methods=['GET', 'POST'])
def view_donor():
    msg=""
    act=request.args.get("act")
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM bb_donor")
    data = mycursor.fetchall()

 
    
    return render_template('view_donor.html',msg=msg,act=act,data=data)

@app.route('/hos_home', methods=['GET', 'POST'])
def hos_home():
    msg=""
    uname=""
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM bb_register where uname=%s",(uname,))
    data = mycursor.fetchone()
        
    return render_template('hos_home.html',data=data)

@app.route('/add_donor', methods=['GET', 'POST'])
def add_donor():
    msg=""
    uname=""
    mess=""
    email=""
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM bb_register where uname=%s",(uname,))
    data = mycursor.fetchone()

    mycursor.execute("SELECT max(id)+1 FROM bb_donor")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1

    if request.method=='POST':
        name=request.form['name']
        gender=request.form['gender']
        dob=request.form['dob']
        address=request.form['address']
        mobile=request.form['mobile']
        email=request.form['email']
        city=request.form['city']
        blood_grp=request.form['blood_grp']
        

        donor="BD"+str(maxid)
        pass1="1234"

        now = date.today() #datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")

        sql = "insert into bb_donor(id,uname,name,gender,dob,address,mobile,email,city,blood_grp,donor,pass) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (maxid,uname,name,gender,dob,address,mobile,email,city,blood_grp,donor,pass1)
        
        mycursor.execute(sql, val)
        mydb.commit()
        mess="Donor Info: Donor ID: "+donor+", Password: "+pass1+" by "+uname+" (Blood Bank)";
        
        print(mycursor.rowcount, "Registered Success")
        msg="success"
        
    return render_template('add_donor.html',data=data,act=act,msg=msg,mess=mess,email=email)

@app.route('/hos_donor', methods=['GET', 'POST'])
def hos_donor():
    msg=""
    uname=""
    st=""
    data2=[]
    city=""
    blood_grp=""
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM bb_register where uname=%s",(uname,))
    data = mycursor.fetchone()

    mycursor.execute("SELECT distinct(city) FROM bb_donor")
    data1 = mycursor.fetchall()

    now = date.today() #datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")

    if request.method=='POST':
        city=request.form['city']
        blood_grp=request.form['blood_grp']
        t1=request.form['t1']
        st="1"
        if city=="" or blood_grp=="":
            mycursor.execute("SELECT * FROM bb_donor order by rand() limit 0,10")
            data2 = mycursor.fetchall()
            
        if city=="":
            mycursor.execute("SELECT * FROM bb_donor where city=%s",(city,))
            data2 = mycursor.fetchall()
        else:
            mycursor.execute("SELECT * FROM bb_donor where blood_grp=%s",(blood_grp,))
            data2 = mycursor.fetchall()


        if t1=="2":
            gid=request.form.getlist('gid[]')
            mess=request.form['mess']
            etime=request.form['etime']

            mycursor.execute("SELECT max(id)+1 FROM bb_send")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
            sql = "insert into bb_send(id,uname,message,etime,blood_grp,rdate,status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = (maxid,uname,mess,etime,blood_grp,rdate,'0')
        
            mycursor.execute(sql, val)
            mydb.commit()
            ##
            for g1 in gid:
                mycursor.execute("SELECT max(id)+1 FROM bb_send_donor")
                maxid2 = mycursor.fetchone()[0]
                if maxid2 is None:
                    maxid2=1
                sql = "insert into bb_send_donor(id,sid,uname,donor,blood_grp,status) VALUES (%s,%s,%s,%s,%s,%s)"
                val = (maxid2,maxid,uname,g1,blood_grp,'0')
            
                mycursor.execute(sql, val)
                mydb.commit()


            msg="sent"
        
       
    return render_template('hos_donor.html',msg=msg,data=data,data1=data1,data2=data2,st=st,city=city,blood_grp=blood_grp)


@app.route('/hos_req', methods=['GET', 'POST'])
def hos_req():
    msg=""
    uname=""
    st=""
    data2=[]
    city=""
    blood_grp=""
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM bb_register where uname=%s",(uname,))
    data = mycursor.fetchone()

    mycursor.execute("SELECT * FROM bb_send where uname=%s order by id desc",(uname,))
    data2 = mycursor.fetchall()

    return render_template('hos_req.html',msg=msg,data=data,data2=data2)

@app.route('/hos_donorst', methods=['GET', 'POST'])
def hos_donorst():
    msg=""
    uname=""
    sid=request.args.get("sid")
    act=request.args.get("act")
    st=""
    data2=[]
    city=""
    blood_grp=""
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM bb_register where uname=%s",(uname,))
    data = mycursor.fetchone()

    mycursor.execute("SELECT * FROM bb_send_donor s,bb_donor d where s.donor=d.donor && s.sid=%s order by s.id desc",(sid,))
    data2 = mycursor.fetchall()

    if act=="donate":
        rid=request.args.get("rid")
        now = date.today() #datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")

        mycursor.execute("SELECT * FROM bb_send_donor where id=%s",(rid,))
        d1 = mycursor.fetchone()
        mycursor.execute("SELECT * FROM bb_donor where donor=%s",(d1[3],))
        d2 = mycursor.fetchone()
        

        fn="C"+rid+".jpg"
        image = cv2.imread('static/img/c1.jpg',cv2.IMREAD_UNCHANGED)

        name=d2[2]
        bgrp=d2[9]
        
        position = (530,390)
        cv2.putText(image, name, position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1) 
        cv2.imwrite("static/upload/"+fn, image)

        position = (550,435)
        cv2.putText(image, bgrp, position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1) 
        cv2.imwrite("static/upload/"+fn, image)

        position = (720,520)
        cv2.putText(image, rdate, position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1) 
        cv2.imwrite("static/upload/"+fn, image)

    
        mycursor.execute("update bb_send_donor set status=3,rdate=%s where id=%s",(rdate,rid))
        mydb.commit()
        msg="ok"

    return render_template('hos_donorst.html',msg=msg,data=data,data2=data2,sid=sid)


@app.route('/donor_home', methods=['GET', 'POST'])
def donor_home():
    msg=""
    uname=""
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM bb_donor where donor=%s",(uname,))
    data = mycursor.fetchone()

    mycursor.execute("SELECT * FROM bb_send_donor d,bb_send s,bb_register h where d.sid=s.id && s.uname=h.uname && d.donor=%s order by d.id desc",(uname,))
    data2 = mycursor.fetchall()

    if act=="yes":
        rid=request.args.get("rid")
        mycursor.execute("update bb_send_donor set status=1 where id=%s",(rid,))
        mydb.commit()
        return redirect(url_for('donor_home'))

    if act=="no":
        rid=request.args.get("rid")
        mycursor.execute("update bb_send_donor set status=2 where id=%s",(rid,))
        mydb.commit()
        return redirect(url_for('donor_home'))
        
    return render_template('donor_home.html',data=data,act=act,data2=data2)

@app.route('/donor_info', methods=['GET', 'POST'])
def donor_info():
    msg=""
    uname=""
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM bb_donor where donor=%s",(uname,))
    data = mycursor.fetchone()

    mycursor.execute("SELECT * FROM bb_send_donor where donor=%s order by id desc",(uname,))
    data2 = mycursor.fetchall()

    return render_template('donor_info.html',data=data,act=act,data2=data2)

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
