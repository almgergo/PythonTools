import sys
import checksumWatcher
	
## expected cmd arguments: 1 - file to check, 2 - lastWriteTime
checksumWatcher.checkSum(sys.argv[1], float(sys.argv[2]))