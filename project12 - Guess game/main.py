import random

LIFE_POINTS = {
    "easy": 15,
    "medium": 10,
    "hard": 5,
}


RANDOM_NUMBER_RANGE = (1, 100)

def get_user_guess() -> int:
    while True:
        try:
            return int(input("Make a guess: ").strip())
        except ValueError:
            print("Please enter a valid number.")

def play(life: int, number_to_guess: int):
    print(f"You have {life} attempts to guess the number")
    guess = int(input("Make a guess: ").lower().strip())

    while life > 0:
        guess = get_user_guess()

        if guess == number_to_guess:
            print(f"🎉 You guessed the number: {number_to_guess}!")
            return

        life -= 1
        if guess > number_to_guess:
            print("Too high.")
        else:
            print("Too low.")

        if life > 0:
            print(f"You have {life} attempts remaining.")
        else:
            print(f"😢 Game over! The correct number was {number_to_guess}.")


def guessing_game():
    random_number = random.randint(*RANDOM_NUMBER_RANGE)
    print(f"I'm thinking of a number between {RANDOM_NUMBER_RANGE[0]} and {RANDOM_NUMBER_RANGE[1]}.")

    difficulty = input("Choose a difficulty (easy, medium, hard): ").strip().lower()
    while difficulty not in LIFE_POINTS:
        print("Invalid difficulty. Please choose: easy, medium, or hard.")
        difficulty = input("Choose a difficulty (easy, medium, hard): ").strip().lower()

    play(LIFE_POINTS[difficulty], random_number)



if __name__ == '__main__':
    guessing_game()

