#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if i < x:
            dt = f"{i}{x}"
            if int(dt) < 89:
                dt += ", "
            print("{}".format(dt), end="")
print("\n", end="")
