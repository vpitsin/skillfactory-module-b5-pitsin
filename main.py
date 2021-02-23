v = "|"     #горизонтальная палка
p1, p2 ="X", "O"

def print_pole(sl):    #красивое полюшко-поле
    print("  "+"0"+" "+"1"+" "+"2")
    print("0"+v+sl[0][0]+v+sl[0][1]+v+sl[0][2])
    print("1"+v+sl[1][0]+v+sl[1][1]+v+sl[1][2])
    print("2"+v+sl[2][0]+v+sl[2][1]+v+sl[2][2])

def order(sl):
    x_count = sl[0].count("X") + sl[1].count("X") + sl[2].count("X")
    o_count = sl[0].count("O") + sl[1].count("O") + sl[2].count("O")
    if x_count>o_count:
        player=p2
        print ("Сейчас ходит O")
    else:
        player=p1
        print("Сейчас ходит X")
    return player

def vvod():    #проверка на корректность ввода - чтобы не буковки и циферки тоже не все
    while True:
        try:
            s = int(input("Введите номер строки:"))
            r = int(input("Введите номер столбца:"))
            if s>2 or r>2 or s<0 or r<0:
                raise  Exception
            return (s, r)
            break
        except Exception:
            print('Неверный ввод. Повторите, пожалуйста.')

def hod(player, sl):
    while True:
        try:
            s,r =vvod()
            if sl[s][r] != "_":
                raise Exception
            sl[s][r] = player
            break
        except Exception:
            print('Клетка занята. Попробуйте другую.')
    print_pole(sl)


def check_win(sl):
    for n in range(3):
        if (sl[n][0]==sl[n][1]==sl[n][2] and sl[n][0]!="_"):
            print ("Победитель "+sl[n][0])
            return ("finish")
        elif (sl[0][n]==sl[1][n]==sl[2][n] and sl[0][n]!="_"):
            print ("Победитель "+sl[0][n])
            return ("finish")
        elif (sl[0][0]==sl[1][1]==sl[2][2] and sl[1][1]!="_") or (sl[0][2]==sl[1][1]==sl[2][0] and sl[1][1]!="_"):
            print ("Победитель "+sl[1][1])
            return ("finish")
        elif (sl[0].count("X") + sl[1].count("X") + sl[2].count("X")+
              sl[0].count("O") + sl[1].count("O") + sl[2].count("O")>=9):
            print ("Ничья")
            return ("finish")
    else:
        return ("continue")


def game():
    while True:
        print ("Для начала новой игры введите: 1")
        start_game=input()
        if start_game=="1":
            pole = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
            print_pole(pole)
            while check_win(pole)!="finish":
                hod(order(pole), pole)
        else:
            exit()
    else:
        exit()


game()