#!/usr/bin/python3
"""
A module used ot solved the locked box task
"""


def canUnlockAll(boxes):
    """ method that determines if all the given boxes can be opened or not"""
    box_length = len(boxes)
    myList = [0]
    for item in myList:
        for i in boxes[item]:
            if i not in myList:
                if i < box_length:
                    myList.append(i)
    if len(myList) == box_length:
        return True
    return False
