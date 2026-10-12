# Solution: Pygame Turbo: Nice Bike! (pygame-turbo-20-nice-bike)
import pgtrun

WIDTH = 500
HEIGHT = 280

def draw():
    screen.fill("skyblue")

    # wheels
    screen.draw.circle((90, 180), 80, "black")
    screen.draw.circle((410, 180), 80, "black")

    # frame: (170, 50) -> (330, 50) -> (250, 180) -> rear wheel center -> back to (170, 50)
    screen.draw.line((170, 50), (330, 50), "black")
    screen.draw.line((330, 50), (250, 180), "black")
    screen.draw.line((250, 180), (90, 180), "black")
    screen.draw.line((90, 180), (170, 50), "black")

    # seat tube: lower frame point (250, 180) up to (150, 20)
    screen.draw.line((250, 180), (150, 20), "black")

    # steering tube: front wheel center up to (310, 20)
    screen.draw.line((410, 180), (310, 20), "black")

    # handlebar: 40 long, centered on the top of the steering tube
    screen.draw.line((290, 20), (330, 20), "black")

    # seat: 80 long, rear end at x = 120
    screen.draw.line((120, 20), (200, 20), "black")

    # bonus: crank and pedal
    screen.draw.filled_circle((250, 180), 20, "white")
    screen.draw.circle((250, 180), 20, "red")
    screen.draw.line((250, 180), (275, 205), "red")
    screen.draw.line((265, 205), (285, 205), "red")

pgtrun.go()
