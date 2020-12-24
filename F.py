# SCHOOL AMINISTRATION PROGRAM

import csv
def write_in_csv(info):
    with open("student_info.csv",'a', newline='') as csv_file:
        write=csv.writer(csv_file)

        if csv_file.tell() == 0:
            write.writerow(["NAME","AGE","CONTACT NO.","E-MAIL"])
        write.writerow(info)


if __name__== '__main__':
    condition =True
    i=1

    while (condition):
        a=str(input("Enter name of student {} : ".format(i)))
        b=int(input("Enter age of student {} : ".format(i)))
        c=int(input("Enter contact of student {} : ".format(i)))
        d=str(input("Enter email of student {} : ".format(i)))

        l=[a,b,c,d]
        print("Information of student no. {} is\nName: {}\nAge: {}\nContact No.: {}\nE-Mail: {}".format(i,a,b,c,d))

        choice=str(input("Is the entered information Correct? (yes/no):"))
        if choice=="yes":
            write_in_csv(l)

            con_check=input("Want to add another student type (yes), otherwise print (no):")
            if con_check=="yes":
                condition=True
            elif con_check=="no":
                condition=False

            i+=1

        elif choice=="no":
            print("Please enter correct information")