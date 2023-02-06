import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from score import score


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Космические защитники')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = score(screen, stats)

    while True:
        controls.event(screen,gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.updatescreen(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen,stats, sc, inos, bullets)
            controls.update_inos(stats, screen,sc, gun, inos, bullets)


run()