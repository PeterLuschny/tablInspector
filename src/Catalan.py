
"""
Functionality and purpose:
    * T(n, k) is the number of TODO. 
    * The triangle is a refinment of the Catalan numbers.
    * The triangle is not integer invertible.
    * The triangle and some of its variants are A106566, A033184, A355173, A030237, A054445.

    Numerical overview: https://peterluschny.github.io/tabl/Catalan.html

Functions:
    catalan(n: int) -> list[int]:
        Computes the coefficients of the n-th Catalan row.

    Catalan(n: int, k: int) -> int:
        Returns the k-th coefficient of the n-th Catalan row.

    The Catalan object can access the coefficients of the Catalan polynomials directly.
    However, it is often more efficient to fetch an entire row using the lowercase version.

Example:
    >>> catalan(3)
    [0, 2, 2, 1] 
    >>> Catalan(3, 2)
    2

The Catalan triangle A106566:
    [0] [1] 
    [1] [0,    1] 
    [2] [0,    1,    1] 
    [3] [0,    2,    2,    1] 
    [4] [0,    5,    5,    3,   1] 
    [5] [0,   14,   14,    9,   4,   1] 
    [6] [0,   42,   42,   28,  14,   5,   1] 
    [7] [0,  132,  132,   90,  48,  20,   6,  1] 
    [8] [0,  429,  429,  297, 165,  75,  27,  7, 1] 
    [9] [0, 1430, 1430, 1001, 572, 275, 110, 35, 8, 1]
"""

from functools import cache
from _tabltypes import Table

@cache
def catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    prev = catalan(n - 1)
    s = sum(prev)
    row = [0, s, s]

    for x in prev[1:-1]:
        row.append(row[-1] - x)

    return row


Catalan = Table(
    catalan,
    "Catalan",
    ["A106566", "A033184", "A355173", "A030237", "A054445"],
    "",
    r"is(k=0) \, ? \, 0^n : \frac{ k \Gamma(2n-k)}{\Gamma(n + 1) \Gamma(n-k+1)}",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Catalan, oeis=False)



''' OEIS
    Catalan_Tantidiag        -> 0 
    Catalan_Tacc             -> 0 
    Catalan_Tder             -> 0 
    Catalan_TablLcm          -> 0 
    Catalan_ColMiddle        -> 0 
    Catalan_CentralO         -> 0 
    Catalan_PolyDiag         -> 0 
    Catalan_RevToff11        -> 0 
    Catalan_RevTrev11        -> 0 
    Catalan_RevTantidiag     -> 0 
    Catalan_RevTder          -> 0 
    Catalan_RevEvenSum       -> 0 
    Catalan_RevOddSum        -> 0 
    Catalan_RevColMiddle     -> 0 
    Catalan_RevTransSqrs     -> 0 
    Catalan_TablCol0         -> https://oeis.org/A7
    Catalan_TablDiag0        -> https://oeis.org/A12
    Catalan_InvBinConv       -> https://oeis.org/A12
    Catalan_RevPolyRow1      -> https://oeis.org/A12
    Catalan_TablDiag1        -> https://oeis.org/A27
    Catalan_PolyRow1         -> https://oeis.org/A27
    Catalan_RevPolyRow2      -> https://oeis.org/A27
    Catalan_TablDiag2        -> https://oeis.org/A96
    Catalan_TablCol1         -> https://oeis.org/A108
    Catalan_TablCol2         -> https://oeis.org/A108
    Catalan_TablMax          -> https://oeis.org/A108
    Catalan_TablSum          -> https://oeis.org/A108
    Catalan_AbsSum           -> https://oeis.org/A108
    Catalan_AccRevSum        -> https://oeis.org/A108
    Catalan_TransNat1        -> https://oeis.org/A108
    Catalan_TablCol3         -> https://oeis.org/A245
    Catalan_TransNat0        -> https://oeis.org/A245
    Catalan_EvenSum          -> https://oeis.org/A957
    Catalan_AltSum           -> https://oeis.org/A957
    Catalan_OddSum           -> https://oeis.org/A958
    Catalan_PolyCol2         -> https://oeis.org/A984
    Catalan_RevPosHalf       -> https://oeis.org/A984
    Catalan_RevAntiDSum      -> https://oeis.org/A1405
    Catalan_RevPolyRow3      -> https://oeis.org/A1844
    Catalan_BinConv          -> https://oeis.org/A1850
    Catalan_PolyRow2         -> https://oeis.org/A2378
    Catalan_RevTransNat0     -> https://oeis.org/A2694
    Catalan_TablDiag3        -> https://oeis.org/A5586
    Catalan_PolyCol3         -> https://oeis.org/A7854
    Catalan_Trev11           -> https://oeis.org/A9766
    Catalan_RevTacc          -> https://oeis.org/A9766
    Catalan_CentralE         -> https://oeis.org/A25174
    Catalan_AntiDSum         -> https://oeis.org/A30238
    Catalan_Tinv11           -> https://oeis.org/A30528
    Catalan_Toff11           -> https://oeis.org/A33184
    Catalan_PolyRow3         -> https://oeis.org/A62158
    Catalan_PosHalf          -> https://oeis.org/A64062
    Catalan_RevPolyCol3      -> https://oeis.org/A64063
    Catalan_NegHalf          -> https://oeis.org/A64311
    Catalan_TransSqrs        -> https://oeis.org/A70857
    Catalan_Triangle         -> https://oeis.org/A106566
    Catalan_Talt             -> https://oeis.org/A106566
    Catalan_RevNegHalf       -> https://oeis.org/A126984
    Catalan_Trev             -> https://oeis.org/A130020
    Catalan_RevTalt          -> https://oeis.org/A130020
    Catalan_Trevinv11        -> https://oeis.org/A169803
    Catalan_RevCentralO      -> https://oeis.org/A174687
    Catalan_TablGcd          -> https://oeis.org/A297382
    Catalan_RevPolyDiag      -> https://oeis.org/A323217
    Catalan_AccSum           -> https://oeis.org/A344191
    Catalan_RevAccRevSum     -> https://oeis.org/A344191
    Catalan_RevTransNat1     -> https://oeis.org/A344191

    Catalan: Distinct: 35, Hits: 52, Misses: 15
'''
