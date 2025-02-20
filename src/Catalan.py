from functools import cache
from _tabltypes import Table

"""Balott Catalan triangle.

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


@cache
def catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    pow = catalan(n - 1) + [0]
    row = pow.copy()
    for k in range(n - 1, 0, -1):
        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]
    row[n] = 1

    return row


Catalan = Table(
    catalan,
    "Catalan",
    ["A128899", "A039598"],
    "A128908",
    r"\sum_{i=1}^{n-k+1} \text{Catalan}(i) T_{k-1, n-i}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Catalan)






''' OEIS
    Catalan_Trev          -> 0 
    Catalan_Trevinv       -> 0 
    Catalan_Tantidiag     -> 0 
    Catalan_Tacc          -> 0 
    Catalan_Tder          -> 0 
    Catalan_TablDiag3     -> 0 
    Catalan_TablLcm       -> 0 
    Catalan_TablMax       -> 0 
    Catalan_ColMiddle     -> 0 
    Catalan_CentralO      -> 0 
    Catalan_InvBinConv    -> 0 
    Catalan_PolyRow3      -> 0 
    Catalan_PolyDiag      -> 0 
    Catalan_RevToff11     -> 0 
    Catalan_RevTrev11     -> 0 
    Catalan_RevTantidiag  -> 0 
    Catalan_RevTacc       -> 0 
    Catalan_RevTalt       -> 0 
    Catalan_RevTder       -> 0 
    Catalan_RevEvenSum    -> 0 
    Catalan_RevOddSum     -> 0 
    Catalan_RevColMiddle  -> 0 
    Catalan_RevNegHalf    -> 0 
    Catalan_RevTransSqrs  -> 0 
    Catalan_RevPolyDiag   -> 0 
    Catalan_TablCol0      -> https://oeis.org/A7
    Catalan_TablDiag0     -> https://oeis.org/A12
    Catalan_RevPolyRow1   -> https://oeis.org/A12
    Catalan_PolyRow1      -> https://oeis.org/A27
    Catalan_TablCol1      -> https://oeis.org/A108
    Catalan_AltSum        -> https://oeis.org/A108
    Catalan_TransNat0     -> https://oeis.org/A302
    Catalan_AntiDSum      -> https://oeis.org/A957
    Catalan_OddSum        -> https://oeis.org/A984
    Catalan_TablSum       -> https://oeis.org/A1700
    Catalan_AbsSum        -> https://oeis.org/A1700
    Catalan_EvenSum       -> https://oeis.org/A1791
    Catalan_TablCol2      -> https://oeis.org/A2057
    Catalan_TransSqrs     -> https://oeis.org/A2457
    Catalan_TablCol3      -> https://oeis.org/A3517
    Catalan_RevPolyRow2   -> https://oeis.org/A5408
    Catalan_PolyRow2      -> https://oeis.org/A5563
    Catalan_TablDiag1     -> https://oeis.org/A5843
    Catalan_TablDiag2     -> https://oeis.org/A14106
    Catalan_BinConv       -> https://oeis.org/A25174
    Catalan_RevCentralO   -> https://oeis.org/A26005
    Catalan_Toff11        -> https://oeis.org/A39598
    Catalan_Trev11        -> https://oeis.org/A50166
    Catalan_NegHalf       -> https://oeis.org/A64062
    Catalan_PolyCol2      -> https://oeis.org/A67336
    Catalan_RevPosHalf    -> https://oeis.org/A67336
    Catalan_Tinv11        -> https://oeis.org/A78812
    Catalan_RevPolyRow3   -> https://oeis.org/A79273
    Catalan_PolyCol3      -> https://oeis.org/A104530
    Catalan_AccRevSum     -> https://oeis.org/A114121
    Catalan_TransNat1     -> https://oeis.org/A114121
    Catalan_Triangle      -> https://oeis.org/A128899
    Catalan_Talt          -> https://oeis.org/A128899
    Catalan_Tinv          -> https://oeis.org/A128908
    Catalan_RevTransNat0  -> https://oeis.org/A172060
    Catalan_Trevinv11     -> https://oeis.org/A172431
    Catalan_PosHalf       -> https://oeis.org/A194723
    Catalan_RevPolyCol3   -> https://oeis.org/A194724
    Catalan_RevAntiDSum   -> https://oeis.org/A224747
    Catalan_AccSum        -> https://oeis.org/A296770
    Catalan_RevAccRevSum  -> https://oeis.org/A296770
    Catalan_RevTransNat1  -> https://oeis.org/A296770
    Catalan_TablGcd       -> https://oeis.org/A318829
    Catalan_CentralE      -> https://oeis.org/A359108

    Catalan: Distinct: 37, Hits: 44, Misses: 25
'''
