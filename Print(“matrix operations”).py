Print(“matrix operations”)

choice='a'
while(choice != 'q'):
    print("\nMenu:")
    print("a. Sum and Difference of matrices")
    print("b. Transpose of a matrix")    
    print("q. quit")
    choice=input("Enter choice:")
    if(choice == 'a'):
        r=int(input("How many rows ?"))
        c=int(input("How many columns ?"))
        mat1=[]
        mat2=[]
        print ("Enter matrix - 1:")
        for i in range(r):
            row=[]
            for j in range(c):   
                print("Row: ", i , "Col: ", j)     
                mat_entry=int(input())
                row.append(mat_entry)
            mat1.append(row)    
        print(mat1)
        print ("Enter matrix - 2:")
        for i in range(r):
            row=[]
            for j in range(c):   
                print("Row: ", i , "Col: ", j)     
                mat_entry=int(input())
                row.append(mat_entry)
            mat2.append(row)    
        print(mat2)
        sum_mat=[]
        diff_mat=[]
        for i in range(len(mat1)):
            sum_row=[]
            diff_row=[]
            for j in range(len(mat1[i])):
                s = mat1[i][j] + mat2[i][j]
                d = mat1[i][j] - mat2[i][j]
                sum_row.append(s)
                diff_row.append(d)
            sum_mat.append(sum_row)
            diff_mat.append(diff_row)     
        print("Sum of matrices:")
        print(sum_mat)
        print("Difference of matrices:")
        print(diff_mat)
    elif(choice == 'b'):
        r=int(input("How many rows ?"))
        c=int(input("How many columns ?"))
        mat1=[]
        tran=[]
        print ("Enter matrix :")
        for i in range(r):
            row=[]
            for j in range(c):   
                print("Row: ", i , "Col: ", j)     
                mat_entry=int(input())
                row.append(mat_entry)
            mat1.append(row)   
        print("Original matrix:") 
        print(mat1)
        for i in range(c):
            row=[]
            for j in range(r):
                row.append(0)
            tran.append(row)
        for i in range(c):
            for j in range(r):
                tran[i][j] = mat1[j][i]
        print("Transpose of the above matrix:")
        print(tran)
