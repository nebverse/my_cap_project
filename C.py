# fibonacci series

print("Enter no of terms:")
n=int(input())
n1=0
n2=1
i=1
list1=[]

if n<=0:
    print("Give positive no. of terms or greater than 0")


elif n==1:
    print("Fibonacci Series for 1 term:\n")
    print(n1)

else:
    print("Fibonacci Series for {} term:\n".format(n))
    while i<=n:
        list1.append(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        i+=1
    print(list1)