# Solution: Actor Positioning and Platforms (pygame-turbo-110-platforms)
import pgtrun

WIDTH = 800
HEIGHT = 600
GRAVITY = 1
JUMP_SPEED = -15

player = Actor("alien")
player.x = WIDTH / 2
player.bottom = HEIGHT
player.jumping = False
player.speed_y = 0

platforms = []
for i in range(WIDTH // 50):
    w = Actor("wall")
    w.bottom = HEIGHT
    w.left = i * 50
    platforms.append(w)

for i in range(8):
    w = Actor("wall")
    w.left = i * 50 + 200
    w.bottom = HEIGHT - 200
    platforms.append(w)

def on_key_down(key):
    # up key and not already jumping
    if key == keys.UP and not player.jumping:
        player.speed_y = JUMP_SPEED
        player.jumping = True

def update():
    # Apply gravity
    player.speed_y += GRAVITY
    player.y += player.speed_y

    # If the movement caused a collision, move position back
    collision_index = player.collidelist(platforms)
    if collision_index != -1:
        # Get the wall piece the player collided with
        collided = platforms[collision_index]

        # Check if the player collided while moving down
        if player.speed_y >= 0:
            # move player up to no collision position
            player.bottom = collided.top
        else:
            # The player collided moving up.
            # move player down to no collision position
            player.top = collided.bottom

        # Set the up/down speed to zero
        player.speed_y = 0
        player.jumping = False

    # Handle player left movement
    if keyboard.left and player.left > 0:
        player.x -= 5

        # if the movement caused a collision
        collision_index = player.collidelist(platforms)
        if collision_index != -1:
            # get object that player collided with
            collided = platforms[collision_index]
            # use it to calculate position where there is no collision
            player.left = collided.right

    # Handle player right movement
    elif keyboard.right and player.right < WIDTH:
        player.x += 5

        # if the movement caused a collision
        collision_index = player.collidelist(platforms)
        if collision_index != -1:
            # get object that player collided with
            collided = platforms[collision_index]
            # use it to calculate position where there is no collision
            player.right = collided.left

def draw():
    screen.fill("skyblue")
    player.draw()
    for p in platforms:
        p.draw()

pgtrun.go()
