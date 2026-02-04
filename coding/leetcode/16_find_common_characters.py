from typing import List


def find_common_characters(words: List[str]) -> List[str]:
    word_map = [[0] * len(words) for _ in range(26)]

    for index, word in enumerate(words):
        for s in word:
            word_map[ord(s) - ord("a")][index] += 1

    results = []
    for index, list in enumerate(word_map):
        results += [chr(index + ord("a"))] * min(list)

    return results


if __name__ == "__main__":
    print(find_common_characters(["bella", "label", "roller"]))
    print(find_common_characters(["cool", "lock", "cook"]))
    print(
        find_common_characters(
            [
                "acabcddd",
                "bcbdbcbd",
                "baddbadb",
                "cbdddcac",
                "aacbcccd",
                "ccccddda",
                "cababaab",
                "addcaccd",
            ]
        )
    )
