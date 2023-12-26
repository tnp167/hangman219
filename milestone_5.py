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
                if letter == len(self.word)-1:
                    print(self.word_guessed[-1])
                else:
                    print(self.word_guessed[letter], end=' ')
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
            break

word_list = ['durian', 'banana', 'mango', 'melon', 'strawberry']

def play_game(word_list):
    num_lives = 5 
    game = Hangman(word_list,num_lives)
    while(True):
        if game.num_lives == 0:
            print("You Lost")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulation. You won the game!")
            break

play_game(word_list)