from functools import cache
from Binomial import Binomial
from _tabltypes import Table


"""Andre numbers (version A375555).
  [0]  1;
  [1]  1, 1;
  [2]  1, 1,    1;
  [3]  1, 1,    2,    1;
  [4]  1, 1,    5,    3,   1;
  [5]  1, 1,   16,    9,   4,   1;
  [6]  1, 1,   61,   19,  14,   5,  1;
  [7]  1, 1,  272,   99,  34,  20,  6,  1;
  [8]  1, 1, 1385,  477,  69,  55, 27,  7, 1;
  [9]  1, 1, 7936, 1513, 496, 125, 83, 35, 8, 1;
"""


# TODO Give a row based recurrence for this.
@cache
def _andre(n: int, k: int) -> int:
    if k == 0 or n == 0:
        return 1

    return -sum(Binomial(k, j) * _andre(n, j) for j in range(0, k, n))


@cache
def andre(n: int) -> list[int]:
    return [abs(_andre(k, n)) for k in range(n + 1)]


Andre = Table(
    andre, 
    "Andre", 
    ["A375555", "A181937"], 
    "A000000",
    r"-\sum_{j = 0 \text{ by } n }^{k-1} \binom{k}{j} T_{n, j}" 
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Andre)






''' OEIS
    Andre_Tinv          -> 0 
    Andre_Trev          -> 0 
    Andre_Tinvrev       -> 0 
    Andre_Trevinv       -> 0 
    Andre_Toff11        -> 0 
    Andre_Trev11        -> 0 
    Andre_Tinv11        -> 0 
    Andre_Tinvrev11     -> 0 
    Andre_Trevinv11     -> 0 
    Andre_Tantidiag     -> 0 
    Andre_Tacc          -> 0 
    Andre_Tder          -> 0 
    Andre_TablLcm       -> 0 
    Andre_EvenSum       -> 0 
    Andre_OddSum        -> 0 
    Andre_AltSum        -> 0 
    Andre_AccSum        -> 0 
    Andre_AccRevSum     -> 0 
    Andre_AntiDSum      -> 0 
    Andre_ColMiddle     -> 0 
    Andre_CentralO      -> 0 
    Andre_PosHalf       -> 0 
    Andre_NegHalf       -> 0 
    Andre_TransNat0     -> 0 
    Andre_TransNat1     -> 0 
    Andre_TransSqrs     -> 0 
    Andre_BinConv       -> 0 
    Andre_InvBinConv    -> 0 
    Andre_PolyCol2      -> 0 
    Andre_PolyCol3      -> 0 
    Andre_PolyDiag      -> 0 
    Andre_RevToff11     -> 0 
    Andre_RevTrev11     -> 0 
    Andre_RevTinv11     -> 0 
    Andre_RevTantidiag  -> 0 
    Andre_RevTacc       -> 0 
    Andre_RevTalt       -> 0 
    Andre_RevTder       -> 0 
    Andre_RevEvenSum    -> 0 
    Andre_RevOddSum     -> 0 
    Andre_RevAccRevSum  -> 0 
    Andre_RevAntiDSum   -> 0 
    Andre_RevPosHalf    -> 0 
    Andre_RevNegHalf    -> 0 
    Andre_RevTransNat0  -> 0 
    Andre_RevTransNat1  -> 0 
    Andre_RevTransSqrs  -> 0 
    Andre_RevPolyCol3   -> 0 
    Andre_RevPolyDiag   -> 0 
    Andre_TablCol0      -> https://oeis.org/A12
    Andre_TablCol1      -> https://oeis.org/A12
    Andre_TablDiag0     -> https://oeis.org/A12
    Andre_TablDiag1     -> https://oeis.org/A27
    Andre_PolyRow1      -> https://oeis.org/A27
    Andre_RevPolyRow1   -> https://oeis.org/A27
    Andre_TablDiag2     -> https://oeis.org/A96
    Andre_TablCol2      -> https://oeis.org/A111
    Andre_TablMax       -> https://oeis.org/A111
    Andre_PolyRow2      -> https://oeis.org/A2061
    Andre_RevPolyRow2   -> https://oeis.org/A2061
    Andre_RevCentralO   -> https://oeis.org/A10763
    Andre_RevColMiddle  -> https://oeis.org/A14495
    Andre_CentralE      -> https://oeis.org/A30662
    Andre_TablDiag3     -> https://oeis.org/A62748
    Andre_PolyRow3      -> https://oeis.org/A100104
    Andre_RevPolyRow3   -> https://oeis.org/A100705
    Andre_TablGcd       -> https://oeis.org/A174965
    Andre_TablCol3      -> https://oeis.org/A178963
    Andre_TablSum       -> https://oeis.org/A375554
    Andre_AbsSum        -> https://oeis.org/A375554
    Andre_Triangle      -> https://oeis.org/A375555
    Andre_Talt          -> https://oeis.org/A375555

    Andre: Distinct: 16, Hits: 23, Misses: 49
'''
