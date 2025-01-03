from functools import cache
from _tabltypes import Table

"""Monotone words (binomial(-n, k)).

[0] [1]
[1] [1, 1]
[2] [1, 2,  3]
[3] [1, 3,  6,  10]
[4] [1, 4, 10,  20,  35]
[5] [1, 5, 15,  35,  70,  126]
[6] [1, 6, 21,  56, 126,  252,  462]
[7] [1, 7, 28,  84, 210,  462,  924, 1716]
[8] [1, 8, 36, 120, 330,  792, 1716, 3432,  6435]
[9] [1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, 24310]
"""


@cache
def monotone(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1 for _ in range(n + 1)]
    row[1] = n
    for k in range(1, n):
        row[k + 1] = (row[k] * (n + k)) // (k + 1)
    return row


Monotone = Table(
    monotone, 
    "Monotone", 
    ["A059481", "A027555"], 
    "",  # not integer-invrtible
    r"\binom{n+k-1}{k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Monotone)


''' OEIS
    Monotone_Trev11        -> 0 
    Monotone_Tantidiag     -> 0 
    Monotone_Tder          -> 0 
    Monotone_TablLcm       -> 0 
    Monotone_EvenSum       -> 0 
    Monotone_OddSum        -> 0 
    Monotone_TransSqrs     -> 0 
    Monotone_PolyRow3      -> 0 
    Monotone_PolyCol3      -> 0 
    Monotone_RevTantidiag  -> 0 
    Monotone_RevTacc       -> 0 
    Monotone_RevTder       -> 0 
    Monotone_RevColMiddle  -> 0 
    Monotone_RevCentralO   -> 0 
    Monotone_RevNegHalf    -> 0 
    Monotone_RevPolyRow3   -> 0 
    Monotone_InvBinConv    -> https://oeis.org/A7
    Monotone_TablCol0      -> https://oeis.org/A12
    Monotone_TablGcd       -> https://oeis.org/A12
    Monotone_TablCol1      -> https://oeis.org/A27
    Monotone_PolyRow1      -> https://oeis.org/A27
    Monotone_RevPolyRow1   -> https://oeis.org/A27
    Monotone_TablCol2      -> https://oeis.org/A217
    Monotone_TablCol3      -> https://oeis.org/A292
    Monotone_TablDiag1     -> https://oeis.org/A984
    Monotone_TablSum       -> https://oeis.org/A984
    Monotone_AbsSum        -> https://oeis.org/A984
    Monotone_TablDiag0     -> https://oeis.org/A1700
    Monotone_TablDiag2     -> https://oeis.org/A1700
    Monotone_TablMax       -> https://oeis.org/A1700
    Monotone_AccSum        -> https://oeis.org/A1700
    Monotone_RevAccRevSum  -> https://oeis.org/A1700
    Monotone_RevTransNat1  -> https://oeis.org/A1700
    Monotone_TablDiag3     -> https://oeis.org/A1791
    Monotone_RevTransNat0  -> https://oeis.org/A1791
    Monotone_BinConv       -> https://oeis.org/A2003
    Monotone_CentralO      -> https://oeis.org/A5809
    Monotone_RevOddSum     -> https://oeis.org/A14300
    Monotone_RevEvenSum    -> https://oeis.org/A26641
    Monotone_PosHalf       -> https://oeis.org/A32443
    Monotone_AccRevSum     -> https://oeis.org/A34275
    Monotone_TransNat1     -> https://oeis.org/A34275
    Monotone_Tacc          -> https://oeis.org/A46899
    Monotone_RevTrev11     -> https://oeis.org/A46899
    Monotone_PolyRow2      -> https://oeis.org/A56109
    Monotone_RevPolyRow2   -> https://oeis.org/A59100
    Monotone_Triangle      -> https://oeis.org/A59481
    Monotone_Talt          -> https://oeis.org/A59481
    Monotone_AltSum        -> https://oeis.org/A72547
    Monotone_ColMiddle     -> https://oeis.org/A81204
    Monotone_RevToff11     -> https://oeis.org/A92392
    Monotone_Trev          -> https://oeis.org/A100100
    Monotone_RevTalt       -> https://oeis.org/A100100
    Monotone_RevPolyCol3   -> https://oeis.org/A100192
    Monotone_RevAntiDSum   -> https://oeis.org/A100217
    Monotone_Tinvrev       -> https://oeis.org/A100218
    Monotone_TransNat0     -> https://oeis.org/A110609
    Monotone_RevTinv11     -> https://oeis.org/A113214
    Monotone_AntiDSum      -> https://oeis.org/A116406
    Monotone_PolyCol2      -> https://oeis.org/A119259
    Monotone_Toff11        -> https://oeis.org/A165257
    Monotone_CentralE      -> https://oeis.org/A165817
    Monotone_RevTransSqrs  -> https://oeis.org/A220101
    Monotone_RevPolyDiag   -> https://oeis.org/A293574
    Monotone_NegHalf       -> https://oeis.org/A367548
    Monotone_PolyDiag      -> https://oeis.org/A368488

    Monotone: Distinct: 36, Hits: 50, Misses: 16
'''
