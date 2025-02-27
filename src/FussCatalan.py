from functools import cache
from itertools import accumulate
from _tabltypes import Table

"""Fuss-Catalan triangle.

[0] [1]
[1] [0, 1]
[2] [0, 1, 2]
[3] [0, 1, 3,  5]
[4] [0, 1, 4,  9, 14]
[5] [0, 1, 5, 14, 28,  42]
[6] [0, 1, 6, 20, 48,  90, 132]
[7] [0, 1, 7, 27, 75, 165, 297, 429]
"""


@cache
def fusscatalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = fusscatalan(n - 1) + [fusscatalan(n - 1)[n - 1]]
    return list(accumulate(row))


FussCatalan = Table(
    fusscatalan,
    "FussCatalan",
    ["A355173", "A030237", "A054445"],
    "",
    r"is(k=0) \, ? \, 0^n : \frac{(n - k + 2) (n + k - 1)!}{(n + 1)! \, (k - 1)!}",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(FussCatalan)






''' OEIS
    FussCatalan_Trev          -> 0 
    FussCatalan_Tinvrev11     -> 0 
    FussCatalan_Tacc          -> 0 
    FussCatalan_Tder          -> 0 
    FussCatalan_TablLcm       -> 0 
    FussCatalan_EvenSum       -> 0 
    FussCatalan_OddSum        -> 0 
    FussCatalan_AccRevSum     -> 0 
    FussCatalan_ColMiddle     -> 0 
    FussCatalan_CentralO      -> 0 
    FussCatalan_NegHalf       -> 0 
    FussCatalan_TransNat0     -> 0 
    FussCatalan_TransNat1     -> 0 
    FussCatalan_TransSqrs     -> 0 
    FussCatalan_BinConv       -> 0 
    FussCatalan_PolyRow3      -> 0 
    FussCatalan_PolyCol2      -> 0 
    FussCatalan_PolyCol3      -> 0 
    FussCatalan_PolyDiag      -> 0 
    FussCatalan_RevToff11     -> 0 
    FussCatalan_RevTrev11     -> 0 
    FussCatalan_RevTantidiag  -> 0 
    FussCatalan_RevTacc       -> 0 
    FussCatalan_RevTalt       -> 0 
    FussCatalan_RevTder       -> 0 
    FussCatalan_RevAntiDSum   -> 0 
    FussCatalan_RevColMiddle  -> 0 
    FussCatalan_RevPosHalf    -> 0 
    FussCatalan_RevNegHalf    -> 0 
    FussCatalan_RevTransSqrs  -> 0 
    FussCatalan_RevPolyCol3   -> 0 
    FussCatalan_RevPolyDiag   -> 0 
    FussCatalan_TablCol0      -> https://oeis.org/A7
    FussCatalan_TablCol1      -> https://oeis.org/A12
    FussCatalan_RevPolyRow1   -> https://oeis.org/A12
    FussCatalan_TablCol2      -> https://oeis.org/A27
    FussCatalan_InvBinConv    -> https://oeis.org/A27
    FussCatalan_PolyRow1      -> https://oeis.org/A27
    FussCatalan_RevPolyRow2   -> https://oeis.org/A27
    FussCatalan_TablCol3      -> https://oeis.org/A96
    FussCatalan_TablDiag0     -> https://oeis.org/A108
    FussCatalan_TablMax       -> https://oeis.org/A108
    FussCatalan_TablDiag1     -> https://oeis.org/A245
    FussCatalan_TablSum       -> https://oeis.org/A245
    FussCatalan_AbsSum        -> https://oeis.org/A245
    FussCatalan_TablDiag3     -> https://oeis.org/A344
    FussCatalan_RevTransNat0  -> https://oeis.org/A344
    FussCatalan_RevEvenSum    -> https://oeis.org/A957
    FussCatalan_AltSum        -> https://oeis.org/A958
    FussCatalan_RevOddSum     -> https://oeis.org/A1558
    FussCatalan_PosHalf       -> https://oeis.org/A1791
    FussCatalan_TablDiag2     -> https://oeis.org/A2057
    FussCatalan_AccSum        -> https://oeis.org/A2057
    FussCatalan_RevAccRevSum  -> https://oeis.org/A2057
    FussCatalan_RevTransNat1  -> https://oeis.org/A2057
    FussCatalan_PolyRow2      -> https://oeis.org/A14105
    FussCatalan_RevCentralO   -> https://oeis.org/A26004
    FussCatalan_RevPolyRow3   -> https://oeis.org/A27688
    FussCatalan_Toff11        -> https://oeis.org/A30237
    FussCatalan_AntiDSum      -> https://oeis.org/A37952
    FussCatalan_Trev11        -> https://oeis.org/A54445
    FussCatalan_TablGcd       -> https://oeis.org/A55229
    FussCatalan_CentralE      -> https://oeis.org/A262394
    FussCatalan_Tantidiag     -> https://oeis.org/A289871
    FussCatalan_Triangle      -> https://oeis.org/A355173
    FussCatalan_Talt          -> https://oeis.org/A355173

    FussCatalan: Distinct: 23, Hits: 34, Misses: 32
'''
