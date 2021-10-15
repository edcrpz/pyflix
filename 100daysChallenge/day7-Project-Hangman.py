
# Challenge 7.1 -- HANGMAN
#
import random
import os

# import hangman_words
from hangman_words import word_list   # instead of importing whole module, we can use from

# = ["advark", "baboon", "camel"]

# word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
#          'coyote crow deer dog donkey duck eagle ferret fox frog goat '
#          'goose hawk lion lizard llama mole monkey moose mouse mule newt '
#          'otter owl panda parrot pigeon python rabbit ram rat raven '
#          'rhino salmon seal shark sheep skunk sloth snake spider '
#          'stork swan tiger toad trout turkey turtle weasel whale wolf '
#          'wombat zebra ').split()

#
# # To do 1 - randomly choose a word from the word_list and assign it to a variable
# # called chosen_word
chosen_word = random.choice(word_list)
#
# # To do 2 - ask the user to guess a letter and assign their answer to a variable called guess. Make guess
# # lowercase.
# guess = (input("Guess a letter: ")).lower()
#
# # To do 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
#
# for letter in chosen_word:  # For works in string
#     if guess == letter:
#         print("Right")
#     else:
#         print("Wrong")

print("\n--------------------------------------\n")

# Challenge 7.2 -- HANGMAN (replacing underscore)

# print(f"The random word to be guessed is: {chosen_word}")
# guess = (input("Guess a letter: ")).lower()
#
# display = []
# for letter in chosen_word:
#     display.append("_")  # or display += "_"
#
# for index in range(0, len(chosen_word)):
#     if chosen_word[index] == guess:
#         display[index] = guess
#
# print(display)

print("\n--------------------------------------\n")

# Challenge 7.3 -- HANGMAN (Repeatability)

# print(f"The random word to be guessed is: {chosen_word}")
#
# play_game = True
# display = []
# for letter in chosen_word:
#         display.append("_")  # or display += "_"
#
# while "_" in display:  # continues if "_" still exists
#     guess = (input("Guess a letter: ")).lower()
#     for index in range(0, len(chosen_word)):
#         if chosen_word[index] == guess:
#             display[index] = guess
#     print(display)
# # If ("_" in display) gets false, while loop ends
#
# print("\n\nYou win.")

print("\n--------------------------------------\n")

# Challenge 7.4 -- HANGMAN (Tracking of Player's Lives)

Hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

banner = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

print(banner)
print(Hangman[0])

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


play_game = True
display = []
for letter in chosen_word:
        display.append("_")  # or display += "_"     # create display list

str_display = ' '.join(display)     # convert to string
print("Word: " + str_display)
# (f"Chosen word: {chosen_word}")   # Uncomment for testing purposes

lives = 6
hangman_index = 0         # to have pointer for Hangman list (ASCII)
continue_game = True

guess_history = []

while continue_game:  # loops if continue_game stays True

    guess = (input("\nGuess a letter: ")).lower()
    guess_history.append(guess)   # stores guesses in a list for future checking
    cls()
    print(banner)

    for index in range(0, len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess              # if guess letter is correct, assign to display

    if guess not in chosen_word:                # if guess letter is not in word (wrong guess)
        if not guess_history.count(guess) > 1:  # checks if guess letter is not repeated by checking guess_history list
            lives -= 1                          # deduct life
            hangman_index += 1                  # add + 1 to Hangman list
            print(f"You've guessed a wrong letter. The letter '{guess}' is not in the word.\nYou lose a life.\n")
        else:  # means the guess letter was repeated, no need to deduct life
            print(f"You've guessed a wrong letter. The letter '{guess}' is not in the word.\n")

    if guess_history.count(guess) > 1:  # this checks for correct guess if repeated:
        print(f"Reminder: You entered a letter ({guess}) which you have already guessed before!\n")

    str_display = ' '.join(display)  # convert the display list to string
    print("Word: " + str_display)    # prints the new display list
    print(Hangman[hangman_index])    # prints corresponding Hangman list

    if "_" not in display:     # if there is no blank in display, player wins
        continue_game = False
        print("\n\nCongratulations! You win!")
    elif lives == 0:            # if lives were dropped to 0, player loses
        continue_game = False
        print("\n\nYou lose!")
        print(f"The correct answer is {chosen_word}")


