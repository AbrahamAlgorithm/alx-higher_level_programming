#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i != 0 or j != 1:
            print(", {:02d}".format(i * 10 + j), end="")
        else:
            print("{:02d}".format(i * 10 + j), end="")
print()
