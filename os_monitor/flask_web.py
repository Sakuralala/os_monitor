#encoding=utf-8

from flask import Flask,render_template
import MySQLdb as mysql
import json
import time

db=mysql.connect(user="root",passwd="qq343541",db="os_info",host="localhost")
db.autocommit(True)
cur=db.cursor()
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/mem')
def mem():
	sql='select * from mem_info'
	cur.execute(sql)
	xx={'usage':[],'time':[],'free':[],'used':[]}
	for i in cur.fetchall():
		xx['usage'].append(i[0])
		xx['free'].append(i[1]/1024/1024)
		xx['used'].append(i[2]/1024/1024)
		xx['time'].append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i[3])))
	return json.dumps(xx)

@app.route('/cpu')
def cpu():
	sql='select * from cpu_info'
	cur.execute(sql)
	xx={'usage':[],'time':[],'user_time':[],'sys_time':[],'idle_time':[]}
	for i in cur.fetchall():
		xx['usage'].append(i[0])
		xx['user_time'].append(i[1])
		xx['sys_time'].append(i[2])
		xx['idle_time'].append(i[3])
		xx['time'].append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i[4])))
	return json.dumps(xx)

@app.route('/disk')
def disk():
	sql='select * from disk_usage'
	cur.execute(sql)
	xx={'usage':[],'time':[]}
	for i in cur.fetchall():
		xx['usage'].append(i[0])
		xx['time'].append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i[1])))
	return json.dumps(xx)

@app.route('/net')
def net():
	sql='select * from net_info'
	cur.execute(sql)
	xx={'send_package':[],'recv_package':[],'time':[]}
	for i in cur.fetchall():
		xx['send_package'].append(i[0])
		xx['recv_package'].append(i[1])
		xx['time'].append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i[2])))
	return json.dumps(xx)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8889,debug=True)

