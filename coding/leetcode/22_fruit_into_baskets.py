# 1. 同じ数字のカウント
# 2. 種類のカウント
#    - 1. が+1されるタイミングで+1する
#    - 種類が2つ以下の間はwindowを拡大する
#    - 種類が3つ以上になったらwindowを縮小する
#    - 1. を-1していき、0になったら種類も-1して終了
# 3. windowの最大数を取得する

from typing import List
from collections import defaultdict


def total_fruit(fruits: List[int]) -> int:
    fruits_counter = defaultdict(int)
    type_counter = 0
    left_index = 0

    max_total_fruit = 0

    for i in range(len(fruits)):
        fruits_counter[fruits[i]] += 1

        if fruits_counter[fruits[i]] == 1:
            type_counter += 1

        while type_counter > 2:
            fruits_counter[fruits[left_index]] -= 1

            if fruits_counter[fruits[left_index]] == 0:
                type_counter -= 1

            left_index += 1

        max_total_fruit = max(max_total_fruit, i - left_index + 1)

    return max_total_fruit


if __name__ == "__main__":
    print(total_fruit(fruits=[1, 2, 1]))
    print(total_fruit(fruits=[0, 1, 2, 2]))
    print(total_fruit(fruits=[1, 2, 3, 2, 2]))
    print(total_fruit(fruits=[1]))
    print(total_fruit(fruits=[1, 2, 3, 4, 5]))
    print(total_fruit(fruits=[1, 1, 1, 1, 1]))