class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


INF = 1 << 30


def good_nodes(root: Node) -> int:
    global ans
    ans = 0

    def _dfs(node: Node, max_value: int):
        if not node:
            return

        max_value = max(node.val, max_value)
        if node.val >= max_value:
            global ans
            ans += 1

        _dfs(node.left, max_value)
        _dfs(node.right, max_value)

    _dfs(root, -INF)

    return ans


def diameter(root: Node) -> int:
    def _diameter(node: Node) -> tuple[int, int]:
        if not node:
            return 0, -1

        left_max, left_depth = _diameter(node.left)
        right_max, right_depth = _diameter(node.right)

        current_max = max(left_max, right_max, left_depth + right_depth + 2)
        current_depth = max(left_depth, right_depth) + 1

        return current_max, current_depth

    ans_max, _ = _diameter(root)

    return ans_max


def diameter_2(root: Node) -> int:
    global ans
    ans = 0

    def _diameter(node: Node) -> int:
        global ans

        if not node:
            return 0

        left_max_depth = _diameter(node.left)
        right_max_depth = _diameter(node.right)

        ans = max(ans, left_max_depth, right_max_depth)

        return max(left_max_depth, right_max_depth) + 1

    _diameter(root)

    return ans
