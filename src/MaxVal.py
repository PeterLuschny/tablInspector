from functools import cache
from _tabltypes import Table

'''
[0] [1]
[1] [0, 1]
[2] [0, 1, 3]
[3] [0, 1, 7, 19]
[4] [0, 1, 15, 65, 175]
[5] [0, 1, 31, 211, 781, 2101]
[6] [0, 1, 63, 665, 3367, 11529, 31031]
[7] [0, 1, 127, 2059, 14197, 61741, 201811, 543607]
[8] [0, 1, 255, 6305, 58975, 325089, 1288991, 4085185, 11012415]   
[9] [0, 1, 511, 19171, 242461, 1690981, 8124571, 30275911, 93864121, 253202761]
'''

@cache
def _pow_row(n: int) -> tuple[int, ...]:
    """Returns (0**n, 1**n, ..., n**n), reusing (n-1)-th powers."""
    if n == 0:
        return (1,)  # 0^0 = 1
    prev = _pow_row(n - 1)
    return tuple(k * prev[k] for k in range(n)) + (n**n,)


@cache
def maxval(n: int) -> list[int]:
    if n == 0:
        return [1]
    pows = _pow_row(n)
    return [0] + [pows[k] - pows[k - 1] for k in range(1, n + 1)]


MaxVal = Table(
    maxval,
    "MaxVal",
    ["A199656"],
    "",
    r"k^n - (k-1)^n",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(MaxVal)
