import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface((1, 1),
                                    pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x, y, 1, 1)

    def update(self):
        if not pygame.sprite.spritecollideany(self, horizontal_borders):
            pygame.mouse.set_pos(600, 650)
        if not pygame.sprite.spritecollideany(self, vertical_borders):
            pygame.mouse.set_pos(600, 650)


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


all_sprites = pygame.sprite.Group()

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

Border(2, 2, 2, 699)
Border(2, 2, 699, 2)
Border(699, 2, 699, 700)
Border(500, 200, 500, 700)
Border(200, 200, 200, 500)
Border(1, 699, 500, 699)

Ball(600, 650)
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x1, y1 = event.pos
            Ball(x1, y1)
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
