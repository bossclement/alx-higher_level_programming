#!/usr/bin/python3
if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        binary = file.read()
        file.close()

    names = dir(binary)
    for name in names:
        if name[:2] != "__":
            print(name)
