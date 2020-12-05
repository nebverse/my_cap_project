print("Enter Filename")
f= str(input())
list=f.split(".")


if (list[1]=="py"):
    print("The extension of the file is of python")
elif (list[1]=="txt"):
    print("The extension of the file is of text")
elif (list[1]=="png"):
    print("The extension of the file is of image")
elif (list[1]=="kv"):
    print("The extension of the file is of kivy")

#