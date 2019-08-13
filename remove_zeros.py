import os
def split(word):
    return [char for char in word]
listData = os.listdir("data") #data = source directory
for i in range (len(listData)):
    newName = ""
    listOldName = split(listData[i])
    firstZero = True
    for x in range (len(listOldName)):
        if listOldName[x] == "0" and firstZero == True:
            newName = newName + ""
        if listOldName[x] != "0":
            newName = newName + listOldName[x]
            firstZero = False
        if listOldName[x] == "0" and firstZero == False:
            newName = newName + listOldName[x]
    print (listData[i] + " - " +newName)
    os.rename("data/"+listData[i], "newData/"+newName) #newData = destination directory
