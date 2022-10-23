import Screen

SQUARE_WIDTH = 22
SQUARE_HEIGHT = 22
SCREEN_ROWS = 25
SCREEN_COLUMNS = 50
SCREEN_WIDTH = SQUARE_WIDTH * SCREEN_COLUMNS
SCREEN_HEIGHT = SQUARE_HEIGHT * SCREEN_ROWS
GREEN = (55, 125, 61)
BACKGROUND_COLOR = GREEN
BLACK = (14, 15, 14)
BACKGROUND_NIGHT_COLOR = BLACK
INITIAL_TEXT = """Welcome to The Flag game.  
Have Fun!"""
FLAG_WIDTH = 4 ###
FLAG_HEIGHT = 4 ###
SOLDIER_WIDTH = 2 ###
SOLDIER_HEIGHT = 4 ###
FONT_NAME = "Calibri"

EXPLOSION = "explotion.png"
FLAG = "flag.png"
GRASS = "grass.png"
INJURY = "injury.png"
MINE = "mine.png"
SNAKE = "snake.png"
SOLDIER = "soldier.png"
SOLDIER2 = "soldier2.png"
SOLDIER_NIGHT = "soldier_night"
INITIAL_POSITION_SOLDIER = Screen.screen.blit(SOLDIER, (0, 0))
FLAG_POSITION = Screen.screen.blit(FLAG, (0, 0))
