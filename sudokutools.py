from random import randint
from copy import deepcopy


def cetak(sudogrid):
    hasilcetak = ''
    for i in range(0, 9):
        for j in range(0, 9):
            hasilcetak += str(sudogrid[i][j]) + ' '
            if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
                hasilcetak += '| '

            if (j == 8):
                hasilcetak += '\n'

            if (j == 8) and ((i + 1) % 3 == 0) and (i + 1 != 9):
                hasilcetak += '- - - - - - - - - - - \n'
    return hasilcetak


def getEmpty(sudogrid):
    for i in range(9):
        for j in range(9):
            if sudogrid[i][j] == 0:
                return (i, j)


def cek(sudogrid, pos, num):
    #appearing on the same row
    for row in range(9):
        if sudogrid[row][pos[1]] == num and (row, pos[1]) != pos:
            return False

    #appearing on the same column
    for column in range(9):
        if sudogrid[pos[0]][column] == num and (pos[0], column) != pos:
            return False

    #appearinn on the same grid
    startRow = (pos[0] // 3) * 3
    startCol = (pos[1] // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudogrid[startRow +
                        i][startCol +
                           j] == num and (startRow + i, startCol + j) != pos:
                return False
    return True


def solve(sudogrid):

    # if there is not empty then the board solved
    empty = getEmpty(sudogrid)
    if not empty:
        return True

    for nums in range(9):
        if cek(sudogrid, empty, nums + 1):
            sudogrid[empty[0]][empty[1]] = nums + 1

            if solve(sudogrid):  # recursive step
                return True
            sudogrid[empty[0]][
                empty[1]] = 0  # this number is wrong so we set it back to 0
    return False


def buat():
    sudogrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(0, 9):
        for j in range(0, 9):
            if (randint(1, 7) >= 5):
                sudogrid[i][j] = randint(1, 9)
                if (not cek(sudogrid, (i, j), sudogrid[i][j])):
                    sudogrid[i][j] = 0
    return sudogrid


# print("Randomized Board: ")
# sudogrid = buat()
# print(cetak(sudogrid))

# print("Solution: ")
# solvedgrid = deepcopy(sudogrid)
# solve(sudogrid)

# if (sudogrid == solvedgrid):
#     print("No Solution")
# else:
#     print(cetak(sudogrid))
