from functools import cache
from _tabltypes import Table

"""Euler-Bernoulli triangle.

[0] [1]
[1] [0,   1]
[2] [0,   1,   1]
[3] [0,   1,   2,   2]
[4] [0,   2,   4,   5,    5]
[5] [0,   5,  10,  14,   16,   16]
[6] [0,  16,  32,  46,   56,   61,   61]
[7] [0,  61, 122, 178,  224,  256,  272,  272]
"""


@cache
def entringer(n: int) -> list[int]:
    if n == 0:
        return [1]

    rowA = entringer(n - 1)
    row = [0] + entringer(n - 1)
    row[1] = row[n]
    for k in range(2, n + 1):
        row[k] = row[k - 1] + rowA[n - k]
    return row


Entringer = Table(
    entringer,
    "Entringer",
    ["A008281", "A008282", "A010094"],
    "",  # not invertible
    r"is(k=0) \ ? \ 0^n : T(n, k-1) + T(n-1, n-k)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Entringer)






''' OEIS
    Entringer_Trev          -> 0 
    Entringer_Tantidiag     -> 0 
    Entringer_Tacc          -> 0 
    Entringer_Tder          -> 0 
    Entringer_TablLcm       -> 0 
    Entringer_EvenSum       -> 0 
    Entringer_OddSum        -> 0 
    Entringer_AltSum        -> 0 
    Entringer_AntiDSum      -> 0 
    Entringer_ColMiddle     -> 0 
    Entringer_PosHalf       -> 0 
    Entringer_NegHalf       -> 0 
    Entringer_TransNat0     -> 0 
    Entringer_TransSqrs     -> 0 
    Entringer_PolyCol2      -> 0 
    Entringer_PolyCol3      -> 0 
    Entringer_PolyDiag      -> 0 
    Entringer_RevToff11     -> 0 
    Entringer_RevTrev11     -> 0 
    Entringer_RevTantidiag  -> 0 
    Entringer_RevTalt       -> 0 
    Entringer_RevTder       -> 0 
    Entringer_RevEvenSum    -> 0 
    Entringer_RevOddSum     -> 0 
    Entringer_RevAntiDSum   -> 0 
    Entringer_RevCentralO   -> 0 
    Entringer_RevPosHalf    -> 0 
    Entringer_RevNegHalf    -> 0 
    Entringer_RevTransSqrs  -> 0 
    Entringer_RevPolyCol3   -> 0 
    Entringer_RevPolyDiag   -> 0 
    Entringer_TablCol0      -> https://oeis.org/A7
    Entringer_RevPolyRow1   -> https://oeis.org/A12
    Entringer_PolyRow1      -> https://oeis.org/A27
    Entringer_RevPolyRow2   -> https://oeis.org/A27
    Entringer_TablCol1      -> https://oeis.org/A111
    Entringer_TablDiag0     -> https://oeis.org/A111
    Entringer_TablDiag1     -> https://oeis.org/A111
    Entringer_TablMax       -> https://oeis.org/A111
    Entringer_TablSum       -> https://oeis.org/A111
    Entringer_AbsSum        -> https://oeis.org/A111
    Entringer_AccRevSum     -> https://oeis.org/A111
    Entringer_TransNat1     -> https://oeis.org/A111
    Entringer_CentralE      -> https://oeis.org/A657
    Entringer_TablCol2      -> https://oeis.org/A1250
    Entringer_BinConv       -> https://oeis.org/A1586
    Entringer_PolyRow2      -> https://oeis.org/A2378
    Entringer_RevPolyRow3   -> https://oeis.org/A2522
    Entringer_RevColMiddle  -> https://oeis.org/A5437
    Entringer_TablDiag2     -> https://oeis.org/A6212
    Entringer_TablDiag3     -> https://oeis.org/A6213
    Entringer_TablCol3      -> https://oeis.org/A6216
    Entringer_Triangle      -> https://oeis.org/A8281
    Entringer_Talt          -> https://oeis.org/A8281
    Entringer_Toff11        -> https://oeis.org/A8282
    Entringer_RevTacc       -> https://oeis.org/A8282
    Entringer_Trev11        -> https://oeis.org/A10094
    Entringer_InvBinConv    -> https://oeis.org/A33999
    Entringer_AccSum        -> https://oeis.org/A34428
    Entringer_RevAccRevSum  -> https://oeis.org/A34428
    Entringer_RevTransNat1  -> https://oeis.org/A34428
    Entringer_PolyRow3      -> https://oeis.org/A48395
    Entringer_TablGcd       -> https://oeis.org/A174965
    Entringer_CentralO      -> https://oeis.org/A240561
    Entringer_RevTransNat0  -> https://oeis.org/A278678

    Entringer: Distinct: 23, Hits: 34, Misses: 31
'''
