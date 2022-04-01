#-*- coding:utf-8 -*-
import sys
import getopt 
import time
import re
import cx_Oracle
import telnetlib
from cx_Oracle import DatabaseError

pe = re.compile(r'^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$')

def getFileType(file_path):
	FileType = "utf-8"
	try:
		htmlf = open(file_path, 'r', encoding=FileType)
		htmlf.read()
	except UnicodeDecodeError:
		FileType = "gb2312"
	else:
		htmlf.close()
	return FileType
	
def Usage():
	print('''
	####################################################################
	#                                                                                      
	#                       Oracle Default User and Password Sc4nner  
	#                       By : Gavin
	#                       reBuild by NOVASEC  WINZERO 
	####################################################################
	Usage:
		python OracleDefault.py -t [target] 
	Option:
		-d [database] The Database which you Want to connect Oracl0. default(orcl).
		-p [port]	 Oracle service port . Default(1521)
		-f [userpwd file]     The user passwd dict file. default('oracle-userpwd-default.txt')
	--------------------------------------------------------------------
	Warn:
		target	 -->  Must be IP.example:192.168.1.x .
	--------------------------------------------------------------------
	''')
	sys.exit()

def oraclelogin(target,user,password,database,port):
	#print("[+] Trying Default User and Password (%s----->%s)" % (user,password))
	try:
		conn = cx_Oracle.connect(user,password,cx_Oracle.makedsn(target,port,database))
		conn.close()
		return (True,user,password)
	except Exception as e:
		#print(e)
		if "ORA-12505" in str(e) : 
			print('Errod SID or server_name!!! :',database)
			sys.exit()
			return (False,user,password)
		elif "ORA-01017" in str(e) : 
			#print('Error Password!!!')
			return (False,user,password)
		elif "ORA-28000" in str(e) : 
			print('The Account is Locked!!! : ',user)
			return (False,user,password)
		elif 'ORA-28009' in str(e) : 
			try:
				print('Test Oracle.SYSDBA Account: ',user)
				conn = cx_Oracle.connect(user,password,cx_Oracle.makedsn(target,port,database),cx_Oracle.SYSDBA)
				conn.close()
				return (True,user,password)
			except Exception as e:
				print(e)
				return (False,user,password)
		else:
			print(e)
			return (False,user,password)
def main():
	port = 1521
	database = 'orcl'
	userfile = 'default-oracle-userpwd.txt'
	try:
		opts,args = getopt.getopt(sys.argv[1:],"t: p: d: f:")
	except: 
		print(e)
		Usage()
	if len(opts) < 1:
		Usage()
	for o,a in opts:
		print(o,a)
		if o == "-t":
			target = a
		if o == "-p":
			port = int(a)
		if o == "-d":
			database = a 
		if o == "-f":
			userfile = a 
			
	if pe.match(target) == None:
		print("\r-------------------------------------------------")
		print("[!]Enter the target error,it Must be IP.")
		sys.exit()
	try:
		tn = telnetlib.Telnet()
		tn.open(target,port)
		tn.close()		
	except: 
		print(e)
		print("\r-------------------------------------------------")
		print("\r[!] Can not connect to the target!")
		tn.close()
		sys.exit()
	data =[]
	fileType = getFileType(userfile) 
	with open(userfile , mode='r' ,encoding=fileType ) as f:
		data= [ i.strip() for i in f.readlines()]
		data = list(set(data))
		#print(data)
	data_count = len(data)
	print("\r----------------------------------------------------")
	print("\r[+] The number of  dict is:%s" % data_count)
	print("\r----------------------------------------------------")
	resault = {}
	try:
		#创建开始时间戳
		start = time.perf_counter()
		for i in data:
			#print(i)
			user = i.split(':')[0]
			password = i.split(':')[1]
			flag = oraclelogin(target,user,password,database,port)
			if flag[0]:
				resault[flag[1]] = flag[2]
			data_count = data_count - 1	
			elapsed = (time.perf_counter() - start)
		if len(resault) != 0:
			print("\r-------------------------------------------------")
			print("\r[!] Good luck O(^.^)O")
			j = 1
			for i in resault:
				print("%2d: User and Password is (%s----->%s)" % (j,i,resault[i]))
				j+=1
			print("\r-------------------------------------------------")
		else :
			print("\r-------------------------------------------------")
			print("\r[!] Done,No Default Passwd Right %>_<%")
			print("\r-------------------------------------------------" )
		#print("\r[+] Time used: %s%s" % (elapsed,"sec"))
		#print("\r[+] Pless enter 'Ctrl + C' or hold 10 sec to exit")
		#time.sleep(10)
		#print("\r-------------------------------------------------")
		print("\r[+] Thank you ! Bye.")
		sys.exit()
	except KeyboardInterrupt as e:
		print(e)
		print("\r-------------------------------------------------")
		print("\r[!] Aborting...")
		print("\r[!] Exiting ... wait")
		sys.exit()
	except Exception as e:
		print(e)
		print("\r-------------------------------------------------")
		print("\r[+] Thank you ! Bye.")
		sys.exit()

if __name__ == "__main__":
	main()
