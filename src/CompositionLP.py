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
    Composition_Triangle      -> 0 
    Composition_Tinv          -> 0 
    Composition_Trev          -> 0 
    Composition_Tinv11        -> 0 
    Composition_Tinvrev11     -> 0 
    Composition_Tantidiag     -> 0 
    Composition_Tacc          -> 0 
    Composition_Talt          -> 0 
    Composition_Tder          -> 0 
    Composition_TablLcm       -> 0 
    Composition_TablMax       -> 0 
    Composition_AltSum        -> 0 
    Composition_AccRevSum     -> 0 
    Composition_ColMiddle     -> 0 
    Composition_CentralO      -> 0 
    Composition_PosHalf       -> 0 
    Composition_NegHalf       -> 0 
    Composition_TransNat1     -> 0 
    Composition_TransSqrs     -> 0 
    Composition_BinConv       -> 0 
    Composition_InvBinConv    -> 0 
    Composition_PolyCol2      -> 0 
    Composition_PolyCol3      -> 0 
    Composition_PolyDiag      -> 0 
    Composition_RevToff11     -> 0 
    Composition_RevTrev11     -> 0 
    Composition_RevTantidiag  -> 0 
    Composition_RevTacc       -> 0 
    Composition_RevTalt       -> 0 
    Composition_RevTder       -> 0 
    Composition_RevEvenSum    -> 0 
    Composition_RevOddSum     -> 0 
    Composition_RevAntiDSum   -> 0 
    Composition_RevColMiddle  -> 0 
    Composition_RevNegHalf    -> 0 
    Composition_RevTransNat0  -> 0 
    Composition_RevTransSqrs  -> 0 
    Composition_RevPolyCol3   -> 0 
    Composition_RevPolyDiag   -> 0 
    Composition_TablCol0      -> https://oeis.org/A7
    Composition_TablCol1      -> https://oeis.org/A12
    Composition_TablDiag0     -> https://oeis.org/A12
    Composition_RevPolyRow1   -> https://oeis.org/A12
    Composition_PolyRow1      -> https://oeis.org/A27
    Composition_RevPolyRow2   -> https://oeis.org/A27
    Composition_TablCol2      -> https://oeis.org/A71
    Composition_TablSum       -> https://oeis.org/A79
    Composition_AbsSum        -> https://oeis.org/A79
    Composition_TablCol3      -> https://oeis.org/A100
    Composition_RevPolyRow3   -> https://oeis.org/A290
    Composition_TablDiag2     -> https://oeis.org/A523
    Composition_PolyRow2      -> https://oeis.org/A2378
    Composition_TablDiag3     -> https://oeis.org/A7600
    Composition_TablGcd       -> https://oeis.org/A33420
    Composition_AccSum        -> https://oeis.org/A39671
    Composition_RevAccRevSum  -> https://oeis.org/A39671
    Composition_RevTransNat1  -> https://oeis.org/A39671
    Composition_RevCentralO   -> https://oeis.org/A45623
    Composition_PolyRow3      -> https://oeis.org/A45991
    Composition_CentralE      -> https://oeis.org/A47859
    Composition_Toff11        -> https://oeis.org/A48004
    Composition_TablDiag1     -> https://oeis.org/A55642
    Composition_TransNat0     -> https://oeis.org/A102712
    Composition_OddSum        -> https://oeis.org/A103421
    Composition_EvenSum       -> https://oeis.org/A103422
    Composition_Trev11        -> https://oeis.org/A140993
    Composition_AntiDSum      -> https://oeis.org/A368279

    Composition: Distinct: 23, Hits: 28, Misses: 39
'''
