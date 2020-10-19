#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# coding=utf-8
#
import re
import subprocess
from io import StringIO
import multiprocessing
import time
import sys
import os
from datetime import datetime


def check_alive(ip):
	result = subprocess.call('ping -w 1000 -n 1 %s' %ip,stdout=subprocess.PIPE,shell=True)
	if result == 0:
		h = subprocess.getoutput('ping ' + ip)
		returnnum = h.split('平均 = ')[1]
		info = ('\033[32m%s\033[0m 能ping通，延迟平均值为：%s' %(ip,returnnum))
		print('\033[32m%s\033[0m 能ping通，延迟平均值为：%s' %(ip,returnnum))
		
		ipp = ip.replace('\n','')
		timee = datetime.now().strftime("%Y-%m-%d %H:%M:%S");
		timeet = datetime.now().strftime("%Y-%m-%d");
		
		# 读取目录下文件列表
		v_foleder='C:/Users/Administrator/Desktop/ping/'
		Vname_list=os.listdir(v_foleder)
		

		# 指定路径创建新文件夹
		file_path='C:/Users/Administrator/Desktop/ping/'+timeet

		if not os.path.exists(file_path): # 判断文件夹是否已经存在    
			os.mkdir(file_path)
			#print (file_path + ' 创建成功')
		#else:
			#print (file_path + ' 目录已存在')
		
		
		file = open('C:/Users/Administrator/Desktop/ping/'+timeet+'/'+ipp+'.txt','a');
		file.write(ipp+'------'+returnnum)
		file.write('------')
		file.write(timee)
		file.write('\n')
		file.close()
		#return info
	else:
		timee = datetime.now().strftime("%Y-%m-%d %H:%M:%S");
		timeet = datetime.now().strftime("%Y-%m-%d");
		ipp = ip.replace('\n','')
		
		# 读取目录下文件列表
		v_foleder='C:/Users/Administrator/Desktop/ping/'
		Vname_list=os.listdir(v_foleder)
		

		# 指定路径创建新文件夹
		file_path='C:/Users/Administrator/Desktop/ping/'+timeet

		if not os.path.exists(file_path): # 判断文件夹是否已经存在    
			os.mkdir(file_path)
			#print (file_path + ' 创建成功')
		#else:
			#print (file_path + ' 目录已存在')
		
		with open('C:/Users/Administrator/Desktop/ping/'+timeet+'/'+ipp+'.txt','a') as f:
			f.write(ipp)
			f.write('------')
			f.write('不通')
			f.write('------')
			f.write(timee)
			f.write('\n')
			f.close()
		with open('C:/Users/Administrator/Desktop/ping/notong.txt','a') as f:
			f.write(ipp)
			f.write('------')
			f.write('不通')
			f.write('------')
			f.write(timee)
			f.write('\n')
			f.close()
		info = ('\033[31m%s\033[0m ping 不通！' % ip)
		#return info
		print('\033[31m%s\033[0m ping 不通！' % ip)
	
	print("完成")
	print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"));

if __name__ == '__main__':
	while True:
		print("开始批量ping所有IP！")
		with open('C:/Users/Administrator/Desktop/ping/ip.txt', 'r') as f:      #ip.txt为本地文件记录所有需要检测连通性的ip
			for i in f:
				p = multiprocessing.Process(target=check_alive, args=(i,))
				p.start()
				
		print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"));
		time.sleep(300)
		

