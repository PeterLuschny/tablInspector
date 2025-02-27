from functools import cache
from _tabltypes import Table
from Binomial import binomial

"""Inverse binomial triangle:

   1;
  -1,    1;
   1,   -2,    1;
  -1,    3,   -3,    1;
   1,   -4,    6,   -4,    1;
  -1,    5,  -10,   10,   -5,    1;
   1,   -6,   15,  -20,   15,   -6,    1;
  -1,    7,  -21,   35,  -35,   21,   -7,    1;
   1,   -8,   28,  -56,   70,  -56,   28,   -8,    1;
  -1,    9,  -36,   84, -126,  126,  -84,   36,   -9,    1;
  ...
"""

@cache
def binomialinv(n: int) -> list[int]:
    return [(-1)**(n - k) * binomial(n)[k] for k in range(n + 1)]


BinomialInv = Table(
    binomialinv,
    "BinomialInv",
    ["A130595"],
    "A007318",
    r"(-1)^{n-k} \, n! \, / (k! \, (n - k)! )",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(BinomialInv)






''' OEIS
    BinomialInv_Tinvrev       -> 0 
    BinomialInv_RevTinv11     -> 0 
    BinomialInv_TablSum       -> https://oeis.org/A7
    BinomialInv_TablDiag0     -> https://oeis.org/A12
    BinomialInv_PolyCol2      -> https://oeis.org/A12
    BinomialInv_RevPosHalf    -> https://oeis.org/A12
    BinomialInv_TablCol1      -> https://oeis.org/A27
    BinomialInv_TablDiag1     -> https://oeis.org/A27
    BinomialInv_PolyRow1      -> https://oeis.org/A27
    BinomialInv_RevPolyRow1   -> https://oeis.org/A27
    BinomialInv_AntiDSum      -> https://oeis.org/A45
    BinomialInv_EvenSum       -> https://oeis.org/A79
    BinomialInv_OddSum        -> https://oeis.org/A79
    BinomialInv_AltSum        -> https://oeis.org/A79
    BinomialInv_AbsSum        -> https://oeis.org/A79
    BinomialInv_PolyCol3      -> https://oeis.org/A79
    BinomialInv_RevEvenSum    -> https://oeis.org/A79
    BinomialInv_RevOddSum     -> https://oeis.org/A79
    BinomialInv_RevPolyCol3   -> https://oeis.org/A79
    BinomialInv_TablCol2      -> https://oeis.org/A217
    BinomialInv_TablDiag2     -> https://oeis.org/A217
    BinomialInv_NegHalf       -> https://oeis.org/A244
    BinomialInv_RevNegHalf    -> https://oeis.org/A244
    BinomialInv_PolyRow2      -> https://oeis.org/A290
    BinomialInv_RevPolyRow2   -> https://oeis.org/A290
    BinomialInv_TablCol3      -> https://oeis.org/A292
    BinomialInv_TablDiag3     -> https://oeis.org/A292
    BinomialInv_PolyRow3      -> https://oeis.org/A578
    BinomialInv_RevPolyRow3   -> https://oeis.org/A578
    BinomialInv_CentralE      -> https://oeis.org/A984
    BinomialInv_InvBinConv    -> https://oeis.org/A984
    BinomialInv_TablMax       -> https://oeis.org/A1405
    BinomialInv_ColMiddle     -> https://oeis.org/A1405
    BinomialInv_RevColMiddle  -> https://oeis.org/A1405
    BinomialInv_CentralO      -> https://oeis.org/A1700
    BinomialInv_RevCentralO   -> https://oeis.org/A1700
    BinomialInv_TablLcm       -> https://oeis.org/A2944
    BinomialInv_Tder          -> https://oeis.org/A3506
    BinomialInv_RevTder       -> https://oeis.org/A3506
    BinomialInv_Triangle      -> https://oeis.org/A7318
    BinomialInv_Tinv          -> https://oeis.org/A7318
    BinomialInv_Trev          -> https://oeis.org/A7318
    BinomialInv_Trevinv       -> https://oeis.org/A7318
    BinomialInv_Talt          -> https://oeis.org/A7318
    BinomialInv_RevTalt       -> https://oeis.org/A7318
    BinomialInv_PolyDiag      -> https://oeis.org/A7778
    BinomialInv_RevPolyDiag   -> https://oeis.org/A7778
    BinomialInv_RevAntiDSum   -> https://oeis.org/A11655
    BinomialInv_Tantidiag     -> https://oeis.org/A11973
    BinomialInv_RevTantidiag  -> https://oeis.org/A11973
    BinomialInv_TablGcd       -> https://oeis.org/A14963
    BinomialInv_AccRevSum     -> https://oeis.org/A19590
    BinomialInv_TransNat1     -> https://oeis.org/A19590
    BinomialInv_TablCol0      -> https://oeis.org/A33999
    BinomialInv_PosHalf       -> https://oeis.org/A33999
    BinomialInv_RevTacc       -> https://oeis.org/A71919
    BinomialInv_Toff11        -> https://oeis.org/A74909
    BinomialInv_Trev11        -> https://oeis.org/A74909
    BinomialInv_Tinv11        -> https://oeis.org/A74909
    BinomialInv_Trevinv11     -> https://oeis.org/A74909
    BinomialInv_RevToff11     -> https://oeis.org/A74909
    BinomialInv_RevTrev11     -> https://oeis.org/A74909
    BinomialInv_Tacc          -> https://oeis.org/A110555
    BinomialInv_BinConv       -> https://oeis.org/A126869
    BinomialInv_AccSum        -> https://oeis.org/A154955
    BinomialInv_RevAccRevSum  -> https://oeis.org/A154955
    BinomialInv_RevTransNat1  -> https://oeis.org/A154955
    BinomialInv_TransNat0     -> https://oeis.org/A209229
    BinomialInv_RevTransNat0  -> https://oeis.org/A209229
    BinomialInv_TransSqrs     -> https://oeis.org/A245196
    BinomialInv_RevTransSqrs  -> https://oeis.org/A245196

    BinomialInv: Distinct: 30, Hits: 69, Misses: 2
'''
