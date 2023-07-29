print("Welcome to the secret question program")

name = ["May", "Amy", "Ronk", "Fav"]
#input("What's your name? ")
bid = 100, 90, 121, 10
#input("What is your bid? $")

bid_infor = {
  "name": [name], "bid": [bid]
}
roundup = "no"
# input("Are there any other bidders? Type Yes or No ").lower()

if roundup == "yes":
  print("clear")
else:
  lists = []
  for bid in bid_infor[bid]:
    no_of_bids = bid
    print(no_of_bids)
    lists = lists.append(no_of_bids)
    lists = sorted(lists)
    highest_no = max(lists)
  print(highest_no)
    