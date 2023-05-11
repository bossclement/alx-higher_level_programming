#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc, argv = len(sys.argv), sys.argv
    print("{0} {1}".format(argc - 1, "arguments:" if argc > 3 else "argument."))
    for i in range(argc - 1):
        print("{0}: {1}".format(i + 1, argv[i + 1]))
