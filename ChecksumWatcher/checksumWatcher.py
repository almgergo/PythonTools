## expected cmd arguments: 1 - file to check, 2 - lastWriteTime

import hashlib
import sys
import os
from shutil import copyfile
import time
import datetime

TIME_SHIFT = 7200 ## python's file modified time has a 2 hour difference to windows event time, this is the correction
MODIFICATION_TIME_TOLERANCE = 2 ## if file is modified withing this many seconds, nothing happens


#print ("###################")
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def checkSum(fname, lastWriteTime):	
	fnameShort = fname[fname.index("\\classes\\"):]
	basePath = fname[:fname.index("target\\")]

	cachedFile = basePath + "cache" + fnameShort
	lastAccessTime = os.path.getmtime(cachedFile) + TIME_SHIFT
	if (lastWriteTime - lastAccessTime < MODIFICATION_TIME_TOLERANCE):
		return

	md5Original = md5(fname)
	
	cachedFilePath = cachedFile[:cachedFile.rindex("\\", 1)]
	try:
		md5Cache = md5(cachedFile)
	
		if (md5Cache != md5Original):
			copyfile(fname, cachedFile)
			print("Cache refreshed")
		else:
			print("Cache is up to date")
	except OSError as e:
		if not os.path.exists(cachedFilePath):
			print("Creating path to cache")
			os.makedirs(cachedFilePath)
		copyfile(fname, cachedFile)
		print("Cache created")
	print("Done: " + fnameShort)
	
	
def checkSum(fname):	
	fnameShort = fname[fname.index('\\classes\\'):]
	basePath = fname[:fname.index('target\\')]

	cachedFile = basePath + "cache" + fnameShort

	md5Original = md5(fname)
	
	cachedFilePath = cachedFile[:cachedFile.rindex("\\", 1)]
	try:
		md5Cache = md5(cachedFile)
	
		if (md5Cache != md5Original):
			copyfile(fname, cachedFile)
			print("Cache refreshed for: " + fname)
		#else:
			#print("Cache is up to date")
	except OSError as e:
		if not os.path.exists(cachedFilePath):
			#print("Creating path to cache")
			os.makedirs(cachedFilePath)
		copyfile(fname, cachedFile)
		#print("Cache created")
	#print("Done: " + fnameShort)

