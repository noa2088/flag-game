import consts
import pygame
import random
import Screen

mine_field = []


def create_mine_field():
    for i in range(int(consts.SCREEN_ROWS)):
        row = []
        for j in range(int(consts.SCREEN_COLUMNS)):
            row.append(consts.EMPTY_SQUARE)
        mine_field.append(row)


create_mine_field()


# for i in range(len(mine_field)):
#     for j in range(len(mine_field[i])):
#         print(mine_field[i][j], end=" ")
#     print()

def convert_position_to_index(position_x, position_y):  # הפונקציה מקבלת מיקום לפי פיקסלים
    index = [position_y / 22, position_x / 22]
    return index


def flag_index():
    flag_x = consts.SCREEN_WIDTH - consts.FLAG_WIDTH * consts.SQUARE_WIDTH
    flag_y = consts.SCREEN_HEIGHT - consts.FLAG_HEIGHT * consts.SQUARE_HEIGHT
    flag_idx = convert_position_to_index(flag_x, flag_y)
    for i in range(len(mine_field)):
        for j in range(len(mine_field[i])):
            if i == flag_idx[0] and j == flag_idx[1]:
                for k in range(int(flag_idx[0]), int(flag_idx[0] + 3)):  # ADD CONST
                    for o in range(int(flag_idx[1]), int(flag_idx[1] + 4)):  # ADD CONST
                        mine_field[k][o] = consts.FLAG_SQUARE
    return mine_field


flag_index()


def add_random_mines(xmax, ymax):
    random_location_list = []
    mine = pygame.image.load(consts.MINE)
    mine = pygame.transform.scale(mine, (consts.MINE_WIDTH, consts.MINE_HEIGHT))
    for i in range(20):
        x = random.randint(0, xmax)
        y = random.randint(0, ymax)
        while (x, y) in random_location_list or x % 22 != 0 or y % 22 != 0 or is_mine_index_invalid(x, y):
            x = random.randint(0, xmax)
            y = random.randint(0, ymax)
        # Screen.screen.blit(mine, (x, y))
        random_location_list.append((x, y))
        # pygame.display.flip()
    return random_location_list


def is_mine_index_invalid(x, y):
    if 1012 <= x <= 1100 and 462 <= y <= 528: #ADD NUMBERS TO CONSTS
        return True
    elif 0 <= x <= 88 and 0 <= y <= 88:
        return True
    return False


random_location_list = add_random_mines(consts.SCREEN_WIDTH-consts.MINE_WIDTH,
                                            consts.SCREEN_HEIGHT-consts.MINE_HEIGHT)

def mines_indexes():
    for location in random_location_list:
        mine_x = location[0]
        mine_y = location[1]
        mine_index = convert_position_to_index(mine_x, mine_y) # gets the left top corner of mine
        for i in range(int(mine_index[1]), int(mine_index[1] + 3)):
            mine_field[int(mine_index[0])][i] = consts.MINE_SQUARE
    return mine_field

mines_indexes()

for i in range(len(mine_field)):
    for j in range(len(mine_field[i])):
        print(mine_field[i][j], end=" ")
    print()