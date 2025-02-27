"""
This module provides functions to generate the coefficients of the Abel polynomials 
and their corresponding triangle. Abel is a `Table` object that provides various
methods to investigate the Abel triangle.

Functions:
    abel(n: int) -> list[int]:
        Computes the coefficients of the n-th Abel polynomial.

    The Abel object can be used to access the coefficients of the Abel polynomials directly.
    However, it is often more efficient to fetch an entire row using the lowercase version.
 
    Abel(n: int, k: int) -> int:
        Returns the k-th coefficient of the n-th Abel polynomial.

Example:
    >>> abel(3)
    [0, 9, 6, 1]
    >>> Abel(3, 2)
    6

References:
    Variants of the triangle are https://oeis.org/A137452 , A061356, and A139526.
    The triangle is invertible and the inverse is A059297, the triangle of idempotent numbers.
    An overview is given in https://peterluschny.github.io/tabl/Abel.html
"""

from functools import cache
from Binomial import binomial
from _tabltypes import Table

"""Abel polynomials (unsigned coefficients).
[0] [1]
[1] [0,        1]
[2] [0,        2,       1]
[3] [0,        9,       6,       1]
[4] [0,       64,      48,      12,      1]
[5] [0,      625,     500,     150,     20,      1]
[6] [0,     7776,    6480,    2160,    360,     30,    1]
[7] [0,   117649,  100842,   36015,   6860,    735,   42,   1]
[8] [0,  2097152, 1835008,  688128, 143360,  17920, 1344,  56, 1]
"""

@cache
def abel(n: int) -> list[int]:
    if n == 0:
        return [1]

    b = binomial(n - 1)
    return [b[k - 1] * n ** (n - k) if k > 0 else 0 for k in range(n + 1)]


Abel = Table(
    abel,      # the generating function
    "Abel",    # name of the table
    ["A137452", "A061356", "A139526"], # similar sequences in OEIS 
    "A059297", # OEIS-id of the inverse sequence
    r"is(k = 0)\ ? \ 0^n : \binom{n-1}{k-1} (-n)^{n - k}" # TeX of the defining formula
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Abel)






''' OEIS
    Abel_Trev          -> 0 
    Abel_Tantidiag     -> 0 
    Abel_Tacc          -> 0 
    Abel_TablDiag2     -> 0 
    Abel_TablDiag3     -> 0 
    Abel_TablLcm       -> 0 
    Abel_AccSum        -> 0 
    Abel_AntiDSum      -> 0 
    Abel_ColMiddle     -> 0 
    Abel_CentralO      -> 0 
    Abel_PolyRow3      -> 0 
    Abel_RevToff11     -> 0 
    Abel_RevTrev11     -> 0 
    Abel_RevTantidiag  -> 0 
    Abel_RevTacc       -> 0 
    Abel_RevTalt       -> 0 
    Abel_RevTder       -> 0 
    Abel_RevEvenSum    -> 0 
    Abel_RevOddSum     -> 0 
    Abel_RevAccRevSum  -> 0 
    Abel_RevAntiDSum   -> 0 
    Abel_RevColMiddle  -> 0 
    Abel_RevCentralO   -> 0 
    Abel_RevNegHalf    -> 0 
    Abel_RevTransNat1  -> 0 
    Abel_RevTransSqrs  -> 0 
    Abel_RevPolyDiag   -> 0 
    Abel_TablCol0      -> https://oeis.org/A7
    Abel_TablDiag0     -> https://oeis.org/A12
    Abel_RevPolyRow1   -> https://oeis.org/A12
    Abel_TablGcd       -> https://oeis.org/A27
    Abel_PolyRow1      -> https://oeis.org/A27
    Abel_TablCol1      -> https://oeis.org/A169
    Abel_TablMax       -> https://oeis.org/A169
    Abel_TablSum       -> https://oeis.org/A272
    Abel_AbsSum        -> https://oeis.org/A272
    Abel_AltSum        -> https://oeis.org/A312
    Abel_TablDiag1     -> https://oeis.org/A2378
    Abel_RevPolyRow2   -> https://oeis.org/A5408
    Abel_PolyRow2      -> https://oeis.org/A5563
    Abel_PolyCol2      -> https://oeis.org/A7334
    Abel_RevPosHalf    -> https://oeis.org/A7334
    Abel_RevPolyRow3   -> https://oeis.org/A16778
    Abel_PosHalf       -> https://oeis.org/A52750
    Abel_RevPolyCol3   -> https://oeis.org/A52752
    Abel_TablCol2      -> https://oeis.org/A53506
    Abel_TablCol3      -> https://oeis.org/A53507
    Abel_Tinv          -> https://oeis.org/A59297
    Abel_Tinv11        -> https://oeis.org/A59298
    Abel_Trevinv       -> https://oeis.org/A59299
    Abel_Trevinv11     -> https://oeis.org/A59300
    Abel_Toff11        -> https://oeis.org/A61356
    Abel_RevTransNat0  -> https://oeis.org/A65513
    Abel_NegHalf       -> https://oeis.org/A85527
    Abel_TransNat0     -> https://oeis.org/A89946
    Abel_Triangle      -> https://oeis.org/A137452
    Abel_Talt          -> https://oeis.org/A137452
    Abel_Trev11        -> https://oeis.org/A139526
    Abel_PolyDiag      -> https://oeis.org/A193678
    Abel_OddSum        -> https://oeis.org/A195136
    Abel_Tder          -> https://oeis.org/A225465
    Abel_TransSqrs     -> https://oeis.org/A225497
    Abel_EvenSum       -> https://oeis.org/A274278
    Abel_PolyCol3      -> https://oeis.org/A362354
    Abel_CentralE      -> https://oeis.org/A367254
    Abel_AccRevSum     -> https://oeis.org/A367255
    Abel_TransNat1     -> https://oeis.org/A367255
    Abel_BinConv       -> https://oeis.org/A367256
    Abel_InvBinConv    -> https://oeis.org/A367257

    Abel: Distinct: 36, Hits: 42, Misses: 27
'''
