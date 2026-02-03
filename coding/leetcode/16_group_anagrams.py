from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    group = defaultdict(list)

    for str in strs:
        counter = [0] * 26

        for s in str:
            counter[ord(s) - ord("a")] += 1

        group[tuple(counter)].append(str)

    return list(group.values())


if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams([""]))
    print(groupAnagrams(["a"]))
