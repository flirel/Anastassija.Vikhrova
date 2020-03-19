import pygame

pygame.init()

FPS = 30
W, H = 600, 300
WHITE = (255, 255, 255)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

motion = 'STOP'

car_surface_main = pygame.image.load('car.png').convert()
car_surface = pygame.image.load('car.png').convert()
x = W // 2
y = H // 2

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = 'LEFT'
            elif i.key == pygame.K_RIGHT:
                motion = 'RIGHT'
            elif i.key == pygame.K_UP:
                motion = 'UP'
            elif i.key == pygame.K_DOWN:
                motion = 'DOWN'
            else:
                motion = 'STOP'

    if motion == 'LEFT':
        x -= 3
        car_surface = pygame.transform.rotate(car_surface_main, 90)
    elif motion == 'RIGHT':
        x += 3
        car_surface = pygame.transform.rotate(car_surface_main, 270)
    elif motion == 'UP':
        y -= 3
        car_surface = car_surface_main
    elif motion == 'DOWN':
        y += 3
        car_surface = pygame.transform.rotate(car_surface_main, 180)

    sc.fill(WHITE)
    sc.blit(car_surface, (x, y))

    pygame.display.update()
    clock.tick(FPS)