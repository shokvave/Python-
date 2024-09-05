name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("you stand at a crossroad which way do you wanna go left or right? ")

if answer == "left":
    
    answer = input("you come to a river you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    if answer == "swim":
       print("you swam across and were eaten by alligator")
        
    elif answer== "walk":
       print("you walked for many miles ran out of water and you lost the game")
        
    else:
     print("not a valid option you lose" )       


elif answer == "right":
     answer == input("you come to a bridge it looks wobbly do you want to cross it or head back (cross/back)? ")

     if answer == "back":
       print("you are a coward you went back and lost")
        
     elif answer== "cross":
       print("you crossed a bridge and met a stranger do you talk to them(yes/no)? ")
       if answer == "yes":
          print("you talked to the stanger and they give you gold , You win !!")
     elif answer == "no":
        print("you ignored the stranger they got offende and stabbed you you bleed to death and lost!") 
     else:
        print("not a valid option your lose")  
        
else:
      print("not a valid option you lose" )

print("Thanks for trying", name)