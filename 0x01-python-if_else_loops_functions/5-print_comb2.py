#!/usr/bin/python3
for i in range(100):
    dt = str(i)
    if i < 10:
        dt = "0" + dt
    if i < 99:
        dt += ", "
    print("{0}".format(dt), end="")
print('\n', end="")
