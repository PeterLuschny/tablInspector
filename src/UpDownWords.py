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
def updownwords(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [1] * (n + 1)
    for k in range(1, n):
        a = (n - k - 1) // 2 + 1
        prev = updownwords(n - 1)[k - 1]
        s = sum(updownwords(2 * j + k - 1)[k - 1] * updownwords(n - 1 - 2 * j)[k]
                for j in range(a))
        row[k] = prev + s
    return row


UpDownWords = Table(
    updownwords, 
    "UpDownWords", 
    ["A050446", "A050447"],
    "A000000", 
    r""
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(UpDownWords)




''' OEIS
    updownwords_Tinv          -> 0 
    updownwords_Tinvrev       -> 0 
    updownwords_Trevinv       -> 0 
    updownwords_Toff11        -> 0 
    updownwords_Trev11        -> 0 
    updownwords_Tinv11        -> 0 
    updownwords_Trevinv11     -> 0 
    updownwords_Tantidiag     -> 0 
    updownwords_Tacc          -> 0 
    updownwords_Tder          -> 0 
    updownwords_TablLcm       -> 0 
    updownwords_TablMax       -> 0 
    updownwords_EvenSum       -> 0 
    updownwords_OddSum        -> 0 
    updownwords_AltSum        -> 0 
    updownwords_AccSum        -> 0 
    updownwords_AccRevSum     -> 0 
    updownwords_AntiDSum      -> 0 
    updownwords_ColMiddle     -> 0 
    updownwords_PosHalf       -> 0 
    updownwords_NegHalf       -> 0 
    updownwords_TransNat0     -> 0 
    updownwords_TransNat1     -> 0 
    updownwords_TransSqrs     -> 0 
    updownwords_BinConv       -> 0 
    updownwords_InvBinConv    -> 0 
    updownwords_PolyCol2      -> 0 
    updownwords_PolyCol3      -> 0 
    updownwords_PolyDiag      -> 0 
    updownwords_RevToff11     -> 0 
    updownwords_RevTrev11     -> 0 
    updownwords_RevTinv11     -> 0 
    updownwords_RevTantidiag  -> 0 
    updownwords_RevTacc       -> 0 
    updownwords_RevTder       -> 0 
    updownwords_RevEvenSum    -> 0 
    updownwords_RevOddSum     -> 0 
    updownwords_RevAccRevSum  -> 0 
    updownwords_RevAntiDSum   -> 0 
    updownwords_RevColMiddle  -> 0 
    updownwords_RevCentralO   -> 0 
    updownwords_RevPosHalf    -> 0 
    updownwords_RevNegHalf    -> 0 
    updownwords_RevTransNat0  -> 0 
    updownwords_RevTransNat1  -> 0 
    updownwords_RevTransSqrs  -> 0 
    updownwords_RevPolyCol3   -> 0 
    updownwords_RevPolyDiag   -> 0 
    updownwords_TablCol0      -> https://oeis.org/A12
    updownwords_TablDiag0     -> https://oeis.org/A12
    updownwords_TablDiag1     -> https://oeis.org/A27
    updownwords_PolyRow1      -> https://oeis.org/A27
    updownwords_RevPolyRow1   -> https://oeis.org/A27
    updownwords_TablCol1      -> https://oeis.org/A45
    updownwords_TablDiag2     -> https://oeis.org/A217
    updownwords_PolyRow2      -> https://oeis.org/A290
    updownwords_RevPolyRow2   -> https://oeis.org/A290
    updownwords_TablDiag3     -> https://oeis.org/A330
    updownwords_PolyRow3      -> https://oeis.org/A578
    updownwords_RevPolyRow3   -> https://oeis.org/A578
    updownwords_TablCol2      -> https://oeis.org/A6356
    updownwords_TablCol3      -> https://oeis.org/A6357
    updownwords_Triangle      -> https://oeis.org/A50446
    updownwords_Talt          -> https://oeis.org/A50446
    updownwords_Trev          -> https://oeis.org/A50447
    updownwords_RevTalt       -> https://oeis.org/A50447
    updownwords_TablGcd       -> https://oeis.org/A99563
    updownwords_CentralO      -> https://oeis.org/A276313
    updownwords_TablSum       -> https://oeis.org/A373353
    updownwords_AbsSum        -> https://oeis.org/A373353
    updownwords_CentralE      -> https://oeis.org/A373659

    updownwords: Distinct: 16, Hits: 23, Misses: 48
'''
