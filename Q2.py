list=[]
for i in range(11):
    i = int(input("Enter your phone number one by one :"))
    list.append(i)
print(list)

def minNum(value):
    print(value)
min = list[0]
for i in list:
    if i < min:
        min = i
minNum(min)

def maxNum(value):
    print(value)
max = list[0]
for i in list:
    if i > max:
        max = i
maxNum(max)