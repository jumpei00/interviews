from collections import deque


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def bfs(root: Node):
    que = deque([root])

    while que:
        node = que.popleft()
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)


def dfs(node: Node):
    if node.left:
        dfs(node.left)
    if node.right:
        dfs(node.right)
