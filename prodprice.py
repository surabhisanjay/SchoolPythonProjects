n=int(input("enter the no of products"))
products={}
for i in range(n):
    p_name=input("enter the name of the product")
    p_price=input("enter the price of the product")
    products.update({p_name : p_price})
print(products)
n=int(input("enter the no of products you want to find in our system"))
for i in range(n):
    f=input("enter the product's name")
    print(products.get(f,"product not found in our system"))