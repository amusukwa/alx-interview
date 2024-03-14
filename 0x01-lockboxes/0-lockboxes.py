#!/usr/bin/python3
""" 0-lockboxes.py"""

from collections import deque

def canUnlockAll(boxes):
    """determines if all boxes can be locked"""
    n = len(boxes)
    visited = set()
    queue = deque([0])  # Start from box 0

    while queue:
        current_box = queue.popleft()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
