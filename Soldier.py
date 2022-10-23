import pygame
import consts
import Screen


def draw_soldier():
    soldier = pygame.image.load(consts.SOLDIER)
    soldier = pygame.transform.scale(soldier, (consts.SOLDIER_WIDTH * consts.SQUARE_WIDTH,
                                               consts.SOLDIER_HEIGHT * consts.SQUARE_HEIGHT))
    Screen.screen.blit(soldier, consts.INITIAL_SOLDIER_POSITION)