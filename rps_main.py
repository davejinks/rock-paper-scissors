import random

while True:  # MAIN MENU
    print("ROCK, PAPER, SCISSOR START MENU")
    print("1. start game")
    print("2. exit game")
    desire = int(input("choose an option: "))
    user_score = 0
    computer_score = 0
    round_played = 0

    if desire == 1:
        print("-----STARTING GAME -----")
        while True:
            game_options = ["rock", "paper", "scissors"]
            players_choice = input("select: rock, paper, scissors, Q to quit: ").lower()

            if players_choice == "q":
                print("game ending.....".upper())
                print(f"rounds played: {round_played}\nscores - USER : {user_score}\nscores - COMPUTER : {computer_score}")
                break
            elif players_choice not in game_options:
                print("Invalid option try again!!!!")
                continue

            computer_choice = random.choice(game_options)
            print(f"COMPUTER chose: {computer_choice}")
            round_played += 1

            if players_choice == computer_choice:
                print("it's a tie")
            elif ((players_choice == "rock" and computer_choice == "scissors") or
                  (players_choice == "paper" and computer_choice == "rock") or
                  (players_choice == "scissors" and computer_choice == "paper")):
                print("you win!!!!!!")
                user_score += 1
            else:
                print("computer wins")
                computer_score += 1

            print("-----GAME OVER-----")
            print(f"rounds: {round_played}\nscores - USER : {user_score}\nscores - COMPUTER : {computer_score}")

    elif desire == 2:
        print("good bye!!!!!".upper())
        break
    else:
        print("invalid option")
