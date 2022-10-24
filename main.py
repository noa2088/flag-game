import pygame
import Screen
import Soldier
import consts
import MineField

state = {"is window open": True, "soldier location": consts.INITIAL_SOLDIER_POSITION, "direction": None}


def main():
    pygame.init()
    Screen.draw_game(state["soldier location"])
    Screen.grass_position()
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
                elif event.key == pygame.K_KP_ENTER or pygame.K_RETURN:
                    Screen.night_screen()
                    Soldier.soldier_in_night_background(state["soldier location"])
                    pygame.time.wait(1000)
                    Screen.draw_game(state["soldier location"])
                Screen.draw_game(move_soldier(state["direction"]))
                Screen.grass_position()
            elif event.type == pygame.QUIT:
                state["is window open"] = False
            if did_soldier_reach_the_flag():
                Screen.draw_win_message()
                state["is window open"] = False
            elif did_soldier_reach_a_mine():
                Screen.draw_lose_message()


def move_soldier(direction):
    if direction == consts.UP:
        if state["soldier location"][1] >= consts.SQUARE_HEIGHT:
            position = list(state["soldier location"])
            position[1] -= consts.STEP
            state["soldier location"] = tuple(position)
    elif direction == consts.DOWN:
        if state["soldier location"][1] <= consts.SCREEN_HEIGHT - consts.SOLDIER_HEIGHT * consts.SQUARE_HEIGHT - \
                consts.SQUARE_HEIGHT:
            position = list(state["soldier location"])
            position[1] += consts.STEP
            state["soldier location"] = tuple(position)
    elif direction == consts.RIGHT:
        if state["soldier location"][0] <= consts.SCREEN_WIDTH - consts.SOLDIER_WIDTH * consts.SQUARE_WIDTH - \
                consts.SQUARE_WIDTH:
            position = list(state["soldier location"])
            position[0] += consts.STEP
            state["soldier location"] = tuple(position)
    elif direction == consts.LEFT:
        if state["soldier location"][0] >= consts.SQUARE_WIDTH:
            position = list(state["soldier location"])
            position[0] -= consts.STEP
            state["soldier location"] = tuple(position)
    return state["soldier location"]


def current_soldier_position(current_position):
    present_location = MineField.convert_position_to_index(current_position[0], current_position[1])
    return present_location


def did_soldier_reach_a_mine():
    for location in Soldier.soldier_legs(current_soldier_position(state["soldier location"])):
        for i in range(len(MineField.mine_field)):
            for j in range(len(MineField.mine_field[i])):
                if i == location[0] and j == location[1]:
                    if MineField.mine_field[i][j] == consts.MINE:
                        return True
    return False


def did_soldier_reach_the_flag():
    for location in Soldier.Soldier_body(current_soldier_position(state["soldier location"])):
        for i in range(len(MineField.mine_field)):
            for j in range(len(MineField.mine_field[i])):
                if i == location[0] and j == location[1]:
                    if MineField.mine_field[i][j] == consts.FLAG:
                        return True
    return False


main()
