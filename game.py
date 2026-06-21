import random


computer=-1
you=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"water",0:"Gun"}
you=youDict[you]
#By now we have 2 numbers(variables),ypu amd computer

print(f"You chose {reverseDict[you]}\nYou chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw")

elif(computer==-1 and you==1):
    print("You win!")

elif(computer==-1 and you==0):
    print("You lose!")

elif (computer ==1 and you ==-1):
    print("You lose!")

elif(computer==1 and you==0):
    print("You win!")

elif (computer ==0 and you ==-1):
    print("You lose!")

elif (computer ==0 and you ==1):
    print("You lose!")


