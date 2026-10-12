# Solution: Projectiles with Lists and Custom Functions (pygame-turbo-60-projectiles)
import pgtrun

WIDTH = 800
HEIGHT = 600

player = Actor("alien")
player.x = 100
player.y = HEIGHT / 2
player.cooldown = 0

hearts = []

def throw_heart():
    h = Actor("heart")
    h.x = player.x + 30 # start slightly in front of player
    h.y = player.y
    hearts.append(h)

def update():
    if player.cooldown > 0:
        player.cooldown = player.cooldown - 1

    if keyboard.space and player.cooldown == 0:
        throw_heart()
        player.cooldown = 10

    for h in hearts.copy():
        h.x = h.x + 10

        if h.x < 0 or h.x > WIDTH or h.y < 0 or h.y > HEIGHT:
            hearts.remove(h)

def draw():
    screen.fill("skyblue")
    player.draw()
    for h in hearts:
        h.draw()

pgtrun.go()
