counting = 0


for i in range(100):
    counting += 1

    if counting % 3 + counting % 5 == 0:
        print("FizzBuzz")

    elif counting % 3 == 0:
        print ("Fizz")

    elif counting % 5 == 0:
        print("Buzz")

    else:
        print (counting)