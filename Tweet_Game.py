import random
random.seed()

fileElonTweets = open("elontweets.txt","r+")
line = "words"
storage1 = []
length = len(storage1)
#makes list called storage1 that goes and, for each line, stores it at that index
while length < 2 or (storage1[length - 2] != "" or storage1[length - 1] != ""):
  line = fileElonTweets.readline()
  line = line[:line.find("\n")]
  storage1.append(line)
  length = len(storage1)
storage1.pop(length - 1)
storage1.pop(length - 2)
storage1.append("#")
fileElonTweets.close()

crush1 = []
cur = ""

for x in storage1:
  if x != "#":
    cur += x + "\n"
  else:
    cur = cur[:line.find("\n",len(cur) - 2)]
    crush1.append(cur)
    cur = ""
crush1.pop(0)

fileNotElonTweets = open("notelontweets.txt","r+")
line = "words"
storage2 = []
length = len(storage2)
#makes list called storage2 that goes and, for each line, stores it at that index
while length < 2 or (storage2[length - 2] != "" or storage2[length - 1] != ""):
  line = fileNotElonTweets.readline()
  line = line[:line.find("\n")]
  storage2.append(line)
  length = len(storage2)
storage2.pop(length - 1)
storage2.pop(length - 2)
storage2.append("#")
fileNotElonTweets.close()

crush2 = []
cur = ""

for x in storage2:
  if x != "#":
    cur += x + "\n"
  else:
    cur = cur[:line.find("\n",len(cur) - 2)]
    crush2.append(cur)
    cur = ""
crush2.pop(0)

def info(): 
  #Ascii art credit: https://patorjk.com/software/taag
  print(" ______ _               __  __           _      _        _____            _")
  print("|  ____| |             |  \/  |         | |    (_)      / ____|          | |")
  print("| |__  | | ___  _ __   | \  / |_   _ ___| | __  _ ___  | |     ___   ___ | |")
  print("|  __| | |/ _ \| '_ \  | |\/| | | | / __| |/ / | / __| | |    / _ \ / _ \| |")
  print("| |____| | (_) | | | | | |  | | |_| \__ \   <  | \__ \ | |___| (_) | (_) | |")
  print("|______|_|\___/|_| |_| |_|  |_|\__,_|___/_|\_\ |_|___/  \_____\___/ \___/|_|")
                                                                             
  print('Welcome to Elon is Cool')
  print("Featuring Elon Musk's tweets")
  print("\"yes\" and \"no\" are acceptable answers. \n ")

info()

def isNumber(check):
  checkS = str(check)
  nums = "1234567890"
  for x in checkS:
    if (nums.find(x) == -1):
      return False
  return True

def isAns (check):
  check.lower()
  return (check == "yes" or check == "no")

new_game = "yes"
while new_game == "yes":
  number = input("How many rounds do you want to play? \n")
  if (isNumber(number) == False):
    while (isNumber(number) == False):
      number = input("Please enter an integer: ")


  score = 0
  def gameplay(score,rounds,number):
    correct = False
    tweetsource = random.randint(1,2)
    print(" \nIs this Elon's tweet? \n")
    if (tweetsource == 1): 
      random_number = random.randint(0,len(crush1) - 1)
      print ('"' + (crush1[random_number]) + '"' + "\n")
    else:
      random_number = random.randint(0,len(crush2) - 1)
      print('"' + crush2[random_number] + '"' + "\n")
    ans = input("")
    ans.lower()
    if (isAns(ans) == False):
      while (isAns(ans) == False):
        ans = input("Please enter a \"yes\" or a \"no\": ")
    
    if (ans == "yes" and tweetsource == 1) or (ans == "no" and tweetsource == 2):
      print('\nCongrats you know the Musk!')
      correct = True
      score += 1
      print("\n\nCurrent score: " + str(score))
      if (rounds != number):
        print('\nOnto the next tweet...')
    else: 
      print('\nWow you suck and you should be ashamed of yourself. You must know the Musk better.')
      correct = False
      print("\nCurrent score: " + str(score))
    return correct

  for x in range(0,int(number),1): 
    if (gameplay(score,x + 1,int(number))):
      score += 1

  def stats():
    print("You played " + number + " rounds of Elon Musk is Cool!")
    print("final score: " + str(score))
    percent = score / int(number) * 100
    rounded_percent = round(percent,2)
    print("\nPercentage of correct answers: " + str(rounded_percent) + "%")

  stats()


  new_game = input("\nDo you want to play again? \n")
  if (isAns(new_game) == False):
      while (isAns(new_game) == False):
        new_game = input("Please enter a \"yes\" or a \"no\": ")

print("\nThanks for playing!")
