import random

choices = ["rock", "paper", "scissors"]
playing = True

while playing:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f"You: {user_choice}")
    print(f"Computer: {computer_choice}")

    if user_choice == computer_choice:
        print("Tie!!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You won!")

    else:
        print("Computer wins!")

    continue_playing = input("Want to play again? (yes/no): ").lower()

    if continue_playing == "no":
        playing = False
    continue