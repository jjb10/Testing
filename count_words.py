import os.path
import sys

try:
    sys.argv[1]
except IndexError:
    print False
else:

    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1]) as f:
            data = f.read()
    else:
        print "the file does not exist"


# print data



splitteddata=data.split()
length_of_spillteddata=len(splitteddata)
g=[]
for j in range(0,length_of_spillteddata):
    if '%' in splitteddata[j] or '$' in splitteddata[j]:
        g.append(splitteddata[j])

length_of_g=len(g)
print length_of_spillteddata-length_of_g

