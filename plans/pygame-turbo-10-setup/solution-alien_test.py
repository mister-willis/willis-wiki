import pgtrun

WIDTH = 800
HEIGHT = 600

alien = Actor("alien")
alien.x = WIDTH / 2
alien.y = HEIGHT / 2

def draw():
    screen.fill("skyblue")
    alien.draw()

pgtrun.go()
