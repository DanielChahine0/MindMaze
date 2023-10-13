import pygame


WIDTH, HEIGHT = 1250, 750
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)


def draw_text(text, fonts, text_col, x, y):
    img = fonts.render(text, True, text_col)
    window.blit(img, (x, y))


class Coin:
    def __init__(self):
        self.value = 0
        self.coin_font = pygame.font.SysFont("arialblack", 40)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (50, 205, 50)
        self.red = (255, 0, 0)

    def add(self, amount):
        self.value += amount

    def take(self, amount):
        self.value -= amount

    def draw(self):
        draw_text(str(self.value) + " COINS", self.coin_font, self.black, 10, HEIGHT-60)




