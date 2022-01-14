# Oracle-Sid-Brute python3

Simple Oracle sid and user Brute Python Script

简单Oracle SID爆破及默认用户名爆破脚本

oracle-brute-sid.py 简单的Oracle SID爆破脚本 

oracle-brute-sid.txt 默认sid字典



实战记录：sid可能使用ora10、 orcl(默认)、 ris（系统名)等多种格式，一般是五位字符以下。



####################################################################

oracle-brute-userpwd.py 简单的Oracle默认口令爆破脚本 

oracle-userpwd-default.txt 默认用户名密码字典

参考：基于OracleDefault.py

####################################################################

#Oracle SID爆破脚本使用：

python3 oracle-brute-sid.py

λ python3 oracle-brute-sid.py -h

Usage:

        python OracleDefault.py -t [target]
        
        
Option:

        -f [sid file]    The sid dict file. default('oracle-brute-sid.txt')
        
        -p [port]        Oracle service port . Default(1521)
        
--------------------------------------------------------------------

λ python3 oracle-brute-sid.py -t 192.168.88.88

λ python3 oracle-brute-sid.py  -f oracle-brute-sid.txt -t 192.168.88.88

λ python3 oracle-brute-sid.py -p 1521 -f oracle-brute-sid.txt -t 192.168.88.88

####################################################################

#Oracle默认口令爆破脚本使用：

python3 oracle-brute-userpwd.py 

Usage:

        python OracleDefault.py -t [target]
        
Option:

        -d [database] The Database which you Want to connect Oracl0. default(orcl).
        
        -p [port]        Oracle service port . Default(1521)
        
        -f [userpwd file]     The user passwd dict file. default('oracle-userpwd-default.txt')

--------------------------------------------------------------------

λ python3 oracle-brute-userpwd.py  -t 192.168.88.88

λ python3 oracle-brute-userpwd.py  -t 192.168.88.88 -f oracle-userpwd-default.txt 

λ python3 oracle-brute-userpwd.py  -t 192.168.88.88 -p 1521 -f oracle-userpwd-default.txt  


####################################################################


报错记录:

DPI-1047: Cannot locate a 64-bit Oracle Client library: "The specified module could not be found". 

解决方案：

windows下需要将instantclient所在目录加入到PATH环境变量，或将脚本置于目录下运行

instantclient下载地址：（建议安装与服务器端Oracle版本相近的版本，本次测试使用19.8版本）

https://www.oracle.com/technetwork/database/database-technologies/instant-client/downloads/index.html




        
