import random
number_to_guess = random.randint(1,100)
while True :
    try :
        guess = int(input("enter a number between 1 and 100 :"))
        if guess < number_to_guess :
             print("your guess is too low!!")

        if guess > number_to_guess :
            print("your guess is too high!!")

        if guess == number_to_guess :
            print("you guessed correctly")
            print(f"the number is {number_to_guess}")
            break

    except ValueError:
        print("invalid number!check again!! ")