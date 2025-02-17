from functools import cache
from _tabltypes import Table

"""Harmonic polynomials (coefficients).

[0] 1
[1] 0,     1
[2] 0,     2,     1
[3] 0,     6,     4,     1
[4] 0,    24,    18,     7,    1
[5] 0,   120,    96,    46,   11,    1
[6] 0,   720,   600,   326,  101,   16,   1
[7] 0,  5040,  4320,  2556,  932,  197,  22,  1
"""


@cache
def harmonic(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = harmonic(n - 1) + [1]
    sav = row[1]

    for k in range(n - 1, 0, -1):
        row[k] = (n - 1) * row[k] + row[k - 1]
    row[1] += sav

    return row


Harmonic = Table(
    harmonic,
    "Harmonic",
    ["A358694", "A109822"],
    "A000000",
    r"T_{n - 1, k - 1} + (n - 1) T_{n - 1, k}; \ T_{n, 1} = n!",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Harmonic)




''' OEIS
    Harmonic_Trev          -> 0 
    Harmonic_Trevinv       -> 0 
    Harmonic_Toff11        -> 0 
    Harmonic_Tinv11        -> 0 
    Harmonic_Trevinv11     -> 0 
    Harmonic_Tantidiag     -> 0 
    Harmonic_Tacc          -> 0 
    Harmonic_Tder          -> 0 
    Harmonic_TablDiag3     -> 0 
    Harmonic_TablLcm       -> 0 
    Harmonic_OddSum        -> 0 
    Harmonic_AccSum        -> 0 
    Harmonic_AccRevSum     -> 0 
    Harmonic_AntiDSum      -> 0 
    Harmonic_ColMiddle     -> 0 
    Harmonic_CentralE      -> 0 
    Harmonic_CentralO      -> 0 
    Harmonic_TransNat1     -> 0 
    Harmonic_TransSqrs     -> 0 
    Harmonic_BinConv       -> 0 
    Harmonic_InvBinConv    -> 0 
    Harmonic_PolyRow3      -> 0 
    Harmonic_PolyCol3      -> 0 
    Harmonic_PolyDiag      -> 0 
    Harmonic_RevToff11     -> 0 
    Harmonic_RevTrev11     -> 0 
    Harmonic_RevTantidiag  -> 0 
    Harmonic_RevTacc       -> 0 
    Harmonic_RevTalt       -> 0 
    Harmonic_RevTder       -> 0 
    Harmonic_RevEvenSum    -> 0 
    Harmonic_RevOddSum     -> 0 
    Harmonic_RevAccRevSum  -> 0 
    Harmonic_RevAntiDSum   -> 0 
    Harmonic_RevColMiddle  -> 0 
    Harmonic_RevCentralO   -> 0 
    Harmonic_RevNegHalf    -> 0 
    Harmonic_RevTransNat0  -> 0 
    Harmonic_RevTransNat1  -> 0 
    Harmonic_RevTransSqrs  -> 0 
    Harmonic_RevPolyCol3   -> 0 
    Harmonic_RevPolyDiag   -> 0 
    Harmonic_TablCol0      -> https://oeis.org/A7
    Harmonic_TablDiag0     -> https://oeis.org/A12
    Harmonic_RevPolyRow1   -> https://oeis.org/A12
    Harmonic_PolyRow1      -> https://oeis.org/A27
    Harmonic_TablDiag1     -> https://oeis.org/A124
    Harmonic_TablCol1      -> https://oeis.org/A142
    Harmonic_TablMax       -> https://oeis.org/A142
    Harmonic_TablSum       -> https://oeis.org/A254
    Harmonic_AbsSum        -> https://oeis.org/A254
    Harmonic_TablCol2      -> https://oeis.org/A1563
    Harmonic_AltSum        -> https://oeis.org/A1710
    Harmonic_RevPolyRow2   -> https://oeis.org/A5408
    Harmonic_PolyRow2      -> https://oeis.org/A5563
    Harmonic_PolyCol2      -> https://oeis.org/A52582
    Harmonic_RevPosHalf    -> https://oeis.org/A52582
    Harmonic_TablCol3      -> https://oeis.org/A67318
    Harmonic_RevPolyRow3   -> https://oeis.org/A80859
    Harmonic_TransNat0     -> https://oeis.org/A81052
    Harmonic_Trev11        -> https://oeis.org/A109822
    Harmonic_PosHalf       -> https://oeis.org/A129890
    Harmonic_TablGcd       -> https://oeis.org/A174965
    Harmonic_EvenSum       -> https://oeis.org/A182541
    Harmonic_NegHalf       -> https://oeis.org/A192459
    Harmonic_Tinv          -> https://oeis.org/A227341
    Harmonic_TablDiag2     -> https://oeis.org/A308305
    Harmonic_Triangle      -> https://oeis.org/A358694
    Harmonic_Talt          -> https://oeis.org/A358694

    Harmonic: Distinct: 23, Hits: 27, Misses: 42
'''
