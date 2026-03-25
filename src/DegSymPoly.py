from functools import cache
from _tabltypes import Table

"""
0 [1]
1 [1,  2]
2 [1,  3,   6]
3 [1,  5,  14,   30]
4 [1,  8,  31,   85,   190]
5 [1, 13,  70,  246,   671,   1547]
6 [1, 21, 157,  707,  2353,   6405,  15106]
7 [1, 34, 353, 2037,  8272,  26585,  72302, 173502]
8 [1, 55, 793, 5864, 29056, 110254, 345775, 940005, 2286648]
"""

@cache
def _S(n: int, k: int) -> int:
    return (_S(n, k - 1) + sum(_S(2 * j, k - 1) * _S(n - 1 - 2 * j, k)
           for j in range(1 + (n - 1) // 2)) if k > 0 else 1)


def degsympoly(n:int) -> list[int]:
    return [_S(n, k) for k in range(n + 1)]


# simpler, but much slower
#from itertools import accumulate
#def Trow(n: int) -> list[int]:
#    vec = [0] * (n + 1)
#    for k in range(n + 1):
#        v = [1] * (k + 1)
#        for _ in range(n):
#            v = list(accumulate(reversed(v)))
#        vec[k] = v[-1]
#    return vec


DegSymPoly = Table(
    degsympoly, 
    "DegSymPoly", 
    ["A394080", "A050446", "A050447"], 
    "", 
    r"T(n, k - 1 ) + \sum_{j = 0}^{\lfloor \frac{n-1}{2} \rfloor} T(2 j, k - 1) T(n - 1 - 2 j, k)"
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(DegSymPoly)
