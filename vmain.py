import os
import sys
import subprocess

foldername = 'results'
for filename in os.listdir('/home/ubuntu/pyview/Test/pics'):
        #print  filename
   	fullFilename = (u'/home/ubuntu/pyview/Test/pics/'+filename)

	#create new path for results
	pathForEachResult = foldername+'/'+filename

	print  'pathForEachResult = '+ pathForEachResult
    	#print fullFilename
	#qx = os.system('python v1-3-arg.py '+fullFilename+' '+pathForEachResult)
	qx = os.system('python v1-3-arg.py fullFilename pathForEachResult')
	#result = subprocess.check_output(os.system('python v1-3-arg.py '+fullFilename+' '+pathForEachResult), shell=True)
	#print 'qx ='+result
	

	#upload to google drive
	# /results/...
	#mainResultDirectory = '0B-VyANMiyv0HUzJhTUFKdTZHRWc'
	#os.system('python /home/ubuntu//uploadToGDrive.py ')
    	
	#sys.stdin.read(1)
        #print output
    
