# Program to display the Fibonacci sequence up to n-th term in a list

n = int(input("How many terms? "))
sequence = [0,1]
#Initial values


for i in range(2,n+1):
    next_num = sequence[-1] + sequence[-2]
    sequence.append(next_num)
print(tuple(sequence))

"""print(sequence)
#fibonacci series in a tuple 
a=0
b=1
for i in range(9):
    a,b=b,a+b"""