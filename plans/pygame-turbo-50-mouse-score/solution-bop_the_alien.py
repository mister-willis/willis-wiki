# Solution: Random Numbers, Mouse Clicks, and Keeping Score (pygame-turbo-50-mouse-score)
# Includes both challenges: misses cost a point, and the respawn keeps a margin.
import pgtrun
import random

WIDTH = 800
HEIGHT = 600
MARGIN = 64  # half the alien's width, so it never hangs off an edge

target = Actor("alien")
target.x = WIDTH / 2
target.y = HEIGHT / 2
target.score = 0

def draw():
    screen.fill("skyblue")
    target.draw()
    screen.draw.text(f"Score: {target.score}", (20, 20), fontsize=48, color="black")

def on_mouse_down(pos):
    if target.collidepoint(pos):
        target.score = target.score + 1
        target.x = random.randint(MARGIN, WIDTH - MARGIN)
        target.y = random.randint(MARGIN, HEIGHT - MARGIN)
    else:
        target.score = target.score - 1

pgtrun.go()
