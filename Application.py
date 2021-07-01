import random
import pygame
from pygame.locals import *

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

def main():
    resolution = (800, 600)
    speed = [1, 1]
    colors = [
            pygame.Color(60, 240, 75),
            pygame.Color(250, 65, 65),
            pygame.Color(65, 90, 240),
            pygame.Color(255, 255, 255),
            pygame.Color(255, 240, 0)]
    window = pygame.display.set_mode(resolution, FULLSCREEN)
    pygame.mouse.set_visible(0)
    pygame.display.set_caption("PowerDVD")
    logo = pygame.image.load("assets//logo.png")
    logo = pygame.transform.smoothscale(logo, (360, 180))
    obj = logo.get_rect()
    clock = pygame.time.Clock()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()

        obj = obj.move(speed)
        if obj.left < 0 or obj.right > resolution[0]:
            speed[0] = -speed[0]
            fill(logo, random.choice(colors))
        if obj.top < 0 or obj.bottom > resolution[1]:
            speed[1] = -speed[1]
            fill(logo, random.choice(colors))

        window.fill(pygame.Color(0, 0, 0))
        window.blit(logo, obj)
        clock.tick(60)
        pygame.display.flip()
    
if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()