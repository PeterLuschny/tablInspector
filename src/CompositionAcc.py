from functools import cache
from itertools import accumulate
from _tabltypes import Table
from CompositionLP import compositionlp

"""Compositions of n into parts of size <= k.

[0] 1;
[1] 0, 1;
[2] 0, 1,  2;
[3] 0, 1,  3,   4;
[4] 0, 1,  5,   7,   8;
[5] 0, 1,  8,  13,  15,  16;
[6] 0, 1, 13,  24,  29,  31,  32;
[7] 0, 1, 21,  44,  56,  61,  63,  64;
[8] 0, 1, 34,  81, 108, 120, 125, 127, 128;
[9] 0, 1, 55, 149, 208, 236, 248, 253, 255, 256;
"""


@cache
def compoacc(n: int) -> list[int]:
    return list(accumulate(compositionlp(n)))


CompoAcc = Table(
    compoacc, 
    "CompositionAcc", 
    ["A126198"], 
    "",  # not integer-invertible
    r"\sum_{j=0}^k C_{LP}(n, j)"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(CompoAcc)




''' OEIS
    CompositionAcc_Tinvrev11     -> https://oeis.org/A-999999
    CompositionAcc_Triangle      -> 0 
    CompositionAcc_Trev          -> 0 
    CompositionAcc_Trev11        -> 0 
    CompositionAcc_Tantidiag     -> 0 
    CompositionAcc_Tacc          -> 0 
    CompositionAcc_Talt          -> 0 
    CompositionAcc_Tder          -> 0 
    CompositionAcc_TablLcm       -> 0 
    CompositionAcc_EvenSum       -> 0 
    CompositionAcc_OddSum        -> 0 
    CompositionAcc_AltSum        -> 0 
    CompositionAcc_AccSum        -> 0 
    CompositionAcc_AccRevSum     -> 0 
    CompositionAcc_AntiDSum      -> 0 
    CompositionAcc_PosHalf       -> 0 
    CompositionAcc_NegHalf       -> 0 
    CompositionAcc_TransNat0     -> 0 
    CompositionAcc_TransNat1     -> 0 
    CompositionAcc_TransSqrs     -> 0 
    CompositionAcc_BinConv       -> 0 
    CompositionAcc_InvBinConv    -> 0 
    CompositionAcc_PolyRow3      -> 0 
    CompositionAcc_PolyCol2      -> 0 
    CompositionAcc_PolyCol3      -> 0 
    CompositionAcc_PolyDiag      -> 0 
    CompositionAcc_RevToff11     -> 0 
    CompositionAcc_RevTrev11     -> 0 
    CompositionAcc_RevTantidiag  -> 0 
    CompositionAcc_RevTacc       -> 0 
    CompositionAcc_RevTalt       -> 0 
    CompositionAcc_RevTder       -> 0 
    CompositionAcc_RevEvenSum    -> 0 
    CompositionAcc_RevOddSum     -> 0 
    CompositionAcc_RevAccRevSum  -> 0 
    CompositionAcc_RevAntiDSum   -> 0 
    CompositionAcc_RevCentralO   -> 0 
    CompositionAcc_RevPosHalf    -> 0 
    CompositionAcc_RevNegHalf    -> 0 
    CompositionAcc_RevTransNat0  -> 0 
    CompositionAcc_RevTransNat1  -> 0 
    CompositionAcc_RevTransSqrs  -> 0 
    CompositionAcc_RevPolyCol3   -> 0 
    CompositionAcc_RevPolyDiag   -> 0 
    CompositionAcc_TablCol0      -> https://oeis.org/A7
    CompositionAcc_TablCol1      -> https://oeis.org/A12
    CompositionAcc_TablGcd       -> https://oeis.org/A12
    CompositionAcc_RevPolyRow1   -> https://oeis.org/A12
    CompositionAcc_PolyRow1      -> https://oeis.org/A27
    CompositionAcc_RevPolyRow2   -> https://oeis.org/A27
    CompositionAcc_TablCol2      -> https://oeis.org/A45
    CompositionAcc_TablCol3      -> https://oeis.org/A73
    CompositionAcc_TablDiag0     -> https://oeis.org/A79
    CompositionAcc_TablMax       -> https://oeis.org/A79
    CompositionAcc_TablDiag1     -> https://oeis.org/A225
    CompositionAcc_CentralE      -> https://oeis.org/A8464
    CompositionAcc_PolyRow2      -> https://oeis.org/A14105
    CompositionAcc_RevPolyRow3   -> https://oeis.org/A14206
    CompositionAcc_TablDiag2     -> https://oeis.org/A36563
    CompositionAcc_TablSum       -> https://oeis.org/A39671
    CompositionAcc_AbsSum        -> https://oeis.org/A39671
    CompositionAcc_CentralO      -> https://oeis.org/A100575
    CompositionAcc_Toff11        -> https://oeis.org/A126198
    CompositionAcc_TablDiag3     -> https://oeis.org/A159741
    CompositionAcc_RevColMiddle  -> https://oeis.org/A336103
    CompositionAcc_ColMiddle     -> https://oeis.org/A368484

    CompositionAcc: Distinct: 19, Hits: 23, Misses: 43
'''
