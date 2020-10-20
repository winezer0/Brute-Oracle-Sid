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
	##################################################
	#                                                                                                                      #
	#                      Oracle Default User and Password Sc4nner                   #
	#                                                  By : Gavin                                                  #
	#                                     reBuild by WINZERO                                            #
	##################################################
	Usage:
		python OracleDefault.py -t [target] 
	Option:
		-f  [sid file]     The Database dict file
		-p [port]	 Oracle service port,Default number is 1521.
	--------------------------------------------------------------------
	Warn:
		target	 -->  Must be IP.example:192.168.1.x .
	--------------------------------------------------------------------
	''')
	sys.exit()

def oraclelogin(target,user,password,database,port):
	#print("[+] Trying  %s %s " % (user,database))
	try:
		conn = cx_Oracle.connect(user,password,cx_Oracle.makedsn(target,port,database))
		conn.close()
		#print('*** SID or server_name Be Found!!!')
		return (True,database)
	except Exception as e:
		#print(e)
		if "ORA-12505" in str(e) : 
			#print('*** Errod SID or server_name!!!')
			return (False,database)
		if "ORA-12504" in str(e) : 
			#print('*** Errod SID or server_name!!!')
			return (False,database)
		if "ORA-12514" in str(e) : 
			#print('*** Errod SID or server_name!!!')
			return (False,database)
		else:
			print(e)
			print('*** SID or server_name  Like Be Found!!!')
			return (True,database)
			
def main():
	port = 1521
	database = 'orcl'
	sidfile = 'oracle-brute-sid.txt'
	user ='sys' #任意
	password = 'asdfghjkl123' #任意
	try:
		opts,args = getopt.getopt(sys.argv[1:],"t: p: f: ")
	except: 
		#print(e)
		Usage()
	if len(opts) < 1:
		Usage()
	for o,a in opts:
		if o == "-t":
			target = a
		if o == "-p":
			port = int(a)
		if o == "-f":
			sidfile = a 
			
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
	fileType = getFileType(sidfile) 
	with open(sidfile , mode='r' ,encoding=fileType ) as f:
		data= [ i.strip() for i in f.readlines()]
		data = list(set(data))
		print(data)
	data_count = len(data)
	print("\r----------------------------------------------------")
	print("\r[+] The number of Default dict is:%s" % data_count)
	print("\r-------------------------------------------------")
	resault = []
	try:
		#创建开始时间戳
		start = time.perf_counter()
		for i in data:
			database = i.split(',')[0]
			flag = oraclelogin(target,user,password,database,port)
			print(flag)
			if flag[0] == True:
				resault.append(flag[1])
			data_count = data_count - 1	
		if len(resault) != 0:
			print("\r-------------------------------------------------")
			print(resault)
			print("\r-------------------------------------------------")
		else :
			print("\r[!] Done,No Sid Right %>_<%")
			print("\r-------------------------------------------------")
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
