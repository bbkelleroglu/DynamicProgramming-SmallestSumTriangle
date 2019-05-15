numbersList = [2, 5, 4, 7, 4, 1, 8, 2, 9, 6, 11, 3, 8, 8, 6]
myList = []
first = 0
lastIndex = 1
last = 1
while last <= len(numbersList):
    myList.append(numbersList[first:last])
    first = last
    lastIndex = lastIndex + 1
    last = last + lastIndex

sum = 0
myArr = []
i=0
while len(myList) is not 1:
    if len(myList) == 2:
        sum = min(myList[-1]) + myList[0][0]
    if myList[-2][-1] + myList[-1][-1] < myList[-2][-1] + myList[-1][-2]:
        myList[-2][-1] = myList[-2][-1] + myList[-1][-1]
    else:
        myList[-2][-1] = myList[-2][-1] + myList[-1][-2]
    myArr.insert(0, myList[-2][-1])

    del myList[-1][-1]
    del myList[-2][-1]
    if len(myList[-2]) == 0:
        myList[-1] = myArr
        myArr = []
        del myList[-2]
        i += 1
        print("Step {}:".format(i),myList)

print ("Smallest Sum :",sum)
