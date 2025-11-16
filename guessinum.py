import random

target=random.randint(1,100)  
while True:
 try:   
    
  a=int(input("Guess the number between 1 to 100:"))
 
  if (a>target):
    print("too high ")
  elif(a<target):
    print("too low")
  else:
    print("contragulation u won ") 
    
 except ValueError:
     print("please  enter the vald number")       