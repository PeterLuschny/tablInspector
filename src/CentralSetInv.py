from functools import cache
from _tabltypes import Table

"""Inverse triangle of the central set factorial numbers.

[0] [1]
[1] [0,      1]
[2] [0,      1,      1]
[3] [0,      4,      5,      1]
[4] [0,     36,     49,     14,     1]
[5] [0,    576,    820,    273,    30,    1]
[6] [0,  14400,  21076,   7645,  1023,   55,  1]
[7] [0, 518400, 773136, 296296, 44473, 3003, 91, 1]
"""

@cache
def centralsetinv(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = centralsetinv(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (n - 1)**2 * row[k] + row[k - 1]
    return row

 
CentralSetInv = Table(
    centralsetinv,
    "CentralSetInv",
    ["A269944", "A204579"],
    "A269945",
    r"%%",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(CentralSetInv)






''' OEIS
    CentralSetInv_Trev          -> 0 
    CentralSetInv_Trevinv       -> 0 
    CentralSetInv_Tantidiag     -> 0 
    CentralSetInv_Tacc          -> 0 
    CentralSetInv_Tder          -> 0 
    CentralSetInv_TablLcm       -> 0 
    CentralSetInv_AccSum        -> 0 
    CentralSetInv_AccRevSum     -> 0 
    CentralSetInv_AntiDSum      -> 0 
    CentralSetInv_ColMiddle     -> 0 
    CentralSetInv_CentralE      -> 0 
    CentralSetInv_CentralO      -> 0 
    CentralSetInv_NegHalf       -> 0 
    CentralSetInv_TransNat0     -> 0 
    CentralSetInv_TransNat1     -> 0 
    CentralSetInv_TransSqrs     -> 0 
    CentralSetInv_BinConv       -> 0 
    CentralSetInv_InvBinConv    -> 0 
    CentralSetInv_PolyRow3      -> 0 
    CentralSetInv_PolyCol2      -> 0 
    CentralSetInv_PolyCol3      -> 0 
    CentralSetInv_PolyDiag      -> 0 
    CentralSetInv_RevToff11     -> 0 
    CentralSetInv_RevTrev11     -> 0 
    CentralSetInv_RevTantidiag  -> 0 
    CentralSetInv_RevTacc       -> 0 
    CentralSetInv_RevTalt       -> 0 
    CentralSetInv_RevTder       -> 0 
    CentralSetInv_RevAccRevSum  -> 0 
    CentralSetInv_RevAntiDSum   -> 0 
    CentralSetInv_RevColMiddle  -> 0 
    CentralSetInv_RevPosHalf    -> 0 
    CentralSetInv_RevNegHalf    -> 0 
    CentralSetInv_RevTransNat0  -> 0 
    CentralSetInv_RevTransNat1  -> 0 
    CentralSetInv_RevTransSqrs  -> 0 
    CentralSetInv_RevPolyDiag   -> 0 
    CentralSetInv_TablCol0      -> https://oeis.org/A7
    CentralSetInv_TablDiag0     -> https://oeis.org/A12
    CentralSetInv_TablGcd       -> https://oeis.org/A12
    CentralSetInv_RevPolyRow1   -> https://oeis.org/A12
    CentralSetInv_PolyRow1      -> https://oeis.org/A27
    CentralSetInv_RevPolyRow2   -> https://oeis.org/A27
    CentralSetInv_TablDiag1     -> https://oeis.org/A330
    CentralSetInv_TablDiag2     -> https://oeis.org/A596
    CentralSetInv_TablDiag3     -> https://oeis.org/A597
    CentralSetInv_TablCol1      -> https://oeis.org/A1044
    CentralSetInv_RevPolyRow3   -> https://oeis.org/A1107
    CentralSetInv_TablCol2      -> https://oeis.org/A1819
    CentralSetInv_TablMax       -> https://oeis.org/A1819
    CentralSetInv_TablCol3      -> https://oeis.org/A1820
    CentralSetInv_PolyRow2      -> https://oeis.org/A2378
    CentralSetInv_Trev11        -> https://oeis.org/A8955
    CentralSetInv_Trevinv11     -> https://oeis.org/A8957
    CentralSetInv_Tinv11        -> https://oeis.org/A36969
    CentralSetInv_EvenSum       -> https://oeis.org/A51893
    CentralSetInv_OddSum        -> https://oeis.org/A51893
    CentralSetInv_RevEvenSum    -> https://oeis.org/A51893
    CentralSetInv_RevOddSum     -> https://oeis.org/A51893
    CentralSetInv_TablSum       -> https://oeis.org/A101686
    CentralSetInv_AbsSum        -> https://oeis.org/A101686
    CentralSetInv_AltSum        -> https://oeis.org/A154955
    CentralSetInv_Toff11        -> https://oeis.org/A204579
    CentralSetInv_RevCentralO   -> https://oeis.org/A234324
    CentralSetInv_Triangle      -> https://oeis.org/A269944
    CentralSetInv_Talt          -> https://oeis.org/A269944
    CentralSetInv_Tinv          -> https://oeis.org/A269945
    CentralSetInv_PosHalf       -> https://oeis.org/A277352
    CentralSetInv_RevPolyCol3   -> https://oeis.org/A277353

    CentralSetInv: Distinct: 24, Hits: 32, Misses: 37
'''
