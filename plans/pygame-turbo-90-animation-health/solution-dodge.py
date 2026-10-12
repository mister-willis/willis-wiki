# Solution: Tiled Images, Animated Motion, and Health (pygame-turbo-90-animation-health)
import pgtrun
import random

WIDTH = 800
HEIGHT = 600

player = Actor("alien")
player.x = WIDTH / 2
player.y = HEIGHT - 100
player.health = 5
player.invincible = 0

health = []
for i in range(player.health):
    h = Actor("hud_heart")
    h.x = 25 + (i * 50)
    h.y = 25
    health.append(h)

weights = []
for i in range(3):
    w = Actor("weight")
    w.y = HEIGHT + 1
    weights.append(w)

def move_player():
    if keyboard.left:
        player.x = player.x - 10
    elif keyboard.right:
        player.x = player.x + 10

    if player.x < 0:
        player.x = WIDTH
    elif player.x > WIDTH:
        player.x = 0

def move_weights():
    for w in weights:
        if w.y >= HEIGHT:
            w.x = random.randint(0, WIDTH)
            w.y = 0
            animate(w, "accelerate", 2.0, y=HEIGHT)

def check_damage():
    # Count down from the last time we took damage
    if player.invincible > 0:
        player.invincible = player.invincible - 1
        player.image = "alien_hit"
    else:
        player.image = "alien"

    # If a weight touches us and the invincibility counter has run out,
    # reduce the health and restart the countdown from 20 frames.
    if player.collidelist(weights) != -1 and player.invincible == 0:
        if player.health >= 0:
            player.health = player.health - 1
            health[player.health].image = "hud_heart_empty"
            player.invincible = 20

def update():
    move_player()
    move_weights()
    check_damage()

def draw():
    screen.fill("white")
    if player.health > 0:
        for i in range(4):
            screen.blit("background_color_trees", (i * 256, HEIGHT - 256))
        player.draw()
        for w in weights:
            w.draw()
        for h in health:
            h.draw()
    else:
        screen.draw.text("Game Over",
                         center=(WIDTH / 2, HEIGHT / 2),
                         color="black", fontsize=60)

pgtrun.go()
