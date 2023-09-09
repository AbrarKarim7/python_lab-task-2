list=[]

for i in range(11):
    i = int(input("Enter your phone number one by one :"))
    list.append(i)
print(list)

evenList=[]
oddList=[]
for i in list:
    if i%2==0:
        evenList.append(i)
    else:
        oddList.append(i)

print("Even numbers in the list are : ",evenList)
print("Odd numbers in the list are : ",oddList)