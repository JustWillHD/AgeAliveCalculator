import time
def daysleft():
  age2 = int(input("sorry can you tell me your age again pls i fucking forgot coz im a dumb fucking robot"))
  wish = int(input("also how long do you wanna live up to? (in years pls): "))
  if wish > 115:
    print("Sorry but i dont think your gonna live for {} years so im not gonna bother".format(wish))
  elif wish < age2: 
    print("ok so why havent you commited suicide yet")
  elif wish == age2:
    print("so u wanna die this year? gl then just throw yourself in front of a train imo its the best way to die since you wont get hurt for that long as you will die instantly since a train going full speed can travel at 200mph which can really fuck you up XD ")
  else:
    seconds_left = wish * 365 * 24 * 60 * 60 - age2 * 365 * 24 * 60 * 60  
    print("ok, you have {years_left} years left, {hours_left} hours left -_- and {seconds_left} seconds left 0_0".format(years_left = wish - age2 , hours_left = wish * 365 * 24 - age2 * 365 * 24, seconds_left ))
    time.sleep(seconds_left)
    while seconds_left > 0: 
      print (seconds_left - 1)
      seconds_left -= 1


    
age = int(input("How old are you?: "))
print("Your are {} years old".format(age))
days = input("Would you also like to know how many days you've been alive?: "))
yes = ["yes","Yes"]
no = ["no","No"]
if days in yes:
  print("You are {days} days old".format(days = age * 365))
  hours = str(input("Do you also want to know how many hours you're alive?: "))
  if hours in yes:
    print("You are {hours} hours old ".format(hours = age * 365 * 24))
    amountleft = (input("Would you also want to know how many hours you have left to live?!: "))
    if amountleft in yes:
        daysleft()
        
    else:
        print("fuck off nigger why u such a pussy i hope u die tmmrow in a car crash")
        
  else: 
    print("fuck off")
    
elif days in no:
  print("this conversation is finished")
else:
  print("Give me a proper answer please")
