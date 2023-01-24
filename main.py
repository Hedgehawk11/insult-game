import random as r
import pygame
import time as t
import sys
import replit

pygame.init()
name = input('name \n')
print('Hello',name + '!')
t.sleep(1)
print('I think you are sluggish, stubborn, and lazy!')
t.sleep(1)

while True:
  response = input('Type your response here \n')
  if response.lower() == 'yes':
    break
  else:
    print('No, u are a slacker')
answer = input('Can you do my homework for me \n')

if answer.lower() == 'no':
  print('eh who cares')
elif answer.lower() == 'yes':
  while True:
    num = r.randint(1,10)
    numGuess = input('guess my number ')
    if num == TypeError:
      print('numbers only')
    elif num == int(numGuess):
      print('You are still a slacker that got', num, 'right')
      break
    else:
      print('Ha ha! You are a slacker! It was', num)
      break
else:
  print('invalid input!')

while True:
  Likes_Spam = input('Do you like spam \n')
  Likes_Spam = Likes_Spam.lower()
  if Likes_Spam == 'yes':
    Likes_Spam = True
    break
  elif Likes_Spam == 'no':
    Likes_Spam = False
    break
  else:
    print('Invalid input! Please answer again!')

if Likes_Spam:
  for i in range(10000):
    print('spam')
if not Likes_Spam:
  print('too bad')
  for i in range(100000):
    print('too bad')
while True:
  q = str(input('ask a question\n'))
  if q == '1+1' or q == '1 + 1':
    print(2)
    break
  elif q != '1+1' or q != '1 + 1':
    print('sorry I can only do 1+1')
  else:
    print('?')
    break


print('spam time')
t.sleep(2)
if Likes_Spam:
  for i in range(10000):
    print('spam')
if not Likes_Spam:
  print('too bad')
  for i in range(100000):
    print('spam')

