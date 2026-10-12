# Solution: Multiple Worlds and Game Over Reset (pygame-turbo-100-game-modes)
import pgtrun

WIDTH = 800
HEIGHT = 600
GROUND = 400
GRAVITY = 1

runner = Actor("ninja0")
runner.x = 100
runner.y = 400
runner.mode = "costume"
runner.speed_y = 0
runner.obstacles_timeout = 0
runner.score = 0

# one animation per costume, from animations/ninja, animations/dino,
# and animations/knight; each runs through all its frames once per second
runner.anim.add("ninja", durations=1.0)
runner.anim.add("dino", durations=1.0)
runner.anim.add("knight", durations=1.0)
runner.anim.set_base("ninja")

obstacles = []

def draw_game():
    screen.fill("skyblue")
    screen.draw.filled_rect(Rect(0, 400,800, 200), (88, 242, 152))
    runner.draw()
    for o in obstacles:
        o.draw()

def draw_score():
    screen.draw.text(f"Score: {runner.score}", (30, 30), color="white", fontsize=60)

def draw_game_over():
    screen.fill("black")
    screen.draw.text("GAME OVER", center=(WIDTH / 2, HEIGHT / 2),
                     color="white", fontsize=60)
    screen.draw.text("Press Return to restart", center=(WIDTH / 2, HEIGHT / 2 + 50),
                     color="white", fontsize=60)

def draw_costume():
    screen.fill("black")
    runner.draw()
    screen.draw.text("Press Space to select a player",
                     centerx=WIDTH / 2, top=20, color="white", fontsize=60)
    screen.draw.text("Press Return to start",
                     center=(WIDTH / 2, HEIGHT / 2), color="white", fontsize=60)

def apply_gravity():
    runner.y += runner.speed_y
    runner.speed_y += GRAVITY
    if runner.y > GROUND:
        runner.speed_y = 0
        runner.y = GROUND

def do_obstacles():
    # obstacles
    runner.obstacles_timeout += 1
    if runner.obstacles_timeout > 50:
        c = Actor('cactus')
        c.x = 850
        c.y = 430
        obstacles.append(c)
        runner.obstacles_timeout = 0

    for o in obstacles.copy():
        o.x -= 8
        if o.x < 0:
            obstacles.remove(o)

def check_damage():
    if runner.collidelist(obstacles) >= 0:
        runner.mode = "game over"

def reset():
    runner.score = 0
    runner.speed_y = 0
    obstacles.clear()
    runner.obstacles_timeout = 0
    runner.mode = "costume"

def change_costume():
    if runner.anim.base == "ninja":
        runner.anim.set_base("dino")
    elif runner.anim.base == "dino":
        runner.anim.set_base("knight")
    elif runner.anim.base == "knight":
        runner.anim.set_base("ninja")

def on_key_down(key):
    if runner.mode == "play":
        if key == keys.SPACE and runner.y == GROUND:
            runner.speed_y = -15
    elif runner.mode == "game over":
        if key == keys.RETURN:
            reset()
    elif runner.mode == "costume":
        if key == keys.SPACE:
            change_costume()
        elif key == keys.RETURN:
            runner.mode = "play"

def update():
    if runner.mode == "play":
        apply_gravity()
        do_obstacles()
        runner.score += 1
        check_damage()

def draw():
    if runner.mode == "play":
        draw_game()
        draw_score()
    elif runner.mode == "game over":
        draw_game_over()
        draw_score()
    elif runner.mode == "costume":
        draw_costume()

pgtrun.go()
