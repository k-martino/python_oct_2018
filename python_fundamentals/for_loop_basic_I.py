# 1) Basic
for count in range(151):
    print(count)


# 2) Multiples of Five
for count in range(5,1000001,5):
    print(count)


# 3) Counting, the Dojo Way
for i in range(1,101,1):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)


# 4) Whoa. That Sucker's Huge
sum = 0
for i in range(0,500001,1):
    if i%2 != 0:
        sum += i
print(sum)


# 5) Countdown by Fours
for count in range(2018,0,-4):
    print(count)


# 6) Flexible Countdown
def flexible(loNum,hiNum,mult):
    for i in range(loNum,hiNum + 1,1):
        if i%mult == 0:
            print(i)
flexible(2,9,3)