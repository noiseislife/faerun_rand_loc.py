import os
import pygame
import random


def main():
    image = pygame.image.load('faerun2.jpg')
    image = pygame.transform.scale(image, (1024, 768))
    pygame.init()
    white = (255, 255, 255)
    red = (255, 0, 0)
    image_size = image.get_size()
    X = image_size[0]
    Y = image_size[1]
    position = (random.randint(0, X), random.randint(0, Y))
    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Faerun')

    while True:
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.circle(display_surface, red, position, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.unicode == 'q'):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.unicode == 'n':
                position = (random.randint(0, X), random.randint(0, Y))
            pygame.display.update()


if __name__ == '__main__':
    main()
