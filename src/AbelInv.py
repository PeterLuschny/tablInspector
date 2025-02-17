"""
This module provides functions to generate the inverse of the Abel Table. They are
considered here in the unsigned (absolute) form in which they are also called idempotent numbers.
InvAbel is a `Table` object that provides various methods to investigate the inverse of the Abel table. 

Functions:
    invabel(n: int) -> list[int]:
        Computes the coefficients of the n-th polynomial that are given by the n-th row of the inverse Abel Table.

    The InvAbel object can be used to access the coefficients of the InvAbel polynomials directly.
    However, it is often more efficient to fetch an entire row using the lowercase version.
 
    InvAbel(n: int, k: int) -> int:
        Returns the k-th coefficient of the n-th InvAbel polynomial.

Example:
    >>> invabel(3)
    [0, 3, 6, 1]
    >>> InvAbel(3, 2)
    6

References:
    Variants of the triangle are https://oeis.org/A059297 and A059298.
    The triangle is invertible and the inverse is A137452, the triangle of the coefficients of the Abel polynomials.
    An overview is given in https://peterluschny.github.io/tabl/Abel.html
"""

from functools import cache
from _tabltypes import Table
from Binomial import binomial
from Powers import powers

'''
Inverse of Abel, unsigned version. Triangle of idempotent numbers. 

[0]  1;
[1]  0,  1;
[2]  0,  2,    1;
[3]  0,  3,    6,     1;
[4]  0,  4,   24,    12,     1;
[5]  0,  5,   80,    90,    20,     1;
[6]  0,  6,  240,   540,   240,    30,     1;
[7]  0,  7,  672,  2835,  2240,   525,    42,    1;
[8]  0,  8, 1792, 11340, 15680,  5880,   980,   56,  1;
[9]  0,  9, 4608, 41580, 94080, 52920, 11760, 1260, 72, 1;
'''

@cache
def abelinv(n: int) -> list[int]:

    b = binomial(n)
    p = powers(n)
    return [b[k] * p[k] for k in range(n + 1)]


AbelInv = Table(
    abelinv,
    "AbelInv",
    ["A059297", "A059298"],
    "A137452",
    r"\binom{n}{k} k^{n - k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(AbelInv)




''' OEIS
    AbelInv_Trevinv       -> 0 
    AbelInv_Tantidiag     -> 0 
    AbelInv_Tacc          -> 0 
    AbelInv_Tder          -> 0 
    AbelInv_TablDiag2     -> 0 
    AbelInv_TablDiag3     -> 0 
    AbelInv_TablLcm       -> 0 
    AbelInv_TablMax       -> 0 
    AbelInv_AccSum        -> 0 
    AbelInv_AccRevSum     -> 0 
    AbelInv_ColMiddle     -> 0 
    AbelInv_CentralO      -> 0 
    AbelInv_TransNat1     -> 0 
    AbelInv_TransSqrs     -> 0 
    AbelInv_PolyRow3      -> 0 
    AbelInv_RevToff11     -> 0 
    AbelInv_RevTrev11     -> 0 
    AbelInv_RevTantidiag  -> 0 
    AbelInv_RevTacc       -> 0 
    AbelInv_RevTder       -> 0 
    AbelInv_RevOddSum     -> 0 
    AbelInv_RevAccRevSum  -> 0 
    AbelInv_RevCentralO   -> 0 
    AbelInv_RevNegHalf    -> 0 
    AbelInv_RevTransNat0  -> 0 
    AbelInv_RevTransNat1  -> 0 
    AbelInv_RevTransSqrs  -> 0 
    AbelInv_TablCol0      -> https://oeis.org/A7
    AbelInv_TablDiag0     -> https://oeis.org/A12
    AbelInv_RevPolyRow1   -> https://oeis.org/A12
    AbelInv_TablCol1      -> https://oeis.org/A27
    AbelInv_TablGcd       -> https://oeis.org/A27
    AbelInv_PolyRow1      -> https://oeis.org/A27
    AbelInv_TablSum       -> https://oeis.org/A248
    AbelInv_AbsSum        -> https://oeis.org/A248
    AbelInv_TablCol2      -> https://oeis.org/A1788
    AbelInv_TablDiag1     -> https://oeis.org/A2378
    AbelInv_AltSum        -> https://oeis.org/A3725
    AbelInv_RevPolyRow2   -> https://oeis.org/A5408
    AbelInv_PolyRow2      -> https://oeis.org/A5563
    AbelInv_EvenSum       -> https://oeis.org/A9121
    AbelInv_OddSum        -> https://oeis.org/A9565
    AbelInv_TablCol3      -> https://oeis.org/A36216
    AbelInv_Triangle      -> https://oeis.org/A59297
    AbelInv_Talt          -> https://oeis.org/A59297
    AbelInv_Toff11        -> https://oeis.org/A59298
    AbelInv_Trev          -> https://oeis.org/A59299
    AbelInv_RevTalt       -> https://oeis.org/A59299
    AbelInv_Trev11        -> https://oeis.org/A59300
    AbelInv_Tinv11        -> https://oeis.org/A61356
    AbelInv_RevPolyRow3   -> https://oeis.org/A100536
    AbelInv_Tinv          -> https://oeis.org/A137452
    AbelInv_Trevinv11     -> https://oeis.org/A139526
    AbelInv_TransNat0     -> https://oeis.org/A185298
    AbelInv_RevEvenSum    -> https://oeis.org/A195509
    AbelInv_PosHalf       -> https://oeis.org/A216689
    AbelInv_PolyCol2      -> https://oeis.org/A275707
    AbelInv_RevPosHalf    -> https://oeis.org/A275707
    AbelInv_RevPolyDiag   -> https://oeis.org/A295552
    AbelInv_PolyDiag      -> https://oeis.org/A295623
    AbelInv_PolyCol3      -> https://oeis.org/A355501
    AbelInv_NegHalf       -> https://oeis.org/A356819
    AbelInv_RevPolyCol3   -> https://oeis.org/A356827
    AbelInv_RevAntiDSum   -> https://oeis.org/A360782
    AbelInv_AntiDSum      -> https://oeis.org/A360814
    AbelInv_CentralE      -> https://oeis.org/A367271
    AbelInv_BinConv       -> https://oeis.org/A367272
    AbelInv_InvBinConv    -> https://oeis.org/A367273
    AbelInv_RevColMiddle  -> https://oeis.org/A367274

    AbelInv: Distinct: 36, Hits: 42, Misses: 27
'''
