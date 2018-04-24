#encoding=utf-8 
import psutil
import time
import MySQLdb as mysql

db=mysql.connect(user="root",passwd="qq343541",db="os_info",host="localhost")
db.autocommit(True)
cur=db.cursor()

def get_cpu_info():
	'''
	desc:return cpu usage.
	'''
	usage=psutil.cpu_percent(interval=1)
	times=psutil.cpu_times()
	t=int(time.time())
	sql='insert into cpu_info (cpu_usage,user_time,sys_time,idle_time,time) value (%s,%s,%s,%s,%s)'%(usage,times.user,times.system,times.idle,t)
	cur.execute(sql)

def get_mem_info():
	'''
	desc:return system memory swap memory usage info.
	'''
	ret=psutil.virtual_memory()
	t=int(time.time())
	sql='insert into mem_info (mem_usage,mem_free,mem_used,time) value (%s,%s,%s,%s)'%(ret.percent,ret.free,ret.used,t)
	cur.execute(sql)

def get_disk_usage():
	'''
	desc:return disk usage.
	'''
	ret=psutil.disk_usage('/')
	t=int(time.time())
	sql='insert into disk_usage (disk_usage,time) value (%s,%s)'%(ret.percent,t)
	cur.execute(sql)

def get_net_io_counters():
	'''
	desc:return net usage info.
	'''
	ret=psutil.net_io_counters()
	t=int(time.time())
	sql='insert into net_info (send_package,recv_package,time) value (%s,%s,%s)'%(ret.packets_sent,ret.packets_recv,t)
	cur.execute(sql)



if __name__=='__main__':
	while True:
		get_mem_info()
		get_disk_usage()
		get_net_io_counters()
		get_cpu_info()
		time.sleep(1)
	
