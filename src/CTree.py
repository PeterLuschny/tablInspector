from functools import cache
from _tabltypes import Table

"""Christmas tree, binomial(n mod 2, k mod 2).

[0]                           1
[1]                          1, 1
[2]                        1, 0, 1
[3]                       1, 1, 1, 1
[4]                     1, 0, 1, 0, 1
[5]                    1, 1, 1, 1, 1, 1
[6]                  1, 0, 1, 0, 1, 0, 1
[7]                 1, 1, 1, 1, 1, 1, 1, 1
[8]               1, 0, 1, 0, 1, 0, 1, 0, 1
[9]              1, 1, 1, 1, 1, 1, 1, 1, 1, 1
"""


@cache
def ctree(n: int) -> list[int]:
    if n % 2 == 1:
        return [1] * (n + 1)

    return [1, 0] * (n // 2) + [1]


CTree = Table(
    ctree, 
    "CTree", 
    ["A106465", "A106470"], 
    "A00000",
    r"is(n \text{ odd})\ ? \ 1 : (k + 1) \text{ mod } 2"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(CTree)


''' OEIS
    CTree_Tacc          -> 0 
    CTree_Tder          -> 0 
    CTree_PosHalf       -> 0 
    CTree_TransSqrs     -> 0 
    CTree_PolyCol2      -> 0 
    CTree_PolyCol3      -> 0 
    CTree_PolyDiag      -> 0 
    CTree_RevTacc       -> 0 
    CTree_RevTder       -> 0 
    CTree_RevTransSqrs  -> 0 
    CTree_RevPolyCol3   -> 0 
    CTree_RevPolyDiag   -> 0 
    CTree_Tinv11        -> https://oeis.org/A12
    CTree_TablCol0      -> https://oeis.org/A12
    CTree_TablCol2      -> https://oeis.org/A12
    CTree_TablDiag0     -> https://oeis.org/A12
    CTree_TablDiag2     -> https://oeis.org/A12
    CTree_TablLcm       -> https://oeis.org/A12
    CTree_TablGcd       -> https://oeis.org/A12
    CTree_TablMax       -> https://oeis.org/A12
    CTree_CentralO      -> https://oeis.org/A12
    CTree_RevTinv11     -> https://oeis.org/A12
    CTree_RevCentralO   -> https://oeis.org/A12
    CTree_PolyRow1      -> https://oeis.org/A27
    CTree_RevPolyRow1   -> https://oeis.org/A27
    CTree_TablCol1      -> https://oeis.org/A35
    CTree_TablCol3      -> https://oeis.org/A35
    CTree_TablDiag1     -> https://oeis.org/A35
    CTree_TablDiag3     -> https://oeis.org/A35
    CTree_CentralE      -> https://oeis.org/A35
    CTree_PolyRow2      -> https://oeis.org/A2522
    CTree_RevPolyRow2   -> https://oeis.org/A2522
    CTree_EvenSum       -> https://oeis.org/A4526
    CTree_RevEvenSum    -> https://oeis.org/A4526
    CTree_TablSum       -> https://oeis.org/A29578
    CTree_AbsSum        -> https://oeis.org/A29578
    CTree_NegHalf       -> https://oeis.org/A52992
    CTree_RevNegHalf    -> https://oeis.org/A52992
    CTree_PolyRow3      -> https://oeis.org/A53698
    CTree_RevPolyRow3   -> https://oeis.org/A53698
    CTree_TransNat0     -> https://oeis.org/A56136
    CTree_RevTransNat0  -> https://oeis.org/A56136
    CTree_InvBinConv    -> https://oeis.org/A103424
    CTree_Triangle      -> https://oeis.org/A106465
    CTree_Trev          -> https://oeis.org/A106465
    CTree_Talt          -> https://oeis.org/A106465
    CTree_RevTalt       -> https://oeis.org/A106465
    CTree_AntiDSum      -> https://oeis.org/A106466
    CTree_RevAntiDSum   -> https://oeis.org/A106466
    CTree_Tinv          -> https://oeis.org/A106468
    CTree_Tinvrev       -> https://oeis.org/A106468
    CTree_OddSum        -> https://oeis.org/A142150
    CTree_AltSum        -> https://oeis.org/A142150
    CTree_RevOddSum     -> https://oeis.org/A142150
    CTree_BinConv       -> https://oeis.org/A158302
    CTree_ColMiddle     -> https://oeis.org/A166486
    CTree_RevColMiddle  -> https://oeis.org/A166486
    CTree_Tantidiag     -> https://oeis.org/A336676
    CTree_RevTantidiag  -> https://oeis.org/A336676
    CTree_AccSum        -> https://oeis.org/A359366
    CTree_AccRevSum     -> https://oeis.org/A359366
    CTree_TransNat1     -> https://oeis.org/A359366
    CTree_RevAccRevSum  -> https://oeis.org/A359366
    CTree_RevTransNat1  -> https://oeis.org/A359366
    CTree_Toff11        -> https://oeis.org/A362448
    CTree_Trev11        -> https://oeis.org/A362448
    CTree_RevToff11     -> https://oeis.org/A362448
    CTree_RevTrev11     -> https://oeis.org/A362448

    CTree: Distinct: 20, Hits: 56, Misses: 12
'''
