from functools import cache
from _tabltypes import Table

"""Bessel2 triangle.

[0] 1
[1] 1, 0
[2] 1, 0,  1
[3] 1, 0,  3, 0
[4] 1, 0,  6, 0,   3
[5] 1, 0, 10, 0,  15, 0
[6] 1, 0, 15, 0,  45, 0,   15
[7] 1, 0, 21, 0, 105, 0,  105, 0
[8] 1, 0, 28, 0, 210, 0,  420, 0, 105
[9] 1, 0, 36, 0, 378, 0, 1260, 0, 945, 0
"""


@cache
def bessel2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]

    row = bessel2(n - 1) + [0]
    row[n] = 0 if n % 2 else row[n - 2]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


Bessel2 = Table(
    bessel2,
    "Bessel2",
    ["A359760", "A073278", "A066325", "A099174", "A111924", "A144299", "A104556"],
    "",
    r"is(k \text{ odd}) \, ? \, 0 : \binom{n}{k} \frac{k!}{2^{k/2} (k/2)!}"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Bessel2)


''' OEIS
    Bessel2_Toff11        -> 0 
    Bessel2_Trev11        -> 0 
    Bessel2_Tantidiag     -> 0 
    Bessel2_Tacc          -> 0 
    Bessel2_Tder          -> 0 
    Bessel2_TablLcm       -> 0 
    Bessel2_TablMax       -> 0 
    Bessel2_AccRevSum     -> 0 
    Bessel2_AntiDSum      -> 0 
    Bessel2_ColMiddle     -> 0 
    Bessel2_CentralO      -> 0 
    Bessel2_TransNat0     -> 0 
    Bessel2_TransNat1     -> 0 
    Bessel2_TransSqrs     -> 0 
    Bessel2_PolyCol3      -> 0 
    Bessel2_RevToff11     -> 0 
    Bessel2_RevTrev11     -> 0 
    Bessel2_RevTinv11     -> 0 
    Bessel2_RevTantidiag  -> 0 
    Bessel2_RevTacc       -> 0 
    Bessel2_RevTder       -> 0 
    Bessel2_RevColMiddle  -> 0 
    Bessel2_RevCentralO   -> 0 
    Bessel2_RevTransSqrs  -> 0 
    Bessel2_RevPolyDiag   -> 0 
    Bessel2_TablCol1      -> https://oeis.org/A7
    Bessel2_TablCol3      -> https://oeis.org/A7
    Bessel2_OddSum        -> https://oeis.org/A7
    Bessel2_TablCol0      -> https://oeis.org/A12
    Bessel2_PolyRow1      -> https://oeis.org/A12
    Bessel2_RevPolyRow1   -> https://oeis.org/A27
    Bessel2_TablSum       -> https://oeis.org/A85
    Bessel2_EvenSum       -> https://oeis.org/A85
    Bessel2_AltSum        -> https://oeis.org/A85
    Bessel2_AbsSum        -> https://oeis.org/A85
    Bessel2_AccSum        -> https://oeis.org/A85
    Bessel2_RevAccRevSum  -> https://oeis.org/A85
    Bessel2_RevTransNat1  -> https://oeis.org/A85
    Bessel2_TablCol2      -> https://oeis.org/A217
    Bessel2_TablDiag3     -> https://oeis.org/A457
    Bessel2_RevAntiDSum   -> https://oeis.org/A1515
    Bessel2_TablDiag2     -> https://oeis.org/A1879
    Bessel2_PolyRow2      -> https://oeis.org/A2522
    Bessel2_RevPolyRow2   -> https://oeis.org/A2522
    Bessel2_PosHalf       -> https://oeis.org/A5425
    Bessel2_NegHalf       -> https://oeis.org/A5425
    Bessel2_RevTransNat0  -> https://oeis.org/A13989
    Bessel2_PolyRow3      -> https://oeis.org/A56107
    Bessel2_RevEvenSum    -> https://oeis.org/A66223
    Bessel2_RevOddSum     -> https://oeis.org/A66224
    Bessel2_TablGcd       -> https://oeis.org/A69834
    Bessel2_RevPolyRow3   -> https://oeis.org/A79908
    Bessel2_Trev          -> https://oeis.org/A99174
    Bessel2_Tinvrev       -> https://oeis.org/A99174
    Bessel2_RevTalt       -> https://oeis.org/A99174
    Bessel2_PolyCol2      -> https://oeis.org/A115329
    Bessel2_RevNegHalf    -> https://oeis.org/A115329
    Bessel2_TablDiag0     -> https://oeis.org/A123023
    Bessel2_TablDiag1     -> https://oeis.org/A123023
    Bessel2_RevPolyCol3   -> https://oeis.org/A202834
    Bessel2_BinConv       -> https://oeis.org/A344501
    Bessel2_InvBinConv    -> https://oeis.org/A344501
    Bessel2_PolyDiag      -> https://oeis.org/A359739
    Bessel2_Triangle      -> https://oeis.org/A359760
    Bessel2_Talt          -> https://oeis.org/A359760
    Bessel2_CentralE      -> https://oeis.org/A359761

    Bessel2: Distinct: 25, Hits: 41, Misses: 25
'''
