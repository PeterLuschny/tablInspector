from functools import cache
from _tabltypes import Table

"""Lehmer-Comtet of 2nd kind, unsigned.


[0] 1;
[1] 0,      1;
[2] 0,      1,      1;
[3] 0,      4,      3,      1;
[4] 0,     27,     19,      6,     1;
[5] 0,    256,    175,     55,    10,    1;
[6] 0,   3125,   2101,    660,   125,   15,   1;
[7] 0,  46656,  31031,   9751,  1890,  245,  21,  1;
[8] 0, 823543, 543607, 170898, 33621, 4550, 434, 28, 1;
"""


@cache
def t(n: int, k: int, m: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return n**k
    return m * t(n, k - 1, m) + t(n - 1, k, m + 1)


@cache
def lehmer(n: int) -> list[int]:
    return [t(k - 1, n - k, n - k) if n != k else 1 for k in range(n + 1)]


Lehmer = Table(
    lehmer,
    "Lehmer",
    ["A354794", "A039621"],
    "A000000",
    r"is(n = k)\ ? \ 1 : \sum_{j=0}^{k-1} (-1)^{j}(n-j-1)^{n-1}/(j! (k-1-j)!)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    # TODO Needs a more efficient implementation.
    InspectTable(Lehmer)


''' OEIS
    Lehmer_Trev          -> 0 
    Lehmer_Trev11        -> 0 
    Lehmer_Tantidiag     -> 0 
    Lehmer_Tacc          -> 0 
    Lehmer_Tder          -> 0 
    Lehmer_TablDiag3     -> 0 
    Lehmer_TablLcm       -> 0 
    Lehmer_EvenSum       -> 0 
    Lehmer_OddSum        -> 0 
    Lehmer_AccSum        -> 0 
    Lehmer_AccRevSum     -> 0 
    Lehmer_AntiDSum      -> 0 
    Lehmer_ColMiddle     -> 0 
    Lehmer_CentralE      -> 0 
    Lehmer_CentralO      -> 0 
    Lehmer_PosHalf       -> 0 
    Lehmer_NegHalf       -> 0 
    Lehmer_TransNat0     -> 0 
    Lehmer_TransNat1     -> 0 
    Lehmer_TransSqrs     -> 0 
    Lehmer_BinConv       -> 0 
    Lehmer_InvBinConv    -> 0 
    Lehmer_PolyRow3      -> 0 
    Lehmer_PolyCol2      -> 0 
    Lehmer_PolyCol3      -> 0 
    Lehmer_PolyDiag      -> 0 
    Lehmer_RevToff11     -> 0 
    Lehmer_RevTrev11     -> 0 
    Lehmer_RevTantidiag  -> 0 
    Lehmer_RevTacc       -> 0 
    Lehmer_RevTalt       -> 0 
    Lehmer_RevTder       -> 0 
    Lehmer_RevEvenSum    -> 0 
    Lehmer_RevOddSum     -> 0 
    Lehmer_RevAccRevSum  -> 0 
    Lehmer_RevAntiDSum   -> 0 
    Lehmer_RevColMiddle  -> 0 
    Lehmer_RevCentralO   -> 0 
    Lehmer_RevNegHalf    -> 0 
    Lehmer_RevTransNat0  -> 0 
    Lehmer_RevTransNat1  -> 0 
    Lehmer_RevTransSqrs  -> 0 
    Lehmer_RevPolyCol3   -> 0 
    Lehmer_RevPolyDiag   -> 0 
    Lehmer_TablCol0      -> https://oeis.org/A7
    Lehmer_TablDiag0     -> https://oeis.org/A12
    Lehmer_TablGcd       -> https://oeis.org/A12
    Lehmer_RevPolyRow1   -> https://oeis.org/A12
    Lehmer_PolyRow1      -> https://oeis.org/A27
    Lehmer_RevPolyRow2   -> https://oeis.org/A27
    Lehmer_TablDiag1     -> https://oeis.org/A217
    Lehmer_TablCol1      -> https://oeis.org/A312
    Lehmer_TablMax       -> https://oeis.org/A312
    Lehmer_PolyRow2      -> https://oeis.org/A2378
    Lehmer_Tinv11        -> https://oeis.org/A8296
    Lehmer_RevPolyRow3   -> https://oeis.org/A33951
    Lehmer_Toff11        -> https://oeis.org/A39621
    Lehmer_TablCol2      -> https://oeis.org/A45531
    Lehmer_TablSum       -> https://oeis.org/A195979
    Lehmer_AbsSum        -> https://oeis.org/A195979
    Lehmer_TablDiag2     -> https://oeis.org/A215862
    Lehmer_TablCol3      -> https://oeis.org/A281596
    Lehmer_AltSum        -> https://oeis.org/A290219
    Lehmer_Triangle      -> https://oeis.org/A354794
    Lehmer_Talt          -> https://oeis.org/A354794
    Lehmer_Tinv          -> https://oeis.org/A354795

    Lehmer: Distinct: 17, Hits: 22, Misses: 44
'''
