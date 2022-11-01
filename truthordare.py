import random

players=int(input("Enter number of players"))
if players==1:
    print("Get a friend")
    
    
elif players==2:
    player1=input("ENTER NAME")
    player2=input("ENETR NAME")
    print("PLAYER1: ",player1)
    print("PLAYER2: ",player2)

elif players==3:
    player1=input("ENTER NAME")
    player2=input("ENTER NAME")
    player3=input("ENTER NAME")
    print("PLAYER1=",player1)
    print("PLAYER2=",player2)
    print("PLAYER3=",player3)

elif players==4:
    player1=input("ENTER NAME")
    player2=input("ENETR NAME")
    player3=input("ENTER NAME")
    player4=input("ENTER NAME")
    print("PLAYER1=",player1)
    print("PLAYER2=",player2)
    print("PLAYER3=",player3)
    print("PLAYER4=",player4)

elif players==5:
    player1=input("ENTER NAME")
    player2=input("ENTER NAME")
    player3=input("ENTER NAME")
    player4=input("ENTER NAME")
    player5=input("ENTER NAME")
    print("PLAYER1=",player1)
    print("PLAYER2=",player2)
    print("PLAYER3=",player3)
    print("PLAYER4=",player4)
    print("PLAYER5=",player5)

else:
    print("This game can accomodate only 5 players.")
    

    
    


ctr=1
while ctr<99:
    if players==1:
        break
    else:
        t_d=random.randint(10,17)
        ctr=ctr+1
        
        

        if t_d==10:
            print("DARE - PLAYER ",random.randint(1,players))
            cantthink=input("Can't think of one? Press y to generate.")
            if cantthink=='y':
                print("Do 10 pushups")
            else:
                print("")
                

        elif t_d==11:
            print("TRUTH - PLAYER ",random.randint(1,players))
            cantthink=input("Can't think of one? Press y to generate.")
            if cantthink=='y':
                print("When was the last time you cried?")
            else:
                print("")

        elif t_d==12:
            print("\nDARE - PLAYER ",random.randint(1,players))
            cantthink=input("Can't think of one? Press y to generate.")
            if cantthink=='y':
                print("Twerk for 10 seconds")
            else:
                print("")

        elif t_d==13:
            print("\nTRUTH - PLAYER ",random.randint(1,players))
            cantthink=input("Can't think of one? Press y to generate.")
            if cantthink=='y':
                print("Would you eat _____ for a billion dollars?")
            else:
                print("")

        elif t_d==14:
            print("\nDARE - PLAYER ",random.randint(1,players))
            cantthink=input("Can't think of one? Press y to generate.")
            if cantthink=='y':
                print("Eat a raw piece of garlic")
            else:
                print("")

        elif t_d==15:
            print("\nTRUTH - PLAYER ",random.randint(1,players))
            cantthink=input("Can't think of one? Press y to generate.")
            if cantthink=='y':
                print("Do you have a hidden talent?")
            else:
                print("")

        elif t_d==16:
            print("\nDARE - PLAYER ",random.randint(1,players))
            cantthink=input("Can't think of one? Press y to generate.")
            if cantthink=='y':
                print("Let the group prank call your friend")
            else:
                print("")

        elif t_d==17:
            print("\nTRUTH -PLAYER ",random.randint(1,players))
            cantthink=input("Can't think of one? Press y to generate.")
            if cantthink=='y':
                print("What is an embarrasing thing that your parents have caught you doing")
            else:
                print("")

        

else:
    print("\nGAME OVER!")




