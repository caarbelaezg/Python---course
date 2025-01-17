import os
bid_dict = {}



def bid():
    add_bidder = True
    while add_bidder:
        name = input("What's your name: ").strip()
        while True:
            try:
                price = float(input("What's your bid price: "))
                break
            except ValueError:
                print("Please enter a valid number for the bid price.")

        bid_dict[name] = price
        os.system('cls')

        new_bidder = input("Is there another bidder? (yes/no): ").strip().lower()
        if new_bidder != "yes":
            add_bidder = False


    if bid_dict:
        winner = max(bid_dict, key=bid_dict.get)
        winning_bid = bid_dict[winner]
        print(f"The winner is {winner} with a bid of ${winning_bid:.2f}")
    else:
        print("No bids were placed.")


if __name__ == '__main__':
    bid()

