def printsudoku():
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(sudoku[i][j], end=" ")
        print()
    print()
def busca0(sudoku):
    # print("antes1")
    for x in range(9):
        # print("antes",x)
        for y in range(9):
            # print("antes",y)
            if sudoku[x][y] == 0:
                # print("depues",x)
                # print("depuess",y)
                return x, y
    return -1, -1
def isValid(sudoku, i, j, e):
    fila = all([e != sudoku[i][x] for x in range(9)])
    if fila:
        columna = all([e != sudoku[x][j] for x in range(9)])
        if columna:
            cuadroX, cuadroY = 3 * (i // 3), 3 * (j // 3)
            for x in range(cuadroX, cuadroX + 3):
                for y in range(cuadroY, cuadroY + 3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False
def solveSudoku(sudoku, i=0, j=0):
    i, j = busca0(sudoku)
    # print("i",i)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False
sudoku = [[0, 7, 1, 4, 0, 0, 0, 3, 0],
          [0, 0, 0, 0, 7, 0, 0, 0, 8],
          [9, 0, 0, 2, 0, 0, 4, 0, 0],
          [3, 0, 0, 9, 0, 0, 8, 0, 0],
          [0, 0, 5, 0, 0, 0, 1, 0, 0],
          [0, 0, 7, 0, 0, 3, 0, 0, 5],
          [0, 0, 2, 0, 0, 6, 0, 0, 9],
          [6, 0, 0, 0, 8, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 2, 7, 8, 0]]
if solveSudoku(sudoku):
    printsudoku()
else:
    print("No solution")

# def vavlidacionX(sudoku, filasx, number):
#     for i in range(9):
#         if sudoku[filasx][i] == number:
#             return False
#     return True


# def validacionY(sudoku, columnasy, number):
#     for i in range(9):
#         if sudoku[i][columnasy] == number:
#             return False
#     return True


# def validacionCuadrado(sudoku, filasx, columnasy, number):
#     start_row, start_col = 3 * (filasx // 3), 3 * (columnasy // 3)
#     for i in range(3):
#         for j in range(3):
#             if sudoku[i + start_row][j + start_col] == number:
#                 return False
#     return True
# def validadito(sudoku, filasx, columnasy, number):
#     return vavlidacionX(sudoku, filasx, number) and validacionY(sudoku, columnasy, number) and validacionCuadrado(sudoku, filasx, columnasy, number)
# def busqueda(sudoku):
#     for i in range(9):
#         for j in range(9):
#             if sudoku[i][j] == 0:
#                 return i, j
#     return -1, -1
# def solucionado(sudoku):
#     filasx, columnasy = busqueda(sudoku)

#     if filasx == -1:
#         return True

#     for number in range(1, 10):
#         if validadito(sudoku, filasx, columnasy, number):
#             sudoku[filasx][columnasy] = number

#             if solucionado(sudoku):
#                 return True

#             sudoku[filasx][columnasy] = 0

#     return False
# def sol(sudoku):
#     if not solucionado(sudoku):
#         print("no tiene solucion")
#         return False

#     printsudoku(sudoku)
#     return True

# sol(sudoku)
