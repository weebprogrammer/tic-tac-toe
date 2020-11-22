board = [[" ", "0", "1", "2"],
         ["0", "-", "-", "-"],
         ["1", "-", "-", "-"],
         ["2", "-", "-", "-"]]
def playBoard():
    for i in range(4):
        print(board[i][0], board[i][1], board[i][2], board[i][3])
playBoard()
print("Это наше игровое поле. ")
def X():
    print("----------сейчас ход крестика----------")
    string = int(input("Введите номер строки: "))
    column = int(input("Введите номер колонки: "))
    if string >= 0 and column <= 2 and board[string + 1][column + 1] != "O" and board[string + 1][column + 1] != "X":
        board[string + 1][column + 1] = "X"
    else:
        print("!!!!!Выберите другую клетку!!!!!")
def O():
    print("----------сейчас ход нолика----------")
    string = int(input("Введите номер строки: "))
    column = int(input("Введите номер колонки: "))
    if string >= 0 and column <= 2 and board[string + 1][column + 1] != "O" and board[string + 1][column + 1] != "X":
        board[string + 1][column + 1] = "O"
    else:
        print("!!!!!Выберите другую клетку!!!!!")
def checkWin():
    for i in range(1,4):
        if board[i][1] == board[i][2] == board[i][3] == "X":
            print("!!!!!!!!!!КРЕСТИК ПОБЕДИТЕЛЬ!!!!!!!!!!")
            return True
        elif board[i][1] == board[i][2] == board[i][3] == "O":
            print("!!!!!!!!!!НОЛИК ПОБЕДИТЕЛЬ!!!!!!!!!!")
            return True
        elif board[1][i] == board[2][i] == board[3][i] == "X":
            print("!!!!!!!!!!КРЕСТИК ПОБЕДИТЕЛЬ!!!!!!!!!!")
            return True
        elif board[1][i] == board[2][i] == board[3][i] == "O":
            print("!!!!!!!!!!НОЛИК ПОБЕДИТЕЛЬ!!!!!!!!!!")
            return True
        elif board[1][1] == board[2][2] == board[3][3] == "X":
            print("!!!!!!!!!!КРЕСТИК ПОБЕДИТЕЛЬ!!!!!!!!!!")
            return True
        elif board[1][1] == board[2][2] == board[3][3] == "O":
            print("!!!!!!!!!!НОЛИК ПОБЕДИТЕЛЬ!!!!!!!!!!")
            return True
        elif board[1][3] == board[2][2] == board[3][1] == "X":
            print("!!!!!!!!!!КРЕСТИК ПОБЕДИТЕЛЬ!!!!!!!!!!")
            return True
        elif board[1][3] == board[2][i] == board[3][1] == "O":
            print("!!!!!!!!!!НОЛИК ПОБЕДИТЕЛЬ!!!!!!!!!!")
            return True
def picPlayer():
    print("За кого будем играть")
    corz = input("Крестик или нолик: ")
    if corz == "x" or corz == "X":
        return 1
    elif corz == "o" or corz == "O":
        return 2
    else:
        print("!!!Введите правильно!!!")
if picPlayer() == 1:
    while True:
        X()
        playBoard()
        if checkWin() is True:
            break
        O()
        playBoard()
        if checkWin() is True:
            break
else:
    while True:
        O()
        playBoard()
        if checkWin() is True:
            break
        X()
        playBoard()
        if checkWin() is True:
            break
