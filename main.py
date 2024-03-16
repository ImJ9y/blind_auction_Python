from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bidding_finished = False
bids = {}


def find_higest_bidder(bidding_record):
  # bidding_record = {"name" : bid, "name1" : bid2}
  higiest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = int(bidding_record[bidder])
    if higiest_bid <= bid_amount:
      winner = bidder
      higiest_bid = bid_amount

  print(f"The winner is {winner} with a bid of {higiest_bid}")


print("Welcome to the secret auction program.")

while not bidding_finished:
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  bids[name] = bid
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'")
  if should_continue == "no":
    bidding_finished = True
    find_higest_bidder(bids)
  elif should_continue == "yes":
    clear()
