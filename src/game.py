def collision_judgement(X: number, Y: number):
    if Y < 0:
        # collision in upper side
        return False
    elif Y > 4:
        # collision in lower side
        return False
    elif (X - 1) < 0:
        # collision in left side
        return False
    elif (X + 1) > 4:
        # collision in right side
        return False
    else:
        return True
def GOOD_END():
    basic.show_string("END")
def daphnia():
    move.change(LedSpriteProperty.X, randint(-1, 1))
    move.change(LedSpriteProperty.Y, randint(-1, 1))
    basic.pause(display_interval)
def BAD_END():
    basic.show_string("DEATH... GAMEOVER")

def on_button_pressed_a():
    global status
    if status < status_max:
        music.play_tone(784, music.beat(BeatFraction.WHOLE))
        status += 1
        basic.show_leds("""
            . # . # .
            . . . . .
            # # # # #
            # . . . #
            . # # # .
            """)
        basic.clear_screen()
    else:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.show_leds("""
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            . . . . .
            """)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def status_updater(dead_time: number):
    global time_break, hungry_interval, time_counter, status, death
    time_break = hungry_interval * time_counter
    if input.running_time() - dead_time > time_break:
        time_counter += 1
        status += 0 - 1
        if status > status_min:
            status += 0 - 1
        else:
            death = True
def opening():
    basic.show_string("Hello!")

def on_button_pressed_b():
    normal = 0
    if status >= happy:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
    elif status >= normal:
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            . # # # .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def growth():
    global dead_time
    opening()
    dead_time = input.running_time()
    # start caring mode
    # 1st stage (daphnia)
    while 5 > (input.running_time() - dead_time) / 1000 and not (death):
        daphnia()
        status_updater(dead_time)
        if 5 <= (input.running_time() - dead_time) / 1000:
            move.delete()
            X = randint(0, 4)
            Y = randint(0, 4)
            break
    # 2nd stage (worm)
    while 5 <= (input.running_time() - dead_time) / 1000 and not (death):
        b = return_coordinate(X, Y)
        X = b[0]
        Y = b[1]
        print(b)
        led.plot(X, Y)
        led.plot(X + 1, Y)
        led.plot(X - 1, Y)
        basic.pause(display_interval)
        basic.clear_screen()
        status_updater(dead_time)
        if 10 <= (input.running_time() - dead_time) / 1000:
            break
    # 3rd stage (human)
    while 10 <= (input.running_time() - dead_time) / 1000 and not (death):
        human()
        status_updater(dead_time)
        if 15 <= (input.running_time() - dead_time) / 1000:
            break
    if not (death):
        GOOD_END()
    else:
        BAD_END()
def return_coordinate(X: number, Y: number):
    while True:
        direction = randint(1, 4)
        if direction == 1:
            # right
            X += 1
            if collision_judgement(X, Y):
                break
        elif direction == 2:
            # left
            X += -1
            if collision_judgement(X, Y):
                break
        elif direction == 3:
            # upper
            Y += -1
            if collision_judgement(X, Y):
                break
        elif direction == 4:
            # lower
            Y += 1
            if collision_judgement(X, Y):
                break
    return [X, Y]
def main():
    growth()
def human():
    basic.show_leds("""
        # . # . #
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.pause(display_interval)
    basic.show_leds("""
        . . # . .
        # # # # #
        # . # . #
        . # . # .
        . # . # .
        """)
    basic.pause(display_interval)
    basic.show_leds("""
        # . # . .
        # # # # #
        . . # . #
        . # . # .
        . # . # .
        """)
    basic.pause(display_interval)
    basic.show_leds("""
        . . # . #
        # # # # #
        # . # . .
        . # . # .
        . # . # .
        """)
    basic.pause(display_interval)
    basic.show_leds("""
        # . # . .
        # # # # #
        . . # . #
        . # . # .
        # . . # .
        """)
    basic.pause(display_interval)
    basic.show_leds("""
        . . # . #
        # # # # #
        # . # . .
        . # . # .
        . # . . #
        """)
    basic.pause(display_interval)
"""

parameters for status meter

"""
"""

parameters for meta info

"""
dead_time = 0
death = False
time_break = 0
status = 0
time_counter = 0
move: game.LedSprite = None
display_interval = 0
happy = 0
status_max = 0
status_min = 0
updater = False
status_min = -100
status_max = 30
happy = 10
# parameters for a character
display_interval = 1000
move = game.create_sprite(0, 0)
# parameters for time
hungry_interval = 3000
time_counter = 1
main()
