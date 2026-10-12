# Solution: Gravity, Jumping, and Bouncing (pygame-turbo-40-gravity-jumping)
import pgtrun

WIDTH = 800
HEIGHT = 600
GROUND_Y = 400  # The y-coordinate of the ground
GRAVITY = 1  # gravity will change the up/down speed of our actors
JUMP_SPEED = -15
BOUNCE_FACTOR = 0.6   # 0 = no bounce, 1 = perfect bounce

alien = Actor("alien")
alien.x = WIDTH / 2
alien.y = 0
alien.speed_y = 0  # how fast the alien should be moving in the up/down direction

def update():
    # add gravity to the alien's up/down speed
    alien.speed_y = alien.speed_y + GRAVITY

    # add jump speed to the alien's up/down speed (only from the ground)
    if keyboard.up and alien.y >= GROUND_Y:
        alien.speed_y = alien.speed_y + JUMP_SPEED

    # apply the total up/down speed to the alien's position
    alien.y += alien.speed_y

    # bounce on the ground
    if alien.y >= GROUND_Y:
        alien.y = GROUND_Y

        # only bounce if we're moving downward
        if alien.speed_y > 0:
            alien.speed_y = -alien.speed_y * BOUNCE_FACTOR

            # optional: stop tiny jittering bounces
            if abs(alien.speed_y) < 1:
                alien.speed_y = 0

def draw():
    screen.fill("skyblue")
    lawn = Rect(0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y)
    screen.draw.filled_rect(lawn, "lightgreen")
    alien.draw()

pgtrun.go()
