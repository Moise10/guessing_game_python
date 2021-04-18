import math 
import time
import calendar

from random import randint

def guess(x):
  random_number = randint(1, x)
  guess = 0
  while guess != random_number:
    guess = int(input(f'guess a number between 1 and {x}: '))
    if guess < random_number:
      print("Sorry please guess again, guess is too low")
    elif guess > random_number:
      print("Sorry pleae guess again, guess is to high")
  print(f"You guessed the right number {random_number}")
    

guess(10)



