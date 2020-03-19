import pygame

pygame.init()
sc = pygame.display.set_mode((500, 500))
pygame.mouse.set_visible(False)
font = pygame.font.Font(None, 40)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    sc.fill((255, 255, 255))
    pygame.draw.rect(sc, (0, 255, 0), (100, 100, 100, 100))
    pygame.draw.rect(sc, (0, 0, 0), (x, y, 30, 30))
    if 170 > x > 100 and 170 > y > 100:
        text = font.render('далой карантин', 1, (255, 0, 0))
        sc.blit(text, (250, 250))
    pygame.display.update()
    pygame.time.delay(20)