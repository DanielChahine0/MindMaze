import pygame
import button
import coin
from os import listdir
from os.path import isfile, join
import time
import random

# Initialization and setting methods
pygame.init()
pygame.display.set_caption("MindMaze")
pygame.mouse.set_cursor(pygame.cursors.broken_x)
WIDTH, HEIGHT = 1250, 750
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
font = pygame.font.SysFont("arialblack", 40)
lock_font = pygame.font.SysFont("arialblack", 20)
TEXT_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)

# VARIABLES
PRICE_BG = 25
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
MAIN_MENU = True
MATH_MENU = True
LOGIC_MENU = False
COMP_MENU = False
OPEN_WINDOW = False
DIFFICULTY = 0
JET_LAG = 0.2
question = ""
line_num = 1


# Load Buttons & creating their parameters
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

# HEIGHT FOR ALL THE BUTTONS
BG_BTN_HEIGHT = 30
BTN_BG_margin = 20

BG1_BTN_img = pygame.image.load(join("assets", "Background2", "1.jpg")).convert_alpha()
BTN_X1 = BTN_BG_margin
BG1_BTN = button.Button(BTN_X1, BG_BTN_HEIGHT, BG1_BTN_img, 1)

BG2_BTN_img = pygame.image.load(join("assets", "Background2", "2.jpg")).convert_alpha()
BTN_X2 = BTN_X1 + BTN_BG_margin + BG1_BTN_img.get_width()
BG2_BTN = button.Button(BTN_X2, BG_BTN_HEIGHT, BG2_BTN_img, 1)

BG3_BTN_img = pygame.image.load(join("assets", "Background2", "3.jpg")).convert_alpha()
BTN_X3 = BTN_X2 + BTN_BG_margin + BG2_BTN_img.get_width()*1
BG3_BTN = button.Button(BTN_X3, BG_BTN_HEIGHT, BG3_BTN_img, 1)

BG4_BTN_img = pygame.image.load(join("assets", "Background2", "4.jpg")).convert_alpha()
BTN_X4 = BTN_X3 + BTN_BG_margin + BG3_BTN_img.get_width()*1
BG4_BTN = button.Button(BTN_X4, BG_BTN_HEIGHT, BG4_BTN_img, 1)

BG5_BTN_img = pygame.image.load(join("assets", "Background2", "5.jpg")).convert_alpha()
BTN_X5 = BTN_X4 + BTN_BG_margin + BG4_BTN_img.get_width()*1
BG5_BTN = button.Button(BTN_X5, BG_BTN_HEIGHT, BG5_BTN_img, 1)

BG6_BTN_img = pygame.image.load(join("assets", "Background2", "6.jpg")).convert_alpha()
BTN_X6 = BTN_X5 + BTN_BG_margin + BG5_BTN_img.get_width()*1
BG6_BTN = button.Button(BTN_X6, BG_BTN_HEIGHT, BG6_BTN_img, 1)

BG7_BTN_img = pygame.image.load(join("assets", "Background2", "7.jpg")).convert_alpha()
BTN_X7 = BTN_X6 + BTN_BG_margin + BG6_BTN_img.get_width()*1
BG7_BTN = button.Button(BTN_X7, BG_BTN_HEIGHT, BG7_BTN_img, 1)

lock_img = pygame.image.load(join("assets", "Buttons", "lock.png")).convert_alpha()
LOCK_MARGIN = 0

# Make all the locks as buttons -> easier to manage and remove
lock1 = button.Button(BG1_BTN.get_x()-LOCK_MARGIN, BG1_BTN.get_y(), lock_img, 1)
lock2 = button.Button(BG2_BTN.get_x()-LOCK_MARGIN, BG2_BTN.get_y(), lock_img, 1)
lock3 = button.Button(BG3_BTN.get_x()-LOCK_MARGIN, BG3_BTN.get_y(), lock_img, 1)
lock4 = button.Button(BG4_BTN.get_x()-LOCK_MARGIN, BG4_BTN.get_y(), lock_img, 1)
lock5 = button.Button(BG5_BTN.get_x()-LOCK_MARGIN, BG5_BTN.get_y(), lock_img, 1)
lock6 = button.Button(BG6_BTN.get_x()-LOCK_MARGIN, BG6_BTN.get_y(), lock_img, 1)
lock7 = button.Button(BG7_BTN.get_x()-LOCK_MARGIN, BG7_BTN.get_y(), lock_img, 1)

# Make the MATH - LOGIC - COMP buttons
MENUS_margin = 50
SCALE1 = 0.9

MATH_BTN_img = pygame.image.load(join("assets", "Buttons", "Mathematics.png")).convert_alpha()
MATH_BTN = button.Button(MENUS_margin, 30, MATH_BTN_img, SCALE1)

LOGIC_BTN_img = pygame.image.load(join("assets", "Buttons", "Logic.png")).convert_alpha()
LOGIC_BTN = button.Button(MENUS_margin+MATH_BTN_img.get_width() * SCALE1 + MATH_BTN.get_x(), 30, LOGIC_BTN_img, SCALE1)

COMP_BTN_img = pygame.image.load(join("assets", "Buttons", "compsci.png")).convert_alpha()
COMP_BTN = button.Button(MENUS_margin+LOGIC_BTN_img.get_width() * SCALE1 + LOGIC_BTN.get_x(), 30, COMP_BTN_img, SCALE1)

# Make the levels for each subject
ML_img = pygame.image.load(join("assets", "Buttons", "Level.png")).convert_alpha()
SCALE_levels = 0.75
level_margin = (WIDTH - ML_img.get_width()*SCALE_levels*3)//4
ML1 = button.Button(level_margin, 150, ML_img, SCALE_levels)
ML2 = button.Button(level_margin*2 + ML_img.get_width()*SCALE_levels, 150, ML_img, SCALE_levels)
ML3 = button.Button(level_margin*3 + ML_img.get_width()*SCALE_levels*2, 150, ML_img, SCALE_levels)
ML4 = button.Button(level_margin, 400, ML_img, SCALE_levels)
ML5 = button.Button(level_margin*2 + ML_img.get_width()*SCALE_levels, 400, ML_img, SCALE_levels)
ML6 = button.Button(level_margin*3 + ML_img.get_width()*SCALE_levels*2, 400, ML_img, SCALE_levels)

CURRENT_WIN_img = pygame.image.load(join("assets", "Buttons", "Level.png")).convert_alpha()
CURRENT_WIN = button.Button(WIDTH//2-CURRENT_WIN_img.get_width()//2, 100,
                            CURRENT_WIN_img, 1)

X_BTN_img = pygame.image.load(join("assets", "Buttons", "x_button.png")).convert_alpha()
X_BTN = button.Button(CURRENT_WIN.get_x()+CURRENT_WIN_img.get_width()-X_BTN_img.get_width()//2-10,
                      CURRENT_WIN.get_y()-X_BTN_img.get_height()//2+10,
                      X_BTN_img, 1)

check_BTN_img = pygame.image.load(join("assets", "Buttons", "check_button.png")).convert_alpha()
check_BTN = button.Button(CURRENT_WIN.get_x()+CURRENT_WIN_img.get_width()//2-check_BTN_img.get_width()//2,
                          CURRENT_WIN.get_y()+CURRENT_WIN_img.get_height()-check_BTN_img.get_height()//2-10,
                          check_BTN_img, 1)


# FUNCTIONS
def draw_text(text, fonts, text_col, x, y):
    img = fonts.render(text, True, text_col)
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


def draw_levels():
    x = [140, 543, 955]
    y = [180, 440]
    draw_text("Level 1", font, WHITE, x[0], y[0])
    draw_text("Level 2", font, WHITE, x[1], y[0])
    draw_text("Level 3", font, WHITE, x[2], y[0])
    draw_text("Level 4", font, WHITE, x[0], y[1])
    draw_text("Level 5", font, WHITE, x[1], y[1])
    draw_text("Level 6", font, WHITE, x[2], y[1])


def rand_question(difficulty):
    # Choose a random number - represent the line number
    random_line = random.randint(1, 10)

    # Open the file according to the difficulty
    f = open(join("assets", "Math Question", str(difficulty) + ".txt"), "r")

    # loop from the first line all the way to the given line
    for line in range(random_line - 1):
        f.readline()

    # read the given random line
    quest = f.readline()
    # Take away the last character as it represent the \n
    quest = quest[:-1]

    return quest, random_line


# Defining the main method that will run and call everything
def main(win):
    global PAUSED, STORE, LOCKED1, LOCKED2, LOCKED3, LOCKED4, LOCKED5, LOCKED6, LOCKED7, MATH_MENU, LOGIC_MENU,\
        COMP_MENU, OPEN_WINDOW, DIFFICULTY, MAIN_MENU, question, line_num

    # Get the background
    background, bg_image = get_background("Blue.png")

    run = True

    Money = coin.Coin()

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
                time.sleep(JET_LAG)
            if quit_BTN.draw(win):
                run = False

        # if the game is in the STORE menu
        elif STORE:
            # Display the number of coins
            # draw_text(str(COINS) + " COINS", font, TEXT_COLOR, 10, HEIGHT - 60)
            Money.draw()

            # If we press any background button
            if BG1_BTN.draw(win):
                if LOCKED1 and Money.value >= PRICE_BG:
                    # COINS -= PRICE_BG
                    Money.take(PRICE_BG)
                    LOCKED1 = False
                elif not LOCKED1:
                    background, bg_image = get_background("Blue.png")
            if BG2_BTN.draw(win):
                if LOCKED2 and Money.value >= PRICE_BG:
                    # COINS -= PRICE_BG
                    Money.take(PRICE_BG)
                    LOCKED2 = False
                elif not LOCKED2:
                    background, bg_image = get_background("Brown.png")
            if BG3_BTN.draw(win):
                if LOCKED3 and Money.value >= PRICE_BG:
                    # COINS -= PRICE_BG
                    Money.take(PRICE_BG)
                    LOCKED3 = False
                elif not LOCKED3:
                    background, bg_image = get_background("Gray.png")
            if BG4_BTN.draw(win):
                if LOCKED4 and Money.value >= PRICE_BG:
                    # COINS -= PRICE_BG
                    Money.take(PRICE_BG)
                    LOCKED4 = False
                elif not LOCKED4:
                    background, bg_image = get_background("Green.png")
            if BG5_BTN.draw(win):
                if LOCKED5 and Money.value >= PRICE_BG:
                    # COINS -= PRICE_BG
                    Money.take(PRICE_BG)
                    LOCKED5 = False
                elif not LOCKED5:
                    background, bg_image = get_background("Pink.png")
            if BG6_BTN.draw(win):
                if LOCKED6 and Money.value >= PRICE_BG:
                    # COINS -= PRICE_BG
                    Money.take(PRICE_BG)
                    LOCKED6 = False
                elif not LOCKED6:
                    background, bg_image = get_background("Purple.png")
            if BG7_BTN.draw(win):
                if LOCKED7 and Money.value >= PRICE_BG:
                    # COINS -= PRICE_BG
                    Money.take(PRICE_BG)
                    LOCKED7 = False
                elif not LOCKED7:
                    background, bg_image = get_background("Yellow.png")

            # If we are in the store, and we press the store button -> we leave the store
            if store_BTN.draw(win):
                STORE = False

            # Check if each Background is locked or unlocked
            if LOCKED1:
                lock1.draw(win)
                draw_text(str(PRICE_BG), lock_font, WHITE, lock1.get_x()+27, lock1.get_y()+70)
            if LOCKED2:
                lock2.draw(win)
                draw_text(str(PRICE_BG), lock_font, WHITE, lock2.get_x()+27, lock1.get_y()+70)
            if LOCKED3:
                lock3.draw(win)
                draw_text(str(PRICE_BG), lock_font, WHITE, lock3.get_x()+27, lock1.get_y()+70)
            if LOCKED4:
                lock4.draw(win)
                draw_text(str(PRICE_BG), lock_font, WHITE, lock4.get_x()+27, lock1.get_y()+70)
            if LOCKED5:
                lock5.draw(win)
                draw_text(str(PRICE_BG), lock_font, WHITE, lock5.get_x()+27, lock1.get_y()+70)
            if LOCKED6:
                lock6.draw(win)
                draw_text(str(PRICE_BG), lock_font, WHITE, lock6.get_x()+27, lock1.get_y()+70)
            if LOCKED7:
                lock7.draw(win)
                draw_text(str(PRICE_BG), lock_font, WHITE, lock7.get_x()+27, lock1.get_y()+70)

        # if the game is NOT pause or NOT in store --> It is in the main menu
        else:

            # Check if it is in the main menu
            if MAIN_MENU:
                # If we press the math button for it's menu
                if MATH_BTN.draw(win):
                    MATH_MENU = True
                    LOGIC_MENU = False
                    COMP_MENU = False
                    OPEN_WINDOW = False
                # If we press the Logic button for it's menu
                elif LOGIC_BTN.draw(win):
                    MATH_MENU = False
                    LOGIC_MENU = True
                    COMP_MENU = False
                # If we press the Computer Science button for it's menu
                elif COMP_BTN.draw(win):
                    MATH_MENU = False
                    LOGIC_MENU = False
                    COMP_MENU = True

                elif MATH_MENU:
                    if ML1.draw(win):
                        DIFFICULTY = 1
                        OPEN_WINDOW = True
                        MAIN_MENU = False
                        question, line_num = rand_question(DIFFICULTY)

                    elif ML2.draw(win):
                        DIFFICULTY = 2
                        OPEN_WINDOW = True
                        MAIN_MENU = False
                    elif ML3.draw(win):
                        DIFFICULTY = 3
                        OPEN_WINDOW = True
                        MAIN_MENU = False
                    elif ML4.draw(win):
                        DIFFICULTY = 4
                        OPEN_WINDOW = True
                        MAIN_MENU = False
                    elif ML5.draw(win):
                        DIFFICULTY = 5
                        OPEN_WINDOW = True
                        MAIN_MENU = False
                    elif ML6.draw(win):
                        DIFFICULTY = 6
                        OPEN_WINDOW = True
                        MAIN_MENU = False
                    draw_levels()

            elif OPEN_WINDOW:
                # draw the current window open
                CURRENT_WIN.draw(win)

                # Display the question on the window
                draw_text(question, lock_font, WHITE, CURRENT_WIN.get_x()+CURRENT_WIN_img.get_width()//2-50,
                          CURRENT_WIN.get_y()+CURRENT_WIN_img.get_height()//2-50)

                if X_BTN.draw(win):
                    OPEN_WINDOW = False
                    MAIN_MENU = True
                    # this delay is important because the mouse clicks are recognizes
                    time.sleep(JET_LAG)

                if check_BTN.draw(win):
                    OPEN_WINDOW = False
                    MAIN_MENU = True
                    Money.add(PRICE_BG)
                    time.sleep(JET_LAG)

            # Display the number of coins
            # draw_text(str(COINS) + " COINS", font, TEXT_COLOR, 10, HEIGHT - 60)
            Money.draw()

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
                    # COINS += 25
                    Money.add(25)


# only run the main when it's ran from m
if __name__ == "__main__":
    main(window)
