import pygame
import button
from os import listdir
from os.path import isfile, join

# Initialization and setting methods
pygame.init()
pygame.display.set_caption("MindMaze")
pygame.mouse.set_cursor(pygame.cursors.broken_x)
WIDTH, HEIGHT = 1250, 750
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
font = pygame.font.SysFont("arialblack", 40)
TEXT_COLOR = (0, 0, 0)

# VARIABLES
COINS = 0
PAUSED = False
STORE = False
LOCKED1 = True
LOCKED2 = True
LOCKED3 = True
LOCKED4 = True
LOCKED5 = True
LOCKED6 = True
LOCKED7 = True



# Load Buttons & creating their
quit_BTN_img = pygame.image.load(join("assets", "Buttons", "button_quit.png")).convert_alpha()
quit_BTN = button.Button(WIDTH//2-quit_BTN_img.get_width()//2, 500, quit_BTN_img, 1)

resume_BTN_img = pygame.image.load(join("assets", "Buttons", "button_resume.png")).convert_alpha()
resume_BTN = button.Button(WIDTH//2-resume_BTN_img.get_width()//2, 100, resume_BTN_img, 1)

back_BTN_img = pygame.image.load(join("assets", "Buttons", "button_back.png")).convert_alpha()
back_BTN = button.Button(WIDTH//2-back_BTN_img.get_width()//2, 300, back_BTN_img, 1)

options_BTN_img = pygame.image.load(join("assets", "Buttons", "button_options.png")).convert_alpha()
options_BTN = button.Button(WIDTH//2-options_BTN_img.get_width()//2, 300, options_BTN_img, 1)

store_BTN_img = pygame.image.load(join("assets", "Buttons", "button_store.png")).convert_alpha()
store_BTN = button.Button(WIDTH-store_BTN_img.get_width(), HEIGHT-store_BTN_img.get_height(), store_BTN_img, 0.8)

BG1_BTN_img = pygame.image.load(join("assets", "Background1", "Blue.png")).convert_alpha()
BG1_BTN = button.Button(20, 20, BG1_BTN_img, 1.5)

BG2_BTN_img = pygame.image.load(join("assets", "Background1", "Brown.png")).convert_alpha()
BG2_BTN = button.Button(120, 20, BG2_BTN_img, 1.5)

BG3_BTN_img = pygame.image.load(join("assets", "Background1", "Gray.png")).convert_alpha()
BG3_BTN = button.Button(220, 20, BG3_BTN_img, 1.5)

BG4_BTN_img = pygame.image.load(join("assets", "Background1", "Green.png")).convert_alpha()
BG4_BTN = button.Button(320, 20, BG4_BTN_img, 1.5)

BG5_BTN_img = pygame.image.load(join("assets", "Background1", "Pink.png")).convert_alpha()
BG5_BTN = button.Button(420, 20, BG5_BTN_img, 1.5)

BG6_BTN_img = pygame.image.load(join("assets", "Background1", "Purple.png")).convert_alpha()
BG6_BTN = button.Button(520, 20, BG6_BTN_img, 1.5)

BG7_BTN_img = pygame.image.load(join("assets", "Background1", "Yellow.png")).convert_alpha()
BG7_BTN = button.Button(620, 20, BG7_BTN_img, 1.5)

lock_img = pygame.image.load(join("assets", "Buttons", "lock.png")).convert_alpha()
lock1 = button.Button(100, 20, lock_img, 0.20)
lock2 = button.Button(200, 20, lock_img, 0.20)
lock3 = button.Button(200, 20, lock_img, 0.20)
lock4 = button.Button(200, 20, lock_img, 0.20)
lock5 = button.Button(200, 20, lock_img, 0.20)
lock6 = button.Button(200, 20, lock_img, 0.20)
lock7 = button.Button(200, 20, lock_img, 0.20)


# FUNCTIONS
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))


def get_background(name):
    image = pygame.image.load(join("assets", "Background1", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(1500 // width + 1):
        for j in range(1200 // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image


# DRAWING FUNCTIONS
def draw_background(surface, background, bg_image):
    for tile in background:
        surface.blit(bg_image, tile)


def draw_background2(surface, number):
    image = pygame.image.load(join("assets", "Background2", "bg"+str(number)+".jpg"))

    surface.blit(image, (0, 0))
    pygame.display.update()


# Defining the main method that will run and call everything
def main(win):
    global PAUSED, STORE, COINS

    # Get the background
    background, bg_image = get_background("Blue.png")

    run = True

    # This is the main loop to keep the game going
    while run:

        # Drawing methods
        draw_background(win, background, bg_image)

        # if the game is paused
        if PAUSED:
            if options_BTN.draw(win):
                pass
            if resume_BTN.draw(win):
                PAUSED = False
            if quit_BTN.draw(win):
                run = False

        # if the game is in the STORE menu
        elif STORE:
            # Display the number of coins
            draw_text(str(COINS) + " COINS", font, TEXT_COLOR, 10, HEIGHT - 60)
            if BG1_BTN.draw(win):
                background, bg_image = get_background("Blue.png")
            if BG2_BTN.draw(win):
                background, bg_image = get_background("Brown.png")
            if BG3_BTN.draw(win):
                background, bg_image = get_background("Gray.png")
            if BG4_BTN.draw(win):
                background, bg_image = get_background("Green.png")
            if BG5_BTN.draw(win):
                background, bg_image = get_background("Pink.png")
            if BG6_BTN.draw(win):
                background, bg_image = get_background("Purple.png")
            if BG7_BTN.draw(win):
                background, bg_image = get_background("Yellow.png")
            if store_BTN.draw(win):
                STORE = False

            lock1.draw(win)
            lock2.draw(win)
            lock3.draw(win)
            lock4.draw(win)
            lock5.draw(win)
            lock6.draw(win)
            lock7.draw(win)

        # if the game is NOT pause or NOT in store
        else:
            # Display the number of coins
            draw_text(str(COINS) + " COINS", font, TEXT_COLOR, 10, HEIGHT - 60)

            # if the game is in the store menu
            if store_BTN.draw(win):
                STORE = True

        pygame.display.update()

        # Checks for the given pygame event
        for event in pygame.event.get():

            # Allows the program to end when Escape is pressed or the Quitting Button
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    PAUSED = not PAUSED
                if event.key == pygame.K_p:
                    COINS += 25


# only run the main when it's ran from m
if __name__ == "__main__":
    main(window)
