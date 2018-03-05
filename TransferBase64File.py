#!/usr/bin/env python

import sys
import base64
import os

def transfor(inputFilePath):
    mylist=[]
    #if os.path.isfile(inputFilePath):
    #    return
    file = open(inputFilePath)
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break;
        for line in lines:
           temp = base64.b64decode(line)
           # print(temp)
           mylist.append(temp)

    return mylist

def getCurrentFileDir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def write(filePath, lists):
    fobj = open(filePath, 'w+')
    fobj.writelines(['%s%s'%(x, os.linesep) for x in lists])
    fobj.close()

if __name__=='__main__':
    inputfilePath = raw_input("input file path:")
    if inputfilePath=="":
       sys.exit(0) 
    lists =  transfor(inputfilePath)
    print(len(lists))
    curPath = getCurrentFileDir()
    print("current dir: "+  curPath)
    outputname = raw_input("output filename: ")
    if outputname == "":
        sys.exit(0)
    outpath = curPath + "/" + outputname
    write(outpath, lists)
