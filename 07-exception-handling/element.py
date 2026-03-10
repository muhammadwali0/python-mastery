## Program to write a function that takes a list and an index as input and returns the element at the given index

from typing import Any, List


def element(items: List[Any], n: int) -> Any:
    try:
        result = items[n]
        return result

    except IndexError as ie:
        print(f"ERROR: {ie}")

    except Exception:
        print("ERROR: an unexpected error occurred")


print("Result:", element(["a", "b", "c", "d", "e"], 9))
