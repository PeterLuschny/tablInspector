from functools import cache
from _tabltypes import Table

"""FiboLucasInv polynomials.

    [0] [  1]
    [1] [ -2,   1]
    [2] [  3,  -2,   1]
    [3] [ -4,   2,  -2,   1]
    [4] [  6,  -2,   1,  -2,   1]
    [5] [-10,   5,   0,   0,  -2,  1]
    [6] [ 15, -10,   5,   2,  -1, -2,  1]
    [7] [-20,  10, -12,   6,   4, -2, -2,  1]
    [8] [ 30,  -8,   4, -16,   8,  6, -3, -2,  1]
    [9] [-52,  26,   8,  -4, -22, 11,  8, -4, -2, 1]

"""


@cache
def fibolucasinv(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [-2, 1]
    fli = fibolucasinv(n - 1)
    row = [1] * (n + 1)
    row[n - 1] = -2
    for k in range(n - 2, 0, -1):
        row[k] = fli[k - 1] - fli[k + 1]
    row[0] = -2 * fli[0] - fli[1]
    return row


FiboLucasInv = Table(
    fibolucasinv, 
    "FiboLucasInv", 
    ["A375025"], 
    "A000000", 
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(FiboLucasInv)


''' OEIS
    FiboLucasInv_Trev          -> 0 
    FiboLucasInv_Toff11        -> 0 
    FiboLucasInv_Trev11        -> 0 
    FiboLucasInv_Tinv11        -> 0 
    FiboLucasInv_Tantidiag     -> 0 
    FiboLucasInv_Tacc          -> 0 
    FiboLucasInv_Tder          -> 0 
    FiboLucasInv_TablCol1      -> 0 
    FiboLucasInv_TablCol2      -> 0 
    FiboLucasInv_TablCol3      -> 0 
    FiboLucasInv_TablLcm       -> 0 
    FiboLucasInv_TablGcd       -> 0 
    FiboLucasInv_TablMax       -> 0 
    FiboLucasInv_EvenSum       -> 0 
    FiboLucasInv_AbsSum        -> 0 
    FiboLucasInv_AccSum        -> 0 
    FiboLucasInv_AccRevSum     -> 0 
    FiboLucasInv_AntiDSum      -> 0 
    FiboLucasInv_ColMiddle     -> 0 
    FiboLucasInv_CentralE      -> 0 
    FiboLucasInv_CentralO      -> 0 
    FiboLucasInv_NegHalf       -> 0 
    FiboLucasInv_TransNat0     -> 0 
    FiboLucasInv_TransNat1     -> 0 
    FiboLucasInv_TransSqrs     -> 0 
    FiboLucasInv_BinConv       -> 0 
    FiboLucasInv_InvBinConv    -> 0 
    FiboLucasInv_PolyRow3      -> 0 
    FiboLucasInv_PolyCol3      -> 0 
    FiboLucasInv_PolyDiag      -> 0 
    FiboLucasInv_RevToff11     -> 0 
    FiboLucasInv_RevTrev11     -> 0 
    FiboLucasInv_RevTantidiag  -> 0 
    FiboLucasInv_RevTacc       -> 0 
    FiboLucasInv_RevTalt       -> 0 
    FiboLucasInv_RevTder       -> 0 
    FiboLucasInv_RevEvenSum    -> 0 
    FiboLucasInv_RevOddSum     -> 0 
    FiboLucasInv_RevAccRevSum  -> 0 
    FiboLucasInv_RevAntiDSum   -> 0 
    FiboLucasInv_RevColMiddle  -> 0 
    FiboLucasInv_RevCentralO   -> 0 
    FiboLucasInv_RevNegHalf    -> 0 
    FiboLucasInv_RevTransNat0  -> 0 
    FiboLucasInv_RevTransNat1  -> 0 
    FiboLucasInv_RevTransSqrs  -> 0 
    FiboLucasInv_RevPolyRow3   -> 0 
    FiboLucasInv_RevPolyCol3   -> 0 
    FiboLucasInv_RevPolyDiag   -> 0 
    FiboLucasInv_TablDiag0     -> https://oeis.org/A12
    FiboLucasInv_PolyRow1      -> https://oeis.org/A27
    FiboLucasInv_PosHalf       -> https://oeis.org/A244
    FiboLucasInv_TablDiag2     -> https://oeis.org/A1477
    FiboLucasInv_RevPolyRow1   -> https://oeis.org/A5408
    FiboLucasInv_TablDiag3     -> https://oeis.org/A5843
    FiboLucasInv_TablDiag1     -> https://oeis.org/A55642
    FiboLucasInv_RevPolyRow2   -> https://oeis.org/A56105
    FiboLucasInv_PolyRow2      -> https://oeis.org/A59100
    FiboLucasInv_TablCol0      -> https://oeis.org/A86990
    FiboLucasInv_TablSum       -> https://oeis.org/A86990
    FiboLucasInv_OddSum        -> https://oeis.org/A86990
    FiboLucasInv_Tinv          -> https://oeis.org/A124038
    FiboLucasInv_PolyCol2      -> https://oeis.org/A126982
    FiboLucasInv_Triangle      -> https://oeis.org/A375025
    FiboLucasInv_Talt          -> https://oeis.org/A375025
    FiboLucasInv_AltSum        -> https://oeis.org/A375026

    FiboLucasInv: Distinct: 15, Hits: 17, Misses: 49
'''
