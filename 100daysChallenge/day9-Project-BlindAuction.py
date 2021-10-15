logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print(logo)
print("\n\n----------------------------------------------")
print("|      Welcome to Blind Auction!             |")
print("----------------------------------------------\n\n")

score_sheet = []
players = {}
auction_continues = True


def calculate(players_tally):  # players_tally should look like {"Eduard": 25, "Janine": 26} (from players dictionary)
    highest_bid = 0
    winner = ''
    for player in players_tally:
        if players_tally[player] > highest_bid:  # checks for every value of a key and compare to highest bid
            highest_bid = players_tally[player]
            winner = player

    print(logo)
    print(f"\n\n\nThe winner of blind auction is {winner} with a bid of ${highest_bid}!")


while auction_continues:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    players[name] = bid

    choice = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if choice == 'yes':
        auction_continues = True
        # clear the screen here
    elif choice == 'no':
        auction_continues = False
        calculate(players)       #  {"name": bid, "name": bid}
    else:
        print("\n\nInvalid answer. Please restart the bidding process.\n")

