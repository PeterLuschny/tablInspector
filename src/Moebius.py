from functools import cache
from _tabltypes import Table
from Divisibility import divisibility

"""Moebius Matrix.

[0] 1
[1] 0,  1
[2] 0, -1,  1
[3] 0, -1,  0,  1
[4] 0,  0, -1,  0,  1
[5] 0, -1,  0,  0,  0, 1
[6] 0,  1, -1, -1,  0, 0, 1
[7] 0, -1,  0,  0,  0, 0, 0, 1
[8] 0,  0,  0,  0, -1, 0, 0, 0, 1
[9] 0,  0,  0, -1,  0, 0, 0, 0, 0, 1
"""


@cache
def _moebius(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return -1
    return -sum(_moebius(k) for k, i in enumerate(divisibility(n)[: n - 1]) if i != 0)


@cache
def moebius(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = [0 for _ in range(n + 1)]
    r[n] = 1
    for k in range(1, n):
        if n % k == 0:
            r[k] = _moebius(n // k)
    return r


Moebius = Table(
    moebius,
    "Moebius",
    ["A363914", "A054525"],
    "A000000",
    r"M^{-1}(n, k); M(n, k) = [k \le n \ \& \ k | n]",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Moebius)






''' OEIS
    Moebius_Trevinv       -> 0 
    Moebius_Tantidiag     -> 0 
    Moebius_Tacc          -> 0 
    Moebius_BinConv       -> 0 
    Moebius_InvBinConv    -> 0 
    Moebius_RevToff11     -> 0 
    Moebius_RevTrev11     -> 0 
    Moebius_RevTacc       -> 0 
    Moebius_RevTalt       -> 0 
    Moebius_RevTder       -> 0 
    Moebius_RevAntiDSum   -> 0 
    Moebius_RevNegHalf    -> 0 
    Moebius_RevTransSqrs  -> 0 
    Moebius_RevPolyCol3   -> 0 
    Moebius_RevPolyDiag   -> 0 
    Moebius_TablCol0      -> https://oeis.org/A7
    Moebius_TablDiag3     -> https://oeis.org/A7
    Moebius_RevCentralO   -> https://oeis.org/A7
    Moebius_AccSum        -> https://oeis.org/A10
    Moebius_AccRevSum     -> https://oeis.org/A10
    Moebius_TransNat0     -> https://oeis.org/A10
    Moebius_TransNat1     -> https://oeis.org/A10
    Moebius_RevAccRevSum  -> https://oeis.org/A10
    Moebius_RevTransNat0  -> https://oeis.org/A10
    Moebius_RevTransNat1  -> https://oeis.org/A10
    Moebius_Trev          -> https://oeis.org/A12
    Moebius_Trev11        -> https://oeis.org/A12
    Moebius_TablCol2      -> https://oeis.org/A12
    Moebius_TablDiag0     -> https://oeis.org/A12
    Moebius_TablLcm       -> https://oeis.org/A12
    Moebius_TablGcd       -> https://oeis.org/A12
    Moebius_TablMax       -> https://oeis.org/A12
    Moebius_CentralE      -> https://oeis.org/A12
    Moebius_RevTantidiag  -> https://oeis.org/A12
    Moebius_RevPolyRow1   -> https://oeis.org/A12
    Moebius_PolyRow1      -> https://oeis.org/A27
    Moebius_RevPolyRow2   -> https://oeis.org/A27
    Moebius_RevColMiddle  -> https://oeis.org/A35
    Moebius_PolyRow2      -> https://oeis.org/A2378
    Moebius_RevPolyRow3   -> https://oeis.org/A5563
    Moebius_TransSqrs     -> https://oeis.org/A7434
    Moebius_PolyRow3      -> https://oeis.org/A7531
    Moebius_TablCol1      -> https://oeis.org/A8966
    Moebius_TablSum       -> https://oeis.org/A19590
    Moebius_PolyCol2      -> https://oeis.org/A27375
    Moebius_RevPosHalf    -> https://oeis.org/A27375
    Moebius_AbsSum        -> https://oeis.org/A34444
    Moebius_Tinv11        -> https://oeis.org/A51731
    Moebius_PolyCol3      -> https://oeis.org/A54718
    Moebius_RevEvenSum    -> https://oeis.org/A79944
    Moebius_AntiDSum      -> https://oeis.org/A98018
    Moebius_Tinv          -> https://oeis.org/A113704
    Moebius_Trevinv11     -> https://oeis.org/A113998
    Moebius_Tder          -> https://oeis.org/A127448
    Moebius_ColMiddle     -> https://oeis.org/A128174
    Moebius_AltSum        -> https://oeis.org/A130779
    Moebius_EvenSum       -> https://oeis.org/A154272
    Moebius_OddSum        -> https://oeis.org/A154955
    Moebius_Toff11        -> https://oeis.org/A174852
    Moebius_TablDiag1     -> https://oeis.org/A209229
    Moebius_CentralO      -> https://oeis.org/A209229
    Moebius_RevOddSum     -> https://oeis.org/A209229
    Moebius_PolyDiag      -> https://oeis.org/A252764
    Moebius_TablDiag2     -> https://oeis.org/A279329
    Moebius_Triangle      -> https://oeis.org/A363914
    Moebius_Talt          -> https://oeis.org/A363914
    Moebius_TablCol3      -> https://oeis.org/A365807
    Moebius_NegHalf       -> https://oeis.org/A367773
    Moebius_PosHalf       -> https://oeis.org/A367774

    Moebius: Distinct: 33, Hits: 54, Misses: 15
'''
