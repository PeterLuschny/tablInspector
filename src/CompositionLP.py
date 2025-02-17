from functools import cache
from _tabltypes import Table

""" Compositions of n with largest part k.
Example: T(5, 3) = 5 because equals 
card({3+2, 2+3, 3+1+1, 1+3+1, 1+1+3}).

[0]  1;
[1]  0,  1;
[2]  0,  1,  1;
[3]  0,  1,  2,   1;
[4]  0,  1,  4,   2,   1;
[5]  0,  1,  7,   5,   2,  1;
[6]  0,  1, 12,  11,   5,  2,  1;
[7]  0,  1, 20,  23,  12,  5,  2,  1;
[8]  0,  1, 33,  47,  27, 12,  5,  2, 1;
[9]  0,  1, 54,  94,  59, 28, 12,  5, 2, 1;
"""


@cache
def _clp(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1 

    return (
        2 * _clp(n - 1, k)
        + _clp(n - 1, k - 1)
        - 2 * _clp(n - 2, k - 1)
        + _clp(n - k - 1, k - 1)
        - _clp(n - k - 2, k)
    )


@cache
def compositionlp(n: int) -> list[int]:
    if n == 0:
        return [1]

    return [_clp(n - 1, k - 1) for k in range(n + 1)]


CompositionLP = Table(
    compositionlp, 
    "CompositionLP", 
    ["A048004"], 
    "A000000",  # invertible, not in OEIS
    r"C_{LP}(n, k)"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(CompositionLP)




''' OEIS
    CompositionLP_Triangle      -> 0 
    CompositionLP_Tinv          -> 0 
    CompositionLP_Trev          -> 0 
    CompositionLP_Trevinv       -> 0 
    CompositionLP_Tinv11        -> 0 
    CompositionLP_Tinvrev11     -> 0 
    CompositionLP_Trevinv11     -> 0 
    CompositionLP_Tantidiag     -> 0 
    CompositionLP_Tacc          -> 0 
    CompositionLP_Talt          -> 0 
    CompositionLP_Tder          -> 0 
    CompositionLP_TablLcm       -> 0 
    CompositionLP_TablMax       -> 0 
    CompositionLP_AltSum        -> 0 
    CompositionLP_AccRevSum     -> 0 
    CompositionLP_ColMiddle     -> 0 
    CompositionLP_CentralO      -> 0 
    CompositionLP_PosHalf       -> 0 
    CompositionLP_NegHalf       -> 0 
    CompositionLP_TransNat1     -> 0 
    CompositionLP_TransSqrs     -> 0 
    CompositionLP_BinConv       -> 0 
    CompositionLP_InvBinConv    -> 0 
    CompositionLP_PolyCol2      -> 0 
    CompositionLP_PolyCol3      -> 0 
    CompositionLP_PolyDiag      -> 0 
    CompositionLP_RevToff11     -> 0 
    CompositionLP_RevTrev11     -> 0 
    CompositionLP_RevTantidiag  -> 0 
    CompositionLP_RevTacc       -> 0 
    CompositionLP_RevTalt       -> 0 
    CompositionLP_RevTder       -> 0 
    CompositionLP_RevEvenSum    -> 0 
    CompositionLP_RevOddSum     -> 0 
    CompositionLP_RevAntiDSum   -> 0 
    CompositionLP_RevColMiddle  -> 0 
    CompositionLP_RevPosHalf    -> 0 
    CompositionLP_RevNegHalf    -> 0 
    CompositionLP_RevTransNat0  -> 0 
    CompositionLP_RevTransSqrs  -> 0 
    CompositionLP_RevPolyCol3   -> 0 
    CompositionLP_RevPolyDiag   -> 0 
    CompositionLP_TablCol0      -> https://oeis.org/A7
    CompositionLP_TablCol1      -> https://oeis.org/A12
    CompositionLP_TablDiag0     -> https://oeis.org/A12
    CompositionLP_RevPolyRow1   -> https://oeis.org/A12
    CompositionLP_PolyRow1      -> https://oeis.org/A27
    CompositionLP_RevPolyRow2   -> https://oeis.org/A27
    CompositionLP_TablCol2      -> https://oeis.org/A71
    CompositionLP_TablSum       -> https://oeis.org/A79
    CompositionLP_AbsSum        -> https://oeis.org/A79
    CompositionLP_TablCol3      -> https://oeis.org/A100
    CompositionLP_RevPolyRow3   -> https://oeis.org/A290
    CompositionLP_TablDiag2     -> https://oeis.org/A523
    CompositionLP_PolyRow2      -> https://oeis.org/A2378
    CompositionLP_TablDiag3     -> https://oeis.org/A7600
    CompositionLP_TablGcd       -> https://oeis.org/A33420
    CompositionLP_AccSum        -> https://oeis.org/A39671
    CompositionLP_RevAccRevSum  -> https://oeis.org/A39671
    CompositionLP_RevTransNat1  -> https://oeis.org/A39671
    CompositionLP_RevCentralO   -> https://oeis.org/A45623
    CompositionLP_PolyRow3      -> https://oeis.org/A45991
    CompositionLP_CentralE      -> https://oeis.org/A47859
    CompositionLP_Toff11        -> https://oeis.org/A48004
    CompositionLP_TablDiag1     -> https://oeis.org/A55642
    CompositionLP_TransNat0     -> https://oeis.org/A102712
    CompositionLP_OddSum        -> https://oeis.org/A103421
    CompositionLP_EvenSum       -> https://oeis.org/A103422
    CompositionLP_Trev11        -> https://oeis.org/A140993
    CompositionLP_AntiDSum      -> https://oeis.org/A368279

    CompositionLP: Distinct: 23, Hits: 28, Misses: 42
'''
