
def piecesApple():
    appleFunc = int(input("Enter the number of apples to be purchased: "))
    return appleFunc

def piecesOrange():
    orangeFunc = int(input("Enter the number of oranges to be purchased: "))
    return orangeFunc

def displayOutput(appleF, orangeF):
    print(f"The total amount is {appleF + orangeF} pesos.")

apple = piecesApple()*20
orange = piecesOrange()*25
displayOutput(apple, orange)