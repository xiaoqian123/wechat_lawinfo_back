#import sys
import os

#sys.path.append('../')
from myapp  import app
from flask import request
#import ..app
import re
from test import *
from myapp.controller.law_oj import law_oj
import json
import pydraco
import urllib

@app.route('/test', methods=['POST', 'GET'])
def select_law():
    if request.method =='GET':
        lpkeyword  = request.values.get('lpKeyword')
        backnum = request.values.get('backnum')
        loadnum = request.values.get('loadnum')

        conn = pydraco.connect(host="172.16.20.18", port=5432, user='crate')
        cursor = conn.cursor()
        cursor.execute('select title, issuing_authority,publish_time,_id from databox.bank_hzyh_legal order by publish_time desc limit '+backnum+' offset '+loadnum )
        
        rows  = cursor.fetchall()
        data_list = []
        for row in rows:
           data_list.append(list(row))
        jstr = json.dumps(data_list)
        print jstr
        return jstr 

@app.route('/selectContent', methods=['POST', 'GET'])
def look_content():
    if request.method=='GET':
        dataid = request.args.get('dataid')
        print '--------------',dataid
        
        conn = pydraco.connect(host="172.16.20.18", port=5432, user='crate')
        cursor = conn.cursor()
        
        #print sql
        sql = 'select title, issuing_authority, publish_time, content, content_path from databox.bank_hzyh_legal where _id=\''+dataid+'\''
        cursor.execute(sql);
        rows  = cursor.fetchone()
        
        content_name = []
        print rows
        content_name = rows[4].split("/")
        name = content_name[len(content_name)-1]
        print name
        print content_name
        file_path='/tmp/myproject/legal_txt/'+name
        if os.path.exists(file_path):
            file_object = open(file_path)
            file_text = file_object.readlines()
            file_object.close()
            file_length = len(file_text)-1

            for i in range(file_length,0,-1):
                if(file_text[i].isspace()):
                    del file_text[i]
       # file_length = len(file_text)-1
       # for index in range(file_length,0,-1):
       #     if(file_text[index-1].strip()==file_text[index].strip()):
       #         del file_text[index]
        else:
            return "";
        rows[4] = file_text
        jstr = json.dumps(rows)
        print jstr
        return jstr
        #else:
        #    return ''
       # #return '123'




@app.route('/lookup', methods=['POST', 'GET'])
def look_up():
    if request.method == 'POST':
        title = request.form['title']
        issuing_authority = request.form['issuing_authority']
        section1 = request.form['section1']
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        backnum = request.values.get('backnum')
        loadnum = request.values.get('loadnum')

        sql = 'select title, issuing_authority,publish_time, _id from databox.bank_hzyh_legal where'
        print 'tile:',title,'iss:',issuing_authority,'sec:',section1,'time:',date_start,date_end

        if title.strip():
            sql = sql+' title LIKE \'%'+title +'%\' AND'
        if issuing_authority != '0':
            sql = sql+' issuing_authority=\''+issuing_authority+'\' AND'
        if section1 != '0':
            sql = sql+' section1=\''+section1+'\' AND'
        if date_start and date_end:
            sql = sql+' publish_time between \''+date_start+'\' AND'+' \''+date_end+'\' AND'
        sql = sql[0:-4]
        sql = sql+' order by publish_time desc limit '+backnum+' offset '+loadnum
        print sql 
         
        conn = pydraco.connect(host="172.16.20.18", port=5432, user='crate')
        cursor = conn.cursor()
        cursor.execute(sql)
        rows  = cursor.fetchall()
        data_list = []
        for row in rows:
            data_list.append(list(row))
        jstr = json.dumps(data_list)
        return jstr
        



@app.route('/getsection', methods=['POST', 'GET'])
def get_section():
    if request.method == 'GET':
        isTrue = request.values.get('isTrue')
        if isTrue:
            sql1 = 'select DISTINCT(section1) from databox.bank_hzyh_legal'
            sql2 = 'select DISTINCT(issuing_authority) from databox.bank_hzyh_legal'
        conn = pydraco.connect(host="172.16.20.18", port=5432, user='crate')
        cursor = conn.cursor()
        cursor.execute(sql1)
        rows_1  = cursor.fetchall()

        data_list = []
        data_list.append([])
        for row in rows_1:
            data_list[0].append(list(row))

        cursor.execute(sql2) 
        rows_2  = cursor.fetchall()
            
        data_list.append([])
        for row in rows_2:
            data_list[1].append(list(row))
        jstr1 = json.dumps(data_list)
        return jstr1



