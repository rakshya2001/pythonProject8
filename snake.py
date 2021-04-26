import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('SNAKE GAME')
game_over= False
while not game_over:
    for event in pygame.event.get():
        print(event) # it prints out all the action that takes place on the screen

pygame.quit()
quit()