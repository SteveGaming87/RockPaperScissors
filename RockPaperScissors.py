import random
import time

while True:

   #list of choices for computer to pick
   choices = ["Rock","Paper","Scissors"]

   print("Welcome to Rock, Paper, Scissors!")

   player_choice = input("Choose Rock, Paper or Scissors:")

   #Goes in a loop if user gets it wrong
   while True:
      if player_choice not in choices:
          print("Try Again")
          player_choice = input("Choose Rock, Paper or Scissors:")

      elif player_choice in choices:
          print("Okay");
          break


   #Computer chooses an object fromt the list
   comp_choice = choices[random.randrange(len(choices))]

   #Prints the choices out
   print("You chose:" ,player_choice)
   print("Computer chose:" ,comp_choice)
   print("")

   #waits 2 seconds before the next game
   time.sleep(2)
