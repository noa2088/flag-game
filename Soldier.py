import pygame
import consts
import Screen


def draw_soldier():
    soldier = pygame.image.load(consts.SOLDIER)
    soldier = pygame.transform.scale(soldier, (consts.SOLDIER_WIDTH * consts.SQUARE_WIDTH,
                                               consts.SOLDIER_HEIGHT * consts.SQUARE_HEIGHT))
    Screen.screen.blit(soldier, consts.INITIAL_SOLDIER_POSITION)


def move_soldier(direction):
    if direction == consts.UP:
        if state["soldier location"][1] >= consts.SQUARE_HEIGHT:
            position = list(state["soldier location"])
            position[1] -= consts.STEP
            state["soldier location"] = tuple(position)
    elif direction == consts.DOWN:
        if state["soldier location"][1] < consts.SCREEN_HEIGHT - consts.SOLDIER_HEIGHT * consts.SQUARE_HEIGHT - \
                consts.SQUARE_HEIGHT:
            position = list(state["soldier location"])
            position[1] += consts.STEP
            state["soldier location"] = tuple(position)
    elif direction == consts.RIGHT:
        if state["soldier location"][0] < consts.SCREEN_WIDTH - consts.SOLDIER_WIDTH * consts.SQUARE_WIDTH - \
                consts.SQUARE_WIDTH:
            position = list(state["soldier location"])
            position[1] += consts.STEP
            state["soldier location"] = tuple(position)
    elif direction == consts.LEFT:
        if state["soldier location"][0] >= consts.SQUARE_WIDTH:
            position = list(state["soldier location"])
            position[1] -= consts.STEP
            state["soldier location"] = tuple(position)
    return state["soldier location"]


def current_soldier_position():
    pass


def soldier_in_night_background(current_location):
    soldier = pygame.image.load(consts.SOLDIER_NIGHT)
    soldier = pygame.transform.scale(soldier, (consts.SOLDIER_WIDTH * consts.SQUARE_WIDTH,
                                               consts.SOLDIER_HEIGHT * consts.SQUARE_HEIGHT))
    Screen.screen.blit(soldier, current_location)
