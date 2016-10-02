import random

while True:
    num = random.randrange(1, 10)

    guess = int(input("Guess a number from 1 to 10."))
    if guess == num:
        print ("GOOD JOB!!! PAPPA WILL TELL YOU YOUR REWARD!")

    else:
        print ("Sorry, the right number was " + str(num))
        print ("PAPPA WILL GIVE YOU A PUNISHMENT!")

    play = input("Do you want to play again? (yes/no): ")
    if play == "no":
        break
print ("Thank you for playing!!!")
