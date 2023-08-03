#!/usr/bin/python3

"""Lockboxes that contains many keys"""


def canUnlockAll(boxes):

    """Keys for the lockboxes"""

    def dfs(box_idx, visited):
        visited.add(box_idx)
        for key in boxes[box_idx]:
            if key not in visited:
                dfs(key, visited)

    n = len(boxes)
    visited = set()
    dfs(0, visited)

    return len(visited) == n


boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))

boxes = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes))
