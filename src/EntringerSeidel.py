from _tabltypes import Table
from Entringer import entringer

"""Seidel boustrophedon algorithm:

[0] [ 1]
[1] [ 0,  1]
[2] [ 1,  1,   0]
[3] [ 0,  1,   2,   2]
[4] [ 5,  5,   4,   2,   0]
[5] [ 0,  5,  10,  14,  16,  16]
[6] [61, 61,  56,  46,  32,  16,   0]
[7] [ 0, 61, 122, 178, 224, 256, 272, 272]
"""

# #@


def entringerseidel(n: int) -> list[int]:
    return entringer(n) if n % 2 else entringer(n)[::-1]


EntringerSeidel = Table(
    entringerseidel, 
    "EntringerSeidel", 
    ["A008280", "A108040", "A236935", "A239005"], 
    "", 
    r"see \text{Entringer} and \text{Seidel} algorithms"
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(EntringerSeidel)

''' OEIS
    EntringerSeidel_Toff11        -> 0 
    EntringerSeidel_Trev11        -> 0 
    EntringerSeidel_Tantidiag     -> 0 
    EntringerSeidel_Tacc          -> 0 
    EntringerSeidel_Tder          -> 0 
    EntringerSeidel_TablCol2      -> 0 
    EntringerSeidel_TablCol3      -> 0 
    EntringerSeidel_TablDiag1     -> 0 
    EntringerSeidel_TablDiag2     -> 0 
    EntringerSeidel_TablDiag3     -> 0 
    EntringerSeidel_TablLcm       -> 0 
    EntringerSeidel_EvenSum       -> 0 
    EntringerSeidel_OddSum        -> 0 
    EntringerSeidel_AltSum        -> 0 
    EntringerSeidel_AccSum        -> 0 
    EntringerSeidel_AccRevSum     -> 0 
    EntringerSeidel_AntiDSum      -> 0 
    EntringerSeidel_ColMiddle     -> 0 
    EntringerSeidel_PosHalf       -> 0 
    EntringerSeidel_NegHalf       -> 0 
    EntringerSeidel_TransNat0     -> 0 
    EntringerSeidel_TransNat1     -> 0 
    EntringerSeidel_TransSqrs     -> 0 
    EntringerSeidel_PolyCol2      -> 0 
    EntringerSeidel_PolyCol3      -> 0 
    EntringerSeidel_PolyDiag      -> 0 
    EntringerSeidel_RevToff11     -> 0 
    EntringerSeidel_RevTrev11     -> 0 
    EntringerSeidel_RevTantidiag  -> 0 
    EntringerSeidel_RevTacc       -> 0 
    EntringerSeidel_RevTder       -> 0 
    EntringerSeidel_RevEvenSum    -> 0 
    EntringerSeidel_RevOddSum     -> 0 
    EntringerSeidel_RevAccRevSum  -> 0 
    EntringerSeidel_RevAntiDSum   -> 0 
    EntringerSeidel_RevCentralO   -> 0 
    EntringerSeidel_RevPosHalf    -> 0 
    EntringerSeidel_RevNegHalf    -> 0 
    EntringerSeidel_RevTransNat0  -> 0 
    EntringerSeidel_RevTransNat1  -> 0 
    EntringerSeidel_RevTransSqrs  -> 0 
    EntringerSeidel_RevPolyCol3   -> 0 
    EntringerSeidel_RevPolyDiag   -> 0 
    EntringerSeidel_RevPolyRow1   -> https://oeis.org/A12
    EntringerSeidel_PolyRow1      -> https://oeis.org/A27
    EntringerSeidel_PolyRow2      -> https://oeis.org/A27
    EntringerSeidel_TablMax       -> https://oeis.org/A111
    EntringerSeidel_TablSum       -> https://oeis.org/A111
    EntringerSeidel_AbsSum        -> https://oeis.org/A111
    EntringerSeidel_CentralE      -> https://oeis.org/A657
    EntringerSeidel_BinConv       -> https://oeis.org/A1586
    EntringerSeidel_RevPolyRow2   -> https://oeis.org/A2378
    EntringerSeidel_RevPolyRow3   -> https://oeis.org/A2522
    EntringerSeidel_RevColMiddle  -> https://oeis.org/A5437
    EntringerSeidel_Triangle      -> https://oeis.org/A8280
    EntringerSeidel_Talt          -> https://oeis.org/A8280
    EntringerSeidel_TablDiag0     -> https://oeis.org/A9006
    EntringerSeidel_InvBinConv    -> https://oeis.org/A33999
    EntringerSeidel_PolyRow3      -> https://oeis.org/A48395
    EntringerSeidel_Trev          -> https://oeis.org/A108040
    EntringerSeidel_RevTalt       -> https://oeis.org/A108040
    EntringerSeidel_TablCol0      -> https://oeis.org/A122045
    EntringerSeidel_TablGcd       -> https://oeis.org/A174965
    EntringerSeidel_CentralO      -> https://oeis.org/A240561
    EntringerSeidel_TablCol1      -> https://oeis.org/A241209

    EntringerSeidel: Distinct: 18, Hits: 22, Misses: 43
'''
