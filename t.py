l = [{'Jnana Sindhu Swadhar Greh': ['+91 98456 35966', 1323.4824377619102]}, {'Vatsalya Seva Trust': ['+91 94808 04867', 16949.393566835377]}, {'Pragathi Pura Seva Trust': ['+91 91080 45020', 24486.442721102827]}]

for Ngo in l:
	print(list(Ngo.keys())) 
	print(list(Ngo.values())[0][0]) 
	print(list(Ngo.values())[0][1])

k = []
v = []
for Ngo in l:
	k.append(list(Ngo.keys()))
	v.append(list((Ngo.values()))[0][0])

for i in range(len(l)):
	print(str(k[i][0])+" : "+str(v[i]))
