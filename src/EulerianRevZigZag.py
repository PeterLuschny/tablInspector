from functools import cache
from Binomial import binomial
from _tabltypes import Table

"""EulerianRevZigZag triangle.

[0] [1]
[1] [0, 1]
[2] [0, 0, 1]
[3] [0, 0, 1,  1]
[4] [0, 0, 1,  3,  1]
[5] [0, 0, 1,  7,   7,    1]
[6] [0, 0, 1, 14,  31,   14,    1]
[7] [0, 0, 1, 26, 109,  109,   26,   1]
[8] [0, 0, 1, 46, 334,  623,  334,  46,  1]
[9] [0, 0, 1, 79, 937, 2951, 2951, 937, 79, 1]
"""


@cache
def _s(n: int, k: int) -> int:
    if k == 0:
        return 1
    return _s(n, k - 1) + sum(
        _s(2 * j, k - 1) * _s(n - 1 - 2 * j, k)
        for j in range(1 + (n - 1) // 2)
    )


@cache
def eulerianrevzigzag(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [0, 1]
    b = [(-1 if j & 1 else 1) * binomial(n + 1)[j] for j in range(n + 1)]
    r = [sum(b[j] * _s(n, k - j) for j in range(k + 1)) for k in range(n - 1)]
    return [0, 0] + r


EulerianRevZigZag = Table(
    eulerianrevzigzag, 
    "EulerianRevZigZag", 
    ["A205497"], 
    "A000000", 
    r"%%"
)

if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(EulerianRevZigZag)
    
    #dim = 8
    #M = EulerianRevZigZag.inv(dim)
    #for r in M: print(r)

"""
[0] [1, 1, 1,   1, 1, 1, 1, 1, 1]
[1] [0, 0, 1,   3, 7, 14, 26, 46, 79]
[2] [0, 0, 1,   7, 31, 109, 334, 937, 2475]
[3] [0, 0, 1,  14, 109, 623, 2951, 12331, 47191]
[4] [0, 0, 1,  26, 334, 2951, 20641, 123216, 656683]
[5] [0, 0, 1,  46, 937, 12331, 123216, 1019051, 7349140]
[6] [0, 0, 1,  79, 2475, 47191, 656683, 7349140, 70148989]
[7] [0, 0, 1, 133, 6267, 169416, 3217526, 47816612, 593513485]
[8] [0, 0, 1, 221, 15393, 579889, 14786816, 287357460, 4571277561]
[9] [0, 0, 1, 364, 36976, 1914226, 64657546, 1622135139, 32672880245]
"""