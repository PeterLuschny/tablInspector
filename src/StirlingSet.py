from functools import cache
from _tabltypes import Table

"""Stirling set numbers.

[0]  1
[1]  0, 1
[2]  0, 1,   1
[3]  0, 1,   3,    1
[4]  0, 1,   7,    6,    1
[5]  0, 1,  15,   25,   10,    1
[6]  0, 1,  31,   90,   65,   15,    1
[7]  0, 1,  63,  301,  350,  140,   21,   1
[8]  0, 1, 127,  966, 1701, 1050,  266,  28,  1
[9]  0, 1, 255, 3025, 7770, 6951, 2646, 462, 36, 1
"""


@cache
def stirlingset(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [0] + stirlingset(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row


StirlingSet = Table(
    stirlingset,
    "StirlingSet",
    [
        "A048993", "A008277", "A008278", "A080417",
        "A106800", "A151511", "A151512", "A154959",
        "A213735",
    ],
    "A132393",
    r"{n \brace k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(StirlingSet)




''' OEIS
    StirlingSet_Tantidiag     -> 0 
    StirlingSet_RevToff11     -> 0 
    StirlingSet_RevTrev11     -> 0 
    StirlingSet_RevTantidiag  -> 0 
    StirlingSet_RevTacc       -> 0 
    StirlingSet_RevTder       -> 0 
    StirlingSet_RevTransSqrs  -> 0 
    StirlingSet_TablCol0      -> https://oeis.org/A7
    StirlingSet_TablCol1      -> https://oeis.org/A12
    StirlingSet_TablDiag0     -> https://oeis.org/A12
    StirlingSet_RevPolyRow1   -> https://oeis.org/A12
    StirlingSet_PolyRow1      -> https://oeis.org/A27
    StirlingSet_RevPolyRow2   -> https://oeis.org/A27
    StirlingSet_TablSum       -> https://oeis.org/A110
    StirlingSet_AbsSum        -> https://oeis.org/A110
    StirlingSet_AccRevSum     -> https://oeis.org/A110
    StirlingSet_TransNat1     -> https://oeis.org/A110
    StirlingSet_TablDiag1     -> https://oeis.org/A217
    StirlingSet_TablCol2      -> https://oeis.org/A225
    StirlingSet_TablCol3      -> https://oeis.org/A392
    StirlingSet_AltSum        -> https://oeis.org/A587
    StirlingSet_TablDiag2     -> https://oeis.org/A1296
    StirlingSet_TablDiag3     -> https://oeis.org/A1297
    StirlingSet_PolyCol2      -> https://oeis.org/A1861
    StirlingSet_RevPosHalf    -> https://oeis.org/A1861
    StirlingSet_PolyRow2      -> https://oeis.org/A2378
    StirlingSet_TablMax       -> https://oeis.org/A2870
    StirlingSet_PosHalf       -> https://oeis.org/A4211
    StirlingSet_RevPolyCol3   -> https://oeis.org/A4212
    StirlingSet_TransNat0     -> https://oeis.org/A5493
    StirlingSet_CentralE      -> https://oeis.org/A7820
    StirlingSet_Toff11        -> https://oeis.org/A8277
    StirlingSet_Trev11        -> https://oeis.org/A8278
    StirlingSet_NegHalf       -> https://oeis.org/A9235
    StirlingSet_RevAntiDSum   -> https://oeis.org/A24428
    StirlingSet_OddSum        -> https://oeis.org/A24429
    StirlingSet_EvenSum       -> https://oeis.org/A24430
    StirlingSet_PolyCol3      -> https://oeis.org/A27710
    StirlingSet_RevPolyRow3   -> https://oeis.org/A28387
    StirlingSet_PolyRow3      -> https://oeis.org/A33445
    StirlingSet_TransSqrs     -> https://oeis.org/A33452
    StirlingSet_Triangle      -> https://oeis.org/A48993
    StirlingSet_Talt          -> https://oeis.org/A48993
    StirlingSet_Trevinv       -> https://oeis.org/A54654
    StirlingSet_TablLcm       -> https://oeis.org/A63040
    StirlingSet_TablGcd       -> https://oeis.org/A89026
    StirlingSet_Trevinv11     -> https://oeis.org/A94638
    StirlingSet_RevEvenSum    -> https://oeis.org/A96647
    StirlingSet_RevOddSum     -> https://oeis.org/A96648
    StirlingSet_Tinvrev11     -> https://oeis.org/A106342
    StirlingSet_Trev          -> https://oeis.org/A106800
    StirlingSet_RevTalt       -> https://oeis.org/A106800
    StirlingSet_BinConv       -> https://oeis.org/A122455
    StirlingSet_RevCentralO   -> https://oeis.org/A129506
    StirlingSet_Tinv11        -> https://oeis.org/A130534
    StirlingSet_Tinv          -> https://oeis.org/A132393
    StirlingSet_AntiDSum      -> https://oeis.org/A171367
    StirlingSet_RevNegHalf    -> https://oeis.org/A213170
    StirlingSet_PolyDiag      -> https://oeis.org/A242817
    StirlingSet_CentralO      -> https://oeis.org/A247238
    StirlingSet_RevTransNat0  -> https://oeis.org/A278677
    StirlingSet_RevPolyDiag   -> https://oeis.org/A301419
    StirlingSet_Tder          -> https://oeis.org/A321331
    StirlingSet_RevColMiddle  -> https://oeis.org/A343278
    StirlingSet_ColMiddle     -> https://oeis.org/A343279
    StirlingSet_InvBinConv    -> https://oeis.org/A343841
    StirlingSet_Tacc          -> https://oeis.org/A359107
    StirlingSet_AccSum        -> https://oeis.org/A359109
    StirlingSet_RevAccRevSum  -> https://oeis.org/A359109
    StirlingSet_RevTransNat1  -> https://oeis.org/A359109

    StirlingSet: Distinct: 53, Hits: 63, Misses: 7
'''
