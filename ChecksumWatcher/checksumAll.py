import checksumWatcher
import os
import sys

## expected cmd arguments: 1 - directory to check files in
rootdir = sys.argv[1]

print ("\r\n#### Refreshing caches... ####")
for subdir, dirs, files in os.walk(rootdir):	
	#print(subdir)
	#print(dirs)
	for file in files:
		fullFileName = os.path.join(subdir,file)
		#print ("#### " + fullFileName + " ####") 
		checksumWatcher.checkSum(fullFileName)