# coding: utf-8

import socket,urllib,json,sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_computer(info):
	key='56338ba412c64aa2bc65dc1c48344f23'
	api='http://www.tuling123.com/openapi/api?key='+key+'&info='+info

	response=urllib.urlopen(api).read()
	dict_json=json.loads(response)
	print dict_json
	return '机器人:'.decode('utf-8')+dict_json['text']

host=socket.gethostbyname(socket.gethostname())
print host
port=8888

s=socket.socket()
s.bind((host,port))
s.listen(1)
while True:
	clnt,addr=s.accept()
	print 'client address:',addr

	while True:
		data=clnt.recv(1024)
		print data
		if not data: sys.exit()
		print 'going to: ',data
		result=get_computer(data)
		if len(result)==0: result='EXD'
		clnt.sendall(result)
clnt.close()