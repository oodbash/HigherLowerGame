import art
import game_data
import random

def main():

    print(art.logo)

    result = 0
    eog = False

    first_item = None
    second_item = None
    while(first_item == second_item):
        first_item = random.randint(0,(len(game_data.data)-1))
        second_item = random.randint(0,(len(game_data.data)-1))
    
    while eog == False:
        print(f"Compare A: {game_data.data[first_item]['name']}, a {game_data.data[first_item]['description']}, from {game_data.data[first_item]['country']}, and..")
        print(f"..against B: {game_data.data[second_item]['name']}, a {game_data.data[second_item]['description']}, from {game_data.data[second_item]['country']}.\n")
        answer = (str(input("Who has more followers? 'A' or 'B': "))).lower()
        if game_data.data[first_item]['follower_count'] > game_data.data[second_item]['follower_count'] and answer == "a":
            result += 1
            print(f"You are right! Current score: {result}\n")
            second_item = random.randint(0,(len(game_data.data)-1))
        elif game_data.data[first_item]['follower_count'] < game_data.data[second_item]['follower_count'] and answer == "b":
            result += 1
            print(f"You are right! Current score: {result}\n")
            first_item = second_item
            while(first_item == second_item):
                second_item = random.randint(0,(len(game_data.data)-1))
        else:
            print(f"\nSorry, that's wrong. Final score: {result}")
            eog = True

main()