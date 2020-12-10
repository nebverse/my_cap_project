n=int(input("Enter no. of the terms for the range:"))
print("Enter the nos for the list")
list1=[]
i=1
while i<=n:
    a=int(input("No. {}: ".format(i)))
    list1.append(a)
    i+=1

print("Input by you :\n{}".format(list1))

print("Positive nos. in the range:")
list2=[]

for j in list1:
     if j>=0:
         list2.append(j)

     else:
         pass
print(list2)
