"""
Functionality and purpose:
    * Convolution triangle of the Catalan numbers.
    * T(n, k) is the number of TODO
    * Refinement of the total number of leaves in all rooted ordered trees with n edges, A088218, A001700.
    * The triangle and some of its variants are OEIS A128899, and A039598.

    Numerical overview: https://peterluschny.github.io/tabl/Catalan.html

    [0] 1;
    [1] 0,    1;
    [2] 0,    2,    1;
    [3] 0,    5,    4,    1;
    [4] 0,   14,   14,    6,    1;
    [5] 0,   42,   48,   27,    8,    1;
    [6] 0,  132,  165,  110,   44,   10,   1;
    [7] 0,  429,  572,  429,  208,   65,  12,   1;
    [8] 0, 1430, 2002, 1638,  910,  350,  90,  14,  1;
    [9] 0, 4862, 7072, 6188, 3808, 1700, 544, 119, 16, 1;
"""


from functools import cache
from _tabltypes import Table

# Alternative:
#$cache
#def catalanconv(n: int) -> list[int]:
#    if n == 0:
#        return [1]
#    if n == 1:
#        return [0, 1]
#    pow = catalanconv(n - 1) + [0]
#    row = pow.copy()
#    for k in range(n - 1, 0, -1):
#        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]
#    row[n] = 1
#    return row
# Same recurrence as above but builds the interior using zip.


@cache
def catalanconv(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    prev = catalanconv(n - 1) + [0]
    middle = [l + 2 * m + r for l, m, r in 
              zip(prev[:-2], prev[1:-1], prev[2:])]
    return [0] + middle + [1]


CatalanConv = Table(
    catalanconv,
    "CatalanConv",
    ["A128899", "A039598"],
    "A128908",
    r"\sum_{i=1}^{n-k+1} \text{Catalan}(i) T_{k-1, n-i}",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(CatalanConv, oeis=False)


''' OEIS
    CatalanConv_Trev         -> 0 
    CatalanConv_Trevinv      -> 0 
    CatalanConv_Tantidiag    -> 0 
    CatalanConv_Tder         -> 0 
    CatalanConv_TablDiag3    -> 0 
    CatalanConv_TablLcm      -> 0 
    CatalanConv_TablMax      -> 0 
    CatalanConv_ColMiddle    -> 0 
    CatalanConv_CentralO     -> 0 
    CatalanConv_InvBinConv   -> 0 
    CatalanConv_PolyRow3     -> 0 
    CatalanConv_PolyDiag     -> 0 
    CatalanConv_RevToff11    -> 0 
    CatalanConv_RevTrev11    -> 0 
    CatalanConv_RevTantidiag -> 0 
    CatalanConv_RevTalt      -> 0 
    CatalanConv_RevTder      -> 0 
    CatalanConv_RevEvenSum   -> 0 
    CatalanConv_RevOddSum    -> 0 
    CatalanConv_RevColMiddle -> 0 
    CatalanConv_RevNegHalf   -> 0 
    CatalanConv_RevTransSqrs -> 0 
    CatalanConv_RevPolyDiag  -> 0 
    CatalanConv_TablCol0     -> https://oeis.org/A7
    CatalanConv_TablDiag0    -> https://oeis.org/A12
    CatalanConv_RevPolyRow1  -> https://oeis.org/A12
    CatalanConv_PolyRow1     -> https://oeis.org/A27
    CatalanConv_TablCol1     -> https://oeis.org/A108
    CatalanConv_AltSum       -> https://oeis.org/A108
    CatalanConv_TransNat0    -> https://oeis.org/A302
    CatalanConv_AntiDSum     -> https://oeis.org/A957
    CatalanConv_OddSum       -> https://oeis.org/A984
    CatalanConv_TablSum      -> https://oeis.org/A1700
    CatalanConv_AbsSum       -> https://oeis.org/A1700
    CatalanConv_EvenSum      -> https://oeis.org/A1791
    CatalanConv_TablCol2     -> https://oeis.org/A2057
    CatalanConv_TransSqrs    -> https://oeis.org/A2457
    CatalanConv_TablCol3     -> https://oeis.org/A3517
    CatalanConv_RevPolyRow2  -> https://oeis.org/A5408
    CatalanConv_PolyRow2     -> https://oeis.org/A5563
    CatalanConv_TablDiag1    -> https://oeis.org/A5843
    CatalanConv_TablDiag2    -> https://oeis.org/A14106
    CatalanConv_BinConv      -> https://oeis.org/A25174
    CatalanConv_RevCentralO  -> https://oeis.org/A26005
    CatalanConv_Toff11       -> https://oeis.org/A39598
    CatalanConv_Tacc         -> https://oeis.org/A50158
    CatalanConv_Trev11       -> https://oeis.org/A50166
    CatalanConv_NegHalf      -> https://oeis.org/A64062
    CatalanConv_PolyCol2     -> https://oeis.org/A67336
    CatalanConv_RevPosHalf   -> https://oeis.org/A67336
    CatalanConv_Tinv11       -> https://oeis.org/A78812
    CatalanConv_RevPolyRow3  -> https://oeis.org/A79273
    CatalanConv_PolyCol3     -> https://oeis.org/A104530
    CatalanConv_AccRevSum    -> https://oeis.org/A114121
    CatalanConv_TransNat1    -> https://oeis.org/A114121
    CatalanConv_Triangle     -> https://oeis.org/A128899
    CatalanConv_Talt         -> https://oeis.org/A128899
    CatalanConv_Tinv         -> https://oeis.org/A128908
    CatalanConv_RevTransNat0 -> https://oeis.org/A172060
    CatalanConv_Trevinv11    -> https://oeis.org/A172431
    CatalanConv_PosHalf      -> https://oeis.org/A194723
    CatalanConv_RevPolyCol3  -> https://oeis.org/A194724
    CatalanConv_RevAntiDSum  -> https://oeis.org/A224747
    CatalanConv_AccSum       -> https://oeis.org/A296770
    CatalanConv_RevAccRevSum -> https://oeis.org/A296770
    CatalanConv_RevTransNat1 -> https://oeis.org/A296770
    CatalanConv_TablGcd      -> https://oeis.org/A318829
    CatalanConv_CentralE     -> https://oeis.org/A359108
    CatalanConv_RevTacc      -> https://oeis.org/A381883

    CatalanConv: Distinct: 39, Hits: 46, Misses: 23
'''
