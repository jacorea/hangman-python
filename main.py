#Step 5

import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
word_count = 0
# Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Create blanks
display = []
for i in range(word_length):
    display += "_"

print(f"{' '.join(display)}")

# make end condition
end_of_game = (word_count == word_length)

# when word not guessed and still have lives 
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You've already guessed {guess}.\n Please choose another letter")
      word_count -= 1
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        if letter == guess:
            display[position] = letter
            word_count += 1

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(hangman_art.stages[lives])
        lives -= 1
        print(f"you have {lives} left.")

        if lives == 0:
            print(hangman_art.stages[lives])
            print("you lose.")
            print("The word was: " + chosen_word)
            end_of_game = True

    #Join all the elements in the list and turn it into a String.
    if word_length > word_count and lives > 0:
      print(f"{' '.join(display)}")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    #TODO-4: - if the user has guessed all the letters in the chosen_word then print "You win!" and set 'end_of_game' to True.
    if word_count == word_length:
        print("you win!")
        print(f"your word was {chosen_word}.")
        end_of_game = True