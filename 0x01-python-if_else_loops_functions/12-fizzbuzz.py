#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        result = str(i)
        if i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz"
        elif i % 3 == 0:
            result = "Fizz"
        elif i % 5 == 0:
            result = "Buzz"
        print(result, end=" ")
    print("\n", end="")
