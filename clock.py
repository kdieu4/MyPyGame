import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((550, 600))
GREY = (150, 150, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True

font = pygame.font.SysFont('sans', 40)
text_1 = font.render('+', True, BLACK)
text_2 = font.render('-', True, BLACK)
text_3 = font.render('Start', True, BLACK)
text_4 = font.render('Reset', True, BLACK)

total_secs = 0
total = 0
start = False
mins = 0

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(GREY)
    sound = pygame.mixer.Sound('alarm.wav')
    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
    pygame.draw.rect(screen, WHITE, (100, 150, 50, 50))
    pygame.draw.rect(screen, WHITE, (300, 150, 150, 50))
    pygame.draw.rect(screen, WHITE, (200, 150, 50, 50))

    screen.blit(text_1, (114, 48))
    screen.blit(text_1, (114 + 100, 48))
    screen.blit(text_2, (118, 48 + 100))
    screen.blit(text_2, (118 + 100, 48 + 100))
    screen.blit(text_3, (300, 48))
    screen.blit(text_4, (300, 48 + 100))

    pygame.draw.rect(screen, BLACK, (90, 500, 370, 70))
    pygame.draw.rect(screen, WHITE, (100, 510, 350, 50))

    pygame.draw.circle(screen, BLACK, (275, 350), 100)
    pygame.draw.circle(screen, WHITE, (275, 350), 95)
    pygame.draw.circle(screen, BLACK, (275, 350), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.pause()
                if (100 <= mouse_x <= 150) and (50 <= mouse_y <= 100):
                    total_secs += 60
                    total = total_secs
                    print("press + minute")
                if (200 <= mouse_x <= 250) and (50 <= mouse_y <= 100):
                    total_secs += 1
                    total = total_secs
                    print("press + second")
                if (100 <= mouse_x <= 150) and (150 <= mouse_y <= 200):
                    total_secs -= 60
                    total = total_secs
                    print("press - minute")
                if (200 <= mouse_x <= 250) and (150 <= mouse_y <= 200):
                    total_secs -= 1
                    total = total_secs
                    print("press - second")
                if (300 <= mouse_x <= 450) and (50 <= mouse_y <= 100):
                    start = True
                    print("press Start")
                if (300 <= mouse_x <= 450) and (150 <= mouse_y <= 200):
                    total_secs = 0
                    start = False
                    print("press Reset")
                print("Total secs: ", total_secs)

    if start:
        total_secs -= 1
        if total_secs == 0:
            print("Time out")
            pygame.mixer.Sound.play(sound)
        time.sleep(1)
        if total_secs < 0:
            start = False
            total_secs = 0
            total = 0
    mins = int(total_secs / 60)
    secs = total_secs - mins * 60

    time_now = str(mins) + " : " + str(secs)
    text_time = font.render(time_now, True, BLACK)
    screen.blit(text_time, (140, 100))

    x_sec = 90 * math.sin(total_secs * math.pi / 180 * 6)
    y_sec = 90 * math.cos(total_secs * math.pi / 180 * 6)
    pygame.draw.line(screen, BLACK, (275, 350), (275 + int(x_sec), 350 - int(y_sec)), 2)

    x_min = 30 * math.sin(mins * math.pi / 180 * 6)
    y_min = 30 * math.cos(mins * math.pi / 180 * 6)
    pygame.draw.line(screen, BLACK, (275, 350), (275 + int(x_min), 350 - int(y_min)), 3)

    if total_secs != 0:
        pygame.draw.rect(screen, (255, 150, 198), (100, 510, int(350 * total_secs / total), 50))

    pygame.display.flip()
pygame.quit()
