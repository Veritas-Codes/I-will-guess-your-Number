from random import randrange as rr

def guess(s, b):
  return int((s + b) / 2)
  
def relation_correct(g, u, a):
  if a in ['<', 'smaller', 'less'] and not (g > u):
    return False
  elif a in ['>', 'bigger', 'more'] and not (g < u):
    return False
  return True
  
s = 1
b = 100
answers = ['<', "smaller", 'less', '>', "bigger", 'more', 'yes']
won = False
replies = []
guesses = []

print("Think of a number from 1-100 (inclusive).\nI will ask you seven times\n\n\
If YOUR number is SMALLER than\nwhat I guess, print '<', 'smaller', or 'less'.\n\n\
If YOUR number is BIGGER than\nwhat I guess, print '>', 'bigger', or 'more'.\n\n\
If my guess is correct, print 'yes'.")

for i in range(1, 8):
  print()
  print(f"{i}. Is your number: {guess(s, b)}?")
  guesses.append(guess(s, b))
  answer = input().lower()
  while answer not in answers:
    answer = input("I do not understand that! ")
  replies.append(answer)
  if answer in ['<', 'smaller', 'less']:
    b = guess(s, b)
  elif answer in ['>', 'bigger', 'more']:
    s = guess(s, b)
  else:
    print(f"I knew it! It took {i} tries.")
    won = True
    break

if not won:
  usr_num = int(input("What number did you think of? "))
  for i in range(7):
 
    if i == 0:
      ind_count = "1st"
    elif i == 1:
      ind_count == "2nd"
    elif i == 2:
      ind_count == "3rd"
    else:
      ind_count = str(i+1) + "th"
    if not relation_correct(guesses[i], usr_num, replies[i]):
      print(f"You did not answer the {ind_count} question\ncorrectly!")
      break
  
    
