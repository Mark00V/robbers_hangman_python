import wordlist
import random
import re
import math

class Start:

    def start(self):
        print("Starting game...")
        while True:
            get_new_word = self.get_new_word()
            this_word = GuessWord(get_new_word)
            print(this_word.print_hangman())
            while True:
                input_letter = input(f"Guesses left: {this_word.guess_left} -> Guess a letter: ")
                if input_letter == 'reveal':
                    print(f"Word revealed: {this_word.revealWord()}")
                    this_word.guess_left += 1
                this_word.revealLetter(input_letter.lower())
                print(f"{this_word}")
                print(this_word.print_hangman())
                if '_' not in str(this_word):
                    print("You won!")
                    break
                if this_word.guess_left == 0:
                    print("You lost!")
                    break
            cont_input = input("New game (y/n)?")
            if cont_input != 'y':
                break


    def get_new_word(self):
        nbr_letters_list = list(wordlist.word_list.keys())
        random_nbr_letters = random.choice(nbr_letters_list)
        random_word = random.choice(wordlist.word_list[random_nbr_letters])
        return random_word
class GuessWord:

    def __init__(self, word):
        self.word = word
        self.hidden = '_' * len(word)
        letters_in_word = len(set(word))
        self.guess_left = math.floor(letters_in_word/3)+2
        self.guess_init = self.guess_left

    def replace_at_position(self, original_string, position, new_substring):
        return original_string[:position] + new_substring + original_string[position + len(new_substring):]

    def revealLetter(self, letter):
        pattern = re.escape(letter)
        matches = re.finditer(pattern, self.word, flags=re.IGNORECASE)
        positions = [match.start() for match in matches]
        if positions:
            for pos in positions:
                self.hidden = self.replace_at_position(self.hidden, pos, letter)
        else:
            self.guess_left -= 1

    def print_hangman(self):
        hangman_parts = [
            """
               _______
              |       |
              |
              |
              |
              |
            """,
            """
               _______
              |       |
              |       O
              |
              |
              |
            """,
            """
               _______
              |       |
              |       O
              |       |
              |
              |
            """,
            """
               _______
              |       |
              |       O
              |      /|
              |
              |
            """,
            """
               _______
              |       |
              |       O
              |      /|\\
              |
              |
            """,
            """
               _______
              |       |
              |       O
              |      /|\\
              |      /
              |
            """,
            """
               _______
              |       |
              |       O
              |      /|\\
              |      / \\
              |
            """
        ]
        if self.guess_left == self.guess_init:
            return hangman_parts[0]
        if self.guess_left > 3:
            return hangman_parts[1]
        elif self.guess_left == 3:
            return hangman_parts[2]
        elif self.guess_left == 2:
            return hangman_parts[3]
        elif self.guess_left == 1:
            return hangman_parts[4]
        elif self.guess_left == 0:
            return hangman_parts[-1]

    def revealWord(self):
        return self.word

    def __str__(self):
        return self.hidden

def main():
    start = Start()
    start.start()

main()

