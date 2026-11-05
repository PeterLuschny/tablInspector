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
    a396200row,  # the generating function
    "A396200",   # name of the table
    ["A396200"], # similar sequences in OEIS
    "",          # id of inverse sequence if it exists
    r"T(n,k)=0"  # TeX form of the defining formula T(n, k)
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(A396200, oeis=False)


''' OEIS
    A396200_Toff11           -> 0 
    A396200_Trev11           -> 0 
    A396200_Tantidiag        -> 0 
    A396200_Tacc             -> 0 
    A396200_Tder             -> 0 
    A396200_TablLcm          -> 0 
    A396200_EvenSum          -> 0 
    A396200_OddSum           -> 0 
    A396200_AltSum           -> 0 
    A396200_AccSum           -> 0 
    A396200_AccRevSum        -> 0 
    A396200_AntiDSum         -> 0 
    A396200_PosHalf          -> 0 
    A396200_NegHalf          -> 0 
    A396200_TransNat0        -> 0 
    A396200_TransNat1        -> 0 
    A396200_TransSqrs        -> 0 
    A396200_BinConv          -> 0 
    A396200_InvBinConv       -> 0 
    A396200_PolyRow2         -> 0 
    A396200_PolyRow3         -> 0 
    A396200_PolyCol2         -> 0 
    A396200_PolyCol3         -> 0 
    A396200_PolyDiag         -> 0 
    A396200_RevToff11        -> 0 
    A396200_RevTrev11        -> 0 
    A396200_RevTantidiag     -> 0 
    A396200_RevTacc          -> 0 
    A396200_RevTder          -> 0 
    A396200_RevEvenSum       -> 0 
    A396200_RevOddSum        -> 0 
    A396200_RevAccRevSum     -> 0 
    A396200_RevAntiDSum      -> 0 
    A396200_RevPosHalf       -> 0 
    A396200_RevNegHalf       -> 0 
    A396200_RevTransNat0     -> 0 
    A396200_RevTransNat1     -> 0 
    A396200_RevTransSqrs     -> 0 
    A396200_RevPolyRow2      -> 0 
    A396200_RevPolyRow3      -> 0 
    A396200_RevPolyCol3      -> 0 
    A396200_RevPolyDiag      -> 0 
    A396200_TablCol0         -> https://oeis.org/A225
    A396200_TablDiag0        -> https://oeis.org/A225
    A396200_TablMax          -> https://oeis.org/A225
    A396200_TablCol1         -> https://oeis.org/A295
    A396200_TablDiag1        -> https://oeis.org/A295
    A396200_CentralE         -> https://oeis.org/A302
    A396200_TablCol2         -> https://oeis.org/A2662
    A396200_TablDiag2        -> https://oeis.org/A2662
    A396200_TablCol3         -> https://oeis.org/A2663
    A396200_TablDiag3        -> https://oeis.org/A2663
    A396200_PolyRow1         -> https://oeis.org/A8585
    A396200_RevPolyRow1      -> https://oeis.org/A8585
    A396200_ColMiddle        -> https://oeis.org/A27306
    A396200_RevColMiddle     -> https://oeis.org/A27306
    A396200_CentralO         -> https://oeis.org/A32443
    A396200_RevCentralO      -> https://oeis.org/A32443
    A396200_TablGcd          -> https://oeis.org/A165022
    A396200_TablSum          -> https://oeis.org/A396199
    A396200_AbsSum           -> https://oeis.org/A396199
    A396200_Triangle         -> https://oeis.org/A396200
    A396200_Trev             -> https://oeis.org/A396200
    A396200_Talt             -> https://oeis.org/A396200
    A396200_RevTalt          -> https://oeis.org/A396200

    A396200: Distinct: 12, Hits: 23, Misses: 42
'''
