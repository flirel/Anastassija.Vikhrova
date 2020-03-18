import pygame
pygame.init()
 
X = 300 #ширина
Y = 300 #высота
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
 
def change_color(last):
    if last: 
        pygame.draw.circle(sc, BLUE, (X//2, Y//2), round((X+Y)/5)) #рисуется синий круг 
        last = False
    else:
        pygame.draw.circle(sc, RED, (X//2, Y//2), round((X+Y)/5))#рисуется красный круг
        last = True
    return last
 
 
sc = pygame.display.set_mode((X, Y)) #основное окно
sc.fill(WHITE)
 
rect1left = pygame.Rect((0, 0), (X//2, Y//2)) #задаем область для верхнего левого сектора
rect2left = pygame.Rect((0, Y//2), (X//2, Y//2)) #задаем область для нижнего левого сектора
 
rect1right = pygame.Rect((X//2, 0), (X//2, Y//2)) #задаем область для верхнего правого сектора
rect2right = pygame.Rect((X//2, Y//2), (X//2, Y//2))#задаем область для нижнего правого сектора
 
pygame.draw.circle(sc, BLUE, (X//2, Y//2), round((X+Y)/5)) 
 
pygame.display.update() #обновляем
 
active_all = False
active_leftd = False
active_rightd = False
last = True
 
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_1: #при нажатии кнопки 1 меняюся цвета у секторов 1 и 4
                print('изменения в секторах 1 и 4')
                active_leftd = True
                active_rightd = False
                active_all = False
            elif i.key == pygame.K_2: #меняется цвет у секторов 2 и 3
                print('изменения в в секторах 2 и 3')
                active_rightd = True
                active_leftd = False
                active_all = False
            elif i.key == pygame.K_0: #меняется цвет у всех секторов
                print('изменения во всех секторах')
                active_all = True
                active_leftd = False
                active_rightd = False
 
    last = change_color(last)
 
    if active_all:
        pygame.display.update()
    if active_leftd:
        pygame.display.update((rect1left, rect2right))
    if active_rightd:
        pygame.display.update((rect1right, rect2left))
 
    pygame.time.delay(200)