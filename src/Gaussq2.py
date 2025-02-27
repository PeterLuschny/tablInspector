from functools import cache
from _tabltypes import Table

"""Gaussian coefficient for q = 2.

[0]  1;
[1]  1,   1;
[2]  1,   3,    1;
[3]  1,   7,    7,     1;
[4]  1,  15,   35,    15,     1;
[5]  1,  31,  155,   155,    31,    1;
[6]  1,  63,  651,  1395,   651,   63,   1;
[7]  1, 127, 2667, 11811, 11811, 2667, 127, 1;
"""


@cache
def gaussq2(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = gaussq2(n - 1)
    pow = [1] + gaussq2(n - 1)
    p = 2
    for k in range(1, n):
        pow[k] = row[k - 1] + p * row[k]
        p *= 2
    return pow


Gaussq2 = Table(
    gaussq2,
    "Gaussq2",
    ["A022166"],
    "A000000",
    r"\prod_{i=k+1}^{n} (2^i - 1) \ / \ \prod_{i=1}^{n-k} (2^i - 1)",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Gaussq2)






''' OEIS
    Gaussq2_Toff11        -> 0 
    Gaussq2_Trev11        -> 0 
    Gaussq2_Tinv11        -> 0 
    Gaussq2_Trevinv11     -> 0 
    Gaussq2_Tantidiag     -> 0 
    Gaussq2_Tacc          -> 0 
    Gaussq2_Tder          -> 0 
    Gaussq2_TablLcm       -> 0 
    Gaussq2_OddSum        -> 0 
    Gaussq2_AccSum        -> 0 
    Gaussq2_AccRevSum     -> 0 
    Gaussq2_AntiDSum      -> 0 
    Gaussq2_NegHalf       -> 0 
    Gaussq2_TransNat0     -> 0 
    Gaussq2_TransNat1     -> 0 
    Gaussq2_TransSqrs     -> 0 
    Gaussq2_BinConv       -> 0 
    Gaussq2_InvBinConv    -> 0 
    Gaussq2_PolyRow3      -> 0 
    Gaussq2_PolyCol3      -> 0 
    Gaussq2_PolyDiag      -> 0 
    Gaussq2_RevToff11     -> 0 
    Gaussq2_RevTrev11     -> 0 
    Gaussq2_RevTinv11     -> 0 
    Gaussq2_RevTantidiag  -> 0 
    Gaussq2_RevTacc       -> 0 
    Gaussq2_RevTder       -> 0 
    Gaussq2_RevOddSum     -> 0 
    Gaussq2_RevAccRevSum  -> 0 
    Gaussq2_RevAntiDSum   -> 0 
    Gaussq2_RevNegHalf    -> 0 
    Gaussq2_RevTransNat0  -> 0 
    Gaussq2_RevTransNat1  -> 0 
    Gaussq2_RevTransSqrs  -> 0 
    Gaussq2_RevPolyRow3   -> 0 
    Gaussq2_RevPolyCol3   -> 0 
    Gaussq2_RevPolyDiag   -> 0 
    Gaussq2_TablCol0      -> https://oeis.org/A12
    Gaussq2_TablDiag0     -> https://oeis.org/A12
    Gaussq2_PolyRow1      -> https://oeis.org/A27
    Gaussq2_RevPolyRow1   -> https://oeis.org/A27
    Gaussq2_TablCol1      -> https://oeis.org/A225
    Gaussq2_TablDiag1     -> https://oeis.org/A225
    Gaussq2_TablCol2      -> https://oeis.org/A6095
    Gaussq2_TablDiag2     -> https://oeis.org/A6095
    Gaussq2_TablCol3      -> https://oeis.org/A6096
    Gaussq2_TablDiag3     -> https://oeis.org/A6096
    Gaussq2_CentralE      -> https://oeis.org/A6098
    Gaussq2_TablMax       -> https://oeis.org/A6099
    Gaussq2_ColMiddle     -> https://oeis.org/A6099
    Gaussq2_RevColMiddle  -> https://oeis.org/A6099
    Gaussq2_TablSum       -> https://oeis.org/A6116
    Gaussq2_AbsSum        -> https://oeis.org/A6116
    Gaussq2_TablGcd       -> https://oeis.org/A19320
    Gaussq2_Triangle      -> https://oeis.org/A22166
    Gaussq2_Trev          -> https://oeis.org/A22166
    Gaussq2_Talt          -> https://oeis.org/A22166
    Gaussq2_RevTalt       -> https://oeis.org/A22166
    Gaussq2_PolyRow2      -> https://oeis.org/A28387
    Gaussq2_RevPolyRow2   -> https://oeis.org/A28387
    Gaussq2_Tinv          -> https://oeis.org/A135950
    Gaussq2_Tinvrev       -> https://oeis.org/A135950
    Gaussq2_Trevinv       -> https://oeis.org/A158474
    Gaussq2_PosHalf       -> https://oeis.org/A182176
    Gaussq2_PolyCol2      -> https://oeis.org/A182176
    Gaussq2_RevPosHalf    -> https://oeis.org/A182176
    Gaussq2_CentralO      -> https://oeis.org/A218449
    Gaussq2_RevCentralO   -> https://oeis.org/A218449
    Gaussq2_EvenSum       -> https://oeis.org/A289541
    Gaussq2_RevEvenSum    -> https://oeis.org/A289541
    Gaussq2_AltSum        -> https://oeis.org/A290974

    Gaussq2: Distinct: 18, Hits: 34, Misses: 37
'''
