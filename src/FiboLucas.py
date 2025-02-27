from functools import cache
from _tabltypes import Table

"""FiboLucas polynomials, m = 2.
  [ 0] [1]
  [ 1] [1, 2]
  [ 2] [1, 2, 1]
  [ 3] [1, 2, 2, 2]
  [ 4] [1, 2, 3, 4, 1]
  [ 5] [1, 2, 4, 6, 3, 2]
  [ 6] [1, 2, 5, 8, 6, 6, 1]
  [ 7] [1, 2, 6, 10, 10, 12, 4, 2]
  [ 8] [1, 2, 7, 12, 15, 20, 10, 8, 1]
  [ 9] [1, 2, 8, 14, 21, 30, 20, 20, 5, 2]
  [10] [1, 2, 9, 16, 28, 42, 35, 40, 15, 10, 1]

# @cache
def T(n: int, k: int) -> int:
    if k > n: return 0
    if k < 2: return k + 1
    return T(n - 1, k) + T(n - 2, k - 2)
"""


@cache
def fibolucas(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [1, 2]
    if n == 2: return [1, 2, 1]

    rowA = fibolucas(n - 2)
    row  = fibolucas(n - 1) + [1 + n % 2]
    row[2] += 1

    for k in range(3, n):
        row[k] += rowA[k - 2]

    return row


FiboLucas = Table(
    fibolucas,
    "FiboLucas",
    ["A374439"],
    "",
    r"2^{k'} \, \binom{n - k' - (k - k') / 2}{(k - k') / 2} \text{ where } k' = k \text{ mod } 2",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable
    InspectTable(FiboLucas)






''' OEIS
    FiboLucas_Toff11        -> 0 
    FiboLucas_Trev11        -> 0 
    FiboLucas_Tantidiag     -> 0 
    FiboLucas_Tacc          -> 0 
    FiboLucas_Tder          -> 0 
    FiboLucas_TablDiag3     -> 0 
    FiboLucas_TablLcm       -> 0 
    FiboLucas_TablMax       -> 0 
    FiboLucas_AccSum        -> 0 
    FiboLucas_AccRevSum     -> 0 
    FiboLucas_AntiDSum      -> 0 
    FiboLucas_ColMiddle     -> 0 
    FiboLucas_CentralE      -> 0 
    FiboLucas_CentralO      -> 0 
    FiboLucas_TransNat0     -> 0 
    FiboLucas_TransNat1     -> 0 
    FiboLucas_TransSqrs     -> 0 
    FiboLucas_BinConv       -> 0 
    FiboLucas_InvBinConv    -> 0 
    FiboLucas_PolyRow3      -> 0 
    FiboLucas_PolyCol3      -> 0 
    FiboLucas_PolyDiag      -> 0 
    FiboLucas_RevToff11     -> 0 
    FiboLucas_RevTrev11     -> 0 
    FiboLucas_RevTinv11     -> 0 
    FiboLucas_RevTantidiag  -> 0 
    FiboLucas_RevTacc       -> 0 
    FiboLucas_RevTder       -> 0 
    FiboLucas_RevAccRevSum  -> 0 
    FiboLucas_RevColMiddle  -> 0 
    FiboLucas_RevCentralO   -> 0 
    FiboLucas_RevNegHalf    -> 0 
    FiboLucas_RevTransNat1  -> 0 
    FiboLucas_RevTransSqrs  -> 0 
    FiboLucas_RevPolyDiag   -> 0 
    FiboLucas_TablCol0      -> https://oeis.org/A12
    FiboLucas_TablCol2      -> https://oeis.org/A27
    FiboLucas_RevPolyRow1   -> https://oeis.org/A27
    FiboLucas_TablSum       -> https://oeis.org/A32
    FiboLucas_AbsSum        -> https://oeis.org/A32
    FiboLucas_TablDiag0     -> https://oeis.org/A34
    FiboLucas_EvenSum       -> https://oeis.org/A45
    FiboLucas_AltSum        -> https://oeis.org/A45
    FiboLucas_NegHalf       -> https://oeis.org/A129
    FiboLucas_PolyRow2      -> https://oeis.org/A290
    FiboLucas_RevPolyRow2   -> https://oeis.org/A290
    FiboLucas_PolyRow1      -> https://oeis.org/A5408
    FiboLucas_TablCol3      -> https://oeis.org/A5843
    FiboLucas_PolyCol2      -> https://oeis.org/A6131
    FiboLucas_RevPosHalf    -> https://oeis.org/A6131
    FiboLucas_OddSum        -> https://oeis.org/A6355
    FiboLucas_RevAntiDSum   -> https://oeis.org/A16116
    FiboLucas_RevTransNat0  -> https://oeis.org/A23607
    FiboLucas_TablDiag1     -> https://oeis.org/A29578
    FiboLucas_PosHalf       -> https://oeis.org/A48654
    FiboLucas_TablCol1      -> https://oeis.org/A55642
    FiboLucas_RevPolyCol3   -> https://oeis.org/A108300
    FiboLucas_Trev          -> https://oeis.org/A124038
    FiboLucas_RevTalt       -> https://oeis.org/A124038
    FiboLucas_TablDiag2     -> https://oeis.org/A131259
    FiboLucas_RevEvenSum    -> https://oeis.org/A133585
    FiboLucas_RevOddSum     -> https://oeis.org/A133586
    FiboLucas_RevPolyRow3   -> https://oeis.org/A188377
    FiboLucas_TablGcd       -> https://oeis.org/A297382
    FiboLucas_Triangle      -> https://oeis.org/A374439
    FiboLucas_Talt          -> https://oeis.org/A374439
    FiboLucas_Tinvrev       -> https://oeis.org/A375025

    FiboLucas: Distinct: 26, Hits: 32, Misses: 35
'''
