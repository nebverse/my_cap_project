# Fibonacci Series

def Fib(n):
    n1=0
    n2=1
    i=1
    l=[]
    if n<=0:
        print("Plz enter positive value")

    elif n==1:
        print("Series is as following:\n",n1)

    elif n>1:
        while i<=n:
            l.append(n1)
            n3=n1+n2
            n1=n2
            n2=n3
            i+=1
        print("Series is as following:\n",l)

if __name__== '__main__':
    n=int(input("Enter the number of terms for the series:"))
    Fib(n)
    con=True
    while con:
        a=input("Do you want to repeat(yes/no)? : ")
        if a=="yes":
            a=int(input("Enter new value for the no. of terms:"))
            Fib(a)

        elif a=="no":
            print("Program ended")
            con=False