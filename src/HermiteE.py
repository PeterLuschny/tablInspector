from functools import cache
from _tabltypes import Table

"""(Probabilist's) Hermite polynomials He, unsigned coefficients.

[0] [ 1]
[1] [ 0,   1]
[2] [ 1,   0,  1]
[3] [ 0,   3,  0,   1]
[4] [ 3,   0,  6,   0,  1]
[5] [ 0,  15,  0,  10,  0,  1]
[6] [15,   0, 45,   0, 15,  0, 1]
[7] [ 0, 105,  0, 105,  0, 21, 0, 1]
"""


@cache
def hermitee(n: int) -> list[int]:
    row = [0] * (n + 1)
    row[n] = 1
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (n - k)
    return row


HermiteE = Table(
    hermitee,
    "HermiteE",
    ["A099174", "A066325", "A073278"],
    "A000000",
    r"is(n - k \text{ odd})\, ? \, 0 : \frac{n!}{k!} \, \frac{1}{(n-k)!!} )",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(HermiteE)




''' OEIS
    HermiteE_TablDiag1     -> https://oeis.org/A-999999
    HermiteE_TablDiag3     -> https://oeis.org/A-999999
    HermiteE_RevOddSum     -> https://oeis.org/A-999999
    HermiteE_Toff11        -> 0 
    HermiteE_Trev11        -> 0 
    HermiteE_Tinv11        -> 0 
    HermiteE_Trevinv11     -> 0 
    HermiteE_Tantidiag     -> 0 
    HermiteE_Tacc          -> 0 
    HermiteE_Tder          -> 0 
    HermiteE_TablLcm       -> 0 
    HermiteE_TablMax       -> 0 
    HermiteE_AccSum        -> 0 
    HermiteE_ColMiddle     -> 0 
    HermiteE_CentralO      -> 0 
    HermiteE_TransSqrs     -> 0 
    HermiteE_PolyDiag      -> 0 
    HermiteE_RevToff11     -> 0 
    HermiteE_RevTrev11     -> 0 
    HermiteE_RevTantidiag  -> 0 
    HermiteE_RevTacc       -> 0 
    HermiteE_RevTder       -> 0 
    HermiteE_RevAccRevSum  -> 0 
    HermiteE_RevAntiDSum   -> 0 
    HermiteE_RevColMiddle  -> 0 
    HermiteE_RevCentralO   -> 0 
    HermiteE_RevTransNat0  -> 0 
    HermiteE_RevTransNat1  -> 0 
    HermiteE_RevTransSqrs  -> 0 
    HermiteE_RevPolyCol3   -> 0 
    HermiteE_TablDiag0     -> https://oeis.org/A12
    HermiteE_RevPolyRow1   -> https://oeis.org/A12
    HermiteE_PolyRow1      -> https://oeis.org/A27
    HermiteE_TablSum       -> https://oeis.org/A85
    HermiteE_AltSum        -> https://oeis.org/A85
    HermiteE_AbsSum        -> https://oeis.org/A85
    HermiteE_AccRevSum     -> https://oeis.org/A85
    HermiteE_TransNat1     -> https://oeis.org/A85
    HermiteE_RevEvenSum    -> https://oeis.org/A85
    HermiteE_TablDiag2     -> https://oeis.org/A217
    HermiteE_TablCol3      -> https://oeis.org/A457
    HermiteE_AntiDSum      -> https://oeis.org/A1515
    HermiteE_TablCol2      -> https://oeis.org/A1879
    HermiteE_PolyRow2      -> https://oeis.org/A2522
    HermiteE_RevPolyRow2   -> https://oeis.org/A2522
    HermiteE_PolyCol2      -> https://oeis.org/A5425
    HermiteE_RevPosHalf    -> https://oeis.org/A5425
    HermiteE_RevNegHalf    -> https://oeis.org/A5425
    HermiteE_TransNat0     -> https://oeis.org/A13989
    HermiteE_RevPolyRow3   -> https://oeis.org/A56107
    HermiteE_EvenSum       -> https://oeis.org/A66223
    HermiteE_OddSum        -> https://oeis.org/A66224
    HermiteE_TablGcd       -> https://oeis.org/A69834
    HermiteE_PolyRow3      -> https://oeis.org/A79908
    HermiteE_Triangle      -> https://oeis.org/A99174
    HermiteE_Tinv          -> https://oeis.org/A99174
    HermiteE_Talt          -> https://oeis.org/A99174
    HermiteE_PosHalf       -> https://oeis.org/A115329
    HermiteE_NegHalf       -> https://oeis.org/A115329
    HermiteE_TablCol0      -> https://oeis.org/A123023
    HermiteE_TablCol1      -> https://oeis.org/A123023
    HermiteE_PolyCol3      -> https://oeis.org/A202834
    HermiteE_BinConv       -> https://oeis.org/A344501
    HermiteE_InvBinConv    -> https://oeis.org/A344501
    HermiteE_RevPolyDiag   -> https://oeis.org/A359739
    HermiteE_Trev          -> https://oeis.org/A359760
    HermiteE_Trevinv       -> https://oeis.org/A359760
    HermiteE_RevTalt       -> https://oeis.org/A359760
    HermiteE_CentralE      -> https://oeis.org/A359761

    HermiteE: Distinct: 25, Hits: 42, Misses: 27
'''
