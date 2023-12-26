import random

class Hangman:
    def __init__(self,word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess_lower = guess.lower()
        if guess_lower in self.word:
            print(f'Good guess! {guess_lower} is in the word')
            for letter in range(0,len(self.word)):
                if self.word[letter] == guess_lower:
                    self.word_guessed[letter] = guess_lower
            self.num_letters-=1
        else:
            self.num_lives-=1
            print(f"Sorry, {guess_lower} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        while(True):
            guess = input("Guess the letter:")
            if not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


hangman = Hangman(['durian', 'banana', 'mango', 'melon', 'strawberry'])
hangman.ask_for_input()