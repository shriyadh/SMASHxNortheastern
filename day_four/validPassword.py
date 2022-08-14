import string
import random

charactersSpecial = list("!@#$%^&*()")

# take password input from user

password = input("What is your password: ")

upper = 0
lower = 0
digit = 0
spl = 0

if(len(password) >= 8) :

  for letter in password:

    # count upper case
    if(letter.isupper()):
      upper += 1

    # count lower case
    if(letter.islower()):
      lower += 1

    # count digit
    if(letter.isdigit()):
      digit += 1

    # count special char
    if(letter in charactersSpecial):
      spl += 1

if( lower >= 1 and upper >= 1 and spl >= 1 and digit >= 1 and lower + upper + spl + digit == len(password)):
  print("Your password : " + password + " : is VALID!")

else :
  print("Your password : " + password + " : is NOT VALID!")
