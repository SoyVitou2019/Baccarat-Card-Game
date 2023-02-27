import pygame
import glob
import random as rd
import math
from pygame import mixer
mixer.init()
pygame.init()


# Music loading
mixer.music.load("sound/flipcard.mp3")
win = mixer.Sound("sound/win.mp3")
you_lose = mixer.Sound("sound/you_lose.mp3")
countdown = mixer.Sound("sound/countdown_sound.mp3")
mixer.music.set_volume(4)

countdown.set_volume(0.2)
win.set_volume(0.9)
you_lose.set_volume(0.9)


X = 1000
Y = 600
Icon_name = pygame.image.load("image/icon_Card.png")

# set initialized window
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_icon(Icon_name)
pygame.display.set_caption('Card Game')

# Background image
bg = pygame.image.load("image/bg.jpg").convert()
bg = pygame.transform.scale(bg, (1000, 600))
imp = pygame.image.load("image/Background.png").convert()
imp = pygame.transform.scale(imp, (1000, 600))
win_stage = pygame.image.load("image/win_stage.jpg").convert()
win_stage = pygame.transform.scale(bg, (1000, 600))

# first background
scrn.blit(bg, (0, 0))

# value of card 1, 2, ..., 6
x_card1_player = 0
x_card2_player = 0
x_card3_player = 0
x_card4_machine = 0
x_card5_machine = 0
x_card6_machine = 0

# surface card1, 2, 3, ..., 6
card1 = pygame.image.load("card/image_09.png")
card2 = pygame.image.load("card/image_51.png")
card3 = pygame.image.load("card/image_34.png")
card4 = pygame.image.load("card/image_44.png")
card5 = pygame.image.load("card/image_24.png")
card6 = pygame.image.load("card/image_24.png")
back_card = pygame.image.load("image/back_card.jpg")
# define function


def text_on_screen(text, pos, font_size=30):
    title_font = pygame.font.SysFont("Arial", font_size)
    title_display = title_font.render(text, True, (255, 255, 255))
    scrn.blit(title_display, pos)


def card(source, x, y):
    source = pygame.transform.scale(source, (130, 200))
    return scrn.blit(source, (x, y))


# 20, 20 , 430, 20
def animation_card3_change_of_machine(player1, player2, machine1, machine2, machine3, x1, y1, x2, y2):
    for i in range(310):
        scrn.blit(imp, (0, 0))
        card(player1, x1+i-100, y1+i)  # 20 + 310 - 100 = 230
        card(player2, x1+i-40, y2+i)  # 20 + 310 - 40 = 290
        card(machine1, x2+i-60, (y1+i)/4)  # 430 + 310 - 60 = 680
        card(machine2, x2+i, (y2+i)/4)  # 430 + 310 = 740
        card(machine3, x2+i + 60, (y2+i)/4)  # 430 + 310 = 740
        pygame.display.update()
    for i in range(300):
        pygame.display.update()


# 20, 20 , 430, 20
def animation_card3_change_of_machine_no_animation(player1, player2, machine1, machine2, machine3):
    card(player1, 230, 330)  # 20 + 310 - 100 = 230
    card(player2, 290, 330)  # 20 + 310 - 40 = 290
    card(machine1, 680, (330)/4)  # 430 + 310 - 60 = 680
    card(machine2, 740, (330)/4)  # 430 + 310 = 740
    card(machine3, 800, (330)/4)  # 430 + 310 = 740


def animation_card3_change_of_machine___add_card(player1, player2, player3, machine1, machine2, machine3, x1, y1):
    for i in range(310):
        scrn.blit(imp, (0, 0))
        card(player1, 230, 330)
        card(player2, 290, 330)  # interval 60
        card(player3, x1+i+20, y1+i)
        card(machine1, 680, (330)/4)
        card(machine2, 740, (330)/4)
        card(machine3, 800, (330)/4)
        pygame.display.update()
    for i in range(300):
        pygame.display.update()


def animation_card3_change_of_machine___add_card_no_animation(player1, player2, player3, machine1, machine2, machine3):
    card(player1, 230, 330)
    card(player2, 290, 330)  # interval 60
    card(player3, 350, 330)
    card(machine1, 680, (330)/4)
    card(machine2, 740, (330)/4)
    card(machine3, 800, (330)/4)


# 20, 20 , 430, 20
def animation_card_machine_get_only_2card(player1, player2, machine1, machine2, x1, y1, x2, y2):
    for i in range(310):
        scrn.blit(imp, (0, 0))
        card(player1, x1+i-100, y1+i)  # 20 + 310 - 100 = 230
        card(player2, x1+i-40, y2+i)  # 20 + 310 - 40 = 290
        card(machine1, x2+i-60, (y1+i)/4)  # 430 + 310 - 60 = 680
        card(machine2, x2+i, (y2+i)/4)  # 430 + 310 = 740
        pygame.display.update()
    for i in range(300):
        pygame.display.update()


# 20, 20 , 430, 20
def animation_card_machine_get_only_2card_no_animation(player1, player2, machine1, machine2):
    card(player1, 230, 330)  # 20 + 310 - 100 = 230
    card(player2, 290, 330)  # 20 + 310 - 40 = 290
    card(machine1, 680, (330)/4)  # 430 + 310 - 60 = 680
    card(machine2, 740, (330)/4)  # 430 + 310 = 740


def animation_card_machine_get_only_2card___add_card(player1, player2, player3, machine1, machine2, x1, y1):
    for i in range(310):
        scrn.blit(imp, (0, 0))
        card(player1, 230, 330)
        card(player2, 290, 330)  # interval 60
        card(player3, x1 + i + 20, y1 + i)
        card(machine1, 680, 330/4)
        card(machine2, 740, (330)/4)
        pygame.display.update()
    for i in range(300):
        pygame.display.update()


def animation_card_machine_get_only_2card___add_card_no_animation(player1, player2, player3, machine1, machine2):
    card(player1, 230, 330)
    card(player2, 290, 330)  # interval 60
    card(player3, 350, 330)
    card(machine1, 680, 330/4)
    card(machine2, 740, (330)/4)


# ========== Function Style ====================#

def button(screen, position, text, size, bg, colortext,increseSize):
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 0.5, colortext)
    x, y, w, h = text_render.get_rect()
    x, y = position
    #top and buttono
    point = pygame.mouse.get_pos()
    rect = pygame.draw.rect(screen, bg, (x , y , w , h ))
    collide = rect.collidepoint(point)
    if collide:
        bg = "#FFC300"
    pygame.draw.rect(screen, bg, pygame.Rect(position[0]-increseSize,position[1]-increseSize, w+(increseSize*2), h+(increseSize*2)))
    
    
    return screen.blit(text_render, (x, y)), rect


def display_variable(screen,possition, diceRoll, size, color):
    #Text through GUI
    x, y = possition
    myFont = pygame.font.SysFont("Times New Roman", size)
    ### pass a string to myFont.render
    diceDisplay = myFont.render(str(diceRoll), 1, color)
    return screen.blit(diceDisplay, (x,y))

def clickOnButton(recttangle, event_list):
    x, y, w, h = recttangle
    check = False
    for event in event_list:
        if event.type == pygame.MOUSEBUTTONUP:
            point = pygame.mouse.get_pos()
            if point[0] > x and point[1] > y and point[0] < x + w and point[1] < y + h:
                check = True
    
    return check




# ============== End Function Style ============================#





folder = 'card/*.png'
cv_im = []
for img in sorted(glob.glob("card/*.png")):
    cv_im.append(pygame.image.load(img))

# FPS
clock = pygame.time.Clock()
FBS = 100

# flip screen one time
pygame.display.flip()

# make button start
button(scrn, (800, 430), "Start", 40, (237, 255, 1), "black", 10)

# initialized card 1 , card 2
player = [0, 0]
machine = [0, 0]

# initialized totoal score
total_score_player = 0
total_score_machine = 0

# initialized boolean value
status = True
# machine 3 card
animation_card3_change_of_machine_boolean = False

# add card with machine 3 card
animation_card3_change_of_machine___add_card_boolean = True

# machine 2 card
animation_card_machine_get_only_2card_boolean = False

# add card with machine 2 card
animation_card_machine_get_only_2card___add_card_boolean = True


# boolean condition
show_start_button = True
show_yes_button = False
machine_got_3_card_boolean = False
machine_got_2_card_boolean = False
change_to_win_stage = False
add_one_card_for_player_boolean = False
continue_button_for_next_boolean = False

#sound win
sound_win = False

#sound lose
sound_lose = False

# parameter for printing or display card in win stage
machine_x = 0
player_x = 0
# mainipolate main game loop
while (status):
    text_on_screen("Dok-Dang || Pro_Vitou_Game", (12, 15))
    event_list = pygame.event.get()
    for i in event_list:
        if i.type == pygame.QUIT:
            status = False

    if show_start_button:
        buton, rect_start = button(
            scrn, (800, 430), "Start", 40, (237, 255, 1), "black", 20)
        if clickOnButton(rect_start, event_list):
            #Play the music
            mixer.music.play()
            machine_x = 0
            player_x = 0
            scrn.blit(imp, (0, 0))
            animation_card_machine_get_only_2card_boolean = True
            show_start_button = False

            # Reset total socore
            total_score_machine = 0
            total_score_player = 0

            # random card
            x_card1_player = rd.randint(0, 51)
            x_card2_player = rd.randint(0, 51)
            x_card3_player = rd.randint(0, 51)
            x_card4_machine = rd.randint(0, 51)
            x_card5_machine = rd.randint(0, 51)
            x_card6_machine = rd.randint(0, 51)

            card1 = cv_im[x_card1_player]
            card2 = cv_im[x_card2_player]
            card3 = cv_im[x_card3_player]
            card4 = cv_im[x_card4_machine]
            card5 = cv_im[x_card5_machine]
            card6 = cv_im[x_card6_machine]

            x_card1_player = math.floor(x_card1_player/4)+1
            x_card2_player = math.floor(x_card2_player/4)+1
            x_card3_player = math.floor(x_card3_player/4)+1
            x_card4_machine = math.floor(x_card4_machine/4)+1
            x_card5_machine = math.floor(x_card5_machine/4)+1
            x_card6_machine = math.floor(x_card6_machine/4)+1

            if x_card1_player > 10:
                x_card1_player = 0
            if x_card2_player > 10:
                x_card2_player = 0
            if x_card3_player > 10:
                x_card3_player = 0
            if x_card4_machine > 10:
                x_card4_machine = 0
            if x_card5_machine > 10:
                x_card5_machine = 0
            if x_card6_machine > 10:
                x_card6_machine = 0

            total_score_machine = x_card4_machine + x_card5_machine

            if total_score_machine > 10:
                total_score_machine = int(str(total_score_machine)[1])
            if total_score_machine < 4 or total_score_machine == 10:
                machine_x = 1
                total_score_machine += x_card6_machine
                animation_card3_change_of_machine_boolean = True
            if total_score_machine == 4:
                # 80 % get one 20 % don't get one
                if rd.randint(1,101) > 20:
                    machine_x = 1
                    total_score_machine += x_card6_machine
                    animation_card3_change_of_machine_boolean = True
            if total_score_machine == 5:
                # 40 % get one 60 % don't get one
                if rd.randint(1,101) > 60:
                    machine_x = 1
                    total_score_machine += x_card6_machine
                    animation_card3_change_of_machine_boolean = True
            if total_score_machine == 6:
                # 10 % get one 90 % don't get one
                if rd.randint(1,101) > 90:
                    machine_x = 1
                    total_score_machine += x_card6_machine
                    animation_card3_change_of_machine_boolean = True
            if total_score_machine > 10:
                total_score_machine = int(str(total_score_machine)[1])

            total_score_player = x_card1_player + x_card2_player

            if total_score_player > 10:
                total_score_player = int(str(total_score_player)[1])

    if animation_card3_change_of_machine_boolean:
        animation_card_machine_get_only_2card_boolean = False
        animation_card3_change_of_machine(
            card1, card2, back_card, back_card, back_card, 20, 20, 430, 20)
        show_yes_button = True
        machine_got_3_card_boolean = True
        animation_card3_change_of_machine_boolean = False
    elif animation_card_machine_get_only_2card_boolean:
        machine_got_3_card_boolean = False
        animation_card_machine_get_only_2card(
            card1, card2, back_card, back_card, 20, 20, 430, 20)
        show_yes_button = True
        machine_got_2_card_boolean = True
        animation_card_machine_get_only_2card_boolean = False

    if machine_got_3_card_boolean:
        machine_got_2_card_boolean = False
        if show_yes_button:
            button_yes, rect_yes = button(
                scrn, (600, 430), " yes ", 40, (237, 255, 1), "black", 10)
            button_no, rect_no = button(
                scrn, (500, 430), " No! ", 40, (237, 255, 1), "black", 10)
            if clickOnButton(rect_yes, event_list):
                #Play the music
                mixer.music.play()
                animation_card3_change_of_machine___add_card(
                    card1, card2, card3, back_card, back_card, back_card, 20, 20)
                show_yes_button = False
                add_one_card_for_player_boolean = True
                change_to_win_stage = True
            if clickOnButton(rect_no, event_list):
                change_to_win_stage = True
                show_yes_button = False
    elif machine_got_2_card_boolean:
        machine_got_3_card_boolean = False
        if show_yes_button:
            button_yes, rect_yes = button(
                scrn, (600, 430), " yes ", 40, (237, 255, 1), "black", 10)
            button_no, rect_no = button(
                scrn, (500, 430), " No! ", 40, (237, 255, 1), "black", 10)
            if clickOnButton(rect_yes, event_list):
                #Play the music
                mixer.music.play()
                animation_card_machine_get_only_2card___add_card(
                    card1, card2, card3, back_card, back_card, 20, 20)
                show_yes_button = False
                add_one_card_for_player_boolean = True
                change_to_win_stage = True
            if clickOnButton(rect_no, event_list):
                change_to_win_stage = True
                show_yes_button = False
    # calculate total socre player
    if add_one_card_for_player_boolean:
        player_x = 1
        total_score_player += x_card3_player
        add_one_card_for_player_boolean = False
        
    # clean scores of player vs machine
    if total_score_player >= 10:
        total_score_player = int(str(total_score_player)[1])
    if total_score_machine >= 10:
        total_score_machine = int(str(total_score_machine)[1])
    if change_to_win_stage:
        # print(total_score_player, total_score_machine)
        # print(player_x, machine_x)
        scrn.blit(win_stage, (0, 0))
        countdown.play()
        for i in range(3800):
            if i == 400:
                display_variable(scrn, (300, 200), 4, 140, "white")
                display_variable(scrn, (500, 200), 4, 140, "white")
            if i == 1000:
                scrn.blit(win_stage, (i/(i+1), i/(i+1)))
                display_variable(scrn, (300, 200), 3, 140, "white")
                display_variable(scrn, (500, 200), 3, 140, "white")
            if i == 2000:
                scrn.blit(win_stage, (i/(i+1), i/(i+1)))
                display_variable(scrn, (300, 200), 2, 140, "white")
                display_variable(scrn, (500, 200), 2, 140, "white")
            if i == 3000:
                scrn.blit(win_stage, (i/(i+1), i/(i+1)))
                display_variable(scrn, (300, 200), 1, 140, "white")
                display_variable(scrn, (500, 200), 1, 140, "white")
            pygame.display.update()
        countdown.stop()
        scrn.blit(win_stage, (i/(i+1), i/(i+1)))

        continue_button_for_next_boolean = True
        change_to_win_stage = False

    if continue_button_for_next_boolean:
        if player_x == 0 and machine_x == 0:
            animation_card_machine_get_only_2card_no_animation(
                card1, card2, card4, card5)
        elif player_x == 1 and machine_x == 0:
            animation_card_machine_get_only_2card___add_card_no_animation(
                card1, card2, card3, card4, card5)
        elif player_x == 0 and machine_x == 1:
            animation_card3_change_of_machine_no_animation(
                card1, card2, card4, card5, card6)
        elif player_x == 1 and machine_x == 1:
            animation_card3_change_of_machine___add_card_no_animation(
                card1, card2, card3, card4, card5, card6)
        if total_score_machine == total_score_player:
            text_on_screen("You Are Draw!", (150, 150), 80)
        elif total_score_player > total_score_machine:
            sound_win = True
            text_on_screen("You Are Win!", (150, 150), 80)
        elif total_score_player < total_score_machine:
            sound_lose = True
            text_on_screen("You Are Lose!", (150, 150), 80)
        button_continue, rect_continue = button(
            scrn, (800, 500), "Continue", 40, (237, 255, 1), "black", 20)
        if clickOnButton(rect_continue, event_list):
            continue_button_for_next_boolean = False
            scrn.blit(win_stage, (0, 0))
            show_start_button = True
    pygame.display.update()
    clock.tick(FBS)


pygame.quit()
