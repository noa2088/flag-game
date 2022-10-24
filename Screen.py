import pygame

import MineField

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
    return random_location_list


random_location_list = add_random_grass(consts.SCREEN_WIDTH - consts.GRASS_WIDTH,
                                        consts.SCREEN_HEIGHT - consts.GRASS_HEIGHT)


def grass_position():
    grass = pygame.image.load(consts.GRASS)
    grass = pygame.transform.scale(grass, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    for grass_location in random_location_list:
        screen.blit(grass, grass_location)
        pygame.display.flip()


def draw_soldier(soldier_location):
    soldier = pygame.image.load(consts.SOLDIER)
    soldier = pygame.transform.scale(soldier, (consts.SOLDIER_WIDTH * consts.SQUARE_WIDTH,
                                               consts.SOLDIER_HEIGHT * consts.SQUARE_HEIGHT))
    screen.blit(soldier, soldier_location)
    pygame.display.flip()


def draw_flag():
    flag = pygame.image.load(consts.FLAG)
    flag = pygame.transform.scale(flag, (consts.FLAG_WIDTH * consts.SQUARE_WIDTH,
                                         consts.FLAG_HEIGHT * consts.SQUARE_HEIGHT))
    screen.blit(flag, consts.FLAG_POSITION)


def draw_game(soldier_position):
    screen.fill(consts.BACKGROUND_COLOR)
    # add_random_grass(consts.SCREEN_WIDTH-consts.GRASS_WIDTH, consts.SCREEN_HEIGHT-consts.GRASS_HEIGHT)
    draw_message(consts.INITIAL_TEXT_1, consts.WHITE, (90, 0))
    draw_message(consts.INITIAL_TEXT_2, consts.WHITE, (90, 20))
    draw_soldier(soldier_position)
    draw_flag()
    pygame.display.flip()


def night_screen():
    mine = pygame.image.load(consts.MINE)
    mine = pygame.transform.scale(mine, (consts.MINE_WIDTH, consts.MINE_HEIGHT))
    screen.fill(consts.BACKGROUND_NIGHT_COLOR)
    draw_horizontal_lines()
    draw_vertical_lines()
    for random_location in MineField.random_location_list:
        screen.blit(mine, random_location)
    pygame.display.flip()


def draw_vertical_lines():
    for i in range(0, consts.SCREEN_HEIGHT, 22):
        pygame.draw.line(screen, consts.LINE_COLOR, (0, i), (consts.SCREEN_WIDTH, i))
        pygame.display.flip()


def draw_horizontal_lines():
    for i in range(0, consts.SCREEN_WIDTH, 22):
        pygame.draw.line(screen, consts.LINE_COLOR, (i, 0), (i, consts.SCREEN_HEIGHT))
        pygame.display.flip()

# def main():
#     # draw_game()
#     night_screen()
#     while True:
#         soldier = pygame.image.load(consts.SOLDIER)
#
#
# main()
