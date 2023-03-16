def merge(list1, list2):
    if not list1:
        return list2
    elif not list2:
        return list1
    
    mergedList = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            mergedList.append(list1[i])
            i += 1
        else:
            mergedList.append(list2[j])
            j += 1
    
    mergedList += list1[i:] + list2[j:]
    return mergedList