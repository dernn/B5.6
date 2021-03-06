def game_over(checkline):
    print(f'~~~~~~~~~~~~~')
    print(f'   {checkline[0]} WINS!   ')
    print(f'~~~~~~~~~~~~~')


def salut():
    print('===========================')
    print('||      Tic-Tac-Toe      ||')
    print('|| (Noughts and Crosses) ||')
    print('===========================')
    print()
    input('Press Enter to continue...')
    print()
    print('Guide: ++++++++++++++++++++')
    print('|| input format: x y     ||')
    print('|| x  -  string          ||')
    print('|| y  -  column          ||')
    print('+++++++++++++++++++++++++++')
    print()
    input('Press Enter to begin...')


def show():
    print()
    print('  | 0 | 1 | 2 |')
    for i, row in enumerate(field):
        row_str = str(i) + ' | ' + ' | '.join(row) + ' | '
        print(row_str)
    print()


def turn():
    while True:
        grid = input('        Your turn: ').split()
        if len(grid) < 2:
            print('Enter 2 numbers!')
            continue

        x, y = grid
        if not x.isdigit() or not y.isdigit():
            print('Enter the numbers!')
            continue

        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Out of range!')
            continue

        if field[x][y] != ' ':
            print('Slot is busy!')
            continue

        return x, y


def win_check():
    winbox = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
              ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
              ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for line in winbox:
        checkline = []
        for i in line:
            checkline.append(field[i[0]][i[1]])
        if len(set(checkline)) == 1 and ' ' not in checkline:
            game_over(checkline)
            return True


salut()

field = [[' '] * 3 for i in range(3)]
num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print('Crosses!')
    else:
        print('Noughts!')

    x, y = turn()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if win_check():
        break

    if num == 7:
        print('Endgame!')
    if num == 9:
        print('Draw!')
        break
