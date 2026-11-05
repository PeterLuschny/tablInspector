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
    a395345row,  # the generating function
    "A395345",   # name of the table
    ["A395345"], # similar sequences in OEIS
    "?",         # id of inverse sequence if it exists
    r"T(n,k)=0"  # TeX form of the defining formula T(n, k)
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(A395345, oeis=False)


''' OEIS
    A395345_Trev             -> 0 
    A395345_Trevinv          -> 0 
    A395345_Toff11           -> 0 
    A395345_Trev11           -> 0 
    A395345_Trevinv11        -> 0 
    A395345_Tantidiag        -> 0 
    A395345_Tacc             -> 0 
    A395345_Tder             -> 0 
    A395345_TablCol2         -> 0 
    A395345_TablCol3         -> 0 
    A395345_TablDiag3        -> 0 
    A395345_TablLcm          -> 0 
    A395345_TablMax          -> 0 
    A395345_TablSum          -> 0 
    A395345_EvenSum          -> 0 
    A395345_OddSum           -> 0 
    A395345_AltSum           -> 0 
    A395345_AbsSum           -> 0 
    A395345_AccSum           -> 0 
    A395345_AccRevSum        -> 0 
    A395345_AntiDSum         -> 0 
    A395345_ColMiddle        -> 0 
    A395345_CentralE         -> 0 
    A395345_CentralO         -> 0 
    A395345_PosHalf          -> 0 
    A395345_NegHalf          -> 0 
    A395345_TransNat0        -> 0 
    A395345_TransNat1        -> 0 
    A395345_TransSqrs        -> 0 
    A395345_BinConv          -> 0 
    A395345_InvBinConv       -> 0 
    A395345_PolyCol2         -> 0 
    A395345_PolyCol3         -> 0 
    A395345_PolyDiag         -> 0 
    A395345_RevToff11        -> 0 
    A395345_RevTrev11        -> 0 
    A395345_RevTantidiag     -> 0 
    A395345_RevTacc          -> 0 
    A395345_RevTalt          -> 0 
    A395345_RevTder          -> 0 
    A395345_RevEvenSum       -> 0 
    A395345_RevOddSum        -> 0 
    A395345_RevAccRevSum     -> 0 
    A395345_RevAntiDSum      -> 0 
    A395345_RevColMiddle     -> 0 
    A395345_RevCentralO      -> 0 
    A395345_RevPosHalf       -> 0 
    A395345_RevNegHalf       -> 0 
    A395345_RevTransNat0     -> 0 
    A395345_RevTransNat1     -> 0 
    A395345_RevTransSqrs     -> 0 
    A395345_RevPolyCol3      -> 0 
    A395345_RevPolyDiag      -> 0 
    A395345_TablCol0         -> https://oeis.org/A7
    A395345_TablDiag0        -> https://oeis.org/A12
    A395345_TablGcd          -> https://oeis.org/A12
    A395345_RevPolyRow1      -> https://oeis.org/A12
    A395345_PolyRow1         -> https://oeis.org/A27
    A395345_RevPolyRow2      -> https://oeis.org/A27
    A395345_TablDiag1        -> https://oeis.org/A217
    A395345_RevPolyRow3      -> https://oeis.org/A384
    A395345_TablDiag2        -> https://oeis.org/A914
    A395345_PolyRow2         -> https://oeis.org/A2378
    A395345_PolyRow3         -> https://oeis.org/A7531
    A395345_TablCol1         -> https://oeis.org/A74059
    A395345_Tinv             -> https://oeis.org/A135338
    A395345_Tinv11           -> https://oeis.org/A135338
    A395345_Triangle         -> https://oeis.org/A395345
    A395345_Talt             -> https://oeis.org/A395345

    A395345: Distinct: 12, Hits: 16, Misses: 53
'''
