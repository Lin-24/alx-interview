#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""

def canUnlockAll(boxes):

    if (type(boxes) is not list):
        return False

    if (len(boxes) == 0):
        return False

    keys = [0]
    for m in keys:
        for n in boxes[m]:
            if n not in keys and n != m and n < len(boxes) and n != 0:
                keys.append(n)
    if len(keys) == len(boxes):
        return True
    else:
        return False
