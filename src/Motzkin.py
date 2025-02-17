from functools import cache
from _tabltypes import Table

"""Motzkin generating function triangle.

[0]    1;
[1]    1,    1;
[2]    2,    2,    1;
[3]    4,    5,    3,    1;
[4]    9,   12,    9,    4,   1;
[5]   21,   30,   25,   14,   5,   1;
[6]   51,   76,   69,   44,  20,   6,   1;
[7]  127,  196,  189,  133,  70,  27,   7,  1;
[8]  323,  512,  518,  392, 230, 104,  35,  8, 1;
[9]  835, 1353, 1422, 1140, 726, 369, 147, 44, 9, 1.
"""


@cache
def motzkin(n: int) -> list[int]:
    if n == 0:
        return [1]

    r = motzkin(n - 1) + [0]
    row = motzkin(n - 1) + [1]
    for k in range(0, n):
        row[k] += r[k - 1] + r[k + 1]
    return row


Motzkin = Table(
    motzkin,
    "Motzkin",
    ["A064189", "A026300", "A009766", "A122896"],
    "A000000",
    r"\binom{n}{k} \text{Hyper}([(k-n)/2, (k-n+1)/2], [k+2], 4)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Motzkin)




''' OEIS
    Motzkin_Tinv          -> https://oeis.org/A-999999
    Motzkin_Trevinv       -> https://oeis.org/A-999999
    Motzkin_Tinv11        -> https://oeis.org/A-999999
    Motzkin_Trevinv11     -> https://oeis.org/A-999999
    Motzkin_Toff11        -> 0 
    Motzkin_Trev11        -> 0 
    Motzkin_Tacc          -> 0 
    Motzkin_Tder          -> 0 
    Motzkin_TablLcm       -> 0 
    Motzkin_PolyDiag      -> 0 
    Motzkin_RevToff11     -> 0 
    Motzkin_RevTrev11     -> 0 
    Motzkin_RevTantidiag  -> 0 
    Motzkin_RevTacc       -> 0 
    Motzkin_RevTder       -> 0 
    Motzkin_RevEvenSum    -> 0 
    Motzkin_RevOddSum     -> 0 
    Motzkin_RevTransNat0  -> 0 
    Motzkin_RevTransSqrs  -> 0 
    Motzkin_RevPolyRow3   -> 0 
    Motzkin_RevPolyCol3   -> 0 
    Motzkin_RevPolyDiag   -> 0 
    Motzkin_TablDiag0     -> https://oeis.org/A12
    Motzkin_TablGcd       -> https://oeis.org/A12
    Motzkin_TablDiag1     -> https://oeis.org/A27
    Motzkin_PolyRow1      -> https://oeis.org/A27
    Motzkin_RevPolyRow1   -> https://oeis.org/A27
    Motzkin_TablDiag2     -> https://oeis.org/A96
    Motzkin_AccRevSum     -> https://oeis.org/A244
    Motzkin_TransNat1     -> https://oeis.org/A244
    Motzkin_TablDiag3     -> https://oeis.org/A297
    Motzkin_TablCol0      -> https://oeis.org/A1006
    Motzkin_RevPolyRow2   -> https://oeis.org/A1844
    Motzkin_TablCol1      -> https://oeis.org/A2026
    Motzkin_EvenSum       -> https://oeis.org/A2426
    Motzkin_PolyRow2      -> https://oeis.org/A2522
    Motzkin_AltSum        -> https://oeis.org/A5043
    Motzkin_AntiDSum      -> https://oeis.org/A5043
    Motzkin_TablCol2      -> https://oeis.org/A5322
    Motzkin_TablCol3      -> https://oeis.org/A5323
    Motzkin_OddSum        -> https://oeis.org/A5717
    Motzkin_TablSum       -> https://oeis.org/A5773
    Motzkin_AbsSum        -> https://oeis.org/A5773
    Motzkin_Trev          -> https://oeis.org/A26300
    Motzkin_RevTalt       -> https://oeis.org/A26300
    Motzkin_CentralE      -> https://oeis.org/A26302
    Motzkin_RevColMiddle  -> https://oeis.org/A26307
    Motzkin_TablMax       -> https://oeis.org/A26938
    Motzkin_AccSum        -> https://oeis.org/A26943
    Motzkin_RevAccRevSum  -> https://oeis.org/A26943
    Motzkin_RevTransNat1  -> https://oeis.org/A26943
    Motzkin_PolyCol2      -> https://oeis.org/A59738
    Motzkin_RevPosHalf    -> https://oeis.org/A59738
    Motzkin_Triangle      -> https://oeis.org/A64189
    Motzkin_Talt          -> https://oeis.org/A64189
    Motzkin_Tantidiag     -> https://oeis.org/A106489
    Motzkin_PolyRow3      -> https://oeis.org/A135859
    Motzkin_RevAntiDSum   -> https://oeis.org/A191519
    Motzkin_RevCentralO   -> https://oeis.org/A327871
    Motzkin_TransNat0     -> https://oeis.org/A330796
    Motzkin_PosHalf       -> https://oeis.org/A330799
    Motzkin_NegHalf       -> https://oeis.org/A330800
    Motzkin_ColMiddle     -> https://oeis.org/A344394
    Motzkin_CentralO      -> https://oeis.org/A344396
    Motzkin_BinConv       -> https://oeis.org/A344502
    Motzkin_InvBinConv    -> https://oeis.org/A344503
    Motzkin_TransSqrs     -> https://oeis.org/A344504
    Motzkin_PolyCol3      -> https://oeis.org/A344506
    Motzkin_RevNegHalf    -> https://oeis.org/A344507

    Motzkin: Distinct: 38, Hits: 51, Misses: 18
'''
