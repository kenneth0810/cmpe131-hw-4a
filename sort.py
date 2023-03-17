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