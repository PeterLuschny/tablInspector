from functools import cache
from _tabltypes import Table

"""Euler triangle.

[0]     1
[1]    -1      1
[2]     1     -2      1
[3]    -2      3     -3      1
[4]     5     -8      6     -4      1
[5]   -16     25    -20     10     -5     1
[6]    61    -96     75    -40     15    -6     1
[7]  -272    427   -336    175    -70    21    -7    1
[8]  1385  -2176   1708   -896    350  -112    28   -8   1
[9] -7936  12465  -9792   5124  -2016   630  -168   36  -9   1
"""


@cache
def euler(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = euler(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))

    return row


Euler = Table(
    euler,
    "Euler",
    ["A363394", "A247453", "A109449"],
    "A000000",
    r"\binom{n}{k} 2^{n-k} \text{Euler}_{n-k}(1/2)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Euler)

# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials


''' OEIS
    Euler_Toff11        -> 0 
    Euler_Trev11        -> 0 
    Euler_Tinv11        -> 0 
    Euler_Tantidiag     -> 0 
    Euler_Tacc          -> 0 
    Euler_TablCol3      -> 0 
    Euler_TablLcm       -> 0 
    Euler_AccSum        -> 0 
    Euler_ColMiddle     -> 0 
    Euler_CentralO      -> 0 
    Euler_TransNat0     -> 0 
    Euler_TransSqrs     -> 0 
    Euler_BinConv       -> 0 
    Euler_InvBinConv    -> 0 
    Euler_PolyCol3      -> 0 
    Euler_PolyDiag      -> 0 
    Euler_RevToff11     -> 0 
    Euler_RevTrev11     -> 0 
    Euler_RevTantidiag  -> 0 
    Euler_RevTacc       -> 0 
    Euler_RevTder       -> 0 
    Euler_RevAccRevSum  -> 0 
    Euler_RevAntiDSum   -> 0 
    Euler_RevColMiddle  -> 0 
    Euler_RevCentralO   -> 0 
    Euler_RevTransNat0  -> 0 
    Euler_RevTransNat1  -> 0 
    Euler_RevTransSqrs  -> 0 
    Euler_RevPolyCol3   -> 0 
    Euler_RevPolyDiag   -> 0 
    Euler_TablDiag0     -> https://oeis.org/A12
    Euler_TablGcd       -> https://oeis.org/A12
    Euler_TablDiag1     -> https://oeis.org/A27
    Euler_PolyRow1      -> https://oeis.org/A27
    Euler_RevPolyRow1   -> https://oeis.org/A27
    Euler_TablCol0      -> https://oeis.org/A111
    Euler_TablDiag2     -> https://oeis.org/A217
    Euler_PolyRow2      -> https://oeis.org/A290
    Euler_RevPolyRow2   -> https://oeis.org/A290
    Euler_AltSum        -> https://oeis.org/A667
    Euler_AbsSum        -> https://oeis.org/A667
    Euler_RevNegHalf    -> https://oeis.org/A752
    Euler_NegHalf       -> https://oeis.org/A834
    Euler_RevEvenSum    -> https://oeis.org/A3701
    Euler_RevPolyRow3   -> https://oeis.org/A5898
    Euler_TablDiag3     -> https://oeis.org/A7290
    Euler_RevOddSum     -> https://oeis.org/A9739
    Euler_OddSum        -> https://oeis.org/A62161
    Euler_TablSum       -> https://oeis.org/A62162
    Euler_EvenSum       -> https://oeis.org/A62272
    Euler_TablCol1      -> https://oeis.org/A65619
    Euler_TablMax       -> https://oeis.org/A65619
    Euler_PolyRow3      -> https://oeis.org/A68601
    Euler_PolyCol2      -> https://oeis.org/A102590
    Euler_Triangle      -> https://oeis.org/A109449
    Euler_Tinv          -> https://oeis.org/A109449
    Euler_Talt          -> https://oeis.org/A109449
    Euler_TablCol2      -> https://oeis.org/A162171
    Euler_Tder          -> https://oeis.org/A294033
    Euler_AccRevSum     -> https://oeis.org/A337443
    Euler_TransNat1     -> https://oeis.org/A337443
    Euler_PosHalf       -> https://oeis.org/A343843
    Euler_AntiDSum      -> https://oeis.org/A343845
    Euler_CentralE      -> https://oeis.org/A343846
    Euler_Trev          -> https://oeis.org/A363394
    Euler_RevTalt       -> https://oeis.org/A363394

    Euler: Distinct: 27, Hits: 36, Misses: 30
'''
