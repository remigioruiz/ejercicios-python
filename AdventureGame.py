import time
import os

weapon = False

def clear_screen():
  try:
    os.system('cls')
  except:
    pass

def typer(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.01)

def play_again():
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            start_game()
        elif play_again == "n":
            print("Thank you for playing! Goodbye. ")
            quit()
        else:
            print("Please enter a valid option ('y' or 'n'). ")

def introScene():
  clear_screen()
  directions = ["left", "right", "forward"]
  typer("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?\n")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    if userInput == "left":
      showShadowFigure()
    elif userInput == "right":
      showSkeletons()
    elif userInput == "forward":
      hauntedRoom()
    elif userInput == "backward":
      typer("You find that this door opens into a wall.\n")
    else: 
      print("Please enter a valid option for the adventure game.")

def showSkeletons():
  clear_screen()
  directions = ["backward", "forward"]
  global weapon
  typer("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?\n")
  userInput = ""
  while userInput not in directions:
    print("Options: left/backward/forward")
    userInput = input()
    if userInput == "left":
      typer("You find that this door opens into a wall. You open some of the drywall to discover a knife.\n")
      weapon = True
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print("Please enter a valid option for the adventure game.")

def strangeCreature():
  clear_screen()
  actions = ["fight", "flee"]
  global weapon
  typer("A strange goul-like creature has appeared. You can either run or fight it. What would you like to do?\n")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      clear_screen()
      if weapon:
        typer("You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
      else:
        typer("The goul-like creature has killed you.\n")
      play_again()
    elif userInput == "flee":
      showSkeletons()
    else:
      print("Please enter a valid option for the adventure game.")

def showShadowFigure():
  clear_screen()
  directions = ["right", "backward"]
  typer("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?\n")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      cameraScene()
    elif userInput == "left":
      clear_screen()
      typer("You find that this door opens into a wall.\n")
      #...
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option for the adventure game.")

def cameraScene():
  clear_screen()
  directions = ["forward", "backward"]
  typer("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?\n")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      clear_screen()
      typer("You made it! You've found an exit.\n")
      play_again()
    elif userInput == "backward":
      showShadowFigure()
    else:
      print("Please enter a valid option for the adventure game.")

def hauntedRoom():
  clear_screen()
  directions = ["right", "left", "backward"]
  typer("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?\n")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      typer("Multiple goul-like creatures start emerging as you enter the room. You are killed.\n")
      play_again()
    elif userInput == "left":
      typer("You made it! You've found an exit.\n")
      play_again()
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option for the adventure game.")

def start_game():
  clear_screen()
  typer("Welcome to the Adventure Game! ")
  typer("As an avid traveler, you have decided to visit the Catacombs of Paris. ")
  typer("However, during your exploration, you find yourself lost. ")
  typer("You can choose to walk in multiple directions to find a way out.\n")
  typer("Let's start with your name: ")
  name = input()
  print("Good luck, " +name+ ".")
  time.sleep(2)
  introScene()

start_game()

if __name__ == '__main__':
  start_game()
