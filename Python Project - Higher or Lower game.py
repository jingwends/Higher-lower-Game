from art import logo, vs
from game_data import data
from replit import clear
import random

clear()




# Break the problem into small solvable trunks

# Display art
print(logo)
print()



# Generate a random account from the game data.
for i in range(1): 
    rand_choice1=random.choice(data)
    
    data.remove(rand_choice1)
  
    
#make the dictory to list to eaily pick whatever we want to print
    content1=list(rand_choice1.values())
    
    # Get follower count of each account.
    follower1=content1[1]
    
    

# Format account data into printable format.
    print("Compare A: "+ content1[0]+", a(n) " + content1[2]+", "+ "from "  + content1[3]+".")

print()
print()
print(vs)
    
#repeat the above process to pick the 2nd choice
for i in range(1):
        rand_choice2=random.choice(data)
        #print(rand_choice2)
        data.remove(rand_choice2)
        content2=list(rand_choice2.values())
        print("Against B: "+ content2[0]+", a(n) " + content2[2]+", "+ "from "  + content2[3]+".")
       
    # Get follower count of each account.
        follower2=content2[1]
    

print()
print()
# Ask user for a guess.
user_guess=input("Who has more followers? Type 'A' or 'B':")




# Clear screen between rounds. Use clear() in replit module

#The initial score is 0.
score = 0

#The first interface
while user_guess != 'A' and user_guess != 'B':
    print ("The value you entered is invalid. ")
    user_guess=input("Who has more followers? Type 'A' or 'B':")

    
# Use if Statement to check if user is correct.    
# Check if user is correct.
# Give user feedback on their guess.
if int(follower1) > int(follower2) and user_guess == 'B' : 
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")

elif int(follower2) > int(follower1) and user_guess == 'A' :
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")

else: 
# Make game repeatable.
    while True:

        # Score Keeping.
        score = score + 1
        clear()
        print(logo)
        print()
        print(f"You're right! Current score: {score}.")

        # Make B become the next A.
        follower1=follower2
        print("Compare A: "+ content2[0]+", a(n) " + content2[2]+", "+ "from "  + content2[3]+".")
        print()
        print(vs)
        for i in range(1):
            rand_choicen=random.choice(data)
           
            data.remove(rand_choicen)
            content2=list(rand_choicen.values())
            print("Against B: "+ content2[0]+", a(n) " + content2[2]+", "+ "from "  + content2[3]+".")
            follower2=content2[1]

            
#Order user to give a valid input
        user_guess=input("Who has more followers? Type 'A' or 'B':")
        while user_guess != 'A' and user_guess != 'B':
            print ("The value you entered is invalid. ")
            user_guess=input("Who has more followers? Type 'A' or 'B':")
        
#Use if Statement to check if user is correct.  
        if int(follower1) < int(follower2) and user_guess == 'A' : 
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            break
      
# Use if Statement to check if user is correct.  
        if int(follower2) < int(follower1) and user_guess == 'B' :
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
        
            break

        

        


