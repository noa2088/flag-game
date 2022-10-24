import pygame

import MineField
import consts
import Screen


def draw_soldier():
    soldier = pygame.image.load(consts.SOLDIER)
    soldier = pygame.transform.scale(soldier, (consts.SOLDIER_WIDTH * consts.SQUARE_WIDTH,
                                               consts.SOLDIER_HEIGHT * consts.SQUARE_HEIGHT))
    Screen.screen.blit(soldier, consts.INITIAL_SOLDIER_POSITION)


def Soldier_body(current_position):
    current_position_x = current_position[0]
    current_position_y = current_position[1]
    body_indexes = []
    for i in range(len(MineField.mine_field)):
        for j in range(len(MineField.mine_field[i])):
            if i == current_position_y and j == current_position_x:
                for k in range(int(current_position_y), int(current_position_y + 2)):  # ADD CONST
                    for o in range(int(current_position_x + 1), int(current_position_x + 3)):  # ADD CONST
                        body_indexes.append([k, o])
    return body_indexes


def soldier_legs(current_position):
    current_position_x = current_position[0]
    current_position_y = current_position[1]
    leg_indexes = []
    for i in range(len(MineField.mine_field)):
        for j in range(len(MineField.mine_field[i])):
            if i == current_position_y and j == current_position_x:
                for k in range(int(current_position_y + 3), int(current_position_y + 4)):  # ADD CONST
                    for o in range(int(current_position_x + 1), int(current_position_x + 3)):  # ADD CONST
                        leg_indexes.append([k, o])
    return leg_indexes


def soldier_in_night_background(current_location):
    soldier = pygame.image.load(consts.SOLDIER_NIGHT)
    soldier = pygame.transform.scale(soldier, (consts.SOLDIER_WIDTH * consts.SQUARE_WIDTH,
                                               consts.SOLDIER_HEIGHT * consts.SQUARE_HEIGHT))
    Screen.screen.blit(soldier, current_location)
    pygame.display.flip()

