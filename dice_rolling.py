import random
while True:
    choice = input("Roll the Dice?(y/n) :").lower()
    if choice == "y":
        die1 = random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1},{die2})")
    if choice == "n":
        print("thankyou for playing!!")
        exit()
    elif choice != "y" and choice != "n":
        print("Invalid Choice!!")