from math import isqrt
from functools import cache
from _tabltypes import Table

"""  A396585

  [0] [    1]
  [1] [    0,     1]
  [2] [    3,     3,     4]
  [3] [    6,     9,    12,    16]
  [4] [   38,    44,    53,    65,    81]
  [5] [  160,   198,   242,   295,   360,   441]
  [6] [  905,  1065,  1263,  1505,  1800,  2160,  2601]
  [7] [ 4830,  5735,  6800,  8063,  9568, 11368, 13528, 16129]
  [8] [28308, 33138, 38873, 45673, 53736, 63304, 74672, 88200, 104329]
"""


@cache
def a396585row(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [0, 1]

    m1 = isqrt(a396585row(n - 1)[-1])
    m2 = isqrt(a396585row(n - 2)[-1])
    m = ((2 * n + 1) * m1 + (3 * n - 3) * m2) // (n + 2)

    row = [0] * (n + 1)
    row[n] = m * m

    prev_row = a396585row(n - 1)
    for k in range(n, 0, -1):
        row[k - 1] = row[k] - prev_row[k - 1]

    return row


A396585 = Table(
    a396585row,  # the generating function
    "A396585",   # name of the table
    ["A396585"], # similar sequences in OEIS
    "",          # id of inverse sequence if it exists
    r"T(n,k)=0"  # TeX form of the defining formula T(n, k)
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(A396585, oeis=False)


''' OEIS
    A396585_Trev             -> 0 
    A396585_Toff11           -> 0 
    A396585_Trev11           -> 0 
    A396585_Tantidiag        -> 0 
    A396585_Tacc             -> 0 
    A396585_Tder             -> 0 
    A396585_TablCol1         -> 0 
    A396585_TablCol2         -> 0 
    A396585_TablCol3         -> 0 
    A396585_TablDiag1        -> 0 
    A396585_TablDiag2        -> 0 
    A396585_TablDiag3        -> 0 
    A396585_TablLcm          -> 0 
    A396585_EvenSum          -> 0 
    A396585_OddSum           -> 0 
    A396585_AltSum           -> 0 
    A396585_AccSum           -> 0 
    A396585_AccRevSum        -> 0 
    A396585_AntiDSum         -> 0 
    A396585_ColMiddle        -> 0 
    A396585_CentralO         -> 0 
    A396585_PosHalf          -> 0 
    A396585_NegHalf          -> 0 
    A396585_TransNat0        -> 0 
    A396585_TransNat1        -> 0 
    A396585_TransSqrs        -> 0 
    A396585_BinConv          -> 0 
    A396585_PolyRow2         -> 0 
    A396585_PolyRow3         -> 0 
    A396585_PolyCol2         -> 0 
    A396585_PolyCol3         -> 0 
    A396585_PolyDiag         -> 0 
    A396585_RevToff11        -> 0 
    A396585_RevTrev11        -> 0 
    A396585_RevTantidiag     -> 0 
    A396585_RevTacc          -> 0 
    A396585_RevTalt          -> 0 
    A396585_RevTder          -> 0 
    A396585_RevEvenSum       -> 0 
    A396585_RevOddSum        -> 0 
    A396585_RevAccRevSum     -> 0 
    A396585_RevAntiDSum      -> 0 
    A396585_RevColMiddle     -> 0 
    A396585_RevCentralO      -> 0 
    A396585_RevPosHalf       -> 0 
    A396585_RevNegHalf       -> 0 
    A396585_RevTransNat0     -> 0 
    A396585_RevTransNat1     -> 0 
    A396585_RevTransSqrs     -> 0 
    A396585_RevPolyRow2      -> 0 
    A396585_RevPolyRow3      -> 0 
    A396585_RevPolyCol3      -> 0 
    A396585_RevPolyDiag      -> 0 
    A396585_TablGcd          -> https://oeis.org/A12
    A396585_InvBinConv       -> https://oeis.org/A12
    A396585_RevPolyRow1      -> https://oeis.org/A12
    A396585_PolyRow1         -> https://oeis.org/A27
    A396585_TablDiag0        -> https://oeis.org/A133053
    A396585_TablMax          -> https://oeis.org/A133053
    A396585_TablCol0         -> https://oeis.org/A172361
    A396585_Triangle         -> https://oeis.org/A396585
    A396585_Talt             -> https://oeis.org/A396585
    A396585_TablSum          -> https://oeis.org/A396648
    A396585_AbsSum           -> https://oeis.org/A396648
    A396585_CentralE         -> https://oeis.org/A397326

    A396585: Distinct: 8, Hits: 12, Misses: 53
'''
