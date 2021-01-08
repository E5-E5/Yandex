import os
import pygame

next = False
s = 1

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = pygame.Color('black')
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Mountain(pygame.sprite.Sprite):
    image = load_image(f"C:/Users/USER/Desktop/piton/RABOTI/Игра/start{s}.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Finish(pygame.sprite.Sprite):
    image = load_image(f"C:/Users/USER/Desktop/piton/RABOTI/Игра/finish{s}.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Finish.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = load_image("C:/Users/USER/Desktop/piton/RABOTI/pt.png", -1)

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if pygame.sprite.collide_mask(self, mountain):
            pygame.mouse.set_pos(450, 500)
        if pygame.sprite.collide_mask(self, finish):
            global next
            next = True


pygame.init()

size = width, height = 750, 750
screen = pygame.display.set_mode(size)

# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

mountain = Mountain()
finish = Finish()
clock = pygame.time.Clock()
land = Landing(500, 500)
running = True
pygame.mouse.set_visible(False)
pygame.mouse.set_pos(450, 500)
while running:
    # в теории эдо должен быть переход на след уровень, но почему так не работает
    if next:
        s += 1
        finish = Finish()
        mountain = Mountain()
        next = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x1, y1 = event.pos
            land.rect.x = x1
            land.rect.y = y1
            screen.fill(pygame.Color("black"))
            all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
