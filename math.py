
import sys
import os.path


try:
    sys.argv[1]
except IndexError:
    print False
else:
    print True
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1]) as f:
            data = f.readlines()
    else:
        print "no"


print data



for i in range(0,len(data)):
    p=data[i].split()

    a = int(str(p[1]))

    b = int(str(p[2]))

    if p[0]=='MUL':
        print a*b
    elif p[0]=='ADD':
        print a+b
    elif p[0]=="DIV":
        if b==0:
            print 'impossible to divide by 0'
        else:
            print a/b
    elif p[0]=='SUB':
        print a-b


