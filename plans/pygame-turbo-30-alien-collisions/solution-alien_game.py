# Solution: More Characters and Collisions (pygame-turbo-30-alien-collisions)
import pgtrun

WIDTH = 800
HEIGHT = 600

# create the alien
alien = Actor("alien")
alien.x = 0
alien.y = 300

# create the bee, away from the alien
bee = Actor("bee_a")
bee.x = 600
bee.y = 300

# the bee's wing flap: animations/bee/bee_0.png and bee_1.png,
# one full flap every 0.2 seconds, looping on its own
bee.anim.add("bee", durations=0.2)
bee.anim.set_base("bee")

def update():
    # keyboard keys for moving the alien
    if keyboard.right:
        alien.x = alien.x + 10
    if keyboard.left:
        alien.x = alien.x - 10
    if keyboard.up:
        alien.y = alien.y - 10
    if keyboard.down:
        alien.y = alien.y + 10

    # keep the alien on the screen...wrap around if it goes beyond the screen
    if alien.x > WIDTH:
        alien.x = 0
    if alien.x < 0:
        alien.x = WIDTH
    if alien.y < 0:
        alien.y = HEIGHT
    if alien.y > HEIGHT:
        alien.y = 0

    # keyboard keys for moving the bee
    if keyboard.d:
        bee.x = bee.x + 10
    if keyboard.a:
        bee.x = bee.x - 10
    if keyboard.w:
        bee.y = bee.y - 10
    if keyboard.s:
        bee.y = bee.y + 10

    # keep the bee on the screen
    if bee.x > WIDTH:
        bee.x = 0
    if bee.x < 0:
        bee.x = WIDTH
    if bee.y < 0:
        bee.y = HEIGHT
    if bee.y > HEIGHT:
        bee.y = 0

    # the alien is allergic to bee stings
    if bee.colliderect(alien):
        alien.image = "alien_hit"
    else:
        alien.image = "alien"

def draw():
    screen.fill("skyblue")
    screen.draw.filled_circle((700, 100), 50, "yellow")
    alien.draw()
    bee.draw()

pgtrun.go()
