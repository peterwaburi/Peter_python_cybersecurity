import random
words = ["python", "programming", "challenge", "developer", "function", "variable", "data", "structure", "object"]
secret_word = random.choice(words) 

letter_count=len(secret_word)
print(f"The secret word is: {"_ "*letter_count}")


# Set max attempts
max_attempts = 6

# Create a list to track letters
guessed_letters=[]


# Fun ction to display th progress
def display_progress():
    # Assume guessed word is empty
    guessed_word=""

    # Loop through the leetters in the secret word
    for letter in secret_word:
        # Check if the letter is in guessed letters
        if letter.lower() in guessed_letters:
            guessed_word +=letter+ ""
        else:    
            guessed_word += "_ "
    
    # Return the guessed word
    return guessed_word


# Function to check if the user has guessed all letters from the secret word
def completed():
    # We make an assumption that they are done
    done=True
    #validate truly if they are done
    for letter in secret_word:
        if letter.lower() not in guessed_letters:
            done=False
            break

    # Return value for done
    return done

# Get user input in a loop as long as attempts are available
while max_attempts > 0:
    # Prompt user to enter their guess
    guess = input("Guess a letter (Only one alphabet at a time): ").lower()

    # Check if tyhe guess in not an empty string or a number or more than one letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter as ingle alphabet!")

    #  heck if the letter was already guessed
    elif guess in guessed_letters:
        print("You already guessed this letter!. Try a different one")

    # The guess is valid 
    else:
        # Add to the list oof guessed letters
        guessed_letters.append(guess)

         # Check if the guessed letter is in  the secret word
        if guess in secret_word.lower():
            print(f"Correct!, {guess} is in the word")
            print(f"The progress so far is: {display_progress()}")
        else:
            print(f"Incorrect {guess} is not in the word")    
            # Update the attempts
            max_attempts -=1
            print(f"Attempts left: {max_attempts}")

        # Check if user is done
        done=completed

        if done: 
            print(f"You won!!, the word was {secret_word}")
            break

# If attempts are depleated
else:
    print(f"You lost! The word was {secret_word}")
