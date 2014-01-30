import os
import os.path as path
import pygit2
import shutil
import random


studentNumbers = open("numbers")
parsedNumbers = open("parsedNumbers","w")
SERVER_PATH = "rw244-2013@eniac.cs.sun.ac.za:simpl-"
TAG = "scanner"
for i in studentNumbers:
    currentSet = i.split()
    for j in currentSet:
        parsedNumbers.write(j + ":url:" + SERVER_PATH + j + ":_:" + TAG+"\n")

