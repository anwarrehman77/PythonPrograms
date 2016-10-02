import random

while True:
    num = random.randrange(1, 10)

    guess = int(input("Guess a number from 1 to 10."))
    if guess == num:
        print ("GOOD JOB!!! PAPPA WILL TELL YOU YOUR REWARD!")

    else:
        print ("Sorry, the right number was " + str(num))
        print ("You suck!")

    playAgain = raw_input("Do you want to play again? (yes/no): ")
    if playAgain == 'no':
        break
print ("Thank you for playing!!!")
