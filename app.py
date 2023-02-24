from os import system
import random

# o funcție care va genera un număr aleatoriu între x și y
def random_numbers(x, y):
    return random.randint(x, y)

# o funcție care va curăța ecranul terminalului
def clear_terminal():
    system("cls")

# o funcție care va imprima un rând nou
def newLine():
    print("\n")

# generăm numere random pentru variabilele care reprezintă poziția roboțelului, bombele, inima si monedele,
# cât și lungimea hărții și starea inițială a punctelor de viață și baterie a roboțelului
LENGTH = random_numbers(20, 40)
roboX  = random_numbers(1, LENGTH)
roboHP, roboBT = [random_numbers(60, 100) for _ in range(2)]
bombX, bombX2 = random_numbers(1, LENGTH), random_numbers(1, LENGTH)
heart, coinX, coinX2, superCoinX = [random_numbers(1, LENGTH) for _ in range(4)]

score  = 0
stepMap = 0
option = ""    # variabila in care vom citi optiunea aleasa de utilizator

symbols = {
    "bomb":      "💣",   # simbolul pentru bomba
    "robo":      "🤖",   # simbolul pentru roboțel
    "hp":        "💓",   # simbolul pentru HP
    "coin":      "🪙",   # simbolul monedei
    "superCoin": "💵",   # simbolul super monedei
}

# bucla jocului
while True:
    stepMap+=1
    
    # 1. desenam harta jocului
    clear_terminal()
    newLine()
    for x in range(1, LENGTH + 1):
        if x == roboX:
            print(symbols["robo"], end=" ")
        elif x == bombX or x == bombX2:
            print(symbols["bomb"], end=" ")
        elif x == heart:
            print(symbols["hp"], end=" ")
        elif x == coinX or x == coinX2:
            print(symbols["coin"], end=" ")
        elif x == superCoinX and stepMap % 10 in [0, 1, 2] :
            print(symbols["superCoin"], end=" ")
        else:
            print(".", end=" ")
            
    newLine()
    print(f"HP: {roboHP}")
    print(f"BT: {roboBT}%")
    print(f"Score: {score}")
    newLine()
    
    # 1. desenam harta jocului
    if roboBT >= 1:
        # 2. citim optiunea aleasa de utilizator
        option = input(">>> ")
        # 2. citim optiunea aleasa de utilizator

        # 3. luam decizia corespunzatoare optiunii alese de utilizator
        if option == "a" and roboX > 1:
            roboX -= 1
            roboBT -= 1

        if option == "d" and roboX < LENGTH:
            roboX += 1
            roboBT -= 1

        # verificam daca s-a ajuns la bomba
        if roboX in (bombX, bombX2):
            if roboX == bombX:
                bombX = random_numbers(1, LENGTH)
            if roboX == bombX2:
                bombX2 = random_numbers(1, LENGTH)
            roboHP -= random_numbers(1, 10)
            if roboHP < 1:
                print("Ops, you lost the game!")
                
        # verificam daca s-a ajuns la HP+
        elif roboX == heart:
            if roboHP < 100:
                roboHP += 10
            if roboBT < 100:
                roboBT += random_numbers(1, 5)
            heart = random_numbers(1, LENGTH)

        # verificam daca s-a ajuns la coinX
        elif roboX in (coinX, coinX2):
            if roboX == coinX:
                coinX = random_numbers(1, LENGTH)
            if roboX == coinX2:
                coinX2 = random_numbers(1, LENGTH)
            score += random_numbers(1, 5)
        
        # verificam daca s-a ajuns la superCoin
        elif roboX == superCoinX:
            score += random_numbers(5, 20)
            superCoinX = random_numbers(1, LENGTH)
            
        elif option == "x":
            clear_terminal()
            print("Thank you for playing !")
            break
        # 3. luam decizia corespunzatoare optiunii alese de utilizator
    else:
        print("Ops, you lost the game, your battery is dead!")
        break