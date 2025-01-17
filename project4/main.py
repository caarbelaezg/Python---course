import random
import figures

figures_array = [figures.paper, figures.rock, figures.scissors]

def rock_paper_scissors():
    user_input = int(input("Pick: 0 - Paper, 1 - Rock, 2 - Scissors "))
    print("You choose")
    if user_input >= 3 or user_input < 0:
        print("invalid input value")
        return
    print(figures_array[int(user_input)])
    machine_input = random.randint(0, 2)
    print("Machine choose")
    print(figures_array[int(machine_input)])
    validate_winner(user_input, machine_input)



def validate_winner(user_input, machine_input):
    if user_input == 2 and machine_input == 0:
        print("You win!")

    if user_input < machine_input :
        print("you win")

    if user_input > machine_input:
        print("you lose")



if __name__ == '__main__':
    rock_paper_scissors()
