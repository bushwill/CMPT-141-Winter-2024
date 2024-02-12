from os.path import exists
from createNewFileFunction import createNewFile

def updateFile(filename):
    if exists(filename):
        createNewFile(filename)
        return True
    else:
        return False