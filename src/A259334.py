from functools import cache
from _tabltypes import Table

"""  A259334

  [0] [1]
  [1] [1, 1]
  [2] [3, 4, 2]
  [3] [16, 24, 18, 6]
  [4] [125, 200, 180, 96, 24]
  [5] [1296, 2160, 2160, 1440, 600, 120]
  [6] [16807, 28812, 30870, 23520, 12600, 4320, 720]
  [7] [262144, 458752, 516096, 430080, 268800, 120960, 35280, 5040]
  [8] [4782969, 8503056, 9920232, 8817984, 6123600, 3265920, 1270080, 322560, 40320]
"""

@cache
def a259334row(n: int) -> list[int]:
    if n == 0: return [1]
    row = [0] * (n + 1)
    row[n] = n * a259334row(n - 1)[n - 1]
    for k in range(n - 1, -1, -1):
        row[k] = (row[k + 1] * (n + 1) * (k + 1)) // ((n - k) * (k + 2))
    return row


A259334 = Table(
    a259334row,  # the generating function
    "A259334",   # name of the table
    ["A259334"], # similar sequences in OEIS
    "",          # id of inverse sequence if it exists
    r"(T(n, k + 1) (n + 1) (k + 1)) / ((n - k) (k + 2))"  # TeX form of the defining formula T(n, k)
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(A259334, oeis=False)
