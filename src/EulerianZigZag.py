from functools import cache
from Binomial import binomial
from DegSymPoly import degsympoly
from _tabltypes import Table

"""EulerianZigZag triangle.

[0] [1]
[1] [1,  1]
[2] [1,  3,   1]
[3] [1,  7,   7,   1]
[4] [1, 14,  31,  14,   1]
[5] [1, 26, 109, 109,  26,  1]
[6] [1, 46, 334, 623, 334, 46, 1]
"""

@cache
def eulerianzigzag(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [1, 1]
    half = (n + 2) // 2
    row = [sum((-1 if j & 1 else 1) * binomial(n + 3)[j] * 
        degsympoly(n+2)[k - j] for j in range(k + 1)) for k in range(half)]
    return (row + row[-2::-1]) if n % 2 == 0 else (row + row[::-1])


EulerianZigZag = Table(
    eulerianzigzag, 
    "EulerianZigZag", 
    ["A205497"], 
    "", 
    r"%%"
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(EulerianZigZag)
    #from _tablutils import Bench
    #Bench(eulerianzigzag, "EulerianZigZag", 4)
    # for n in range(7): print(eulerianzigzag(n))


''' OEIS
    EulerianZigZag_Trev          -> 0 
    EulerianZigZag_Tinvrev       -> 0 
    EulerianZigZag_Toff11        -> 0 
    EulerianZigZag_Trev11        -> 0 
    EulerianZigZag_Tantidiag     -> 0 
    EulerianZigZag_Tacc          -> 0 
    EulerianZigZag_Talt          -> 0 
    EulerianZigZag_Tder          -> 0 
    EulerianZigZag_TablLcm       -> 0 
    EulerianZigZag_TablGcd       -> 0 
    EulerianZigZag_AccSum        -> 0 
    EulerianZigZag_AccRevSum     -> 0 
    EulerianZigZag_AntiDSum      -> 0 
    EulerianZigZag_ColMiddle     -> 0 
    EulerianZigZag_CentralE      -> 0 
    EulerianZigZag_CentralO      -> 0 
    EulerianZigZag_PosHalf       -> 0 
    EulerianZigZag_NegHalf       -> 0 
    EulerianZigZag_TransNat1     -> 0 
    EulerianZigZag_TransSqrs     -> 0 
    EulerianZigZag_BinConv       -> 0 
    EulerianZigZag_InvBinConv    -> 0 
    EulerianZigZag_PolyCol3      -> 0 
    EulerianZigZag_PolyDiag      -> 0 
    EulerianZigZag_RevToff11     -> 0 
    EulerianZigZag_RevTrev11     -> 0 
    EulerianZigZag_RevTinv11     -> 0 
    EulerianZigZag_RevTantidiag  -> 0 
    EulerianZigZag_RevTacc       -> 0 
    EulerianZigZag_RevTalt       -> 0 
    EulerianZigZag_RevTder       -> 0 
    EulerianZigZag_RevAccRevSum  -> 0 
    EulerianZigZag_RevAntiDSum   -> 0 
    EulerianZigZag_RevColMiddle  -> 0 
    EulerianZigZag_RevCentralO   -> 0 
    EulerianZigZag_RevTransNat0  -> 0 
    EulerianZigZag_RevTransNat1  -> 0 
    EulerianZigZag_RevTransSqrs  -> 0 
    EulerianZigZag_RevPolyCol3   -> 0 
    EulerianZigZag_RevPolyDiag   -> 0 
    EulerianZigZag_TablDiag0     -> https://oeis.org/A7
    EulerianZigZag_TablDiag1     -> https://oeis.org/A7
    EulerianZigZag_TablCol0      -> https://oeis.org/A12
    EulerianZigZag_TablDiag2     -> https://oeis.org/A12
    EulerianZigZag_PolyRow1      -> https://oeis.org/A12
    EulerianZigZag_PolyRow2      -> https://oeis.org/A12
    EulerianZigZag_PolyRow3      -> https://oeis.org/A27
    EulerianZigZag_RevPolyRow1   -> https://oeis.org/A27
    EulerianZigZag_TablSum       -> https://oeis.org/A111
    EulerianZigZag_AbsSum        -> https://oeis.org/A111
    EulerianZigZag_RevPolyRow2   -> https://oeis.org/A290
    EulerianZigZag_TablCol1      -> https://oeis.org/A1924
    EulerianZigZag_TablDiag3     -> https://oeis.org/A1924
    EulerianZigZag_TransNat0     -> https://oeis.org/A6326
    EulerianZigZag_RevPolyRow3   -> https://oeis.org/A11379
    EulerianZigZag_TablCol2      -> https://oeis.org/A205492
    EulerianZigZag_TablCol3      -> https://oeis.org/A205493
    EulerianZigZag_Triangle      -> https://oeis.org/A205497
    EulerianZigZag_PolyCol2      -> https://oeis.org/A350354
    EulerianZigZag_RevPosHalf    -> https://oeis.org/A350354
    EulerianZigZag_AltSum        -> https://oeis.org/A373388
    EulerianZigZag_RevNegHalf    -> https://oeis.org/A373389
    EulerianZigZag_EvenSum       -> https://oeis.org/A373752
    EulerianZigZag_RevEvenSum    -> https://oeis.org/A373752
    EulerianZigZag_OddSum        -> https://oeis.org/A373753
    EulerianZigZag_RevOddSum     -> https://oeis.org/A373753
    EulerianZigZag_TablMax       -> https://oeis.org/A373755

    EulerianZigZag: Distinct: 18, Hits: 27, Misses: 40
'''
