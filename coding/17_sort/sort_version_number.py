from typing import List
from functools import cmp_to_key


def sort_versions(versions: List[str]) -> List[str]:
    def sort_key(version: str) -> List[int]:
        return [int(s) for s in version.split(".")]

    versions.sort(key=sort_key)
    return versions


def sort_versions_v2(versions: List[str]) -> List[str]:
    def compare(v1: str, v2: str) -> int:
        a = [int(v) for v in v1.split(".")]
        b = [int(v) for v in v2.split(".")]

        if a == b:
            return 0
        if a < b:
            return -1
        return 1

    versions.sort(key=cmp_to_key(compare))
    return versions


if __name__ == "__main__":
    print(sort_versions(["10.1.0", "1.1.0", "0.1.1"]))
    print(sort_versions(["0.12.1", "0.2.1"]))
    print(sort_versions_v2(["10.1.0", "1.1.0", "0.1.1"]))
    print(sort_versions_v2(["0.12.1", "0.2.1"]))
