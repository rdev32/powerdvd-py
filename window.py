import random
import os
import pygame
from pygame.locals import *

WINDOW_SIZE = {
    '800x600': (800, 600),
    '1024x768': (1024, 768),
    '1280x800': (1280, 720),
    '1366x768': (1366, 768),
    '1680x1050': (1680, 1050),
    '1920x1080': (1920, 1080),
    '2560x1600': (2560, 1600)
}


def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def main():
    resolution = WINDOW_SIZE['800x600']
    speed = [1, 1]
    colors = [
        pygame.Color(60, 240, 75),
        pygame.Color(250, 65, 65),
        pygame.Color(65, 90, 240),
        pygame.Color(255, 255, 255),
        pygame.Color(255, 240, 0)
    ]
    window = pygame.display.set_mode(resolution, vsync=1)
    pygame.mouse.set_visible(0)
    pygame.display.set_caption("PowerDVD")
    logopath = os.path.abspath(os.path.join('assets', 'logo.png'))
    if (not os.path.exists(logopath)):
        raise FileNotFoundError('logo.png not found')
    logo = pygame.image.load(logopath)
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
