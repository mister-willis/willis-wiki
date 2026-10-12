# Solution: Dumb Enemies and Smart Enemies (pygame-turbo-80-enemies)
import pgtrun
import random

WIDTH = 800
HEIGHT = 600

player = Actor("tank_blue")
player.x = WIDTH / 2
player.y = HEIGHT / 2

enemies = []
for i in range(3):
    e = Actor("tank_red")
    e.x = random.randint(0, WIDTH)
    e.y = random.randint(0, HEIGHT)
    e.angle = random.randint(0, 3) * 90
    enemies.append(e)

def move_player():
    if keyboard.right:
        player.angle = 0
        player.x = player.x + 1
    elif keyboard.up:
        player.angle = 90
        player.y = player.y - 1
    elif keyboard.left:
        player.angle = 180
        player.x = player.x - 1
    elif keyboard.down:
        player.angle = 270
        player.y = player.y + 1

def move_enemies():
    for e in enemies:
        if e.angle == 0:  # facing right
            e.x = e.x + 1
        elif e.angle == 90:  # facing up
            e.y = e.y - 1
        elif e.angle == 180:  # facing left
            e.x = e.x - 1
        elif e.angle == 270:  # facing down
            e.y = e.y + 1

        if e.x < 0 or e.x > WIDTH or e.y < 0 or e.y > HEIGHT:
            e.angle = (e.angle + 180) % 360

def move_enemies_smart():
    for e in enemies:
        if e.x > player.x:
            e.angle = 180
        elif e.x < player.x:
            e.angle = 0
        elif e.y > player.y:
            e.angle = 90
        elif e.y < player.y:
            e.angle = 270

    move_enemies()

def update():
    move_player()
    # move_enemies()
    move_enemies_smart()

def draw():
    screen.fill("lawngreen")
    player.draw()
    for e in enemies:
        e.draw()

pgtrun.go()

# Challenge version, using Pygame Turbo's angle_to() and move_forward():
#
# def move_enemies_smart():
#     for e in enemies:
#         e.angle = e.angle_to(player)
#         e.move_forward(1)
