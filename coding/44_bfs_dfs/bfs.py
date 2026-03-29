from typing import List
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def depth(root: Node) -> List[int]:
    queue = deque([(root, 0)])
    answer = []

    while queue:
        node, level = queue.popleft()
        answer.append(level)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return answer


def binary_tree_structure(root: Node) -> List[List[int]]:
    queue = deque([(root, 0)])

    current_level = 0
    current_node_vals = []
    ans = []

    while queue:
        node, level = queue.popleft()
        if level == current_level:
            current_node_vals.append(node.val)
        else:
            ans.append(current_node_vals)

            current_level = level
            current_node_vals = [node.val]

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    ans.append(current_node_vals)

    return ans


def good_nodes(root: Node) -> int:
    ans = 0

    queue = deque([(root, root.val)])
    while queue:
        node, path_max = queue.popleft()
        if node.val >= path_max:
            ans += 1

        if node.left:
            queue.append((node.left, max(path_max, node.left.val)))

        if node.right:
            queue.append((node.right, max(path_max, node.right.val)))

    return ans
