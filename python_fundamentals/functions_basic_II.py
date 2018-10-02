# 1) Countdown
def countdown(num):
    arr = []
    for i in range(num,-1,-1):
        arr.append(i)
    return arr

# 2) Print and Return
def printReturn(arr):
    print(arr[0])
    return(arr[1])

# 3) First Plus Length
def firstPlusLength(arr):
    sum = arr[0] + len(arr)
    return sum

# 4) Values Greater than Second
def greaterThan2nd(arr):
    if len(arr) == 1:
        return False
    else:
        newArr = []
        for element in arr:
            if element > arr[1]:
                newArr.append(element)
        print(len(newArr))
        return newArr

# 5) This Length, That Value
def lengthAndValue(size, value):
    list = []
    for _ in range(size):
        list.append(value)
    return list