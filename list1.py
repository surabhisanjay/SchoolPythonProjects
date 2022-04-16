print("Menu based program for String operations")

choice='a'

while(choice != 'q'):
    print("\nMenu:")
    print("a. Check if it is a palindrome")
    print("b. Reverse each word in a sentence")
    print("c. Remove duplicate entries of words")
    print("q. quit")
    choice=input("Enter choice:")
    if(choice == 'a'):
        s=input("Enter string:")
        flag=0
        for i in range(len(s)):
            if ( s[i] != s[len(s) - i - 1]):
                flag=1
                break
            else :
                continue
        if(flag==0):
            print( s , " is a palindrome")
        else:
            print(s, " is not a palindrome")
    elif(choice == 'b'):
        s=input("Enter string:")
        wordlist = s.split(" ")
        leng = len(wordlist)
        print(wordlist)
        for i in range(leng):
            word = wordlist[i]
            newstr=""
            len_str = len(word)
            for a in range(-1, (-len_str-1), -1):
                newstr +=  word[a]
            wordlist[i] = newstr      
        print("Reversed strings in the list")
        print(wordlist)
    elif(choice == 'c'):
        s=input("Enter string:")
        wordlist = s.split(" ")
        newlist=[]
        for i in wordlist:
            if i not in newlist:
                newlist.append(i)
        print("List with duplicates removed:")
        print(newlist)

    

