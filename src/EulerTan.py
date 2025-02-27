from functools import cache
from Binomial import binomial
from _tabltypes import Table

"""Euler tangent polynomials.

[0]    0;
[1]    1,     0;
[2]    0,     2,     0;
[3]   -2,     0,     3,   0;
[4]    0,    -8,     0,   4,    0;
[5]   16,     0,   -20,   0,    5,    0;
[6]    0,    96,     0, -40,    0,    6,    0;
[7] -272,     0,   336,   0,  -70,    0,    7,  0;
[8]    0, -2176,     0, 896,    0, -112,    0,  8,  0;
[9] 7936,     0, -9792,   0, 2016,    0, -168,  0,  9,  0;
"""


@cache
def eulertan(n: int) -> list[int]:
    b = binomial(n)
    row = [b[k] * eulertan(n - k)[0] if k > 0 else 0 for k in range(n + 1)]
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1

    return row


EulerTan = Table(
    eulertan,
    "EulerTan",
    ["A162660", "A350972", "A155585", "A009006", "A000182"],
    "",
    r"[x^k]( -x^n + \sum_{k=0}^{n} \binom{n}{k} \text{Euler}(k) (x+1)^{n - k})",
)


def eulerT(n: int) -> int:
    return 0 if n % 2 == 0 else eulertan(n)[0]


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(EulerTan)

    print("Bonus:")
    print([eulerT(n) for n in range(30)])


# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials






''' OEIS
    EulerTan_Trev          -> 0 
    EulerTan_Toff11        -> 0 
    EulerTan_Trev11        -> 0 
    EulerTan_Tantidiag     -> 0 
    EulerTan_Tacc          -> 0 
    EulerTan_Tder          -> 0 
    EulerTan_TablCol2      -> 0 
    EulerTan_TablCol3      -> 0 
    EulerTan_TablLcm       -> 0 
    EulerTan_TablMax       -> 0 
    EulerTan_AccSum        -> 0 
    EulerTan_AccRevSum     -> 0 
    EulerTan_AntiDSum      -> 0 
    EulerTan_ColMiddle     -> 0 
    EulerTan_CentralO      -> 0 
    EulerTan_TransNat0     -> 0 
    EulerTan_TransNat1     -> 0 
    EulerTan_TransSqrs     -> 0 
    EulerTan_BinConv       -> 0 
    EulerTan_InvBinConv    -> 0 
    EulerTan_PolyCol2      -> 0 
    EulerTan_PolyCol3      -> 0 
    EulerTan_RevToff11     -> 0 
    EulerTan_RevTrev11     -> 0 
    EulerTan_RevTantidiag  -> 0 
    EulerTan_RevTacc       -> 0 
    EulerTan_RevTalt       -> 0 
    EulerTan_RevTder       -> 0 
    EulerTan_RevAccRevSum  -> 0 
    EulerTan_RevAntiDSum   -> 0 
    EulerTan_RevColMiddle  -> 0 
    EulerTan_RevCentralO   -> 0 
    EulerTan_RevPosHalf    -> 0 
    EulerTan_RevNegHalf    -> 0 
    EulerTan_RevTransNat0  -> 0 
    EulerTan_RevTransNat1  -> 0 
    EulerTan_RevTransSqrs  -> 0 
    EulerTan_RevPolyRow3   -> 0 
    EulerTan_RevPolyCol3   -> 0 
    EulerTan_RevPolyDiag   -> 0 
    EulerTan_TablDiag0     -> https://oeis.org/A4
    EulerTan_TablDiag2     -> https://oeis.org/A4
    EulerTan_RevEvenSum    -> https://oeis.org/A4
    EulerTan_PolyRow1      -> https://oeis.org/A12
    EulerTan_TablDiag1     -> https://oeis.org/A27
    EulerTan_RevPolyRow1   -> https://oeis.org/A27
    EulerTan_EvenSum       -> https://oeis.org/A35
    EulerTan_PolyRow2      -> https://oeis.org/A5843
    EulerTan_RevPolyRow2   -> https://oeis.org/A5843
    EulerTan_TablGcd       -> https://oeis.org/A6519
    EulerTan_TablDiag3     -> https://oeis.org/A7290
    EulerTan_TablCol0      -> https://oeis.org/A9006
    EulerTan_AbsSum        -> https://oeis.org/A9739
    EulerTan_OddSum        -> https://oeis.org/A9744
    EulerTan_TablSum       -> https://oeis.org/A9832
    EulerTan_AltSum        -> https://oeis.org/A9832
    EulerTan_RevOddSum     -> https://oeis.org/A9832
    EulerTan_PolyRow3      -> https://oeis.org/A100536
    EulerTan_TablCol1      -> https://oeis.org/A109573
    EulerTan_Triangle      -> https://oeis.org/A162660
    EulerTan_Talt          -> https://oeis.org/A162660
    EulerTan_CentralE      -> https://oeis.org/A214447
    EulerTan_PolyDiag      -> https://oeis.org/A302587
    EulerTan_PosHalf       -> https://oeis.org/A326325
    EulerTan_NegHalf       -> https://oeis.org/A326325

    EulerTan: Distinct: 18, Hits: 25, Misses: 40
'''
