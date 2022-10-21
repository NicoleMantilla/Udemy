#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random 
palabra = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#if the letter at that position matches 'guess' the reveal that letter un the display at that position. 
adivina = input("Dime una letra: ")

for letra in palabra: 
  if letra == adivina:
    print("Vas bien.")
  else:
    print("Esa no era")

#TODO-3 - print 'display' you should see the guessed letter in the correct position and every other letter replace with'_'

