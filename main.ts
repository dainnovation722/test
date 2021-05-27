let b: number[];
function collision_judgement(X: number, Y: number): boolean {
    if (Y < 0) {
        //  collision in upper side
        return false
    } else if (Y > 4) {
        //  collision in lower side
        return false
    } else if (X - 1 < 0) {
        //  collision in left side
        return false
    } else if (X + 1 > 4) {
        //  collision in right side
        return false
    } else {
        return true
    }
    
}

function return_coordinate(X: number, Y: number): number[] {
    let direction: number;
    while (true) {
        direction = randint(1, 4)
        if (direction == 1) {
            //  right
            X += 1
            if (collision_judgement(X, Y)) {
                break
            }
            
        } else if (direction == 2) {
            //  left
            X += -1
            if (collision_judgement(X, Y)) {
                break
            }
            
        } else if (direction == 3) {
            //  upper
            Y += -1
            if (collision_judgement(X, Y)) {
                break
            }
            
        } else if (direction == 4) {
            //  lower
            Y += 1
            if (collision_judgement(X, Y)) {
                break
            }
            
        }
        
    }
    return [X, Y]
}

let X = 0
let Y = 0
while (true) {
    b = return_coordinate(X, Y)
    X = b[0]
    Y = b[1]
    console.log(b)
    led.plot(X, Y)
    led.plot(X + 1, Y)
    led.plot(X - 1, Y)
    basic.pause(1000)
    basic.clearScreen()
}
