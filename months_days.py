M={"jan":31,"feb":28,"mar":31,"april":30,"may":31}
print(sorted(M.keys()))

A=input("enter the month")
print("the no of days are",M.get(A))
S=sorted(M.values())
#show the months with 31 days
for i in M:
    if M.get(i)==31:
        print(i)
    
