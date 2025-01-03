from functools import cache
from _tabltypes import Table

"""Rencontres triangle.

[0]       1;
[1]       0,      1;
[2]       1,      0,     1;
[3]       2,      3,     0,     1;
[4]       9,      8,     6,     0,    1;
[5]      44,     45,    20,    10,    0,    1;
[6]     265,    264,   135,    40,   15,    0,   1;
[7]    1854,   1855,   924,   315,   70,   21,   0,  1;
[8]   14833,  14832,  7420,  2464,  630,  112,  28,  0, 1;
[9]  133496, 133497, 66744, 22260, 5544, 1134, 168, 36, 0, 1;
"""


@cache
def rencontres(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = [
        (n - 1) * (rencontres(n - 1)[0] + rencontres(n - 2)[0])
    ] + rencontres(n - 1)
    for k in range(1, n - 1):
        row[k] = (n * row[k]) // k
    return row


Rencontres = Table(
    rencontres,
    "Rencontres",
    ["A008290", "A098825"],
    "A055137",
    r"\binom{n}{k} derangements(n - k)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Rencontres)


''' OEIS
    Rencontres_Toff11        -> 0 
    Rencontres_Trev11        -> 0 
    Rencontres_Tinv11        -> 0 
    Rencontres_Tantidiag     -> 0 
    Rencontres_Tacc          -> 0 
    Rencontres_TablLcm       -> 0 
    Rencontres_AntiDSum      -> 0 
    Rencontres_ColMiddle     -> 0 
    Rencontres_CentralO      -> 0 
    Rencontres_BinConv       -> 0 
    Rencontres_InvBinConv    -> 0 
    Rencontres_PolyRow3      -> 0 
    Rencontres_RevToff11     -> 0 
    Rencontres_RevTrev11     -> 0 
    Rencontres_RevTacc       -> 0 
    Rencontres_RevTder       -> 0 
    Rencontres_RevEvenSum    -> 0 
    Rencontres_RevOddSum     -> 0 
    Rencontres_RevColMiddle  -> 0 
    Rencontres_RevCentralO   -> 0 
    Rencontres_RevTransSqrs  -> 0 
    Rencontres_RevPolyRow3   -> 0 
    Rencontres_RevPolyCol3   -> 0 
    Rencontres_RevPolyDiag   -> 0 
    Rencontres_TablDiag1     -> https://oeis.org/A7
    Rencontres_TablDiag0     -> https://oeis.org/A12
    Rencontres_TablGcd       -> https://oeis.org/A12
    Rencontres_RevPolyRow1   -> https://oeis.org/A12
    Rencontres_AltSum        -> https://oeis.org/A23
    Rencontres_PolyRow1      -> https://oeis.org/A27
    Rencontres_TablSum       -> https://oeis.org/A142
    Rencontres_AbsSum        -> https://oeis.org/A142
    Rencontres_TransNat0     -> https://oeis.org/A142
    Rencontres_TablCol0      -> https://oeis.org/A166
    Rencontres_TablDiag2     -> https://oeis.org/A217
    Rencontres_TablCol1      -> https://oeis.org/A240
    Rencontres_PosHalf       -> https://oeis.org/A354
    Rencontres_TablCol2      -> https://oeis.org/A387
    Rencontres_TablCol3      -> https://oeis.org/A449
    Rencontres_PolyCol2      -> https://oeis.org/A522
    Rencontres_AccSum        -> https://oeis.org/A1563
    Rencontres_RevAccRevSum  -> https://oeis.org/A1563
    Rencontres_RevTransNat1  -> https://oeis.org/A1563
    Rencontres_PolyRow2      -> https://oeis.org/A2522
    Rencontres_RevPolyRow2   -> https://oeis.org/A2522
    Rencontres_TablDiag3     -> https://oeis.org/A7290
    Rencontres_Triangle      -> https://oeis.org/A8290
    Rencontres_Talt          -> https://oeis.org/A8290
    Rencontres_PolyCol3      -> https://oeis.org/A10842
    Rencontres_RevNegHalf    -> https://oeis.org/A10843
    Rencontres_AccRevSum     -> https://oeis.org/A52849
    Rencontres_TransNat1     -> https://oeis.org/A52849
    Rencontres_TransSqrs     -> https://oeis.org/A52849
    Rencontres_Tinv          -> https://oeis.org/A55137
    Rencontres_RevTransNat0  -> https://oeis.org/A62119
    Rencontres_EvenSum       -> https://oeis.org/A62282
    Rencontres_OddSum        -> https://oeis.org/A63083
    Rencontres_Trev          -> https://oeis.org/A98825
    Rencontres_RevTalt       -> https://oeis.org/A98825
    Rencontres_TablMax       -> https://oeis.org/A174318
    Rencontres_Tder          -> https://oeis.org/A180188
    Rencontres_PolyDiag      -> https://oeis.org/A217701
    Rencontres_CentralE      -> https://oeis.org/A281262
    Rencontres_NegHalf       -> https://oeis.org/A343582
    Rencontres_RevTantidiag  -> https://oeis.org/A371995
    Rencontres_RevAntiDSum   -> https://oeis.org/A372102

    Rencontres: Distinct: 32, Hits: 42, Misses: 24
'''
