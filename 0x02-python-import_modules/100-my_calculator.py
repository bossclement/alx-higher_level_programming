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
    op = argv[2]
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(
        argv[1], op, argv[3], ops[op](argv[1], argv[3])
        )
    )
