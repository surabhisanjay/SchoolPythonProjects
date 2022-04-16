#creating a dictionary
w={"surabhi":122,"apoorva":233,"nisha":344}
print(w.keys())
print(w.values())
#create new dictionary from 3 dictionaries . CONCATENATION 
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1):
    dic4.update(d)

print(dic4)