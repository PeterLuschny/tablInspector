from functools import cache
from Binomial import binomial
from _tabltypes import Table

"""Euler secant polynomials.

[0] [   1]
[1] [   0,     1]
[2] [  -1,     0,     1]
[3] [   0,    -3,     0,   1]
[4] [   5,     0,    -6,   0,   1]
[5] [   0,    25,     0, -10,   0,   1]
[6] [ -61,     0,    75,   0, -15,   0,   1]
[7] [   0,  -427,     0, 175,   0, -21,   0,  1]
[8] [1385,     0, -1708,   0, 350,   0, -28,  0,  1]
"""


@cache
def eulersec(n: int) -> list[int]:
    if n == 0:
        return [1]

    b = binomial(n)
    row = [b[k] * eulersec(n - k)[0] if k > 0 else 0 for k in range(n + 1)]
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row


EulerSec = Table(
    eulersec,
    "EulerSec",
    ["A119879", "A081658", "A153641"],
    "A000000",
    r"\binom{n}{k}\, 2^{n-k}\ \text{Euler} (n-k, 1/2)",
)


def eulerS(n: int) -> int:
    return 0 if n % 2 == 1 else eulersec(n)[0]


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(EulerSec)

    print("Bonus:")
    print([eulerS(n) for n in range(30)])

# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials




''' OEIS
    EulerSec_Tacc          -> https://oeis.org/A-999999
    EulerSec_TablDiag1     -> https://oeis.org/A-999999
    EulerSec_TablDiag3     -> https://oeis.org/A-999999
    EulerSec_RevOddSum     -> https://oeis.org/A-999999
    EulerSec_Toff11        -> 0 
    EulerSec_Trev11        -> 0 
    EulerSec_Tinv11        -> 0 
    EulerSec_Trevinv11     -> 0 
    EulerSec_Tantidiag     -> 0 
    EulerSec_Tder          -> 0 
    EulerSec_TablCol2      -> 0 
    EulerSec_TablCol3      -> 0 
    EulerSec_TablLcm       -> 0 
    EulerSec_TablMax       -> 0 
    EulerSec_AccSum        -> 0 
    EulerSec_AntiDSum      -> 0 
    EulerSec_ColMiddle     -> 0 
    EulerSec_CentralO      -> 0 
    EulerSec_TransSqrs     -> 0 
    EulerSec_BinConv       -> 0 
    EulerSec_InvBinConv    -> 0 
    EulerSec_RevToff11     -> 0 
    EulerSec_RevTrev11     -> 0 
    EulerSec_RevTantidiag  -> 0 
    EulerSec_RevTacc       -> 0 
    EulerSec_RevTder       -> 0 
    EulerSec_RevAccRevSum  -> 0 
    EulerSec_RevAntiDSum   -> 0 
    EulerSec_RevColMiddle  -> 0 
    EulerSec_RevCentralO   -> 0 
    EulerSec_RevTransNat0  -> 0 
    EulerSec_RevTransNat1  -> 0 
    EulerSec_RevTransSqrs  -> 0 
    EulerSec_EvenSum       -> https://oeis.org/A7
    EulerSec_TablDiag0     -> https://oeis.org/A12
    EulerSec_RevPolyRow1   -> https://oeis.org/A12
    EulerSec_PolyRow1      -> https://oeis.org/A27
    EulerSec_TablDiag2     -> https://oeis.org/A217
    EulerSec_RevPolyCol3   -> https://oeis.org/A810
    EulerSec_PosHalf       -> https://oeis.org/A1586
    EulerSec_NegHalf       -> https://oeis.org/A1586
    EulerSec_AbsSum        -> https://oeis.org/A3701
    EulerSec_PolyRow2      -> https://oeis.org/A5563
    EulerSec_RevPolyRow2   -> https://oeis.org/A5563
    EulerSec_TablSum       -> https://oeis.org/A9006
    EulerSec_OddSum        -> https://oeis.org/A9006
    EulerSec_AltSum        -> https://oeis.org/A9006
    EulerSec_RevEvenSum    -> https://oeis.org/A9006
    EulerSec_AccRevSum     -> https://oeis.org/A9725
    EulerSec_TransNat1     -> https://oeis.org/A9725
    EulerSec_TablCol1      -> https://oeis.org/A9843
    EulerSec_PolyRow3      -> https://oeis.org/A58794
    EulerSec_RevPolyRow3   -> https://oeis.org/A80663
    EulerSec_Trev          -> https://oeis.org/A81658
    EulerSec_RevTalt       -> https://oeis.org/A81658
    EulerSec_TransNat0     -> https://oeis.org/A109573
    EulerSec_Tinv          -> https://oeis.org/A119467
    EulerSec_Triangle      -> https://oeis.org/A119879
    EulerSec_Talt          -> https://oeis.org/A119879
    EulerSec_PolyCol2      -> https://oeis.org/A119880
    EulerSec_RevPosHalf    -> https://oeis.org/A119880
    EulerSec_RevNegHalf    -> https://oeis.org/A119880
    EulerSec_PolyCol3      -> https://oeis.org/A119881
    EulerSec_TablCol0      -> https://oeis.org/A122045
    EulerSec_Trevinv       -> https://oeis.org/A141665
    EulerSec_TablGcd       -> https://oeis.org/A155457
    EulerSec_CentralE      -> https://oeis.org/A214445
    EulerSec_PolyDiag      -> https://oeis.org/A302585
    EulerSec_RevPolyDiag   -> https://oeis.org/A378063

    EulerSec: Distinct: 27, Hits: 40, Misses: 29
'''
