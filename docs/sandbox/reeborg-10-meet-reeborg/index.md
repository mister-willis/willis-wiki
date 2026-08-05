---
title: "Meet Reeborg!"
lab_id: reeborg-10-meet-reeborg
unit: reeborg
sequence: 10
builds_on: []
courses: [cs6]
lesson_plan: lesson-plan.md
status: published
tags: [python, sequencing, functions, comments]
---

# Meet Reeborg!

![Reeborg, a friendly robot, waving hello.](images/reeborg-robot.png){ width="240" }

Reeborg is a robot who lives on a grid and does exactly what you tell it — no
more, no less. That is the whole problem. Today you'll send Reeborg on a few
short missions and find out just how literal a computer really is.

---

## Overview

You'll learn the Python basics for controlling Reeborg — moving, turning,
picking things up, and keeping your code readable — by solving a series of
short missions.

!!! note "Before you start"
    Each mission below has its own button that loads the right world. **Save
    your work after every step** — you'll turn all of them in at the end.

!!! abstract "You've got it when…"
    - [x] Reeborg completes every mission: returns home, clears the dandelions, walks around the lake, and cleans up the gravel path.
    - [x] Your code uses **comments** and blank lines so it's easy to read.
    - [x] You've saved a `.py` file for every step.

!!! info "Collaboration & AI"
    **Work:** On your own. You can compare notes with a neighbor, but write your own commands.

    **AI — AIAS Level 1, No AI:** These missions are about learning to think like the robot. Write every command yourself this time. [What the levels mean.](https://aiassessmentscale.com/)

---

## The Missions

### Step 0 — Meet Reeborg

[Open Step 0](https://reeborg.cs20.ca/?lang=en&mode=python&menu=worlds/menus/sk_menu.json&name=Step%200){ .md-button }

We'll do this one together: playing and resetting Reeborg's world, adding a
command, dealing with errors, using Reeborg's keyboard, and saving and loading
your work.

### Step 1 — Return Home

[Open Step 1](https://reeborg.cs20.ca/?lang=en&mode=python&menu=worlds/menus/sk_menu.json&name=Step%201){ .md-button }

**Your mission:** give Reeborg the instructions to return home.

### Step 2 — Take and Put

[Open Step 2](https://reeborg.cs20.ca/?lang=en&mode=python&menu=worlds/menus/sk_menu.json&name=Step%202){ .md-button }

Use the `take()` function to pick an item up, and the `put()` function to set it
down.

**Your mission:** pick up the dandelions, put them in the garbage, and return
home.

### Step 3 — Turning

[Open Step 3](https://reeborg.cs20.ca/?lang=en&mode=python&menu=worlds/menus/sk_menu.json&name=Step%203){ .md-button }

Use the `turn_left()` function to make Reeborg turn left.

**Your mission:** make Reeborg walk around the lake.

### Step 4 — Comments and Whitespace

[Open Step 4](https://reeborg.cs20.ca/?lang=en&mode=python&menu=worlds/menus/sk_menu.json&name=Step%204){ .md-button }

Use **comments** to organize your code and make it easier to read. A comment is
a note for humans that the computer ignores; it starts with the `#` symbol. Use
**whitespace** — blank lines — the same way, to group your code into sections
the computer also ignores.

```python
# This is an example of
# a simple program where Reeborg draws a square,
# leaving an object behind at each corner.

# draw the first side
move()
move()
turn_left()
put()

# draw the second side
move()
move()
turn_left()
put()

# draw the third side
move()
turn_left()
put()

# draw the fourth side
move()
move()
turn_left()
put()
```

Use the `pause()` function to make Reeborg wait for you to click the play
button.

**Your mission:** make Reeborg walk down the gravel path, picking up dandelions
as it finds them and dropping them in the garbage cans (the grey dandelion
images). Have Reeborg `pause()` at each dandelion it picks. Use comments and
whitespace to keep your solution readable.

---

## Turn It In

Turn in your Python (`.py`) file for each step:

- [ ] Step 0.py
- [ ] Step 1.py
- [ ] Step 2.py
- [ ] Step 3.py
- [ ] Step 4.py

---

*Credit: Adapted from Dan Schellenberg's [Computer Science 20 textbook](https://cs20.ca/).*
