stocks = {
        "info": [600,630,620],
        "ril" : [1430,1490,1567],
        "mtl" : [234,180,160]
    }

def print_stocks():
    for key in stocks:
        n = len(stocks[key])
        avg = round((sum(stocks[key])/n), 2)
        print(f"{key} ==> {stocks[key]} ==> avg: {avg}")
            
def add():
    stock = input("Enter stock ticker:").lower()
    new_price = int(input("Enter price:").lower())   
    if stock in stocks:
        stocks[stock].append(new_price)
    else:
        stocks[stock] = [new_price]
    print_stocks()

  
        
def main():
    operation = input(f"Please enter operation value, Either Print of Add: ").lower()
    if operation == "print":
      print_stocks()
    elif operation == "add":
      add()
    else:
        print("Unsupported operation")


if __name__ == '__main__':
    main()