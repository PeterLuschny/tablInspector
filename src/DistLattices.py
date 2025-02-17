from functools import cache
from _tabltypes import Table


""" Cardinalities of finite distributive lattices.
    [0] 1;
    [1] 1,  1;
    [2] 1,  2,  1;
    [3] 1,  3,  3,  1;
    [4] 1,  5,  6,  4,  1;
    [5] 1,  8, 14, 10,  5, 1;
    [6] 1, 13, 31, 30, 15, 6, 1;
    [7] 1, 21, 70, 85, 55, 21, 7, 1;
"""

@cache
def _distlattices(n: int, k: int) -> int:
    if k == 0 or n == 0: return 1

    s = [_distlattices(2 * j, k - 1) * _distlattices(n - 1 - 2 * j, k) 
            for j in range(1 + (n - 1) // 2)]
    return sum(s) + _distlattices(n, k - 1)


# TODO Give a row based recurrence for this.
@cache
def distlattices(n: int) -> list[int]:
    return [_distlattices(n - k, k) for k in range(n + 1)]


DistLattices = Table(
    distlattices, 
    "DistLattices", 
    ["A050446", "A050447"],
    "A000000", 
    r""
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(DistLattices)




''' OEIS
    DistLattices_Talt          -> https://oeis.org/A-999999
    DistLattices_Tinv          -> 0 
    DistLattices_Tinvrev       -> 0 
    DistLattices_Trevinv       -> 0 
    DistLattices_Toff11        -> 0 
    DistLattices_Trev11        -> 0 
    DistLattices_Tinv11        -> 0 
    DistLattices_Trevinv11     -> 0 
    DistLattices_Tantidiag     -> 0 
    DistLattices_Tacc          -> 0 
    DistLattices_Tder          -> 0 
    DistLattices_TablLcm       -> 0 
    DistLattices_TablMax       -> 0 
    DistLattices_EvenSum       -> 0 
    DistLattices_OddSum        -> 0 
    DistLattices_AltSum        -> 0 
    DistLattices_AccSum        -> 0 
    DistLattices_AccRevSum     -> 0 
    DistLattices_AntiDSum      -> 0 
    DistLattices_ColMiddle     -> 0 
    DistLattices_PosHalf       -> 0 
    DistLattices_NegHalf       -> 0 
    DistLattices_TransNat0     -> 0 
    DistLattices_TransNat1     -> 0 
    DistLattices_TransSqrs     -> 0 
    DistLattices_BinConv       -> 0 
    DistLattices_InvBinConv    -> 0 
    DistLattices_PolyCol2      -> 0 
    DistLattices_PolyCol3      -> 0 
    DistLattices_PolyDiag      -> 0 
    DistLattices_RevToff11     -> 0 
    DistLattices_RevTrev11     -> 0 
    DistLattices_RevTinv11     -> 0 
    DistLattices_RevTantidiag  -> 0 
    DistLattices_RevTacc       -> 0 
    DistLattices_RevTder       -> 0 
    DistLattices_RevEvenSum    -> 0 
    DistLattices_RevOddSum     -> 0 
    DistLattices_RevAccRevSum  -> 0 
    DistLattices_RevAntiDSum   -> 0 
    DistLattices_RevColMiddle  -> 0 
    DistLattices_RevCentralO   -> 0 
    DistLattices_RevPosHalf    -> 0 
    DistLattices_RevNegHalf    -> 0 
    DistLattices_RevTransNat0  -> 0 
    DistLattices_RevTransNat1  -> 0 
    DistLattices_RevTransSqrs  -> 0 
    DistLattices_RevPolyCol3   -> 0 
    DistLattices_RevPolyDiag   -> 0 
    DistLattices_TablCol0      -> https://oeis.org/A12
    DistLattices_TablDiag0     -> https://oeis.org/A12
    DistLattices_TablDiag1     -> https://oeis.org/A27
    DistLattices_PolyRow1      -> https://oeis.org/A27
    DistLattices_RevPolyRow1   -> https://oeis.org/A27
    DistLattices_TablCol1      -> https://oeis.org/A45
    DistLattices_TablDiag2     -> https://oeis.org/A217
    DistLattices_PolyRow2      -> https://oeis.org/A290
    DistLattices_RevPolyRow2   -> https://oeis.org/A290
    DistLattices_TablDiag3     -> https://oeis.org/A330
    DistLattices_PolyRow3      -> https://oeis.org/A578
    DistLattices_RevPolyRow3   -> https://oeis.org/A578
    DistLattices_TablCol2      -> https://oeis.org/A6356
    DistLattices_TablCol3      -> https://oeis.org/A6357
    DistLattices_Triangle      -> https://oeis.org/A50446
    DistLattices_Trev          -> https://oeis.org/A50447
    DistLattices_RevTalt       -> https://oeis.org/A50447
    DistLattices_TablGcd       -> https://oeis.org/A99563
    DistLattices_CentralO      -> https://oeis.org/A276313
    DistLattices_TablSum       -> https://oeis.org/A373353
    DistLattices_AbsSum        -> https://oeis.org/A373353
    DistLattices_CentralE      -> https://oeis.org/A373659

    DistLattices: Distinct: 17, Hits: 23, Misses: 48
'''
