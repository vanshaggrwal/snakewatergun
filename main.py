import random
computer=random.choice([-1,0,1])
youstr=input("Enter Your Choice ")
youDict={"s":1,"w":-1,"g":0}
revDict={1:"Snake",-1:"Water",0:"gun"}
you=youDict[youstr]
print(f"You choose {revDict[you]}\nComputer choose {revDict[computer]}")
if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Lose!")
    else:
        print("Something Went Wrong")

    
    
    
