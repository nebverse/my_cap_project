import operator
def freq(str1):
    dic={}
    for i in str1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    sorted_d = (sorted(dic.items(), key=operator.itemgetter(1), reverse=True))


    print("frequency of each letter in {} is as following".format(str1))

    for j in sorted_d:
        print(j)

a=str(input("Enter the string:"))
freq(a)