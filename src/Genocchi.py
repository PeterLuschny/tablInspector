from functools import cache
from _tabltypes import Table

"""Genocchi triangle.

[0] [     1]
[1] [     1,      1]
[2] [     2,      3,      3]
[3] [     8,     14,     17,     17]
[4] [    56,    104,    138,    155,    155]
[5] [   608,   1160,   1608,   1918,   2073,   2073]
[6] [  9440,  18272,  25944,  32008,  36154,  38227,  38227]
[7] [198272, 387104, 557664, 702280, 814888, 891342, 929569, 929569]
"""


@cache
def genocchi(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = [0] + genocchi(n - 1) + [0]

    for k in range(n, 0, -1):
        row[k] += row[k + 1]

    for k in range(2, n + 2):
        row[k] += row[k - 1]

    return row[1:]


Genocchi = Table(
    genocchi, 
    "Genocchi", 
    ["A297703"], 
    "", 
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Genocchi)


''' OEIS
    Genocchi_Trev          -> 0 
    Genocchi_Toff11        -> 0 
    Genocchi_Trev11        -> 0 
    Genocchi_Tantidiag     -> 0 
    Genocchi_Tacc          -> 0 
    Genocchi_Tder          -> 0 
    Genocchi_TablCol1      -> 0 
    Genocchi_TablCol2      -> 0 
    Genocchi_TablCol3      -> 0 
    Genocchi_TablDiag2     -> 0 
    Genocchi_TablDiag3     -> 0 
    Genocchi_TablLcm       -> 0 
    Genocchi_EvenSum       -> 0 
    Genocchi_OddSum        -> 0 
    Genocchi_AltSum        -> 0 
    Genocchi_AccSum        -> 0 
    Genocchi_AntiDSum      -> 0 
    Genocchi_ColMiddle     -> 0 
    Genocchi_CentralE      -> 0 
    Genocchi_CentralO      -> 0 
    Genocchi_PosHalf       -> 0 
    Genocchi_NegHalf       -> 0 
    Genocchi_TransNat0     -> 0 
    Genocchi_TransSqrs     -> 0 
    Genocchi_BinConv       -> 0 
    Genocchi_PolyRow3      -> 0 
    Genocchi_PolyCol2      -> 0 
    Genocchi_PolyCol3      -> 0 
    Genocchi_PolyDiag      -> 0 
    Genocchi_RevToff11     -> 0 
    Genocchi_RevTrev11     -> 0 
    Genocchi_RevTantidiag  -> 0 
    Genocchi_RevTacc       -> 0 
    Genocchi_RevTalt       -> 0 
    Genocchi_RevTder       -> 0 
    Genocchi_RevEvenSum    -> 0 
    Genocchi_RevOddSum     -> 0 
    Genocchi_RevAccRevSum  -> 0 
    Genocchi_RevAntiDSum   -> 0 
    Genocchi_RevColMiddle  -> 0 
    Genocchi_RevCentralO   -> 0 
    Genocchi_RevNegHalf    -> 0 
    Genocchi_RevTransNat0  -> 0 
    Genocchi_RevTransNat1  -> 0 
    Genocchi_RevTransSqrs  -> 0 
    Genocchi_RevPolyRow3   -> 0 
    Genocchi_RevPolyCol3   -> 0 
    Genocchi_RevPolyDiag   -> 0 
    Genocchi_TablGcd       -> https://oeis.org/A12
    Genocchi_PolyRow1      -> https://oeis.org/A27
    Genocchi_RevPolyRow1   -> https://oeis.org/A27
    Genocchi_TablCol0      -> https://oeis.org/A5439
    Genocchi_TablSum       -> https://oeis.org/A5439
    Genocchi_AbsSum        -> https://oeis.org/A5439
    Genocchi_RevPolyRow2   -> https://oeis.org/A33816
    Genocchi_InvBinConv    -> https://oeis.org/A36968
    Genocchi_PolyRow2      -> https://oeis.org/A77588
    Genocchi_TablDiag0     -> https://oeis.org/A110501
    Genocchi_TablDiag1     -> https://oeis.org/A110501
    Genocchi_TablMax       -> https://oeis.org/A110501
    Genocchi_AccRevSum     -> https://oeis.org/A110501
    Genocchi_TransNat1     -> https://oeis.org/A110501
    Genocchi_Triangle      -> https://oeis.org/A297703
    Genocchi_Talt          -> https://oeis.org/A297703

    Genocchi: Distinct: 9, Hits: 16, Misses: 48
'''
