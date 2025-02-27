from functools import cache
from _tabltypes import Table

"""Sierpiński's triangle, binomial(n, k) mod 2.

[0]                               1
[1]                              1, 1
[2]                            1, 0, 1
[3]                           1, 1, 1, 1
[4]                         1, 0, 0, 0, 1
[5]                        1, 1, 0, 0, 1, 1
[6]                      1, 0, 1, 0, 1, 0, 1
[7]                     1, 1, 1, 1, 1, 1, 1, 1
[8]                   1, 0, 0, 0, 0, 0, 0, 0, 1
[9]                  1, 1, 0, 0, 0, 0, 0, 0, 1, 1
"""


@cache
def sierpinski(n: int) -> list[int]:
    return [int(not ~n & k) for k in range(n + 1)]


Sierpinski = Table(
    sierpinski,
    "Sierpinski",
    ["A047999", "A090971", "A114700", "A143200", "A166282"],
    "A000000",
    r"\binom{n}{k} \text{ mod } 2",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Sierpinski)






''' OEIS
    Sierpinski_Tantidiag     -> 0 
    Sierpinski_AccSum        -> 0 
    Sierpinski_AccRevSum     -> 0 
    Sierpinski_NegHalf       -> 0 
    Sierpinski_TransNat1     -> 0 
    Sierpinski_TransSqrs     -> 0 
    Sierpinski_InvBinConv    -> 0 
    Sierpinski_PolyDiag      -> 0 
    Sierpinski_RevTantidiag  -> 0 
    Sierpinski_RevAccRevSum  -> 0 
    Sierpinski_RevNegHalf    -> 0 
    Sierpinski_RevTransNat1  -> 0 
    Sierpinski_RevTransSqrs  -> 0 
    Sierpinski_RevPolyDiag   -> 0 
    Sierpinski_CentralE      -> https://oeis.org/A7
    Sierpinski_TablCol0      -> https://oeis.org/A12
    Sierpinski_TablDiag0     -> https://oeis.org/A12
    Sierpinski_TablLcm       -> https://oeis.org/A12
    Sierpinski_TablGcd       -> https://oeis.org/A12
    Sierpinski_TablMax       -> https://oeis.org/A12
    Sierpinski_PolyRow1      -> https://oeis.org/A27
    Sierpinski_RevPolyRow1   -> https://oeis.org/A27
    Sierpinski_TablCol1      -> https://oeis.org/A35
    Sierpinski_TablDiag1     -> https://oeis.org/A35
    Sierpinski_TablSum       -> https://oeis.org/A1316
    Sierpinski_OddSum        -> https://oeis.org/A1316
    Sierpinski_AltSum        -> https://oeis.org/A1316
    Sierpinski_AbsSum        -> https://oeis.org/A1316
    Sierpinski_RevOddSum     -> https://oeis.org/A1316
    Sierpinski_PosHalf       -> https://oeis.org/A1317
    Sierpinski_PolyCol2      -> https://oeis.org/A1317
    Sierpinski_RevPosHalf    -> https://oeis.org/A1317
    Sierpinski_AntiDSum      -> https://oeis.org/A2487
    Sierpinski_RevAntiDSum   -> https://oeis.org/A2487
    Sierpinski_PolyRow2      -> https://oeis.org/A2522
    Sierpinski_RevPolyRow2   -> https://oeis.org/A2522
    Sierpinski_Triangle      -> https://oeis.org/A47999
    Sierpinski_Tinv          -> https://oeis.org/A47999
    Sierpinski_Trev          -> https://oeis.org/A47999
    Sierpinski_Tinvrev       -> https://oeis.org/A47999
    Sierpinski_Trevinv       -> https://oeis.org/A47999
    Sierpinski_Talt          -> https://oeis.org/A47999
    Sierpinski_RevTalt       -> https://oeis.org/A47999
    Sierpinski_PolyRow3      -> https://oeis.org/A53698
    Sierpinski_RevPolyRow3   -> https://oeis.org/A53698
    Sierpinski_EvenSum       -> https://oeis.org/A60632
    Sierpinski_RevEvenSum    -> https://oeis.org/A60632
    Sierpinski_BinConv       -> https://oeis.org/A88560
    Sierpinski_Toff11        -> https://oeis.org/A90971
    Sierpinski_Trev11        -> https://oeis.org/A90971
    Sierpinski_Tinv11        -> https://oeis.org/A90971
    Sierpinski_Trevinv11     -> https://oeis.org/A90971
    Sierpinski_RevToff11     -> https://oeis.org/A90971
    Sierpinski_RevTrev11     -> https://oeis.org/A90971
    Sierpinski_RevTinv11     -> https://oeis.org/A90971
    Sierpinski_PolyCol3      -> https://oeis.org/A100307
    Sierpinski_RevPolyCol3   -> https://oeis.org/A100307
    Sierpinski_TablCol3      -> https://oeis.org/A121262
    Sierpinski_TablDiag3     -> https://oeis.org/A121262
    Sierpinski_TablCol2      -> https://oeis.org/A133872
    Sierpinski_TablDiag2     -> https://oeis.org/A133872
    Sierpinski_Tder          -> https://oeis.org/A158810
    Sierpinski_RevTder       -> https://oeis.org/A158810
    Sierpinski_ColMiddle     -> https://oeis.org/A209229
    Sierpinski_CentralO      -> https://oeis.org/A209229
    Sierpinski_RevColMiddle  -> https://oeis.org/A209229
    Sierpinski_RevCentralO   -> https://oeis.org/A209229
    Sierpinski_Tacc          -> https://oeis.org/A261363
    Sierpinski_RevTacc       -> https://oeis.org/A261363
    Sierpinski_TransNat0     -> https://oeis.org/A335063
    Sierpinski_RevTransNat0  -> https://oeis.org/A335063

    Sierpinski: Distinct: 21, Hits: 57, Misses: 14
'''
