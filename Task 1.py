import random

def get_random_word():
    word_list = ['python', 'hangman', 'challenge', 'programming', 'openai', 'gpt']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts_left = 6  # You can change the difficulty here

    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        print("Attempts left:", attempts_left)
        
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman()
