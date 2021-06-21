import pygame


width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = (x,y,width,height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.keys.get_pressed()

        if keys[pygame.K_LEFT]:
            pass
        if keys[pygame.K_RIGHT]:
            pass
        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass

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
        redrawWindow()