from functools import cache
from _tabltypes import Table

"""  A394824

  [0]         1;
  [1]         1,       1;
  [2]         4,       3,       1;
  [3]        27,      17,       5,      1;
  [4]       256,     142,      38,      7,     1;
  [5]      3125,    1569,     389,     67,     9,    1;
  [6]     46656,   21576,    5016,    816,   104,   11,   1;
  [7]    823543,  355081,   78077,  12085,  1471,  149,  13,  1;
  [8]  16777216, 6805296, 1424560, 210968, 24648, 2402, 202, 15, 1;
"""

@cache
def a394824row(n: int) -> list[int]:
    row = [0] * (n + 1)
    row[n] = 1
    for k in range(n, 0, -1):
        row[k - 1] = (2 * k - 1) * row[k] + k * (n - k) * (row[k + 1] if k + 1 <= n else 0)
    return row


A394824 = Table(
    a394824row,  # the generating function
    "A394824",   # name of the table
    ["A394824"], # similar sequences in OEIS
    "",          # id of inverse sequence if it exists
    r"((2k + 1)T(n, k+1) + (k + 1)T(n, k+2))/(n - k)"  # TeX form of the defining formula
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(A394824, oeis=True)
