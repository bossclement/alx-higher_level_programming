#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    argc = len(argv)

    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        sys.exit(1)
    argv[1] = int(argv[1])
    argv[3] = int(argv[3])
    match argv[2]:
        case "+":
            print("{} + {} = {}".format(argv[1], argv[3], add(argv[1], argv[3])))
        case "-":
            print("{} - {} = {}".format(argv[1], argv[3], sub(argv[1], argv[3])))
        case "*":
            print("{} * {} = {}".format(argv[1], argv[3], mul(argv[1], argv[3])))
        case "/":
            print("{} / {} = {}".format(argv[1], argv[3], div(argv[1], argv[3])))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
