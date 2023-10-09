num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
 #question 01
for num in num_list:
    print(num)

#question 02
for num in num_list:
    if(num > 45):
        print(num)

#question 03
for num in num_list:
    if(num > 45):
        print("over 45:",num)
    else:
        print("under 45",num)

#question 04
for index, num in enumerate(num_list):
    if(num == 36):
        print("number found at position",index)

#question 05,6,7,8
for index, num in enumerate(num_list):
    if(num == 36):
        count += 1
        print("number found at position",index)
        break
    print("total value of count=",count)