#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
   is a method that determines if all the boxes can be opened.
    Returns: True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
