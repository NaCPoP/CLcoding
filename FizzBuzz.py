counting = 0
timer = 0
timer2 = 0

fizz = "fizz"
buzz = "buzz"
fizzBuzz = "fizzBuzz"

for i in range(200):
    counting += 1
    timer += 1
    timer2 += 1

    if timer + timer2 == 8:
        print(fizzBuzz)
        timer = 0
        timer2 = 0

    elif timer2 == 5:
        print(buzz)
        timer2 = 0

    elif timer == 3:
        print(fizz)
        timer = 0

    else:
        print(counting)