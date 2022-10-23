import pygame

state = {"is window open": True}


def main():
    pygame.init()
    while state["is window open"]:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_KP_ENTER:
                    pass
            elif event.type == pygame.QUIT:
                state["is window open"] = False


def did_soldier_reach_the_flag():
    pass


def did_soldier_reach_a_mine():
    pass