# Solution: Rotation, Tiles, and Solid Walls (pygame-turbo-70-rotation-walls)
import pgtrun

WIDTH = 800
HEIGHT = 600

tank = Actor("tank_blue")
tank.x = WIDTH / 2
tank.y = HEIGHT / 2
tank.angle = 0

walls = []
for i in range(10):
    w = Actor("wall")
    w.x = i * 50
    w.y = 100
    walls.append(w)

def update():
    original_x = tank.x
    original_y = tank.y

    if keyboard.left:
        tank.x = tank.x - 2
        tank.angle = 180
    elif keyboard.right:
        tank.x = tank.x + 2
        tank.angle = 0
    elif keyboard.up:
        tank.y = tank.y - 2
        tank.angle = 90
    elif keyboard.down:
        tank.y = tank.y + 2
        tank.angle = 270

    if tank.collidelist(walls) != -1:
        tank.x = original_x
        tank.y = original_y

def draw():
    screen.fill("lawngreen")
    tank.draw()
    for w in walls:
        w.draw()

pgtrun.go()

# Challenge version of the keyboard block, using Pygame Turbo's move_forward():
#
#     if keyboard.left:
#         tank.angle = 180
#     elif keyboard.right:
#         tank.angle = 0
#     elif keyboard.up:
#         tank.angle = 90
#     elif keyboard.down:
#         tank.angle = 270
#     if keyboard.left or keyboard.right or keyboard.up or keyboard.down:
#         tank.move_forward(2)
