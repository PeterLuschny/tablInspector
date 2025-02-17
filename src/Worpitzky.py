from functools import cache
from _tabltypes import Table

"""Worpitzky triangle.

[0]  1;
[1]  1,   1;
[2]  1,   3,    2;
[3]  1,   7,   12,     6;
[4]  1,  15,   50,    60,     24;
[5]  1,  31,  180,   390,    360,    120;
[6]  1,  63,  602,  2100,   3360,   2520,    720;
[7]  1, 127, 1932, 10206,  25200,  31920,  20160,   5040;
[8]  1, 255, 6050, 46620, 166824, 317520, 332640, 181440, 40320;
"""


@cache
def worpitzky(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = worpitzky(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row


Worpitzky = Table(
    worpitzky,
    "Worpitzky",
    ["A028246", "A053440", "A075263", "A130850", "A163626"],
    "",
    r"\sum_{j=0}^{n} \text{Eulerian}(n, j) \binom{n-j}{n-k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Worpitzky)




''' OEIS
    Worpitzky_Trev11        -> 0 
    Worpitzky_Tantidiag     -> 0 
    Worpitzky_Tacc          -> 0 
    Worpitzky_Tder          -> 0 
    Worpitzky_TablLcm       -> 0 
    Worpitzky_TablMax       -> 0 
    Worpitzky_AccSum        -> 0 
    Worpitzky_ColMiddle     -> 0 
    Worpitzky_CentralO      -> 0 
    Worpitzky_TransSqrs     -> 0 
    Worpitzky_PolyRow3      -> 0 
    Worpitzky_RevToff11     -> 0 
    Worpitzky_RevTrev11     -> 0 
    Worpitzky_RevTinv11     -> 0 
    Worpitzky_RevTantidiag  -> 0 
    Worpitzky_RevTder       -> 0 
    Worpitzky_RevAccRevSum  -> 0 
    Worpitzky_RevAntiDSum   -> 0 
    Worpitzky_RevColMiddle  -> 0 
    Worpitzky_RevCentralO   -> 0 
    Worpitzky_RevTransNat0  -> 0 
    Worpitzky_RevTransNat1  -> 0 
    Worpitzky_RevTransSqrs  -> 0 
    Worpitzky_RevPolyRow3   -> 0 
    Worpitzky_RevPolyDiag   -> 0 
    Worpitzky_AltSum        -> https://oeis.org/A7
    Worpitzky_TablCol0      -> https://oeis.org/A12
    Worpitzky_TablGcd       -> https://oeis.org/A12
    Worpitzky_PolyRow1      -> https://oeis.org/A27
    Worpitzky_RevPolyRow1   -> https://oeis.org/A27
    Worpitzky_TablDiag0     -> https://oeis.org/A142
    Worpitzky_BinConv       -> https://oeis.org/A169
    Worpitzky_TablCol1      -> https://oeis.org/A225
    Worpitzky_PolyRow2      -> https://oeis.org/A384
    Worpitzky_TablSum       -> https://oeis.org/A629
    Worpitzky_AbsSum        -> https://oeis.org/A629
    Worpitzky_EvenSum       -> https://oeis.org/A670
    Worpitzky_OddSum        -> https://oeis.org/A670
    Worpitzky_AccRevSum     -> https://oeis.org/A670
    Worpitzky_TransNat1     -> https://oeis.org/A670
    Worpitzky_RevEvenSum    -> https://oeis.org/A670
    Worpitzky_RevOddSum     -> https://oeis.org/A670
    Worpitzky_RevNegHalf    -> https://oeis.org/A670
    Worpitzky_TablDiag1     -> https://oeis.org/A1710
    Worpitzky_RevPolyRow2   -> https://oeis.org/A2378
    Worpitzky_TablDiag2     -> https://oeis.org/A5460
    Worpitzky_TablDiag3     -> https://oeis.org/A5461
    Worpitzky_NegHalf       -> https://oeis.org/A9006
    Worpitzky_TablCol2      -> https://oeis.org/A28243
    Worpitzky_TablCol3      -> https://oeis.org/A28244
    Worpitzky_Triangle      -> https://oeis.org/A28246
    Worpitzky_Talt          -> https://oeis.org/A28246
    Worpitzky_Toff11        -> https://oeis.org/A53440
    Worpitzky_RevTacc       -> https://oeis.org/A54255
    Worpitzky_Tinvrev       -> https://oeis.org/A106340
    Worpitzky_PosHalf       -> https://oeis.org/A123227
    Worpitzky_Trev          -> https://oeis.org/A130850
    Worpitzky_RevTalt       -> https://oeis.org/A130850
    Worpitzky_CentralE      -> https://oeis.org/A185157
    Worpitzky_PolyCol2      -> https://oeis.org/A201339
    Worpitzky_RevPosHalf    -> https://oeis.org/A201339
    Worpitzky_PolyCol3      -> https://oeis.org/A201354
    Worpitzky_RevPolyCol3   -> https://oeis.org/A201355
    Worpitzky_AntiDSum      -> https://oeis.org/A229046
    Worpitzky_TransNat0     -> https://oeis.org/A343583
    Worpitzky_InvBinConv    -> https://oeis.org/A343584
    Worpitzky_PolyDiag      -> https://oeis.org/A372312

    Worpitzky: Distinct: 31, Hits: 42, Misses: 25
'''
