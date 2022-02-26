import random

generated_number = random.randint(1,100)

user_mode = input("choose hard mode or easy mode = ")
users_choice = int(input("choose a number from 1 to 100 = "))

attempts = 0

if user_mode == "hard":
    attempts += 5
else:
    attempts +=10

while not attempts == 1:
    if users_choice == generated_number:
        print("you got the number")
        attempts = 1
    else:
        attempts-= 1
        if users_choice < generated_number:
            print(f"too low and u got {attempts} left ")

        else:
            print(f"too high and u got {attempts} left")

        users_choice = int(input("choose a number = "))