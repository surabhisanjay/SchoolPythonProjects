W=int(input("What do you want to play \n 1.Rock paper scissors \n 2.Quiz game\n"))
if W==2:
    #QUIZ GAME
    N=input("enter your name ")
    Q=input("are you ready to quiz?")
    if Q=="yes":
        q1=int(input("1.What Indian city is the capital of two states?\n 1.Delhi \n 2.Chandigarh \n 3.Kolkata \n 4.Bengaluru \n ans:"))
        Scr=[]
    if q1==2:
        Scr+=[1]
    else:
        pass
    q2=int(input(" 2.Which among the following was the first Indian woman who went into space? \n 1. Kalpana Chawl \n 2. Sunita Williams\n 3. Koneru Humpy\n4. None of the above \n ans:"))
    if q2==1:
        Scr+=[1]
    else:
        pass
    q3=int(input("3. Who wrote the Indian National Anthem? \n1. Bakim Chandra Chatterji\n2. Rabindranath Tagore\n3. Swami Vivekanand\n4. None of the above \n ans:"))
    if q2==2:
        Scr+=[1]
    else:
        pass
    w=print("your score is ",len(Scr))
    #ROCK PAPER SCISSORS 
if W==1:
    import random 
    print("winning rules of rock paper scissor game as follows: rock vs paper : paper wins \n paper vs scissor : scissor wins \n rock vs scissor : rock wins ")

    print("enter choice \n1 for Rock \n 2 for paper \n 3 for scissor ")
    #taking user's input 
    choice=int(input("rock paper scissor shoot:    "))
    if choice==1:
        choice_user="rock"
    elif choice==2:
        choice_user="paper"
    else:
        choice_user="scissor"
    print("You have chosen ",choice_user)

    print("Now it is the computers turn ")
    #computer selects its choice
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name="rock"
    elif comp_choice==2:
        comp_choice_user="paper"
    else:
        comp_choice_name="scissor"
    while comp_choice==choice:
        comp_choice=random.randint(1,3)

    print("computer has chosen", comp_choice_name)

    #establishing the winner 

    if ((choice==1 and comp_choice==2)or (choice==2 and comp_choice==1)):
        print("Paper wins ")
        winner=2
    elif((choice==1 and comp_choice==3)or (choice==3 and comp_choice==1)):
        print("Rock wins")
        winner=1
    elif((choice==2 and comp_choice==3)or (choice==3 and comp_choice==2)):
        print("scissor wins")
        winner=3
    if winner==choice:
        print("Congratulations you won !!")
    else:
        print("You lose :( Better luck next time!! ")
    

