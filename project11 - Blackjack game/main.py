import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
BLACKJACK = 21
DEALER_MIN_SCORE = 17

def create_deck() -> list[int]:
    """Create a new deck."""
    return cards.copy()

def get_cards(deck: list[int], amount: int) -> list[int]:
    drawn_cards = random.sample(deck, k=amount)
    for card in drawn_cards:
        deck.remove(card)
    return drawn_cards

def sum_cards(card_list: list[int]) -> int:
    return sum(card_list)

def cards_printer(cards_list: list[int]) -> str:
    """Format cards as a string."""
    return ', '.join(map(str, cards_list))

def blackjack():
    deck = create_deck()
    my_deck = get_cards(deck, 2)
    dealer_cards = get_cards(deck, 2)

    while True:
        print(f"    Your cards: [{cards_printer(my_deck)}], your score: {sum_cards(my_deck)}")
        print(f"    Dealer first card: {dealer_cards[0]}")

        if sum(my_deck) < BLACKJACK:
            draw = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()

            if draw == 'y':
                my_deck += get_cards(deck, 1)
            elif draw == 'n':
                while sum_cards(dealer_cards) < DEALER_MIN_SCORE:
                    dealer_cards += (get_cards(deck, 1))

                print(f"    Your final hand [{cards_printer(my_deck)}], your score: {sum_cards(my_deck)}")
                print(f"    Dealer final hand [{cards_printer(dealer_cards)}], your score: {sum_cards(dealer_cards)}")

                if sum_cards(dealer_cards) > BLACKJACK or sum_cards(my_deck) > sum_cards(dealer_cards):
                    print("You win!")
                    break
                elif sum_cards(my_deck) == sum_cards(dealer_cards):
                    print("It's a draw")
                    break
                else:
                    print("Dealer wins")
                    break
            else:
                print("Invalid input. Please type 'y' or 'n'.")
        else:
            print(f"    Your final hand: [{cards_printer(my_deck)}], your score: {sum_cards(my_deck)}")
            print(
                f"    Dealer's final hand: [{cards_printer(dealer_cards)}], dealer's score: {sum_cards(dealer_cards)}")
            print("You went over! You lose!")
            break

if __name__ == '__main__':
    blackjack()

