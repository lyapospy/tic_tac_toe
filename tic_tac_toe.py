def console_field():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

def ask():
    while True:
        cords = input("        Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print(" Некрорректный диапазон! ")
            continue

        if field[x][y] != "-":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл нолик!")
            return True
    return False

print("Формат хода по координатам x (строка) y (столбец) ")
field = [["-"] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    console_field()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print("Ничья!")
        break