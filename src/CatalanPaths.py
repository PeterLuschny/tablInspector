from functools import cache
from _tabltypes import Table

"""Catalan paths.

[0]   1,
[1]   0,   1,
[2]   1,   0,   1,
[3]   0,   2,   0,   1,
[4]   2,   0,   3,   0,   1,
[5]   0,   5,   0,   4,   0,   1,
[6]   5,   0,   9,   0,   5,   0,   1,
[7]   0,  14,   0,  14,   0,   6,   0,  1,
[8]  14,   0,  28,   0,  20,   0,   7,  0,  1,
[9]   0,  42,   0,  48,   0,  27,   0,  8,  0,  1.
"""


@cache
def catalanpaths(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return catalanpaths(n - 1)[k] if k >= 0 and k < n else 0

    row = catalanpaths(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row


CatalanPaths = Table(
    catalanpaths,
    "CatalanPaths",
    ["A053121", "A052173", "A112554", "A322378"],
    "A049310",  # this is the Chebyshev S triangle
    r"is(k = 0)\ ? \ 0 : \frac{k+1}{n+1} \binom{n+1}{(n-k)/2}",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(CatalanPaths)






''' OEIS
    CatalanPaths_Trev11        -> 0 
    CatalanPaths_Trevinv11     -> 0 
    CatalanPaths_Tantidiag     -> 0 
    CatalanPaths_Tacc          -> 0 
    CatalanPaths_Tder          -> 0 
    CatalanPaths_TablLcm       -> 0 
    CatalanPaths_ColMiddle     -> 0 
    CatalanPaths_TransSqrs     -> 0 
    CatalanPaths_PolyDiag      -> 0 
    CatalanPaths_RevToff11     -> 0 
    CatalanPaths_RevTrev11     -> 0 
    CatalanPaths_RevTantidiag  -> 0 
    CatalanPaths_RevTder       -> 0 
    CatalanPaths_RevColMiddle  -> 0 
    CatalanPaths_RevTransNat0  -> 0 
    CatalanPaths_RevTransSqrs  -> 0 
    CatalanPaths_RevPolyDiag   -> 0 
    CatalanPaths_TablDiag1     -> https://oeis.org/A4
    CatalanPaths_TablDiag3     -> https://oeis.org/A4
    CatalanPaths_RevOddSum     -> https://oeis.org/A4
    CatalanPaths_TablDiag0     -> https://oeis.org/A12
    CatalanPaths_RevPolyRow1   -> https://oeis.org/A12
    CatalanPaths_TablDiag2     -> https://oeis.org/A27
    CatalanPaths_PolyRow1      -> https://oeis.org/A27
    CatalanPaths_AccRevSum     -> https://oeis.org/A79
    CatalanPaths_TransNat1     -> https://oeis.org/A79
    CatalanPaths_TablCol2      -> https://oeis.org/A245
    CatalanPaths_TablSum       -> https://oeis.org/A1405
    CatalanPaths_AltSum        -> https://oeis.org/A1405
    CatalanPaths_AbsSum        -> https://oeis.org/A1405
    CatalanPaths_RevEvenSum    -> https://oeis.org/A1405
    CatalanPaths_TablCol3      -> https://oeis.org/A2057
    CatalanPaths_PolyRow2      -> https://oeis.org/A2522
    CatalanPaths_RevPolyRow2   -> https://oeis.org/A2522
    CatalanPaths_RevCentralO   -> https://oeis.org/A26005
    CatalanPaths_TransNat0     -> https://oeis.org/A45621
    CatalanPaths_Trev          -> https://oeis.org/A52173
    CatalanPaths_RevTalt       -> https://oeis.org/A52173
    CatalanPaths_Triangle      -> https://oeis.org/A53121
    CatalanPaths_Talt          -> https://oeis.org/A53121
    CatalanPaths_PolyCol2      -> https://oeis.org/A54341
    CatalanPaths_RevPosHalf    -> https://oeis.org/A54341
    CatalanPaths_RevNegHalf    -> https://oeis.org/A54341
    CatalanPaths_PolyRow3      -> https://oeis.org/A54602
    CatalanPaths_RevPolyRow3   -> https://oeis.org/A58331
    CatalanPaths_TablMax       -> https://oeis.org/A101461
    CatalanPaths_RevTacc       -> https://oeis.org/A107430
    CatalanPaths_Tinv11        -> https://oeis.org/A112552
    CatalanPaths_Toff11        -> https://oeis.org/A112554
    CatalanPaths_PosHalf       -> https://oeis.org/A121724
    CatalanPaths_NegHalf       -> https://oeis.org/A121724
    CatalanPaths_RevPolyCol3   -> https://oeis.org/A121725
    CatalanPaths_TablCol0      -> https://oeis.org/A126120
    CatalanPaths_TablCol1      -> https://oeis.org/A126120
    CatalanPaths_AntiDSum      -> https://oeis.org/A126120
    CatalanPaths_CentralE      -> https://oeis.org/A126596
    CatalanPaths_EvenSum       -> https://oeis.org/A126869
    CatalanPaths_PolyCol3      -> https://oeis.org/A126931
    CatalanPaths_OddSum        -> https://oeis.org/A138364
    CatalanPaths_Trevinv       -> https://oeis.org/A162515
    CatalanPaths_Tinv          -> https://oeis.org/A168561
    CatalanPaths_RevAntiDSum   -> https://oeis.org/A274112
    CatalanPaths_AccSum        -> https://oeis.org/A296663
    CatalanPaths_RevAccRevSum  -> https://oeis.org/A296663
    CatalanPaths_RevTransNat1  -> https://oeis.org/A296663
    CatalanPaths_TablGcd       -> https://oeis.org/A297382
    CatalanPaths_BinConv       -> https://oeis.org/A344500
    CatalanPaths_InvBinConv    -> https://oeis.org/A344500
    CatalanPaths_CentralO      -> https://oeis.org/A359108

    CatalanPaths: Distinct: 34, Hits: 52, Misses: 17
'''
