def furDistance (list1):
    lowest = highest = list1[0]
    for i in list1:
        if i<lowest:
            lowest = i
        if i> highest:
            highest = i

    return highest-lowest

list2 = [1,2,3,4,5,5,6,7,78,8]
print(furDistance(list2))