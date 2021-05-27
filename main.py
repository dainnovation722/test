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

X = 0
Y = 0


while True:
    b = return_coordinate(X, Y)
    X = b[0]
    Y = b[1]
    print(b)
    led.plot(X, Y)
    led.plot(X + 1, Y)
    led.plot(X - 1, Y)
    basic.pause(1000)
    basic.clear_screen()