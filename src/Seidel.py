from _tabltypes import Table
from Entringer import entringer


"""Seidel boustrophedon:

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


def seidel(n: int) -> list[int]:
    return entringer(n) if n % 2 else entringer(n)[::-1]


Seidel = Table(
    seidel, 
    "Seidel", 
    ["A008280", "A108040", "A236935", "A239005"], 
    "", 
    r""
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Seidel)






''' OEIS
    Seidel_Toff11        -> 0 
    Seidel_Trev11        -> 0 
    Seidel_Tantidiag     -> 0 
    Seidel_Tacc          -> 0 
    Seidel_Tder          -> 0 
    Seidel_TablCol2      -> 0 
    Seidel_TablCol3      -> 0 
    Seidel_TablDiag1     -> 0 
    Seidel_TablDiag2     -> 0 
    Seidel_TablDiag3     -> 0 
    Seidel_TablLcm       -> 0 
    Seidel_EvenSum       -> 0 
    Seidel_OddSum        -> 0 
    Seidel_AltSum        -> 0 
    Seidel_AccSum        -> 0 
    Seidel_AccRevSum     -> 0 
    Seidel_AntiDSum      -> 0 
    Seidel_ColMiddle     -> 0 
    Seidel_PosHalf       -> 0 
    Seidel_NegHalf       -> 0 
    Seidel_TransNat0     -> 0 
    Seidel_TransNat1     -> 0 
    Seidel_TransSqrs     -> 0 
    Seidel_PolyCol2      -> 0 
    Seidel_PolyCol3      -> 0 
    Seidel_PolyDiag      -> 0 
    Seidel_RevToff11     -> 0 
    Seidel_RevTrev11     -> 0 
    Seidel_RevTantidiag  -> 0 
    Seidel_RevTacc       -> 0 
    Seidel_RevTder       -> 0 
    Seidel_RevEvenSum    -> 0 
    Seidel_RevOddSum     -> 0 
    Seidel_RevAccRevSum  -> 0 
    Seidel_RevAntiDSum   -> 0 
    Seidel_RevCentralO   -> 0 
    Seidel_RevPosHalf    -> 0 
    Seidel_RevNegHalf    -> 0 
    Seidel_RevTransNat0  -> 0 
    Seidel_RevTransNat1  -> 0 
    Seidel_RevTransSqrs  -> 0 
    Seidel_RevPolyCol3   -> 0 
    Seidel_RevPolyDiag   -> 0 
    Seidel_RevPolyRow1   -> https://oeis.org/A12
    Seidel_PolyRow1      -> https://oeis.org/A27
    Seidel_PolyRow2      -> https://oeis.org/A27
    Seidel_TablMax       -> https://oeis.org/A111
    Seidel_TablSum       -> https://oeis.org/A111
    Seidel_AbsSum        -> https://oeis.org/A111
    Seidel_CentralE      -> https://oeis.org/A657
    Seidel_BinConv       -> https://oeis.org/A1586
    Seidel_RevPolyRow2   -> https://oeis.org/A2378
    Seidel_RevPolyRow3   -> https://oeis.org/A2522
    Seidel_RevColMiddle  -> https://oeis.org/A5437
    Seidel_Triangle      -> https://oeis.org/A8280
    Seidel_Talt          -> https://oeis.org/A8280
    Seidel_TablDiag0     -> https://oeis.org/A9006
    Seidel_InvBinConv    -> https://oeis.org/A33999
    Seidel_PolyRow3      -> https://oeis.org/A48395
    Seidel_Trev          -> https://oeis.org/A108040
    Seidel_RevTalt       -> https://oeis.org/A108040
    Seidel_TablCol0      -> https://oeis.org/A122045
    Seidel_TablGcd       -> https://oeis.org/A174965
    Seidel_CentralO      -> https://oeis.org/A240561
    Seidel_TablCol1      -> https://oeis.org/A241209

    Seidel: Distinct: 18, Hits: 22, Misses: 43
'''
