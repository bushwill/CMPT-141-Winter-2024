# This function utilizes the createNewFile function to update an existing file
# Important to note that if the file does not exist, this function returns false. 
# This function extends the functionality of createNewFile to check a file's existence
# and not operate on nonexistent files.

from os.path import exists
from createNewFileFunction import createNewFile

def updateFile(filename):
    if exists(filename):
        createNewFile(filename)
        return True
    else:
        return False