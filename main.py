import pygame

print("Hello")

pygame.init()

screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
screen.fill(pygame.Color("white"))

pygame.display.set_caption("TIC TAC TOE GAME")

clock = pygame.time.Clock()

running = True

while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False