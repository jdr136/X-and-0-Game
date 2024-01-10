import random
import time 

b = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def printBoard():
    for row in range(0,3):
        print("-------------")
        print(f"| {b[row][0]} | {b[row][1]} | {b[row][2]} |")
    print("-------------")

def checkWin(sym):
    win = 0
    for i in range(0,3):
        if b[i][0] == b[i][1] and b[i][0] == b[i][2] and b[i][0] != " ": 
            win = 1
        if b[0][i] == b[1][i] and b[0][i] == b[2][i] and b[0][i] != " ": 
            win = 1

    if b[0][0] == b[1][1] and b[0][0] == b[2][2] and b[0][0] != " ":
        win = 1
    if b[0][2] == b[1][1] and b[0][2] == b[2][0] and b[0][2] != " ":
        win = 1
    
    if win == 1:
        return True 
    return False

def getCoords(move):
    movePart = move.split()
    x = int(movePart[0])
    y = int(movePart[1])
    return x, y


def getMove():
    print()
    print("Where would you like to play?")
    move = input("> ")
    x,y = getCoords(move)
    

    while x not in [1,2,3] or y not in [1,2,3] or b[x-1][y-1] != " ":
        print("Sorry, that square is invalid or taken. Please choose again. ")
        move = input("> ")
        x,y = getCoords(move)
        
    return x-1, y-1

def botMove(botSym):
    botX = random.randint(0, 2)
    botY = random.randint(0, 2)
    while b[botX][botY] != " ":
        botX = random.randint(0, 2)
        botY = random.randint(0, 2)

    b[botX][botY] = botSym

def win(sym):
    time.sleep(1)
    print()
    print("#######")
    print(sym + " WINS!")

    

def placeToken(sym, x, y):
    b[x][y] = sym

def reset(): 
    for row in range(0,3):
        for col in range(0,3): 
            b[row][col] = " "
    main()


def onePlayer():
    print()
    print("#### ONE PLAYER MODE #####") 
    print()
    print("Do you wan't to be X or 0? ")
    sym = input("> ")
    while (sym not in ["X","0"]):
        print("Sorry, please enter 'X' or '0'")
        sym = input("> ")

    if sym == "X":
        botSym = "0"
    else: 
        botSym = "X"   

    print()
    print("")
    first = random.randint(0,2)
    if first == 0:
        print("The bot is to go first. ")
        time.sleep(1)
        botMove(botSym)
        printBoard()
    else: 
        print("You are to go first. ")
        time.sleep(1)
        printBoard()

    while True: 
        x, y = getMove()
        placeToken(sym, x, y)
        printBoard()
        if checkWin(sym):
            win(sym)
            break
        time.sleep(1)
        print()
        print("### Now the Bot's move ###")

        botMove(botSym)
        printBoard()
        if checkWin(botSym):
            win(botSym)
            break
        

    print()
    print("Would you like to play again? ")
    playAgain = input("> ")

    while playAgain not in ["Y", "N"]:
        print("Sorry, please enter Y or N")
        playAgain = input("> ")

    if playAgain == "N":
        exit()
    elif playAgain == "Y":
        print()
        reset()
    

def twoPlayer():
    print()
    print("#### TWO PLAYER MODE #####") 
    print() 

    print("Player 1 is X, Player 2 is 0")
    
    first = random.randint(0,2)
    if first == 0:
        print("X is to go first")
        sym = "X"
    else: 
        print("0 is to go first")
        sym = "0"
    printBoard()

    while True: 
        x,y = getMove()
        placeToken(sym, x, y)
        printBoard()
        if checkWin(sym):
            win(sym)
            break
        time.sleep(1)
        if sym == "X":
            sym = "0"
        else: 
            sym = "X"
        print("It is "+sym+"'s turn")
    
    print()
    print("Would you like to play again? ")
    playAgain = input("> ")

    while playAgain not in ["Y", "N"]:
        print("Sorry, please enter Y or N")
        playAgain = input("> ")

    if playAgain == "N":
        exit()
    elif playAgain == "Y":
        print()
        reset()

def main(): 
    print("Hello, welcome to X and O, the fun parlor game!")
    print("1 or 2 players? ")
    
    playerNum = input("> ")
    while (playerNum not in ["1","2"]):
        print("Sorry, please enter '1' or '2'")
        playerNum = input("> ")

    print("Very well, "+playerNum+" player it is then. Lets get started.")

    if playerNum == "1":
        onePlayer()
    elif playerNum == "2":
        twoPlayer()



if __name__ == "__main__":
    main()


