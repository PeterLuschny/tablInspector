from functools import cache
from _tabltypes import Table

"""Coefficients of Motzkin polynomials.

[0] 1
[1] 1, 0
[2] 1, 0,  1
[3] 1, 0,  3, 0
[4] 1, 0,  6, 0,   2
[5] 1, 0, 10, 0,  10, 0
[6] 1, 0, 15, 0,  30, 0,   5
[7] 1, 0, 21, 0,  70, 0,  35, 0
[8] 1, 0, 28, 0, 140, 0, 140, 0,  14
[9] 1, 0, 36, 0, 252, 0, 420, 0, 126, 0
"""


@cache
def motzkinpoly(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]

    h = 0 if n % 2 else (motzkinpoly(n - 2)[n - 2] * 2 * (n - 1)) // (n // 2 + 1)
    row = motzkinpoly(n - 1) + [h]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


MotzkinPoly = Table(
    motzkinpoly,
    "MotzkinPoly",
    ["A359364"],
    "",
    r"k \ \text{odd} \ ? \ 0 \ : \ \binom{n}{k} \text{Catalan}\left(\frac{k}{2}\right)"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(MotzkinPoly)


''' OEIS
    MotzkinPoly_Tinvrev       -> 0 
    MotzkinPoly_Toff11        -> 0 
    MotzkinPoly_Trev11        -> 0 
    MotzkinPoly_Tantidiag     -> 0 
    MotzkinPoly_Tacc          -> 0 
    MotzkinPoly_Tder          -> 0 
    MotzkinPoly_TablLcm       -> 0 
    MotzkinPoly_TablGcd       -> 0 
    MotzkinPoly_TablMax       -> 0 
    MotzkinPoly_ColMiddle     -> 0 
    MotzkinPoly_CentralO      -> 0 
    MotzkinPoly_TransNat0     -> 0 
    MotzkinPoly_TransSqrs     -> 0 
    MotzkinPoly_BinConv       -> 0 
    MotzkinPoly_InvBinConv    -> 0 
    MotzkinPoly_PolyCol3      -> 0 
    MotzkinPoly_RevToff11     -> 0 
    MotzkinPoly_RevTrev11     -> 0 
    MotzkinPoly_RevTinv11     -> 0 
    MotzkinPoly_RevTantidiag  -> 0 
    MotzkinPoly_RevTacc       -> 0 
    MotzkinPoly_RevTder       -> 0 
    MotzkinPoly_RevColMiddle  -> 0 
    MotzkinPoly_RevCentralO   -> 0 
    MotzkinPoly_RevTransSqrs  -> 0 
    MotzkinPoly_TablCol1      -> https://oeis.org/A7
    MotzkinPoly_TablCol3      -> https://oeis.org/A7
    MotzkinPoly_OddSum        -> https://oeis.org/A7
    MotzkinPoly_TablCol0      -> https://oeis.org/A12
    MotzkinPoly_PolyRow1      -> https://oeis.org/A12
    MotzkinPoly_RevPolyRow1   -> https://oeis.org/A27
    MotzkinPoly_PosHalf       -> https://oeis.org/A108
    MotzkinPoly_NegHalf       -> https://oeis.org/A108
    MotzkinPoly_TablCol2      -> https://oeis.org/A217
    MotzkinPoly_TablSum       -> https://oeis.org/A1006
    MotzkinPoly_EvenSum       -> https://oeis.org/A1006
    MotzkinPoly_AltSum        -> https://oeis.org/A1006
    MotzkinPoly_AbsSum        -> https://oeis.org/A1006
    MotzkinPoly_RevPolyCol3   -> https://oeis.org/A2212
    MotzkinPoly_TablDiag2     -> https://oeis.org/A2457
    MotzkinPoly_PolyRow2      -> https://oeis.org/A2522
    MotzkinPoly_RevPolyRow2   -> https://oeis.org/A2522
    MotzkinPoly_TablDiag3     -> https://oeis.org/A2802
    MotzkinPoly_RevTransNat0  -> https://oeis.org/A5717
    MotzkinPoly_RevAntiDSum   -> https://oeis.org/A6318
    MotzkinPoly_AntiDSum      -> https://oeis.org/A23426
    MotzkinPoly_AccRevSum     -> https://oeis.org/A25179
    MotzkinPoly_TransNat1     -> https://oeis.org/A25179
    MotzkinPoly_RevEvenSum    -> https://oeis.org/A26945
    MotzkinPoly_PolyRow3      -> https://oeis.org/A56107
    MotzkinPoly_RevPolyRow3   -> https://oeis.org/A79908
    MotzkinPoly_PolyCol2      -> https://oeis.org/A91147
    MotzkinPoly_RevNegHalf    -> https://oeis.org/A91147
    MotzkinPoly_Trev          -> https://oeis.org/A97610
    MotzkinPoly_RevTalt       -> https://oeis.org/A97610
    MotzkinPoly_RevOddSum     -> https://oeis.org/A99250
    MotzkinPoly_TablDiag0     -> https://oeis.org/A126120
    MotzkinPoly_TablDiag1     -> https://oeis.org/A138364
    MotzkinPoly_AccSum        -> https://oeis.org/A189912
    MotzkinPoly_RevAccRevSum  -> https://oeis.org/A189912
    MotzkinPoly_RevTransNat1  -> https://oeis.org/A189912
    MotzkinPoly_RevPolyDiag   -> https://oeis.org/A247496
    MotzkinPoly_Triangle      -> https://oeis.org/A359364
    MotzkinPoly_Talt          -> https://oeis.org/A359364
    MotzkinPoly_CentralE      -> https://oeis.org/A359647
    MotzkinPoly_PolyDiag      -> https://oeis.org/A359649

    MotzkinPoly: Distinct: 28, Hits: 41, Misses: 25
'''
