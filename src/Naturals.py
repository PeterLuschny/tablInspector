from functools import cache
from Tables import Table

"""
This is a demo (!) of the most primitive use of the 'Table' module.

The function 'natural' computes the n-th row of a regular integer
triangle. It has to be defined for n >= 0.
"""


@cache
def naturals(n: int) -> list[int]:
    R = range((n * (n + 1)) // 2, ((n + 1) * (n + 2)) // 2)
    return [i + 1 for i in R]


Naturals = Table(
    naturals, 
    "Naturals", 
    ["A000027", "A001477"],
    "",  # not integer-invertible
    r"n+1 + (k+n) (k+n+1)/2"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Naturals)  # type: ignore




''' OEIS
    Naturals_Trev11        -> 0 
    Naturals_Tacc          -> 0 
    Naturals_Tder          -> 0 
    Naturals_OddSum        -> 0 
    Naturals_AltSum        -> 0 
    Naturals_AccSum        -> 0 
    Naturals_PosHalf       -> 0 
    Naturals_NegHalf       -> 0 
    Naturals_TransSqrs     -> 0 
    Naturals_PolyRow2      -> 0 
    Naturals_PolyRow3      -> 0 
    Naturals_PolyCol2      -> 0 
    Naturals_PolyCol3      -> 0 
    Naturals_PolyDiag      -> 0 
    Naturals_RevToff11     -> 0 
    Naturals_RevTantidiag  -> 0 
    Naturals_RevTacc       -> 0 
    Naturals_RevTder       -> 0 
    Naturals_RevEvenSum    -> 0 
    Naturals_RevOddSum     -> 0 
    Naturals_RevAccRevSum  -> 0 
    Naturals_RevAntiDSum   -> 0 
    Naturals_RevPosHalf    -> 0 
    Naturals_RevNegHalf    -> 0 
    Naturals_RevTransNat1  -> 0 
    Naturals_RevTransSqrs  -> 0 
    Naturals_RevPolyRow2   -> 0 
    Naturals_RevPolyRow3   -> 0 
    Naturals_RevPolyCol3   -> 0 
    Naturals_RevPolyDiag   -> 0 
    Naturals_TablGcd       -> https://oeis.org/A12
    Naturals_Triangle      -> https://oeis.org/A27
    Naturals_Talt          -> https://oeis.org/A27
    Naturals_TablDiag1     -> https://oeis.org/A96
    Naturals_TablCol0      -> https://oeis.org/A124
    Naturals_TablDiag0     -> https://oeis.org/A217
    Naturals_TablMax       -> https://oeis.org/A217
    Naturals_ColMiddle     -> https://oeis.org/A982
    Naturals_CentralO      -> https://oeis.org/A1105
    Naturals_CentralE      -> https://oeis.org/A1844
    Naturals_RevPolyRow1   -> https://oeis.org/A5408
    Naturals_TablSum       -> https://oeis.org/A6003
    Naturals_AbsSum        -> https://oeis.org/A6003
    Naturals_RevTrev11     -> https://oeis.org/A14132
    Naturals_PolyRow1      -> https://oeis.org/A16789
    Naturals_InvBinConv    -> https://oeis.org/A19590
    Naturals_TablDiag2     -> https://oeis.org/A34856
    Naturals_Trev          -> https://oeis.org/A38722
    Naturals_RevTalt       -> https://oeis.org/A38722
    Naturals_TablDiag3     -> https://oeis.org/A55998
    Naturals_Tantidiag     -> https://oeis.org/A56536
    Naturals_RevCentralO   -> https://oeis.org/A58331
    Naturals_TablLcm       -> https://oeis.org/A61431
    Naturals_AntiDSum      -> https://oeis.org/A79824
    Naturals_Toff11        -> https://oeis.org/A80036
    Naturals_BinConv       -> https://oeis.org/A84850
    Naturals_RevColMiddle  -> https://oeis.org/A99392
    Naturals_EvenSum       -> https://oeis.org/A131474
    Naturals_AccRevSum     -> https://oeis.org/A132117
    Naturals_TransNat1     -> https://oeis.org/A132117
    Naturals_TablCol3      -> https://oeis.org/A145018
    Naturals_TransNat0     -> https://oeis.org/A152457
    Naturals_TablCol1      -> https://oeis.org/A152948
    Naturals_TablCol2      -> https://oeis.org/A152950
    Naturals_RevTransNat0  -> https://oeis.org/A176060

    Naturals: Distinct: 31, Hits: 35, Misses: 30
'''
