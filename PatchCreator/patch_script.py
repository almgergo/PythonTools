# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:05:01 2017

@author: almge
"""
CONTENT_SIZE= 3
PATCH_LOCATION = 'p:\\Collection.ING\\DEV\\database\\oracle\\upgrade\\'
VERSION = '1.0.0\\'
PATCHLIST = 'patchlist.reg'
PATCH_COMMENT = '-- @PATCHCOMMENT =\''
PATCH_COMMENT_ENDING = '\'\n'
EXPECTED_TIME = '-- @EXPECTEDEXECTIME =\'< 1 sec\'\n\n'

print ('enter')

import os
print('imported os')
from tkinter import *
print('imported tkinter')
import tkinter.scrolledtext as tkst

print('imported all')

def getPatchNumber( file_object ):
    for line in file_object:
        pass
        last = line         
    parts = re.split('[ \t\n]+',last)
    out = str(int(parts[1])+1)
    for i in range (0,4-len(out)):
        out = '0' + out
    return out

def makeentry(parent, caption, position, width=None):
    content = StringVar()
    #content.set(caption)
    Label(parent, text=caption).pack(side=position)
    entry = Entry(parent, textvariable=content)
    if width:
        entry.config(width=width)
    entry.pack(side=position)
    return content    

def appendAllocatePatch():
    file_object = open('M:\\COLLECTION_BASEL_POOL\\PROJECTS_COLLECTION\\ING\\TR\\allocatepatch.txt','r+')
    patchNumber = getPatchNumber(file_object)
    finalText = "\n" + contents[0].get() + "\t" + patchNumber + "\t" + os.getlogin() + "\t" + contents[1].get() + "\t" + contents[2].get()
    file_object.write(finalText)
    file_object.close()
    return patchNumber

def createPatchFile(patchName):
    patchFile = open(PATCH_LOCATION + patchName,'w')
    patchFile.write(PATCH_COMMENT + contents[3].get() + PATCH_COMMENT_ENDING)
    patchFile.write(EXPECTED_TIME)
    patchFile.write(sqlBox.get(0.0,END))
    patchFile.close()

def editPatchlistReg(patchName):
    patchList = open(PATCH_LOCATION + VERSION + PATCHLIST,'a')
    patchList.write('\n@@' + patchName)
    patchList.close()
    

def callback():
    patchNumber = appendAllocatePatch()
    patchName = patchNumber + "_" + contents[1].get() + "." + contents[2].get() + ".sql"
    createPatchFile(patchName)
    editPatchlistReg(patchName)
    print (patchName )
    
import win32clipboard

# get clipboard data
def getClipboardText():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

print ('master')
# MASTER
master = Tk()
master.title( 'Sexy patchING generator')

print ('info')
# INFO
captions=['Environment','Table','Action']
contents = []
for i in range(0,CONTENT_SIZE):
    contents.append( makeentry(master,captions[i],'top',100))
    
print ('jira')
# JIRA
contents.append(makeentry(master,'JIRA','top',100))

print ('sql')
# SQL
Label(master, text='SQL').pack(side='top')
sqlBox = tkst.ScrolledText(master)
sqlBox.pack(expand=1,side='top')
sqlBox.config(width=100,height=10)

print ('button')
#BUTTON
b = Button(master, text="get", width=10, command=callback)
b.pack()

print ('end')
master.mainloop()
print ('rip')
