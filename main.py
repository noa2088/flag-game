import pygame
import Screen
import consts

state = {"is window open": True, "soldier location": consts.INITIAL_SOLDIER_POSITION, "direction": None}


def main():
    pygame.init()
    Screen.draw_game()
    while state["is window open"]:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    state["direction"] = consts.LEFT
                elif event.key == pygame.K_RIGHT:
                    state["direction"] = consts.RIGHT
                elif event.key == pygame.K_UP:
                    state["direction"] = consts.UP
                elif event.key == pygame.K_DOWN:
                    state["direction"] = consts.DOWN
                elif event.key == pygame.K_KP_ENTER:
                    Screen.night_screen()
                    pygame.time.wait(1000)
                move_soldier(state["direction"])
                Screen.draw_soldier(state["soldier location"])
            elif event.type == pygame.QUIT:
                state["is window open"] = False


def move_soldier(direction):
    if direction == consts.UP:
        if state["soldier location"][1] > 0:
            state["soldier location"][1] = state["soldier location"][1] - consts.STEP
    elif direction == consts.DOWN:
        if state["soldier location"][1] < consts.SCREEN_ROWS - 1:
            state["soldier location"][1] = state["soldier location"][1] + consts.STEP
    elif direction == consts.RIGHT:
        if state["soldier location"][0] < consts.SCREEN_COLUMNS - 1:
            state["soldier location"][0] = state["soldier location"][0] + consts.STEP
    elif direction == consts.LEFT:
        if state["soldier location"][0] > 0:
            state["soldier location"][0] = state["soldier location"][0] - consts.STEP
    return state["soldier location"]


def current_soldier_position():
    pass


def did_soldier_reach_the_flag():
    pass


def did_soldier_reach_a_mine():
    pass



main()
