import random

stoke = ['appel','banaan','peer','kiwi','druif','mango','aardbei','druiven','orange']

word = random.choice(stoke)
guesses = ''
turns = len(word)*2
name = input("Enter your name : ")
print(f'wellcome in Word Guessing Game \n\t Good Luck {name} \n\t You have {turns} turns to win the game')
print('Guess the Word! Hint : Ward is a name of  fruit\n')

while turns > 0:
  faild = 0
  for char in word:
    if char in guesses:
      print(char,end=' ')
    else:
      print('_',end=' ')
      faild += 1

  if faild == 0:
    print(f'\n\tcongratulations! {name} You win the game')

    break
  guess = input('\n\nGuess a character : ')
  if len(guess) > 1:
    print('Please enter only one character')
    continue
  elif guess in guesses:
    print('You have already guessed this character! Chose Another Letter')
    continue
  elif guess.isalpha() == False:
    print('Please enter only alphabets!')
    continue
  else:
    guesses+= guess.lower()
    
  if guess not in word:
    turns -= 1
    print('\tWrong')
    print('You have',turns,'more guesses')

  if turns == 0:
    print(f'\n\t{name} You lose the game')
    print('The word is:',word)
    print('Try again')
    break
  