from functools import cache
from _tabltypes import Table

"""  A395345

[0]  1
[1]  0, 1
[2]  0, 1, 1
[3]  0, 2, 3, 1
[4]  0, 7, 11, 6, 1
[5]  0, 34, 55, 35, 10, 1
[6]  0, 213, 349, 240, 85, 15, 1
[7]  0, 1630, 2695, 1939, 770, 175, 21, 1
[8]  0, 14747, 24527, 18186, 7749, 2030, 322, 28, 1
"""

@cache
def a395345row(n: int) -> list[int]:
    if n == 0: return [1]
    row = [0]*(n + 1)
    row[n] = 1
    prev = a395345row(n - 1)
    for k in range(n - 1, 0, -1):
        row[k] = k * row[k+1] + prev[k-1] - (n-k-1) * prev[k]
    return row


A395345 = Table(
    a395345row,     # the generating function
    "A395345",   # name of the table
    ["A395345"], # similar sequences in OEIS
    "?",         # id of inverse sequence if it exists
    r"T(n,k)=0"  # TeX form of the defining formula T(n, k)
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(A395345)
