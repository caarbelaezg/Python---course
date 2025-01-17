import random

word_list = ['chocha', 'culo', 'teta']

guess = random.choice(word_list)
guess_len = len(guess)
guess_list = list(guess)

lives = len(guess)
win = False
blank_spaces_arr = ['_' for i in range(0, guess_len)]

while lives > 0 and not win:
    blank_spaces = ''.join(blank_spaces_arr)
    print(blank_spaces)

    guessed_letter = input('Guess a letter: ').lower()
    # TODO: Find the indexes of the occurrences
    idxs = [ i for i, letter in enumerate(guess) if letter == guessed_letter]

    if idxs:
        for i in idxs:
            blank_spaces_arr[i] = guessed_letter
    else:
        print(f"Incorrect guess! The letter '{guessed_letter}' is not in the word.")
        lives -= 1

    if blank_spaces_arr.count('_') == 0:
        win = True

if win:
    print(f"\nCongratulations! You guessed the word: {guess}")
else:
    print(f"\nGame Over! The correct word was: {guess}")



