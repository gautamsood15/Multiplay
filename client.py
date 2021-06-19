import pygame


width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

def redrawWindow():

    win.fill((255,255,255))
    pygame.display.update()

def main():
    pass

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()