# Positive return values

def Pos(list):
    print("INPUT=",list)
    l2=[]
    for i in list:
        if i>=0:
            l2.append(i)
    print("These are the positive nos. from the range given:\nOUTPUT=",l2)

if __name__== '__main__':
    n=int(input("Enter no. of the terms for the list:"))
    i=1
    l1=[]
    while i<=n:
        a=float(input("Enter no. {} : ".format(i)))
        l1.append(a)
        i+=1
    Pos(l1)