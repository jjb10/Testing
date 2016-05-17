import os.path

if os.path.isfile('C:\Users\Nafora\PycharmProjects\stockfighter\gaby.txt'):
    with open('C:\Users\Nafora\PycharmProjects\stockfighter\gaby.txt') as f:
        data = f.read()
else:
    print "no"


print data


for i in range(0,len(data)):
    p=data.split()
a=len(p)
g=[]
for j in range(0,len(p)):
    if '%' in p[j] or '$' in p[j]:
        g.append(p[j])

b=len(g)
print a-b

