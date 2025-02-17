from functools import cache
from _tabltypes import Table

"""Inverse of the Motzkin triangle.

  [0]  1;
  [1] -1,  1;
  [2]  0, -2,   1;
  [3]  1,  1,  -3,   1;
  [4] -1,  2,   3,  -4,   1;
  [5]  0, -4,   2,   6,  -5,   1;
  [6]  1,  2,  -9,   0,  10,  -6,   1;
  [7] -1,  3,   9, -15,  -5,  15,  -7,   1;
"""

@cache
def motzkininv(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [-1, 1]

    r2  = motzkininv(n - 2) + [0]
    r1  = motzkininv(n - 1) + [0]
    r   = motzkininv(n - 1) + [1]
    for k in range(0, n):
        r[k] = r1[k - 1] - r2[k] - r1[k]
    return r


MotzkinInv = Table(
    motzkininv,
    "MotzkinInv",
    ["A104562", "A101950", "A344566"],
    "A064189",
    r"\binom{n}{k} \text{Hyper}([(k-n)/2, (k-n+1)/2], [k+2], 4)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(MotzkinInv)




''' OEIS
    MotzkinInv_Triangle      -> https://oeis.org/A-999999
    MotzkinInv_Trev          -> https://oeis.org/A-999999
    MotzkinInv_Toff11        -> https://oeis.org/A-999999
    MotzkinInv_Trev11        -> https://oeis.org/A-999999
    MotzkinInv_TablSum       -> https://oeis.org/A-999999
    MotzkinInv_AntiDSum      -> https://oeis.org/A-999999
    MotzkinInv_Tinv11        -> 0 
    MotzkinInv_Trevinv11     -> 0 
    MotzkinInv_Tacc          -> 0 
    MotzkinInv_Tder          -> 0 
    MotzkinInv_TablCol3      -> 0 
    MotzkinInv_TablLcm       -> 0 
    MotzkinInv_TablMax       -> 0 
    MotzkinInv_AbsSum        -> 0 
    MotzkinInv_ColMiddle     -> 0 
    MotzkinInv_CentralE      -> 0 
    MotzkinInv_BinConv       -> 0 
    MotzkinInv_InvBinConv    -> 0 
    MotzkinInv_PolyDiag      -> 0 
    MotzkinInv_RevToff11     -> 0 
    MotzkinInv_RevTrev11     -> 0 
    MotzkinInv_RevTantidiag  -> 0 
    MotzkinInv_RevTacc       -> 0 
    MotzkinInv_RevTalt       -> 0 
    MotzkinInv_RevTder       -> 0 
    MotzkinInv_RevAntiDSum   -> 0 
    MotzkinInv_RevColMiddle  -> 0 
    MotzkinInv_RevCentralO   -> 0 
    MotzkinInv_RevTransSqrs  -> 0 
    MotzkinInv_RevPolyRow3   -> 0 
    MotzkinInv_RevPolyDiag   -> 0 
    MotzkinInv_TablDiag0     -> https://oeis.org/A12
    MotzkinInv_TablDiag1     -> https://oeis.org/A27
    MotzkinInv_AltSum        -> https://oeis.org/A27
    MotzkinInv_PolyRow1      -> https://oeis.org/A27
    MotzkinInv_PolyCol3      -> https://oeis.org/A27
    MotzkinInv_RevPolyRow1   -> https://oeis.org/A27
    MotzkinInv_TablDiag2     -> https://oeis.org/A217
    MotzkinInv_RevNegHalf    -> https://oeis.org/A1906
    MotzkinInv_OddSum        -> https://oeis.org/A4524
    MotzkinInv_RevOddSum     -> https://oeis.org/A4524
    MotzkinInv_EvenSum       -> https://oeis.org/A4525
    MotzkinInv_RevEvenSum    -> https://oeis.org/A4525
    MotzkinInv_RevPolyRow2   -> https://oeis.org/A5408
    MotzkinInv_PolyRow2      -> https://oeis.org/A5563
    MotzkinInv_TablDiag3     -> https://oeis.org/A5586
    MotzkinInv_TablCol0      -> https://oeis.org/A11655
    MotzkinInv_PolyCol2      -> https://oeis.org/A11655
    MotzkinInv_RevPosHalf    -> https://oeis.org/A11655
    MotzkinInv_RevPolyCol3   -> https://oeis.org/A25170
    MotzkinInv_Trevinv       -> https://oeis.org/A26300
    MotzkinInv_AccSum        -> https://oeis.org/A26741
    MotzkinInv_RevAccRevSum  -> https://oeis.org/A26741
    MotzkinInv_RevTransNat1  -> https://oeis.org/A26741
    MotzkinInv_RevTransNat0  -> https://oeis.org/A29578
    MotzkinInv_NegHalf       -> https://oeis.org/A49072
    MotzkinInv_AccRevSum     -> https://oeis.org/A57979
    MotzkinInv_TransNat1     -> https://oeis.org/A57979
    MotzkinInv_Tinv          -> https://oeis.org/A64189
    MotzkinInv_TablGcd       -> https://oeis.org/A99563
    MotzkinInv_Talt          -> https://oeis.org/A101950
    MotzkinInv_PosHalf       -> https://oeis.org/A106853
    MotzkinInv_TablCol2      -> https://oeis.org/A128504
    MotzkinInv_TransSqrs     -> https://oeis.org/A129889
    MotzkinInv_TransNat0     -> https://oeis.org/A142150
    MotzkinInv_TablCol1      -> https://oeis.org/A186731
    MotzkinInv_PolyRow3      -> https://oeis.org/A242135
    MotzkinInv_Tantidiag     -> https://oeis.org/A249303
    MotzkinInv_CentralO      -> https://oeis.org/A350383

    MotzkinInv: Distinct: 29, Hits: 44, Misses: 25
'''
