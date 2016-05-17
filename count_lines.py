import sys
import os.path


try:
      sys.argv[1]
except IndexError:
      print False
else:
      #print True
      if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1]) as f:
                  print len(f.readlines())
      else:
            print "the file does not exist"
