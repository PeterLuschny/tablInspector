from functools import cache
from _tabltypes import Table

"""Bessel triangle.

[0] [1]
[1] [0,      1]
[2] [0,      1,      1]
[3] [0,      3,      3,     1]
[4] [0,     15,     15,     6,     1]
[5] [0,    105,    105,    45,    10,    1]
[6] [0,    945,    945,   420,   105,   15,   1]
[7] [0,  10395,  10395,  4725,  1260,  210,  21,  1]
[8] [0, 135135, 135135, 62370, 17325, 3150, 378, 28, 1]
"""


@cache
def bessel(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = bessel(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = row[k - 1] + (2 * (n - 1) - k) * row[k]
    return row


Bessel = Table(
    bessel, 
    "Bessel", 
    ["A132062", "A001497", "A001498", "A122850"], 
    "A122848",
    r"2^{k - n} \binom{2n - 2k}{n - k} \binom{2n - k - 1}{k - 1} (n - k)!" 
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Bessel)






''' OEIS
    Bessel_Tantidiag     -> 0 
    Bessel_Tacc          -> 0 
    Bessel_Tder          -> 0 
    Bessel_TablLcm       -> 0 
    Bessel_AccSum        -> 0 
    Bessel_AccRevSum     -> 0 
    Bessel_AntiDSum      -> 0 
    Bessel_ColMiddle     -> 0 
    Bessel_CentralO      -> 0 
    Bessel_TransNat1     -> 0 
    Bessel_TransSqrs     -> 0 
    Bessel_BinConv       -> 0 
    Bessel_InvBinConv    -> 0 
    Bessel_PolyDiag      -> 0 
    Bessel_RevToff11     -> 0 
    Bessel_RevTrev11     -> 0 
    Bessel_RevTantidiag  -> 0 
    Bessel_RevTacc       -> 0 
    Bessel_RevTder       -> 0 
    Bessel_RevEvenSum    -> 0 
    Bessel_RevOddSum     -> 0 
    Bessel_RevAccRevSum  -> 0 
    Bessel_RevColMiddle  -> 0 
    Bessel_RevNegHalf    -> 0 
    Bessel_RevTransNat1  -> 0 
    Bessel_RevTransSqrs  -> 0 
    Bessel_RevPolyDiag   -> 0 
    Bessel_TablCol0      -> https://oeis.org/A7
    Bessel_TablDiag0     -> https://oeis.org/A12
    Bessel_RevPolyRow1   -> https://oeis.org/A12
    Bessel_PolyRow1      -> https://oeis.org/A27
    Bessel_RevPolyRow2   -> https://oeis.org/A27
    Bessel_RevAntiDSum   -> https://oeis.org/A85
    Bessel_TablDiag1     -> https://oeis.org/A217
    Bessel_TablCol1      -> https://oeis.org/A1147
    Bessel_TablCol2      -> https://oeis.org/A1147
    Bessel_TablMax       -> https://oeis.org/A1147
    Bessel_Toff11        -> https://oeis.org/A1497
    Bessel_Trev11        -> https://oeis.org/A1498
    Bessel_RevTransNat0  -> https://oeis.org/A1514
    Bessel_TablSum       -> https://oeis.org/A1515
    Bessel_AbsSum        -> https://oeis.org/A1515
    Bessel_PosHalf       -> https://oeis.org/A1517
    Bessel_RevPolyCol3   -> https://oeis.org/A1518
    Bessel_TablCol3      -> https://oeis.org/A1879
    Bessel_NegHalf       -> https://oeis.org/A2119
    Bessel_PolyRow2      -> https://oeis.org/A2378
    Bessel_RevPolyRow3   -> https://oeis.org/A3215
    Bessel_OddSum        -> https://oeis.org/A25164
    Bessel_EvenSum       -> https://oeis.org/A36244
    Bessel_Tinv11        -> https://oeis.org/A49403
    Bessel_TablDiag2     -> https://oeis.org/A50534
    Bessel_PolyRow3      -> https://oeis.org/A68601
    Bessel_TablGcd       -> https://oeis.org/A69834
    Bessel_Trev          -> https://oeis.org/A104548
    Bessel_RevTalt       -> https://oeis.org/A104548
    Bessel_TransNat0     -> https://oeis.org/A107103
    Bessel_PolyCol2      -> https://oeis.org/A107104
    Bessel_RevPosHalf    -> https://oeis.org/A107104
    Bessel_Trevinv11     -> https://oeis.org/A111924
    Bessel_Tinv          -> https://oeis.org/A122848
    Bessel_Triangle      -> https://oeis.org/A132062
    Bessel_Talt          -> https://oeis.org/A132062
    Bessel_Trevinv       -> https://oeis.org/A144299
    Bessel_TablDiag3     -> https://oeis.org/A240440
    Bessel_RevCentralO   -> https://oeis.org/A245066
    Bessel_AltSum        -> https://oeis.org/A278990
    Bessel_PolyCol3      -> https://oeis.org/A369746
    Bessel_CentralE      -> https://oeis.org/A376872

    Bessel: Distinct: 35, Hits: 42, Misses: 27
'''
