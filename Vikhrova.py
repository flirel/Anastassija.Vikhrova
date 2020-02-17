from tkinter import * #пакет для графического дизайна
import random #генератор случайных чисел
root = Tk() #окно
root.title('Крестики Нолики') #название окна
Game = True #переменная для игры
field = [] #список для кнопок игрового поля
cross_count = 0 # переменная для ничьи
"""Нажатие кнопок"""
def new_game(): #функция для кнопки "новая игра"
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global Game
    Game = True
    global cross_count
    cross_count = 0
def click(row, col): #функция для нажатия
    if Game and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if Game and cross_count < 5:
            computer_move()
            check_win('O')
"""Проверка победы"""
def check_win(symbol): #функция осущетсвляет проверку победы
#symbol - переменная для символов крестика и нолика
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], symbol)
        check_line(field[0][n], field[1][n], field[2][n], symbol)
    check_line(field[0][0], field[1][1], field[2][2], symbol)
    check_line(field[2][0], field[1][1], field[0][2], symbol)

def check_line(a1,a2,a3,symbol):
    if a1['text'] == symbol and a2['text'] == symbol and a3['text'] == symbol:
        a1['background'] = a2['background'] = a3['background'] = 'lime'
        global Game
        Game = False
def can_win(a1,a2,a3,symbol):
    res = False
    if a1['text'] == symbol and a2['text'] == symbol and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == symbol and a2['text'] == ' ' and a3['text'] == symbol:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == symbol and a3['text'] == symbol:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='новая игра', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()