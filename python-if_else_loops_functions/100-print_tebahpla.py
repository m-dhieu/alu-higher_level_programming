#!/usr/bin/python3


for i in range(25, -1, -1):
    print("{:c}".format(97 + i) if i % 2 == 0 else "{:c}".format(65 + i), end='')
