from functools import cache
from _tabltypes import Table

"""Uno, the all 1's triangle.

[0]  1
[1]  1,  1
[2]  1,  1,  1
[3]  1,  1,  1,  1
[4]  1,  1,  1,  1,  1
[5]  1,  1,  1,  1,  1,  1
[6]  1,  1,  1,  1,  1,  1,  1
[7]  1,  1,  1,  1,  1,  1,  1,  1
[8]  1,  1,  1,  1,  1,  1,  1,  1,  1
"""


@cache
def one(n: int) -> list[int]:
    if n == 0:
        return [1]
    return one(n - 1) + [1]


One = Table(
    one, 
    "One", 
    ["A000012", "A008836", "A014077"], 
    "A167374",
    r"1"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(One)






''' OEIS
    One_Trevinv       -> 0 
    One_Trevinv11     -> 0 
    One_InvBinConv    -> https://oeis.org/A7
    One_Triangle      -> https://oeis.org/A12
    One_Trev          -> https://oeis.org/A12
    One_Toff11        -> https://oeis.org/A12
    One_Trev11        -> https://oeis.org/A12
    One_Tantidiag     -> https://oeis.org/A12
    One_Talt          -> https://oeis.org/A12
    One_TablCol0      -> https://oeis.org/A12
    One_TablCol1      -> https://oeis.org/A12
    One_TablCol2      -> https://oeis.org/A12
    One_TablCol3      -> https://oeis.org/A12
    One_TablDiag0     -> https://oeis.org/A12
    One_TablDiag1     -> https://oeis.org/A12
    One_TablDiag2     -> https://oeis.org/A12
    One_TablDiag3     -> https://oeis.org/A12
    One_TablLcm       -> https://oeis.org/A12
    One_TablGcd       -> https://oeis.org/A12
    One_TablMax       -> https://oeis.org/A12
    One_ColMiddle     -> https://oeis.org/A12
    One_CentralE      -> https://oeis.org/A12
    One_CentralO      -> https://oeis.org/A12
    One_RevToff11     -> https://oeis.org/A12
    One_RevTrev11     -> https://oeis.org/A12
    One_RevTantidiag  -> https://oeis.org/A12
    One_RevTalt       -> https://oeis.org/A12
    One_RevColMiddle  -> https://oeis.org/A12
    One_RevCentralO   -> https://oeis.org/A12
    One_TablSum       -> https://oeis.org/A27
    One_AbsSum        -> https://oeis.org/A27
    One_PolyRow1      -> https://oeis.org/A27
    One_RevPolyRow1   -> https://oeis.org/A27
    One_AltSum        -> https://oeis.org/A35
    One_BinConv       -> https://oeis.org/A79
    One_AccSum        -> https://oeis.org/A217
    One_AccRevSum     -> https://oeis.org/A217
    One_TransNat0     -> https://oeis.org/A217
    One_TransNat1     -> https://oeis.org/A217
    One_RevAccRevSum  -> https://oeis.org/A217
    One_RevTransNat0  -> https://oeis.org/A217
    One_RevTransNat1  -> https://oeis.org/A217
    One_PosHalf       -> https://oeis.org/A225
    One_PolyCol2      -> https://oeis.org/A225
    One_RevPosHalf    -> https://oeis.org/A225
    One_TransSqrs     -> https://oeis.org/A330
    One_RevTransSqrs  -> https://oeis.org/A330
    One_NegHalf       -> https://oeis.org/A1045
    One_RevNegHalf    -> https://oeis.org/A1045
    One_PolyRow2      -> https://oeis.org/A2061
    One_RevPolyRow2   -> https://oeis.org/A2061
    One_Tacc          -> https://oeis.org/A2260
    One_Tder          -> https://oeis.org/A2260
    One_RevTacc       -> https://oeis.org/A2260
    One_RevTder       -> https://oeis.org/A2260
    One_PolyCol3      -> https://oeis.org/A3462
    One_RevPolyCol3   -> https://oeis.org/A3462
    One_EvenSum       -> https://oeis.org/A4526
    One_OddSum        -> https://oeis.org/A4526
    One_AntiDSum      -> https://oeis.org/A4526
    One_RevEvenSum    -> https://oeis.org/A4526
    One_RevOddSum     -> https://oeis.org/A4526
    One_RevAntiDSum   -> https://oeis.org/A4526
    One_PolyDiag      -> https://oeis.org/A31973
    One_RevPolyDiag   -> https://oeis.org/A31973
    One_PolyRow3      -> https://oeis.org/A53698
    One_RevPolyRow3   -> https://oeis.org/A53698
    One_Tinv          -> https://oeis.org/A97806
    One_Tinvrev       -> https://oeis.org/A97806
    One_Tinv11        -> https://oeis.org/A97806
    One_Tinvrev11     -> https://oeis.org/A97806
    One_RevTinv11     -> https://oeis.org/A97806

    One: Distinct: 17, Hits: 70, Misses: 2
'''
