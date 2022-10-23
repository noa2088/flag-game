import pygame
import Soldier
import consts
import random

pygame.init()
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("The Flag")
screen.fill(consts.BACKGROUND_COLOR)


def draw_message(message, color, location):
    font_size = 20
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def add_random_grass(xmax, ymax):
    random_location_list = []
    grass = pygame.image.load(consts.GRASS)
    grass = pygame.transform.scale(grass, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    for i in range(20):
        x = random.randint(0, xmax)
        y = random.randint(0, ymax)
        while (x, y) in random_location_list:
            x = random.randint(0, xmax)
            y = random.randint(0, ymax)
        screen.blit(grass, (x, y))
        random_location_list.append((x, y))
        pygame.display.flip()


def draw_soldier():
    soldier = pygame.image.load(consts.SOLDIER)
    soldier = pygame.transform.scale(soldier, (consts.SOLDIER_WIDTH * consts.SQUARE_WIDTH,
                                               consts.SOLDIER_HEIGHT * consts.SQUARE_HEIGHT))
    screen.blit(soldier, consts.INITIAL_SOLDIER_POSITION)


def draw_flag():
    flag = pygame.image.load(consts.FLAG)
    flag = pygame.transform.scale(flag, (consts.FLAG_WIDTH * consts.SQUARE_WIDTH,
                                         consts.FLAG_HEIGHT * consts.SQUARE_HEIGHT))
    screen.blit(flag, consts.FLAG_POSITION)


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    add_random_grass(consts.SCREEN_WIDTH-consts.GRASS_WIDTH, consts.SCREEN_HEIGHT-consts.GRASS_HEIGHT)
    draw_message(consts.INITIAL_TEXT_1, consts.WHITE, (90, 0))
    draw_message(consts.INITIAL_TEXT_2, consts.WHITE, (90, 20))
    draw_soldier()
    draw_flag()
    pygame.display.flip()


def main():
    draw_game()
    while True:
        soldier = pygame.image.load(consts.SOLDIER)


main()