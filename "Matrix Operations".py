print("Matrix Operations")



def transpose_matrix():
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