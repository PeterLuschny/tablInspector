from functools import cache
from _tabltypes import Table

"""
Inverse of Bessel, unsigned version.

[0]  [1]
[1]  [0, 1]
[2]  [0, 1, 1]
[3]  [0, 0, 3,  1]
[4]  [0, 0, 3,  6,   1]
[5]  [0, 0, 0, 15,  10,   1]
[6]  [0, 0, 0, 15,  45,  15,    1]
[7]  [0, 0, 0,  0, 105, 105,   21,   1]
[8]  [0, 0, 0,  0, 105, 420,  210,  28,  1]
[9]  [0, 0, 0,  0,   0, 945, 1260, 378, 36, 1]
"""

@cache
def besselinv(n: int) -> list[int]:
    if n == 0:
        return [1]

    b = besselinv(n - 1)
    return [0] + [(2*k - n + 1)*b[k] + 
            b[k-1] for k in range(1, n)] + [1]


BesselInv = Table(
    besselinv,    # the generating function
    "BesselInv",  # name of the table
    ["A122848", "A104556", "A096713"],  # similar sequences in OEIS
    "A132062",    # id of inverse sequence
    r"T(n,k)"     # TeX of defining formula
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(BesselInv)






''' OEIS
    BesselInv_Tantidiag     -> 0 
    BesselInv_Tacc          -> 0 
    BesselInv_Tder          -> 0 
    BesselInv_TablCol2      -> 0 
    BesselInv_TablCol3      -> 0 
    BesselInv_TablLcm       -> 0 
    BesselInv_TablMax       -> 0 
    BesselInv_OddSum        -> 0 
    BesselInv_AccSum        -> 0 
    BesselInv_TransSqrs     -> 0 
    BesselInv_BinConv       -> 0 
    BesselInv_InvBinConv    -> 0 
    BesselInv_PolyDiag      -> 0 
    BesselInv_RevToff11     -> 0 
    BesselInv_RevTrev11     -> 0 
    BesselInv_RevTantidiag  -> 0 
    BesselInv_RevTacc       -> 0 
    BesselInv_RevTder       -> 0 
    BesselInv_RevAccRevSum  -> 0 
    BesselInv_RevAntiDSum   -> 0 
    BesselInv_RevTransNat1  -> 0 
    BesselInv_CentralO      -> https://oeis.org/A4
    BesselInv_TablCol0      -> https://oeis.org/A7
    BesselInv_TablDiag0     -> https://oeis.org/A12
    BesselInv_RevPolyRow1   -> https://oeis.org/A12
    BesselInv_PolyRow1      -> https://oeis.org/A27
    BesselInv_RevPolyRow2   -> https://oeis.org/A27
    BesselInv_TablSum       -> https://oeis.org/A85
    BesselInv_AbsSum        -> https://oeis.org/A85
    BesselInv_TablDiag1     -> https://oeis.org/A217
    BesselInv_RevEvenSum    -> https://oeis.org/A704
    BesselInv_PolyCol2      -> https://oeis.org/A898
    BesselInv_RevPosHalf    -> https://oeis.org/A898
    BesselInv_CentralE      -> https://oeis.org/A1147
    BesselInv_RevCentralO   -> https://oeis.org/A1147
    BesselInv_AltSum        -> https://oeis.org/A1464
    BesselInv_RevOddSum     -> https://oeis.org/A1465
    BesselInv_AccRevSum     -> https://oeis.org/A1475
    BesselInv_TransNat1     -> https://oeis.org/A1475
    BesselInv_Tinv11        -> https://oeis.org/A1497
    BesselInv_Trevinv11     -> https://oeis.org/A1498
    BesselInv_PolyRow2      -> https://oeis.org/A2378
    BesselInv_RevPolyRow3   -> https://oeis.org/A16777
    BesselInv_TablCol1      -> https://oeis.org/A19590
    BesselInv_PosHalf       -> https://oeis.org/A47974
    BesselInv_Toff11        -> https://oeis.org/A49403
    BesselInv_TablDiag2     -> https://oeis.org/A50534
    BesselInv_RevNegHalf    -> https://oeis.org/A62267
    BesselInv_TablGcd       -> https://oeis.org/A69834
    BesselInv_EvenSum       -> https://oeis.org/A85386
    BesselInv_Trevinv       -> https://oeis.org/A104548
    BesselInv_Trev11        -> https://oeis.org/A111924
    BesselInv_RevPolyCol3   -> https://oeis.org/A115327
    BesselInv_Triangle      -> https://oeis.org/A122848
    BesselInv_Talt          -> https://oeis.org/A122848
    BesselInv_AntiDSum      -> https://oeis.org/A122849
    BesselInv_ColMiddle     -> https://oeis.org/A123023
    BesselInv_Tinv          -> https://oeis.org/A132062
    BesselInv_RevColMiddle  -> https://oeis.org/A133221
    BesselInv_Trev          -> https://oeis.org/A144299
    BesselInv_RevTalt       -> https://oeis.org/A144299
    BesselInv_RevTransNat0  -> https://oeis.org/A162970
    BesselInv_RevTransSqrs  -> https://oeis.org/A174764
    BesselInv_TransNat0     -> https://oeis.org/A189940
    BesselInv_TablDiag3     -> https://oeis.org/A240440
    BesselInv_RevPolyDiag   -> https://oeis.org/A277614
    BesselInv_NegHalf       -> https://oeis.org/A293604
    BesselInv_PolyCol3      -> https://oeis.org/A335819
    BesselInv_PolyRow3      -> https://oeis.org/A366151

    BesselInv: Distinct: 41, Hits: 48, Misses: 21
'''
