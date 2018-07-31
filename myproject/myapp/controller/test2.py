#import json
#from myapp.controller import JSONObject 
#from myapp.controller.JSt import *

#s = '{"name": "ACME", "shares": 50, "price": 490.1}'
#data = json.loads(s, object_hook=JSt)
#print data.name

fp = open('test.txt', 'w')
fp.write('host')
fp.write('\r')
fp.write('cpu')
fp.write('\n')
fp.write('mem')
fp.close()
print 'write finish!l'

fp = open('test.txt', 'r')
lines = fp.readlines()
print lines
fp1 = open('test1.text','w')
fp1.write(str(lines))
fp.close()
fp1.close()
