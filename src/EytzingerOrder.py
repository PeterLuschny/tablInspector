from functools import cache
from _tabltypes import Table

"""
    The Eytzinger order arranges elements of an array
    so that a binary search can be performed starting with
    index k = 1 and at a given k step to 2*k or 2*k + 1,
    depending on whether the target is smaller or larger
    than the element at k.

    Args: n, length of array
    Returns: The given array in Eytzinger order.

    Variant 1, A375825, mostly used when (1, 1)-based.
    [0] [0]
    [1] [0, 1]
    [2] [0, 2, 1]
    [3] [0, 2, 1, 3]
    [4] [0, 3, 2, 4, 1]
    [5] [0, 4, 2, 5, 1, 3]
    [6] [0, 4, 2, 6, 1, 3, 5]
    [7] [0, 4, 2, 6, 1, 3, 5, 7]
    [8] [0, 5, 3, 7, 2, 4, 6, 8, 1]
    [9] [0, 6, 4, 8, 2, 5, 7, 9, 1, 3]

    Variant 2, we use this one:
    [0] [0]
    [1] [1, 0]
    [2] [1, 0, 2]
    [3] [2, 1, 3, 0]
    [4] [3, 1, 4, 0, 2]
    [5] [3, 1, 5, 0, 2, 4]
    [6] [3, 1, 5, 0, 2, 4, 6]
    [7] [4, 2, 6, 1, 3, 5, 7, 0]
    [8] [5, 3, 7, 1, 4, 6, 8, 0, 2]
    [9] [6, 3, 8, 1, 5, 7, 9, 0, 2, 4]
"""


# $cache  #  Variant 1, not used here!
def Xeytzingerorder(n: int) -> list[int]:
    row = [0] * (n + 1)

    def e_rec(k: int, i: int) -> int:
        if k <= n:
            i = e_rec(2 * k, i)
            row[k] = i
            i = e_rec(2 * k + 1, i + 1)
        return i
    e_rec(1, 1)
    return row


@cache
def eytzingerorder(n: int) -> list[int]:
    row = [0] * (n + 1)
    def e_rec(k: int, i: int) -> int:
        if k <= n + 1:
            i = e_rec(2 * k, i)
            row[k - 1] = i
            i = e_rec(2 * k + 1, i + 1)
        return i
    e_rec(1, 0)
    return row


EytzingerOrder = Table(
    eytzingerorder, 
    "EytzingerOrder", 
    ["A375825"],
    "",
    r"%%"
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(EytzingerOrder)






''' OEIS
    EytzingerOrder_Trev          -> 0 
    EytzingerOrder_Toff11        -> 0 
    EytzingerOrder_Trev11        -> 0 
    EytzingerOrder_Tantidiag     -> 0 
    EytzingerOrder_Tacc          -> 0 
    EytzingerOrder_Talt          -> 0 
    EytzingerOrder_Tder          -> 0 
    EytzingerOrder_TablCol1      -> 0 
    EytzingerOrder_TablCol2      -> 0 
    EytzingerOrder_TablCol3      -> 0 
    EytzingerOrder_TablDiag0     -> 0 
    EytzingerOrder_TablDiag1     -> 0 
    EytzingerOrder_TablDiag2     -> 0 
    EytzingerOrder_TablDiag3     -> 0 
    EytzingerOrder_EvenSum       -> 0 
    EytzingerOrder_OddSum        -> 0 
    EytzingerOrder_AltSum        -> 0 
    EytzingerOrder_AccSum        -> 0 
    EytzingerOrder_AccRevSum     -> 0 
    EytzingerOrder_AntiDSum      -> 0 
    EytzingerOrder_ColMiddle     -> 0 
    EytzingerOrder_CentralE      -> 0 
    EytzingerOrder_CentralO      -> 0 
    EytzingerOrder_PosHalf       -> 0 
    EytzingerOrder_NegHalf       -> 0 
    EytzingerOrder_TransNat0     -> 0 
    EytzingerOrder_TransNat1     -> 0 
    EytzingerOrder_TransSqrs     -> 0 
    EytzingerOrder_BinConv       -> 0 
    EytzingerOrder_InvBinConv    -> 0 
    EytzingerOrder_PolyCol2      -> 0 
    EytzingerOrder_PolyCol3      -> 0 
    EytzingerOrder_PolyDiag      -> 0 
    EytzingerOrder_RevToff11     -> 0 
    EytzingerOrder_RevTrev11     -> 0 
    EytzingerOrder_RevTantidiag  -> 0 
    EytzingerOrder_RevTacc       -> 0 
    EytzingerOrder_RevTalt       -> 0 
    EytzingerOrder_RevTder       -> 0 
    EytzingerOrder_RevEvenSum    -> 0 
    EytzingerOrder_RevOddSum     -> 0 
    EytzingerOrder_RevAccRevSum  -> 0 
    EytzingerOrder_RevAntiDSum   -> 0 
    EytzingerOrder_RevColMiddle  -> 0 
    EytzingerOrder_RevCentralO   -> 0 
    EytzingerOrder_RevPosHalf    -> 0 
    EytzingerOrder_RevNegHalf    -> 0 
    EytzingerOrder_RevTransNat0  -> 0 
    EytzingerOrder_RevTransNat1  -> 0 
    EytzingerOrder_RevTransSqrs  -> 0 
    EytzingerOrder_RevPolyRow3   -> 0 
    EytzingerOrder_RevPolyCol3   -> 0 
    EytzingerOrder_RevPolyDiag   -> 0 
    EytzingerOrder_TablGcd       -> https://oeis.org/A12
    EytzingerOrder_PolyRow1      -> https://oeis.org/A12
    EytzingerOrder_TablMax       -> https://oeis.org/A27
    EytzingerOrder_RevPolyRow1   -> https://oeis.org/A27
    EytzingerOrder_TablSum       -> https://oeis.org/A217
    EytzingerOrder_AbsSum        -> https://oeis.org/A217
    EytzingerOrder_TablLcm       -> https://oeis.org/A3418
    EytzingerOrder_PolyRow2      -> https://oeis.org/A58331
    EytzingerOrder_RevPolyRow2   -> https://oeis.org/A59100
    EytzingerOrder_PolyRow3      -> https://oeis.org/A131649
    EytzingerOrder_TablCol0      -> https://oeis.org/A279521
    EytzingerOrder_Triangle      -> https://oeis.org/A375825

    EytzingerOrder: Distinct: 10, Hits: 12, Misses: 53
'''
