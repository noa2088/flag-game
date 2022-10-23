import pygame
import consts
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("The Flag")
screen.fill(consts.BACKGROUND_COLOR)

pygame.quit()