
def amount_money():
    moneyFunc = int(input("Enter the amount of money you have on hand: "))
    return moneyFunc

def apple_price():
    priceFunc = int(input("Enter the price for each apple: "))
    return priceFunc

def displayOutput(pieces_appleF, changeF):
    print(f"You can buy {pieces_appleF} apples and your change is {changeF} pesos.")

money = amount_money()
applePrice = apple_price()
pieces_apple = money // applePrice
change = money % applePrice
displayOutput(pieces_apple, change)