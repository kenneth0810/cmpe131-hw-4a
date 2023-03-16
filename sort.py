def sort_dictionary(myDict):
    keys = []
    myList = []
    for key in myDict.keys():
        keys.append(key)

    while(myDict):
        smallest = 0
        i = 0
        size = len(myDict)
        while i < size:
            if myDict[keys[i]][1] < myDict[keys[smallest]][1]:
                smallest = i
            else:
                i += 1
        myList.append((keys[smallest], myDict[keys[smallest]][0]))
        myDict.pop(keys[smallest])
        keys.pop(smallest)
    return myList

myDict = {'Tom': (5464512, 19), 
        'Sara' : (5446987, 32),
        'Mary' : (1557896, 20),
        'Kerry' : (12345263, 22)}
print(sort_dictionary(myDict))