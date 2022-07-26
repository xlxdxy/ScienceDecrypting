import os
path = os.getcwd()

fileList = os.listdir(path)

for fileName in fileList:
    oldName = path + os.sep + fileName
    if '.dec' in oldName:
        newName = oldName.replace('.dec', '')
        os.rename(oldName, newName)