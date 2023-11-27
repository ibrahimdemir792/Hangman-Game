from wonderwords import RandomWord
import random, hangman_stages

w = RandomWord()



def main():
    remaining_attempts = 6
    guessed_letters = ""
    
    print("Welcome to Hangman!")
    difficulty = select_difficulty()
    word = w.random_words(word_max_length=difficulty, word_min_length=difficulty)
    word = word[0]
    print(word)

    while remaining_attempts > 0 and len(guessed_letters) < len(set(word)):
        guess = guess_letter()
        
        if guess_check(guess, word):
            if guess in guessed_letters:
                print(f"Letter \'{guess}\' is guessed already")
            else:
                print(f"Yes! The letter \'{guess}\' is found")
                guessed_letters += guess
        else:
            print(f"No! The letter \'{guess}\' is not found")
            remaining_attempts -= 1

        print(hangman_stages.get_hangman_stage(remaining_attempts))
        print(f"\n{remaining_attempts} attemps remaining\n")
        print_dashes(word, guessed_letters)

    if len(guessed_letters) == len(set(word)):
        print("+++ You have won the game! +++")
    else:
        print("--- You have lost the game---\n")



def select_difficulty():
    while True:
        try:
            difficulty = int(input("Select difficulty (3-10): "))
            if 3 <= difficulty <= 10:
                return difficulty
            else:
                print("!! Enter an integer between 3-10 !!")
        except:
            print("!! Enter an integer between 3-10 !!")


def print_dashes(word,guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(f"{letter} ", end="", sep=" ")
        else:
            print("_ ", end="", sep=" ")
    print("\n")


def guess_letter():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Guess only one letter")


def guess_check(guess, word):
    if guess in word:
        return True
    else:
        return False



if __name__ == "__main__":
    main()
