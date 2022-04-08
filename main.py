import json
import random
from stranger import get_advice
from os import system, name
import time


# define our clear function
def clear():
  if name == 'nt': #windows
    _ = system('cls')
  else:
    _ = system('clear') #mac or linux
    
#setting variables
message = "Welcome to my site! Thank you for stopping by\n\nThis is a great place to explore some of my code and creativity."

options = "Main Menu\n\n[1] Interactive Professional Resume\n[2] Play an adventure game\n[3] idea coming soon...\n"

option1 = "[1] Competencies\n[2] Education\n[3] Certifications\n[4] Contact\n"  

competencies = "SQL\nPython\nR\nPower BI\nARCGIS\nPandas\nAnalytical and problem-solving skills\nMicrosoft Office proficiency\nExcellent communication skills\nCritical thinking skills\n"

education = "2011 – 2016 Pure and Applied Mathematics - Federal University of Technology Minna\n\nSeptember 2021 – to date Business Analytics - Cambrian College\n"

certifications = ["https://www.datacamp.com/statement-of-accomplishment/course/be40f66ed9298b63a86c247ce4c50550a9b6c412", "https://www.datacamp.com/statement-of-accomplishment/course/76e0738211a29ea986a8f8db3996f6a644dfe3c6"]

contact = "sharonbandele@gmail.com"

while True:  
  clear()
  
  try:
    print(message)
    time.sleep(2)
    print(options)  
    
    choice = input("Please make a selection: ")
       
    if choice == "1":
      clear()
      print(option1)      
      choice1 = input("Please make a selection: ")
      if choice1 == "1":
        clear()
        print(competencies)
        print()
        time.sleep(3)
        input = input("continue (y/n):")
        if input == 'n':
          break
        elif input == 'n':
          break
        else:
          continue
      elif choice1 == "2":
        clear()
        print(education)
        print()
        time.sleep(3)
        input = input("continue (y/n):")
        if input == 'y':
          continue
        elif input == 'n':
          break
        else:
          print("Please select a valid option")
          continue
      elif choice1 == "3":
        clear()
        print(certifications)
        print()
        time.sleep(3)
        input = input("continue (y/n):")
        if input == 'y':
          continue
        elif input == 'n':
          break
        else:
          print("Please select a valid option")
          continue
      elif choice1 == "4":
        clear()
        print(contact)
        print()
        time.sleep(3)
        input = input("continue (y/n):")
        if input == 'y':
          continue
        elif input == 'n':
          break
        else:
          print("Please select a valid option")
          continue
      else:
        print("Please select a valid option")
        continue 
        
    elif choice == "2":
      # read file
      with open('data.json', 'r') as myfile:
        data=myfile.read()
        # parse file
        data = json.loads(data)
      
      room = 0      
      while True:
        clear()
      
        chance = random.randint(1,2)
        if chance == 1:
          if data[room]["luck"] == 1:
            print("You are very lucky!")
            #something happens?
        if chance == 2:
          if data[room]["stranger"] == 1:
            print("A stranger walks by and starts talking to you")
            get_advice()
        
          #print(data[room])
          
          print(data[room]["story"])
          
          if data[room]["win"] == 1:
            print("You win the game!")
            #reset 
            break
          
          if data[room]["die"] == 1:
            print("You lose the game!")
            #reset 
            break
          
          print(data[room]["nav"])
          
          choice = input("Please make a selection ")
          try:
            if choice == '1':
              room = data[room]["c1"] - 1
            elif choice == '2':
              room = data[room]["c2"] - 1
            elif choice == '3':
              room = data[room]["c3"] - 1
            else:
              print("Please select a valid option")
          except:
            continue 
    elif choice == "3":
      print('idea coming sooon')
      continue
      
  except:
    continue
          