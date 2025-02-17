from functools import cache
from _tabltypes import Table


"""Laguerre polynomials n! * L(n, x) (unsigned coefficients).

[0]      1
[1]      1,       1
[2]      2,       4,       1
[3]      6,      18,       9,       1
[4]     24,      96,      72,      16,       1
[5]    120,     600,     600,     200,      25,      1
[6]    720,    4320,    5400,    2400,     450,     36,     1
[7]   5040,   35280,   52920,   29400,    7350,    882,    49,    1
[8]  40320,  322560,  564480,  376320,  117600,  18816,  1568,   64,  1
"""


@cache
def laguerre(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [0] + laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row


Laguerre = Table(
    laguerre,
    "Laguerre",
    ["A021009", "A021010", "A144084"],
    "A000000",
    r"\binom{n}{k}\, \frac{n!}{k!}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Laguerre)




''' OEIS
    Laguerre_Toff11        -> 0 
    Laguerre_Trev11        -> 0 
    Laguerre_Tinv11        -> 0 
    Laguerre_Trevinv11     -> 0 
    Laguerre_Tacc          -> 0 
    Laguerre_Tder          -> 0 
    Laguerre_TablLcm       -> 0 
    Laguerre_TablMax       -> 0 
    Laguerre_AccSum        -> 0 
    Laguerre_CentralO      -> 0 
    Laguerre_PolyRow3      -> 0 
    Laguerre_RevToff11     -> 0 
    Laguerre_RevTrev11     -> 0 
    Laguerre_RevTantidiag  -> 0 
    Laguerre_RevTacc       -> 0 
    Laguerre_RevTder       -> 0 
    Laguerre_RevEvenSum    -> 0 
    Laguerre_RevOddSum     -> 0 
    Laguerre_RevAccRevSum  -> 0 
    Laguerre_RevAntiDSum   -> 0 
    Laguerre_RevColMiddle  -> 0 
    Laguerre_RevCentralO   -> 0 
    Laguerre_RevTransNat1  -> 0 
    Laguerre_RevTransSqrs  -> 0 
    Laguerre_RevPolyRow3   -> 0 
    Laguerre_TablDiag0     -> https://oeis.org/A12
    Laguerre_PolyRow1      -> https://oeis.org/A27
    Laguerre_RevPolyRow1   -> https://oeis.org/A27
    Laguerre_TablCol0      -> https://oeis.org/A142
    Laguerre_AccRevSum     -> https://oeis.org/A262
    Laguerre_TransNat1     -> https://oeis.org/A262
    Laguerre_TablDiag1     -> https://oeis.org/A290
    Laguerre_AntiDSum      -> https://oeis.org/A1040
    Laguerre_TablCol1      -> https://oeis.org/A1563
    Laguerre_TablCol2      -> https://oeis.org/A1809
    Laguerre_TablCol3      -> https://oeis.org/A1810
    Laguerre_TablSum       -> https://oeis.org/A2720
    Laguerre_AbsSum        -> https://oeis.org/A2720
    Laguerre_PolyRow2      -> https://oeis.org/A8865
    Laguerre_AltSum        -> https://oeis.org/A9940
    Laguerre_Triangle      -> https://oeis.org/A21009
    Laguerre_Tinv          -> https://oeis.org/A21009
    Laguerre_Talt          -> https://oeis.org/A21009
    Laguerre_NegHalf       -> https://oeis.org/A25166
    Laguerre_PosHalf       -> https://oeis.org/A25167
    Laguerre_RevPolyRow2   -> https://oeis.org/A56220
    Laguerre_Tantidiag     -> https://oeis.org/A84950
    Laguerre_PolyCol2      -> https://oeis.org/A87912
    Laguerre_RevPosHalf    -> https://oeis.org/A87912
    Laguerre_TablGcd       -> https://oeis.org/A102631
    Laguerre_RevPolyCol3   -> https://oeis.org/A102757
    Laguerre_TransNat0     -> https://oeis.org/A103194
    Laguerre_TransSqrs     -> https://oeis.org/A105219
    Laguerre_RevTransNat0  -> https://oeis.org/A105219
    Laguerre_Trev          -> https://oeis.org/A144084
    Laguerre_Trevinv       -> https://oeis.org/A144084
    Laguerre_RevTalt       -> https://oeis.org/A144084
    Laguerre_TablDiag2     -> https://oeis.org/A163102
    Laguerre_TablDiag3     -> https://oeis.org/A179058
    Laguerre_BinConv       -> https://oeis.org/A216831
    Laguerre_PolyDiag      -> https://oeis.org/A277373
    Laguerre_PolyCol3      -> https://oeis.org/A277382
    Laguerre_RevNegHalf    -> https://oeis.org/A295382
    Laguerre_CentralE      -> https://oeis.org/A295383
    Laguerre_RevPolyDiag   -> https://oeis.org/A330260
    Laguerre_EvenSum       -> https://oeis.org/A331325
    Laguerre_OddSum        -> https://oeis.org/A331326
    Laguerre_ColMiddle     -> https://oeis.org/A343580
    Laguerre_InvBinConv    -> https://oeis.org/A343840

    Laguerre: Distinct: 36, Hits: 44, Misses: 25
'''
