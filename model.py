#-*- coding:utf-8 -*-

import sqlite3

def tno():
	st =[] 
	conn =sqlite3.connect("teacherDB.db")
	cur = conn.cursor()
	cur.execute( 'select tno from teacher')
	st = cur.fetchall()
	cur.close()
	cur.close()
	return st
def ntno(tn):
	st =[] 
	conn =sqlite3.connect("teacherDB.db")
	cur = conn.cursor()
	cur.execute('select tno from teacher where tname="%s" ' % tn)
	st = cur.fetchall()
	cur.close()
	cur.close()
	return st	
def result(form):
	st =[] 
	conn =sqlite3.connect("teacherDB.db")
	cur = conn.cursor()
	tno = form["tno"]#.decode('utf-8').encode('utf-8')
	menu = form["menu"]#.decode('utf-8').encode('utf-8')
	tname = form["tname"]#.decode('utf-8').encode('utf-8')
	tzhicheng = form["tzhicheng"]#.decode('utf-8').encode('utf-8')
	txueyuan = form["txueyuan"]#.decode('utf-8').encode('utf-8')
	tphone = form["tphone"]#.decode('utf-8').encode('utf-8')
	tbangongshi = form["tbangongshi"]#.decode('utf-8').encode('utf-8')
	temail = form["temail"]#.decode('utf-8').encode('utf-8')
	if "select" == menu :
		cur.execute( 'select * from teacher where tno="%s" ' % tno)
	elif "update" == menu:
		conn.execute( 'update teacher set tname="%s",tzhicheng="%s",\
		txueyuan="%s",tphone="%s",tbangongshi="%s",temail="%s" where \
		tno="%s" ' %(tname,tzhicheng,txueyuan,tphone,tbangongshi,temail,tno))
		conn.commit()
		cur.execute( 'select * from teacher where tno="%s" ' % tno)
	elif "delete" == menu:
		conn.execute('delete  from teacher where tno ="%s";' % tno )
		conn.commit()
		pass
	elif "insert" == menu:
		conn.execute('insert into teacher (tno,tname,tzhicheng,txueyuan,tphone,tbangongshi,temail) values ("%s","%s","%s","%s","%s","%s","%s")' % (tno,tname,tzhicheng,txueyuan,tphone,tbangongshi,temail))
		conn.commit()
		pass
	else:
		pass
	st = cur.fetchall()
	cur.close()
	cur.close()
	return st
	
	
# tno,tname,tzhicheng,txueyuan,tphone,tbangongshi,temail	

# tno CHAR(10) PRIMARY KEY,
# tname CHAR(20),
# tzhicheng CHAR(20),
# txueyuan CHAR(20),
# tphone CHAR(20),
# tbangongshi CHAR(20),
# temail CHAR(20)
 