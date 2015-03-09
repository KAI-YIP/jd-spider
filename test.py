#coding=utf-8
f=open('./test/手机_手机通讯_手机_id_price.txt','r',encoding='utf-8')
ID_list=[]
for line in f.readlines():
	line_clean=line.strip().split('///')
	ID_list.append(line_clean[1])
print (ID_list)


