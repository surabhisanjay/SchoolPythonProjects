print("Student Details:")
n=int(input("How many students ?"))

studentlist=[]

for i in range(n):
    fname=input("Firstname:")
    lname=input("Lastname:")
    percentage=float(input("Percentage:"))
    height=int(input("Height in cms:"))
    row=[]
    row.append(fname)
    row.append(lname)
    row.append(percentage)
    row.append(height)
    studentlist.append(row)

print(studentlist)
choice='a'
while(choice != 'q'):
    print("\nMenu:")
    print("a. Generate Roll Numbers")
    print("b. Ascending order of height")
    print("c. Decreasing order of percentage")
    print("q. quit")
    choice=input("Enter choice:")
    if(choice == 'a'):
        names=[]
        for i in range(len(studentlist)):
            names.append(studentlist[i][0])
        names.sort()
        print(names)
        for i in range(len(names)):
            print("Roll No: ", i+1, names[i])
    elif(choice == 'b') :
        n=len(studentlist)
        for i in range(n):
            for j in range(n-i-1):
                if studentlist[j][3] > studentlist[j+1][3]:
                    tmplist = studentlist[j]
                    studentlist[j] = studentlist[j+1]
                    studentlist[j+1] = tmplist
        for i in range(n):
            print(studentlist[i])
    elif(choice == 'c') :
        n=len(studentlist)
        for i in range(1, n):
            key = studentlist[i][2]
            keylist=studentlist[i]
            j=i-1
            while j>=0 and key > studentlist[j][2]:
                studentlist[j+1]= studentlist[j]
                j=j-1
            else:
                studentlist[j+1] = keylist
        for i in range(n):
            print(studentlist[i])
            