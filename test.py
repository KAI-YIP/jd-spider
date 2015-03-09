#coding=utf-8
f=open('./test/手机_手机通讯_手机_id_price.txt','r',encoding='utf-8')
ID_list=[]
for line in f.readlines():
	line_clean=line.strip().split('///')
	ID_list.append(line_clean[1])
for id in ID_list:
	url="club.jd.com/review/"+str(id)+"-0-1-0.html"
	print (url)
	break


