prevNumber = 0
currentNumber = 0
number = 0

if currentNumber <= 0:
    number += 1

for i in range(50):
    currentNumber = prevNumber + number
    number = currentNumber
    prevNumber = number - prevNumber

    print(currentNumber)