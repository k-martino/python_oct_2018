#1 Biggie Size
def makeItBig(arr):
    length = 0
    for _ in arr:
        length += 1
    for i in range(length):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

print(makeItBig([-1,3,5,-5]))


#2 Count Positives
def countPositives(arr):
    length = 0
    countPos = 0
    for _ in arr:
        length += 1
    for i in range(length):
        if arr[i] > 0:
            countPos += 1
    arr[length-1] = countPos
    return arr

print(countPositives([-1,1,1,1]))


#3 SumTotal
def sumTotal(arr):
    sum = 0
    for element in arr:
        sum += element
    return sum

print(sumTotal([1,2,3,4]))


#4 Average
def average(arr):
    sum = 0
    length = 0
    for _ in arr:
        length += 1
    for element in arr:
        sum += element
    avg = sum / length
    return avg

print(average([1,2,3,4]))


#5 Length
def length(arr):
    length = 0
    for _ in arr:
        length += 1
    return length

print(length([1,2,3,4]))


#6 Minimum
def minimum(arr):
    length = 0
    for _ in arr:
        length += 1
    if length == 0:
        return False
    else:
        min = arr[0]
        for i in range(1,length):
            if arr[i] < min:
                min = arr[i]
    return min

print(minimum([-1,-2,-3,-4]))


#7 Maximum
def maximum(arr):
    length = 0
    for _ in arr:
        length += 1
    if length == 0:
        return False
    else:
        max = arr[0]
        for i in range(1,length):
            if arr[i] > max:
                max = arr[i]
    return max

print(maximum([-1,-2,-3,-4]))


#8 UltimateAnalyze
def ultimateAnalyze(arr):
    return dict(
        sumTotal = sumTotal(arr),
        average = average(arr),
        minimum = minimum(arr),
        maximum = maximum(arr),
        length = length(arr)
        )

print(ultimateAnalyze([4,5,6,7,8,9,10,-1]))


#9 ReverseList
def reverse(arr):
    if len(arr) % 2 == 0:
        half = int(len(arr) / 2) + 1
    else:
        half = int(len(arr) / 2)
    for i in range(half):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    return arr

print(reverse([1, 2, 3, 4, 5]))