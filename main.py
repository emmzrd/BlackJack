from art import logo
from replit import clear
import random

print(logo)

should_continue = True
while should_continue:
    user_cards = []
    computer_cards = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    play = input("Do you want to play a game of Black Jack? Type 'y' or 'no': ")

    if play == "y":
        clear()
        print(logo)

        for char in range(2):
            user_cards.append(random.choice(cards))
        print(f"Your cards: {user_cards}, current score:", sum(user_cards))

        for char in range(2):
            computer_cards.append(random.choice(cards))

        print(f"Computer's first card: {computer_cards[0]}")

        if sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))

        should_continue2 = True
        while should_continue2:
            another_card = input("Type 'y' for another card, 'n' to pass. ")

            if another_card == "y":
                user_cards.append(random.choice(cards))
                print(f"Your cards: {user_cards}, current score:", sum(user_cards))
                print(f"Computer's first card: {computer_cards[0]}")

            elif another_card == "n":
                print(f"Your final hand: {user_cards}, final score:", sum(user_cards))
                print(f"Computer's final hand: {computer_cards}, current score:", sum(computer_cards))
                should_continue2 = False


                def compare(user_cards, computer_cards):

                    if sum(user_cards) > 21:
                        print("You Lose")
                    elif sum(computer_cards) > 21:
                        print("You Win")
                    elif sum(user_cards) > sum(computer_cards):
                        print("You Win")
                    elif sum(user_cards) < sum(computer_cards):
                        print("You Lose")
                    elif sum(user_cards) == sum(computer_cards):
                        print("It's a draw")


                compare(user_cards, computer_cards)

    elif play == "n":
        print("Thank you for playing. Good Bye.")
        should_continue = False
