#dict
d={'cc':22,'bb':11,'mm':'00'}
if('cc' in d):
 print(d['cc'])
print(d)
d['dd'] = 90
print(d)
d.pop('mm')
print(d)

def  appendL(d):
	d['ee']=99
appendL(d)
print(d)
#python迭代对象
for x in 'asdfg':
	print(x)

for value in enumerate([1,2,3]):
	print(value)

for i,value in enumerate([1,2,3]):
	print(i,value)

L1 = ['Hello','World',18,'Apple',None]

L2 = [s.lower() for s in L1 if isinstance(s,str) ]
print(L2)