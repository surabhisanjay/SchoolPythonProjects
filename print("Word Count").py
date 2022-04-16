print("Word Count")
wordslist=[]
n=int(input("Enter number of words:"))
for i in range(n) :
    word=input("Enter word:")
    wordslist.append(word)

#print(wordslist)

wordcount_dict={}

for i in wordslist: 
    if i not in wordcount_dict:   
        wordcount_dict[i] = wordslist.count(i)

print("Word count :")
print(wordcount_dict)

new_dict={}
for i in wordcount_dict:
    if wordcount_dict[i] >= 5 :
        if "newword" in new_dict:
            count = new_dict["newword"]
            new_dict["newword"] = count + wordcount_dict[i]
        else:
            new_dict["newword"] = wordcount_dict[i]
    else :
        new_dict[i] = wordcount_dict[i]

print("Word count after replacing words having count>=5 with newword")
print (new_dict)


tmplist = ["newword" if wordslist.count(x)>=5 else x for x in wordslist]

print("Modified list : ")
print(tmplist)