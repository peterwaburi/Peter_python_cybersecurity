import random
words = ["python", "programming", "challenge", "developer", "function", "variable", "data", "structure", "object"]
word = random.choice(words) 


guesses = ["."] * len(word)
attempts = 6

print("-----Welcome to the Word Guessing Game!-----")
print("I have selected a word. Can you guess it?")


def display_word_progress():
    print("The word is:"+"".join(guesses))

while attempts>0:
        display_word_progress()
        guesses=input("guess a letter(can only be one letter)").lower()

    
# display_word_progress()