from functools import cache
from _tabltypes import Table

"""Leibniz's Triangle, FallingFactorial(n + 1, n) / (k! * (n - k)!).

[0]  1
[1]  2   2
[2]  3   6    3
[3]  4  12   12    4
[4]  5  20   30   20    5
[5]  6  30   60   60   30    6
[6]  7  42  105  140  105   42    7
[7]  8  56  168  280  280  168   56    8
[8]  9  72  252  504  630  504  252   72   9
[9] 10  90  360  840 1260 1260  840  360  90  10
"""


@cache
def leibniz(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = leibniz(n - 1) + [n + 1]
    row[0] = row[n] = n + 1
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


Leibniz = Table(
    leibniz, 
    "Leibniz", 
    ["A003506"], 
    "", 
    r"(k+1) \, \binom{n+1}{k+1}"
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Leibniz)






''' OEIS
    Leibniz_Toff11        -> 0 
    Leibniz_Trev11        -> 0 
    Leibniz_Tacc          -> 0 
    Leibniz_TransSqrs     -> 0 
    Leibniz_RevToff11     -> 0 
    Leibniz_RevTrev11     -> 0 
    Leibniz_RevTacc       -> 0 
    Leibniz_RevTransSqrs  -> 0 
    Leibniz_AltSum        -> https://oeis.org/A7
    Leibniz_TablCol0      -> https://oeis.org/A27
    Leibniz_TablDiag0     -> https://oeis.org/A27
    Leibniz_TablGcd       -> https://oeis.org/A27
    Leibniz_NegHalf       -> https://oeis.org/A27
    Leibniz_RevNegHalf    -> https://oeis.org/A27
    Leibniz_PolyDiag      -> https://oeis.org/A312
    Leibniz_RevPolyDiag   -> https://oeis.org/A312
    Leibniz_AntiDSum      -> https://oeis.org/A1629
    Leibniz_RevAntiDSum   -> https://oeis.org/A1629
    Leibniz_TablSum       -> https://oeis.org/A1787
    Leibniz_AbsSum        -> https://oeis.org/A1787
    Leibniz_AccSum        -> https://oeis.org/A1788
    Leibniz_AccRevSum     -> https://oeis.org/A1788
    Leibniz_TransNat1     -> https://oeis.org/A1788
    Leibniz_RevAccRevSum  -> https://oeis.org/A1788
    Leibniz_RevTransNat1  -> https://oeis.org/A1788
    Leibniz_TransNat0     -> https://oeis.org/A1815
    Leibniz_RevTransNat0  -> https://oeis.org/A1815
    Leibniz_TablCol1      -> https://oeis.org/A2378
    Leibniz_TablDiag1     -> https://oeis.org/A2378
    Leibniz_CentralE      -> https://oeis.org/A2457
    Leibniz_InvBinConv    -> https://oeis.org/A2457
    Leibniz_PolyCol3      -> https://oeis.org/A2697
    Leibniz_RevPolyCol3   -> https://oeis.org/A2697
    Leibniz_TablLcm       -> https://oeis.org/A3418
    Leibniz_Triangle      -> https://oeis.org/A3506
    Leibniz_Trev          -> https://oeis.org/A3506
    Leibniz_Talt          -> https://oeis.org/A3506
    Leibniz_RevTalt       -> https://oeis.org/A3506
    Leibniz_CentralO      -> https://oeis.org/A5430
    Leibniz_RevCentralO   -> https://oeis.org/A5430
    Leibniz_PolyRow1      -> https://oeis.org/A5843
    Leibniz_RevPolyRow1   -> https://oeis.org/A5843
    Leibniz_PosHalf       -> https://oeis.org/A27471
    Leibniz_PolyCol2      -> https://oeis.org/A27471
    Leibniz_RevPosHalf    -> https://oeis.org/A27471
    Leibniz_TablCol2      -> https://oeis.org/A27480
    Leibniz_TablDiag2     -> https://oeis.org/A27480
    Leibniz_PolyRow2      -> https://oeis.org/A33428
    Leibniz_RevPolyRow2   -> https://oeis.org/A33428
    Leibniz_PolyRow3      -> https://oeis.org/A33430
    Leibniz_RevPolyRow3   -> https://oeis.org/A33430
    Leibniz_TablCol3      -> https://oeis.org/A33488
    Leibniz_TablDiag3     -> https://oeis.org/A33488
    Leibniz_BinConv       -> https://oeis.org/A37965
    Leibniz_EvenSum       -> https://oeis.org/A57711
    Leibniz_OddSum        -> https://oeis.org/A57711
    Leibniz_RevEvenSum    -> https://oeis.org/A57711
    Leibniz_RevOddSum     -> https://oeis.org/A57711
    Leibniz_TablMax       -> https://oeis.org/A100071
    Leibniz_ColMiddle     -> https://oeis.org/A100071
    Leibniz_RevColMiddle  -> https://oeis.org/A100071
    Leibniz_Tantidiag     -> https://oeis.org/A128502
    Leibniz_RevTantidiag  -> https://oeis.org/A128502
    Leibniz_Tder          -> https://oeis.org/A140880
    Leibniz_RevTder       -> https://oeis.org/A140880

    Leibniz: Distinct: 25, Hits: 57, Misses: 8
'''
