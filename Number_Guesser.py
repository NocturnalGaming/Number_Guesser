#Number_Guesser

import random
try:
  num = int(input("Enter the max number in the range: "))
  if num < 1:
    print("Upper Bound should be greater that 1")
except:
  print("Not a valid Number")
guess = range(1,num)
random_guess = random.choice(guess)
user_guess = ""
attempts = 0

try:
  while user_guess != random_guess:
    user_guess = int(input("Guess your Number Between [1-" + str(num) + "]: "))
    if user_guess > random_guess:
      print("Your Expectations are too High")
      attempts += 1
      print("{} Guesses wrong".format(attempts))
    elif user_guess < random_guess:
      print("Think Big,Become Big")
      attempts += 1
      print("{} Guesses wrong".format(attempts))
    elif user_guess > num or user_guess < 1:
      print("Your Number is not in between [1-" + str(num) + "]")
    else:
      attempts += 1
      print("Congrats! That's the number in my mind. You took {} attempts to guess it.".format(attempts))
except ValidError:
  print("Only Integers are accepted as Guesses")

#Optional .txt saver (Not compatible with android. Remove all hases in pc)

#open ("Attempts_Logger", "a")
#Attempts_Logger.write("Original Number = " + print(random_guess) + "\nAttempts taken = {}".format(attempts))
#Attempts_Logger.close()