from functools import cache
from FiboLucas import fibolucas
from _tabltypes import Table

"""FiboLucasRev polynomials, m = 2.

| [1] |
| [2, 1] |
| [1, 2, 1] |
| [2, 2, 2, 1] |
| [1, 4, 3, 2, 1] |
| [2, 3, 6, 4, 2, 1] |
| [1, 6, 6, 8, 5, 2, 1] |
| [2, 4, 12, 10, 10, 6, 2, 1] |

# @cache
def T(n: int, k: int) -> int:
    if k > n: return 0
    if k < 2: return k + 1
    return T(n - 1, k) + T(n - 2, k - 2)
"""


@cache
def fibolucasrev(n: int) -> list[int]:
    if n == 0:
        return [1]
    return list(reversed(fibolucas(n)))


FiboLucasRev = Table(
    fibolucasrev, 
    "FiboLucasRev", 
    ["A124038"], 
    "A000000", 
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable
    InspectTable(FiboLucasRev)






''' OEIS
    FiboLucasRev_Trevinv       -> 0 
    FiboLucasRev_Toff11        -> 0 
    FiboLucasRev_Trev11        -> 0 
    FiboLucasRev_Tinv11        -> 0 
    FiboLucasRev_Trevinv11     -> 0 
    FiboLucasRev_Tantidiag     -> 0 
    FiboLucasRev_Tacc          -> 0 
    FiboLucasRev_Tder          -> 0 
    FiboLucasRev_TablCol3      -> 0 
    FiboLucasRev_TablLcm       -> 0 
    FiboLucasRev_TablMax       -> 0 
    FiboLucasRev_AccSum        -> 0 
    FiboLucasRev_AccRevSum     -> 0 
    FiboLucasRev_ColMiddle     -> 0 
    FiboLucasRev_CentralE      -> 0 
    FiboLucasRev_CentralO      -> 0 
    FiboLucasRev_NegHalf       -> 0 
    FiboLucasRev_TransNat1     -> 0 
    FiboLucasRev_TransSqrs     -> 0 
    FiboLucasRev_BinConv       -> 0 
    FiboLucasRev_InvBinConv    -> 0 
    FiboLucasRev_PolyDiag      -> 0 
    FiboLucasRev_RevToff11     -> 0 
    FiboLucasRev_RevTrev11     -> 0 
    FiboLucasRev_RevTantidiag  -> 0 
    FiboLucasRev_RevTacc       -> 0 
    FiboLucasRev_RevTder       -> 0 
    FiboLucasRev_RevAccRevSum  -> 0 
    FiboLucasRev_RevAntiDSum   -> 0 
    FiboLucasRev_RevColMiddle  -> 0 
    FiboLucasRev_RevCentralO   -> 0 
    FiboLucasRev_RevTransNat0  -> 0 
    FiboLucasRev_RevTransNat1  -> 0 
    FiboLucasRev_RevTransSqrs  -> 0 
    FiboLucasRev_RevPolyRow3   -> 0 
    FiboLucasRev_RevPolyCol3   -> 0 
    FiboLucasRev_RevPolyDiag   -> 0 
    FiboLucasRev_TablDiag0     -> https://oeis.org/A12
    FiboLucasRev_TablDiag2     -> https://oeis.org/A27
    FiboLucasRev_PolyRow1      -> https://oeis.org/A27
    FiboLucasRev_TablSum       -> https://oeis.org/A32
    FiboLucasRev_AbsSum        -> https://oeis.org/A32
    FiboLucasRev_TablCol0      -> https://oeis.org/A34
    FiboLucasRev_AltSum        -> https://oeis.org/A45
    FiboLucasRev_RevEvenSum    -> https://oeis.org/A45
    FiboLucasRev_RevNegHalf    -> https://oeis.org/A129
    FiboLucasRev_PolyRow2      -> https://oeis.org/A290
    FiboLucasRev_RevPolyRow2   -> https://oeis.org/A290
    FiboLucasRev_RevPolyRow1   -> https://oeis.org/A5408
    FiboLucasRev_TablDiag3     -> https://oeis.org/A5843
    FiboLucasRev_PosHalf       -> https://oeis.org/A6131
    FiboLucasRev_RevOddSum     -> https://oeis.org/A6355
    FiboLucasRev_AntiDSum      -> https://oeis.org/A16116
    FiboLucasRev_TransNat0     -> https://oeis.org/A23607
    FiboLucasRev_TablCol1      -> https://oeis.org/A29578
    FiboLucasRev_PolyCol2      -> https://oeis.org/A48654
    FiboLucasRev_RevPosHalf    -> https://oeis.org/A48654
    FiboLucasRev_TablDiag1     -> https://oeis.org/A55642
    FiboLucasRev_PolyCol3      -> https://oeis.org/A108300
    FiboLucasRev_Triangle      -> https://oeis.org/A124038
    FiboLucasRev_Talt          -> https://oeis.org/A124038
    FiboLucasRev_TablCol2      -> https://oeis.org/A131259
    FiboLucasRev_EvenSum       -> https://oeis.org/A133585
    FiboLucasRev_OddSum        -> https://oeis.org/A133586
    FiboLucasRev_PolyRow3      -> https://oeis.org/A188377
    FiboLucasRev_TablGcd       -> https://oeis.org/A297382
    FiboLucasRev_Trev          -> https://oeis.org/A374439
    FiboLucasRev_RevTalt       -> https://oeis.org/A374439
    FiboLucasRev_Tinv          -> https://oeis.org/A375025

    FiboLucasRev: Distinct: 26, Hits: 32, Misses: 37
'''
