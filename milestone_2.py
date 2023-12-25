import random 

word_list = ['durian', 'banana', 'mango', 'melon', 'strawberry']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Guess the word:")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")
