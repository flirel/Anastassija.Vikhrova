 import tkinter as tk
import tkinter.ttk as ttk
from random import choice,randint,sample,shuffle
    
OX = ['O', 'X']
VINS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
PS = [[0, 2, 6, 8], [1, 3, 5, 7]]
S='Сыграно игр: {}.\nИз них:\n    побед - {};\n    поражений - {};\n    ничьих - {}.'
    
class Square(tk.Label):
    '''Создаёт ячейки для игры "Крестики - Нолики"'''
    def __init__(self, fr, app, c, r, num, **kwargs):
        self.app = app
        self.square_num = num
        kwargs.update({'font': 'Menlo 100', 'bd': 3, 'anchor': 'center', 'relief': 'raise', 'width': 2})
        tk.Label.__init__(self, fr, **kwargs)
        self.grid(column=c, row=r+2, sticky='nsew')
    
    def bind_(self):
        '''Назначает ячейке событие "Нажатие мышкой" с передачей номера ячейки в вызываемую функцию'''
        self.bind("<Button-1>", lambda x: App.turn_user(self.app, self.square_num))
    
    
class App(tk.Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        # статистика игры
        self.drawn_game = 0
        self.user_win = 0
        self.pc_win = 0
        self.create_widgets()
    
    def create_widgets(self):
        # статистика
        statistics = ttk.LabelFrame(self, text='Статистика')
        statistics.grid(column=0, row=0, rowspan=2, sticky='nsew')
        self.stat_msg = tk.StringVar(value=S.format(0,0,0,0))
        ttk.Label(statistics, textvariable=self.stat_msg, justify='left').grid()
    
        # Выбор хода
        step_choice = ttk.LabelFrame(self, text='Выбрать ход')
        step_choice.grid(column=1, row=0, rowspan=2, sticky='nsew')
        self.step = tk.IntVar()
        step0 = ttk.Radiobutton(step_choice, text='Случайным', variable=self.step, value=0)
        step1 = ttk.Radiobutton(step_choice, text='Первым', variable=self.step, value=1)
        step2 = ttk.Radiobutton(step_choice, text='Вторым', variable=self.step, value=2)
        step0.grid(column=0, row=0, sticky='we')
        step1.grid(column=0, row=1, sticky='we')
        step2.grid(column=0, row=2, sticky='we')
    
        # Выбор знака
        sign_choice = ttk.LabelFrame(self, text='Выбор знака')
        sign_choice.grid(column=2, row=0, sticky='nsew')
        self.sign = tk.IntVar()
        sign0 = ttk.Radiobutton(sign_choice, text='Ваш знак "0"', variable=self.sign, value=0)
        sign1 = ttk.Radiobutton(sign_choice, text='Ваш знак "X"', variable=self.sign, value=1)
        sign0.grid(column=0, row=0, sticky='we')
        sign1.grid(column=0, row=1, sticky='we')
        # кнопка старт
        btn = ttk.Button(self, text="Старт", command=self.start)
        btn.grid(column=2, row=1, sticky='nsew')
    
        # Статус игры
        status = ttk.LabelFrame(self, text='Статус игры')
        status.grid(column=0, row=2, columnspan=3, sticky='nsew')
        self.status_msg = tk.StringVar(value='Здарова, братан!Ну что, поиграем?')
        ttk.Label(status, textvariable=self.status_msg).grid()
    
        self.widgets = [sign0, sign1, step0, step1, step2, btn]  #все радиокнопки и кнопка для активации и деактивации
    
        fr=tk.Frame(self)
        fr.grid(column=0, row=3, columnspan=3)
        self.squares = [Square(fr, self, i % 3, i // 3, i) for i in range(9)]  #список полей
    
    def start(self):
        self.continue_ = True
        self.board = [''] * 9
        self.free_squares = [x for x in range(9)]
        self.status_msg.set('Игра началась! Забей, ты всё равно проиграешь')
        for square in self.squares:
            square.bind_()
            square.config(background='white', text='')
        if self.step.get() == 2:
            self.turn_pc()
        elif self.step.get() == 0:
            if choice([1, 2]) == 2:
                self.turn_pc()
        self.widget_state()
    
    def widget_state(self, wst='disabled'):
        for widget in self.widgets:
            widget.config(state=wst)
    
    def find_best_turn(self, sign):
        for iturn in self.free_squares:
            iboard = self.board[:]
            iboard[iturn] = sign
            for a, b, c in VINS:
                if iboard[a] == iboard[b] == iboard[c] == sign:
                    return iturn
    
    def default_choice(self):
        choise = [4]
        for i in PS:
            shuffle(i)
            choise.extend(i)
        for iturn in choise:
            if iturn in self.free_squares:
                return iturn
    
    def turn_pc(self):
        ''' ход пк '''
        square_num = self.find_best_turn(not self.sign.get())
        if square_num == None:
            square_num = self.find_best_turn(self.sign.get())
            if square_num == None:
                square_num = self.default_choice()
        self.turn(square_num, not self.sign.get())
    
    def turn(self, square_num, sign):
        square = self.squares[square_num]
        square.unbind("<Button-1>")             #отключает ячейку
        square.config(text=OX[sign])            #пишет символ в ячейку
        self.board[square_num] = sign
        self.free_squares.remove(square_num)
        self.test_win(sign)
    
    def turn_user(self, square_num):
        ''' ход игрока '''
        self.turn(square_num, self.sign.get())
        if self.continue_:
            self.turn_pc()          #передача хода компьютеру
    
    def test_win(self, sign):
        ''' определение исхода игры '''
        for a, b, c in VINS:
            if self.board[a] == self.board[b] == self.board[c] == sign:
                if sign == self.sign.get():
                    self.status_msg.set('Да я тебе поддался, чё ты.')
                    self.user_win += 1
                    color = 'lime'
                else:
                    self.status_msg.set('Лох, Я предупреждал')
                    self.pc_win += 1
                    color = 'orchid'
                for i in a, b, c:
                    self.squares[i].config(background=color)    #окраска выигравших или проигравших ячеек
                for i in self.free_squares:
                    self.squares[i].unbind("<Button-1>")        #в случае выигрыша делает оставшиеся ячейки не активными
                self.game_over()
                return
    
        if not self.free_squares:
            self.status_msg.set('Ну ты пытался, азахаахахах.')
            self.drawn_game += 1
            [square.config(background='gold') for square in self.squares]
            self.game_over()
    
    def game_over(self):
        ''' окончание игры '''
        self.continue_ = False
        self.stat_msg.set(S.format(self.user_win + self.pc_win + self.drawn_game, self.user_win, self.pc_win, self.drawn_game))
        self.widget_state('normal')
    
    
def main():
    root = tk.Tk()
    root.title("Тупая игра")
    root.resizable(False, False)
    App(root).grid()
    root.mainloop()
    
if __name__=='__main__':
    main()