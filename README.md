# 准确爆破 Oracle 数据库



## 依赖

```
程序依赖instantclient

下载地址：
https://www.oracle.com/technetwork/database/database-technologies/instant-client/downloads/index.html
（建议安装与服务器端Oracle版本相近的版本或更高版本，测试使用19.8版本,依赖文件75MB，无法直接上传）

报错记录:
DPI-1047: Cannot locate a 64-bit Oracle Client library: "The specified module could not be found". 

解决方案：
windows下需要将instantclient所在目录加入到PATH环境变量，或将脚本置于目录下运行
```

## Brute-Oracle-Sid.py  Oracle SID爆破Demo 

```
λ python3 brute-oracle-sid.py -h

Usage:
	python brute-oracle-sid.py -t [target]

Option:
	-f [sid file]    The sid dict file. default('oracle-brute-sid.txt')
	-p [port]        Oracle service port . Default(1521)
	
λ python3 oracle-brute-sid.py -t 192.168.88.88
λ python3 oracle-brute-sid.py -f brute-oracle-sid.txt -t 192.168.88.88
λ python3 oracle-brute-sid.py -p 1521 -f oracle-brute-sid.txt -t 192.168.88.88

sid 可能使用ora10、 orcl(默认)、 ris（系统名)等多种格式, 一般是五位字符以下。
```

## oracle-brute-userpwd.py  Oracle默认口令爆破Demo

```
python3 oracle-brute-userpwd.py 

Usage:
        python OracleDefault.py -t [target]
        
Option:
        -d [database] The Database which you Want to connect Oracl0. default(orcl).
        -p [port]        Oracle service port . Default(1521)
        -f [userpwd file]     The user passwd dict file. default('oracle-userpwd-default.txt')

python3 oracle-brute-userpwd.py  -t 192.168.88.88
python3 oracle-brute-userpwd.py  -t 192.168.88.88 -f default-oracle-userpwd.txt 
python3 oracle-brute-userpwd.py  -t 192.168.88.88 -p 1521 -f oracle-userpwd-default.txt  
```




​        
