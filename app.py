import random

def validate_user_input(var): 
  if (var>0 and var<=1000):
      print("Valid Input!! You are all set to play this Lottery Jackpot")
      return 1
  else:
      return "Sorry! Invalid number.. Try Guessing a number between 1 and 1000"
    
def perform_check(var,i):  
     no = random.randint(1,1000)   
     if var in [no]:
         print("Hurray! Jackpot")
         return 0
     else:
       if(i==2):
         print("Sorry... You lost!! the lottery no was {} you have used your chance no {}".format(no,i+1))
       else:
         print("Better luck next time! the lottery no was {} you have used your chance no {}".format(no,i+1))
		 
def start_app():
  for i in range(3):
    var = int(input("Guess the Lottery Number between 1 and 1000: "))
    if((validate_user_input(var))!=1):
      message = validate_user_input(var)
      print(message)
      print("Please provide a valid number to play this jackpot")
      break
    else:
      if((perform_check(var,i))==0):
        break

start_app()

