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

    InspectTable(A394824, oeis=False)


''' OEIS
    A394824_Trev             -> 0 
    A394824_Toff11           -> 0 
    A394824_Trev11           -> 0 
    A394824_Tinv11           -> 0 
    A394824_Trevinv11        -> 0 
    A394824_Tantidiag        -> 0 
    A394824_Tacc             -> 0 
    A394824_Tder             -> 0 
    A394824_TablCol2         -> 0 
    A394824_TablCol3         -> 0 
    A394824_TablDiag3        -> 0 
    A394824_TablLcm          -> 0 
    A394824_TablSum          -> 0 
    A394824_EvenSum          -> 0 
    A394824_OddSum           -> 0 
    A394824_AltSum           -> 0 
    A394824_AbsSum           -> 0 
    A394824_AccSum           -> 0 
    A394824_AccRevSum        -> 0 
    A394824_AntiDSum         -> 0 
    A394824_ColMiddle        -> 0 
    A394824_CentralE         -> 0 
    A394824_CentralO         -> 0 
    A394824_PosHalf          -> 0 
    A394824_NegHalf          -> 0 
    A394824_TransNat0        -> 0 
    A394824_TransNat1        -> 0 
    A394824_TransSqrs        -> 0 
    A394824_BinConv          -> 0 
    A394824_InvBinConv       -> 0 
    A394824_PolyRow3         -> 0 
    A394824_PolyCol2         -> 0 
    A394824_PolyCol3         -> 0 
    A394824_PolyDiag         -> 0 
    A394824_RevToff11        -> 0 
    A394824_RevTrev11        -> 0 
    A394824_RevTantidiag     -> 0 
    A394824_RevTacc          -> 0 
    A394824_RevTalt          -> 0 
    A394824_RevTder          -> 0 
    A394824_RevEvenSum       -> 0 
    A394824_RevOddSum        -> 0 
    A394824_RevAccRevSum     -> 0 
    A394824_RevAntiDSum      -> 0 
    A394824_RevColMiddle     -> 0 
    A394824_RevCentralO      -> 0 
    A394824_RevPosHalf       -> 0 
    A394824_RevNegHalf       -> 0 
    A394824_RevTransNat0     -> 0 
    A394824_RevTransNat1     -> 0 
    A394824_RevTransSqrs     -> 0 
    A394824_RevPolyRow3      -> 0 
    A394824_RevPolyCol3      -> 0 
    A394824_RevPolyDiag      -> 0 
    A394824_TablDiag0        -> https://oeis.org/A12
    A394824_TablGcd          -> https://oeis.org/A12
    A394824_PolyRow1         -> https://oeis.org/A27
    A394824_RevPolyRow1      -> https://oeis.org/A27
    A394824_TablCol0         -> https://oeis.org/A312
    A394824_TablMax          -> https://oeis.org/A312
    A394824_TablCol1         -> https://oeis.org/A1865
    A394824_TablDiag1        -> https://oeis.org/A5408
    A394824_PolyRow2         -> https://oeis.org/A14206
    A394824_RevPolyRow2      -> https://oeis.org/A33951
    A394824_TablDiag2        -> https://oeis.org/A182868
    A394824_Triangle         -> https://oeis.org/A394824
    A394824_Talt             -> https://oeis.org/A394824

    A394824: Distinct: 10, Hits: 13, Misses: 54
'''
