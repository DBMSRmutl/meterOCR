import os
import sys

foldername = 'results'
for filename in os.listdir('/home/ubuntu/pyview/Test/pics'):
        #print  filename
   	fullFilename = ('/home/ubuntu/pyview/Test/pics/'+filename)
    	#print fullFilename
	os.system('python v1-3-arg.py '+fullFilename+' '+foldername+'/'+filename)
    	
	sys.stdin.read(1)
        #print output
    
