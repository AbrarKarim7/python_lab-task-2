list=[]

for i in range(11):
    i = int(input("Enter your phone number one by one :"))
    list.append(i)
print("Before sorting in ascending order : ",list)

for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            temp = list[j+1]
            list[j+1]=list[j]
            list[j]=temp
print("After sorting in ascending order : ",list)
