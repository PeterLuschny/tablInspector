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


''' OEIS
    A259334_Toff11 -> 0 
    A259334_Trev11 -> 0 
    A259334_Tantidiag -> 0 
    A259334_Tacc -> 0 
    A259334_Tder -> 0 
    A259334_TablCol2 -> 0 
    A259334_TablCol3 -> 0 
    A259334_TablDiag3 -> 0 
    A259334_TablLcm -> 0 
    A259334_TablMax -> 0 
    A259334_AltSum -> 0 
    A259334_AccSum -> 0 
    A259334_AntiDSum -> 0 
    A259334_ColMiddle -> 0 
    A259334_CentralE -> 0 
    A259334_CentralO -> 0 
    A259334_PosHalf -> 0 
    A259334_NegHalf -> 0 
    A259334_TransSqrs -> 0 
    A259334_BinConv -> 0 
    A259334_PolyRow3 -> 0 
    A259334_PolyCol2 -> 0 
    A259334_PolyCol3 -> 0 
    A259334_PolyDiag -> 0 
    A259334_RevToff11 -> 0 
    A259334_RevTrev11 -> 0 
    A259334_RevTantidiag -> 0 
    A259334_RevTacc -> 0 
    A259334_RevTder -> 0 
    A259334_RevEvenSum -> 0 
    A259334_RevOddSum -> 0 
    A259334_RevAccRevSum -> 0 
    A259334_RevAntiDSum -> 0 
    A259334_RevColMiddle -> 0 
    A259334_RevCentralO -> 0 
    A259334_RevPosHalf -> 0 
    A259334_RevNegHalf -> 0 
    A259334_RevTransNat1 -> 0 
    A259334_RevTransSqrs -> 0 
    A259334_RevPolyRow3 -> 0 
    A259334_RevPolyCol3 -> 0 
    A259334_RevPolyDiag -> 0 
    A259334_PolyRow1         -> https://oeis.org/A27
    A259334_RevPolyRow1      -> https://oeis.org/A27
    A259334_TablDiag0        -> https://oeis.org/A142
    A259334_TablSum          -> https://oeis.org/A169
    A259334_AbsSum           -> https://oeis.org/A169
    A259334_TablCol0         -> https://oeis.org/A272
    A259334_TransNat0        -> https://oeis.org/A435
    A259334_TablDiag1        -> https://oeis.org/A1563
    A259334_AccRevSum        -> https://oeis.org/A1865
    A259334_TransNat1        -> https://oeis.org/A1865
    A259334_RevPolyRow2      -> https://oeis.org/A56105
    A259334_PolyRow2         -> https://oeis.org/A58331
    A259334_TablGcd          -> https://oeis.org/A62763
    A259334_TablCol1         -> https://oeis.org/A89946
    A259334_Trev             -> https://oeis.org/A122525
    A259334_RevTalt          -> https://oeis.org/A122525
    A259334_EvenSum          -> https://oeis.org/A133297
    A259334_RevTransNat0     -> https://oeis.org/A185391
    A259334_Triangle         -> https://oeis.org/A259334
    A259334_Talt             -> https://oeis.org/A259334
    A259334_TablDiag2        -> https://oeis.org/A317527
    A259334_InvBinConv       -> https://oeis.org/A334316
    A259334_OddSum           -> https://oeis.org/A347994

    A259334: Distinct: 19, Hits: 23, Misses: 42
'''
