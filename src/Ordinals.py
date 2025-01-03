from functools import cache
from _tabltypes import Table

"""von Neumann ordinals (kind of).

[0] [0]
[1] [0,  1]
[2] [0,  1,  2]
[3] [0,  1,  2,  3]
[4] [0,  1,  2,  3,  4]
[5] [0,  1,  2,  3,  4,  5]
[6] [0,  1,  2,  3,  4,  5,  6]
[7] [0,  1,  2,  3,  4,  5,  6,  7]
"""


@cache
def ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]
    return ordinals(n - 1) + [n]


Ordinals = Table(
    ordinals, 
    "Ordinals", 
    ["A002262", "A002260", "A004736", "A025581"], 
    "", 
    r"k"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Ordinals)


''' OEIS
    Ordinals_TablCol0      -> https://oeis.org/A7
    Ordinals_InvBinConv    -> https://oeis.org/A7
    Ordinals_TablCol1      -> https://oeis.org/A12
    Ordinals_TablGcd       -> https://oeis.org/A12
    Ordinals_RevPolyRow1   -> https://oeis.org/A12
    Ordinals_TablDiag0     -> https://oeis.org/A27
    Ordinals_TablDiag1     -> https://oeis.org/A27
    Ordinals_TablDiag2     -> https://oeis.org/A27
    Ordinals_TablDiag3     -> https://oeis.org/A27
    Ordinals_TablMax       -> https://oeis.org/A27
    Ordinals_CentralE      -> https://oeis.org/A27
    Ordinals_CentralO      -> https://oeis.org/A27
    Ordinals_PolyRow1      -> https://oeis.org/A27
    Ordinals_RevCentralO   -> https://oeis.org/A27
    Ordinals_RevPolyRow2   -> https://oeis.org/A27
    Ordinals_TablSum       -> https://oeis.org/A217
    Ordinals_AbsSum        -> https://oeis.org/A217
    Ordinals_AccSum        -> https://oeis.org/A292
    Ordinals_RevAccRevSum  -> https://oeis.org/A292
    Ordinals_RevTransNat0  -> https://oeis.org/A292
    Ordinals_RevTransNat1  -> https://oeis.org/A292
    Ordinals_PosHalf       -> https://oeis.org/A295
    Ordinals_TransNat0     -> https://oeis.org/A330
    Ordinals_RevPolyCol3   -> https://oeis.org/A340
    Ordinals_TransSqrs     -> https://oeis.org/A537
    Ordinals_BinConv       -> https://oeis.org/A1787
    Ordinals_Toff11        -> https://oeis.org/A2260
    Ordinals_Triangle      -> https://oeis.org/A2262
    Ordinals_Talt          -> https://oeis.org/A2262
    Ordinals_RevTrev11     -> https://oeis.org/A2262
    Ordinals_RevTransSqrs  -> https://oeis.org/A2415
    Ordinals_RevEvenSum    -> https://oeis.org/A2620
    Ordinals_RevOddSum     -> https://oeis.org/A2620
    Ordinals_RevAntiDSum   -> https://oeis.org/A2620
    Ordinals_TablLcm       -> https://oeis.org/A3418
    Ordinals_AltSum        -> https://oeis.org/A4526
    Ordinals_ColMiddle     -> https://oeis.org/A4526
    Ordinals_RevColMiddle  -> https://oeis.org/A4526
    Ordinals_Trev11        -> https://oeis.org/A4736
    Ordinals_AccRevSum     -> https://oeis.org/A7290
    Ordinals_TransNat1     -> https://oeis.org/A7290
    Ordinals_OddSum        -> https://oeis.org/A8794
    Ordinals_AntiDSum      -> https://oeis.org/A8805
    Ordinals_TablCol3      -> https://oeis.org/A10701
    Ordinals_PolyRow2      -> https://oeis.org/A14105
    Ordinals_Trev          -> https://oeis.org/A25581
    Ordinals_RevToff11     -> https://oeis.org/A25581
    Ordinals_RevTalt       -> https://oeis.org/A25581
    Ordinals_PolyCol2      -> https://oeis.org/A36799
    Ordinals_NegHalf       -> https://oeis.org/A53088
    Ordinals_Tantidiag     -> https://oeis.org/A55087
    Ordinals_TablCol2      -> https://oeis.org/A55642
    Ordinals_RevPolyRow3   -> https://oeis.org/A59100
    Ordinals_RevPolyDiag   -> https://oeis.org/A62805
    Ordinals_PolyDiag      -> https://oeis.org/A62806
    Ordinals_PolyRow3      -> https://oeis.org/A67389
    Ordinals_RevTantidiag  -> https://oeis.org/A82375
    Ordinals_RevTder       -> https://oeis.org/A94053
    Ordinals_EvenSum       -> https://oeis.org/A110660
    Ordinals_Tacc          -> https://oeis.org/A112367
    Ordinals_Tder          -> https://oeis.org/A133819
    Ordinals_RevNegHalf    -> https://oeis.org/A140960
    Ordinals_RevTacc       -> https://oeis.org/A141418
    Ordinals_Tinvrev11     -> https://oeis.org/A167194
    Ordinals_PolyCol3      -> https://oeis.org/A289399

    Ordinals: Distinct: 40, Hits: 65, Misses: 0
'''
