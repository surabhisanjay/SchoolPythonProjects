 import math 
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))

d = b ** 2 - 4 * a * c > 0

if d > 0:
    d_root_2 = math.pow(d, 0.5)
    x1 = (-b + d_root_2)/(2 * a)
    x2 = (-b - d_root_2)/(2 * a)
else:
    x1 = x2 = None
    pass

print("The roots are {} and {}".format(x1, x2))
                