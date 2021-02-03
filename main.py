from art import logo , vs
from game_data import data
import random
from replit import clear



playing = True
score = 0


num_position_a = random.randint(0,49)

print(logo)

while playing is True:

    
    
    
    num_position_b = random.randint(0, 49)

    name_a = data[num_position_a]["name"]
    description_a = data[num_position_a]["description"]
    country_a = data[num_position_a]["country"]

    print(f"compare A: {name_a}, {description_a}, {country_a}"  )

    followers_a = data[num_position_a]["follower_count"]
    # print(followers_a) 

    print(vs)

    name_b = data[num_position_b]["name"]
    description_b = data[num_position_b]["description"]
    country_b = data[num_position_b]["country"]

    print(f"compare B: {name_b}, {description_b}, {country_b}"  )

    followers_b = data[num_position_b]["follower_count"]
    # print(followers_b)    

     
    player_guess = input("Who has more followers? Tyoe 'A' or 'B': ").lower()

    if followers_a > followers_b:
        if player_guess == "a":
            score += 1
            clear()
            print(logo)
            print(f"Right! your score: {score}")
            num_position_a = num_position_b
            
           
        else:
            playing = False
            clear()
            print(f"You are wrong! Final score: {score}")
            
    else:
        if player_guess == "b":
            score += 1
            clear() 
            print(logo)
            print(f"Right! your score: {score}")
            num_position_a = num_position_b
        else:
            playing = False
            clear()
            print(f"You are wrong! Final score: {score}")
         
                   
    


