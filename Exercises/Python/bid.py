print("Welcome to Bidding platform")

bidders = {}




continuous = False
while continuous == False:
  name  = input("What is your name? ")
  bid_price = int(input("Please enter your bid price $"))
  bidders[name] = bid_price
  con_question = input("are there other users who want to bid? Enter Yes or No ").lower()
  if con_question == "yes":
    clear = clear
  else:
    continuous = True
    highest_bid = 0
    for n in bidders:
      bid_amount = bidders[n]
      print(bid_amount)
      if bid_amount > highest_bid:
        highest_bid = bid_amount