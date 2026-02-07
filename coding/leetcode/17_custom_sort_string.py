from collections import defaultdict


def custom_sort_string(order: str, s: str) -> str:
    order_map = defaultdict(int)

    for i in range(len(order)):
        order_map[order[i]] = i

    return "".join(sorted(s, key=lambda c: order_map[c]))


if __name__ == "__main__":
    print(custom_sort_string(order="cba", s="abcd"))
    print(custom_sort_string(order="bcafg", s="abcd"))
