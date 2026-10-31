from functools import cache
from _tabltypes import Table

"""
T(n, k) = Sum_{i=0..n} binomial(2*i, i) * binomial(n - 2*i, k - i).

  [0]     1;
  [1]     3,    3;
  [2]     7,    4,   7;
  [3]    15,   11,  11,  15;
  [4]    31,   26,  16,  26,  31;
  [5]    63,   57,  42,  42,  57,  63;
  [6]   127,  120,  99,  64,  99, 120, 127;
  [7]   255,  247, 219, 163, 163, 219, 247, 255;
  [8]   511,  502, 466, 382, 256, 382, 466, 502,  511;
  [9]  1023, 1013, 968, 848, 638, 638, 848, 968, 1013, 1023;
"""

@cache
def a396200row(n: int) -> list[int]:
    if n == 0:
        return [1]

    prev = a396200row(n - 1)
    p0 = prev[0]
    row = [0]*(n + 1)

    row[0] = 2*p0 + 1
    row[n] = row[0]

    for k in range(1, n):
        row[k] = prev[k-1] + prev[k]

    if n % 2 == 0: 
        row[n//2] = p0 + 1

    return row


A396200 = Table(
    a396200row,     # the generating function
    "A396200",   # name of the table
    ["A396200"], # similar sequences in OEIS
    "",          # id of inverse sequence if it exists
    r"T(n,k)=0"  # TeX form of the defining formula T(n, k)
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(A396200)
