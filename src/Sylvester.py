from functools import cache
from Binomial import Binomial
from StirlingCycle import StirlingCycle
from _tabltypes import Table

"""Sylvester polynomials.

[0] 1;
[1] 0,   2;
[2] 0,   1,    4;
[3] 0,   2,    6,    8;
[4] 0,   6,   19,   24,   16;
[5] 0,  24,   80,  110,   80,   32;
[6] 0, 120,  418,  615,  500,  240,  64;
[7] 0, 720, 2604, 4046, 3570, 1960, 672, 128;
"""


@cache
def sylvester(n: int) -> list[int]:
    def s(n: int, k: int) -> int:
        return sum(Binomial(n, k - j) * StirlingCycle(n - k + j, j) 
               for j in range(k + 1) )
    return [s(n, k) for k in range(n + 1)]


Sylvester = Table(
    sylvester,
    "Sylvester",
    ["A341101"],
    "",
    r"\sum_{j=0}^{k} (-1)^{n-k} \binom{n}{k-j} {n - k + j \brack j}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Sylvester)






''' OEIS
    Sylvester_Trev          -> 0 
    Sylvester_Toff11        -> 0 
    Sylvester_Trev11        -> 0 
    Sylvester_Tantidiag     -> 0 
    Sylvester_Tacc          -> 0 
    Sylvester_Tder          -> 0 
    Sylvester_TablCol2      -> 0 
    Sylvester_TablCol3      -> 0 
    Sylvester_TablDiag2     -> 0 
    Sylvester_TablDiag3     -> 0 
    Sylvester_TablLcm       -> 0 
    Sylvester_TablMax       -> 0 
    Sylvester_EvenSum       -> 0 
    Sylvester_OddSum        -> 0 
    Sylvester_AccSum        -> 0 
    Sylvester_AccRevSum     -> 0 
    Sylvester_AntiDSum      -> 0 
    Sylvester_ColMiddle     -> 0 
    Sylvester_CentralE      -> 0 
    Sylvester_CentralO      -> 0 
    Sylvester_NegHalf       -> 0 
    Sylvester_TransNat0     -> 0 
    Sylvester_TransNat1     -> 0 
    Sylvester_TransSqrs     -> 0 
    Sylvester_BinConv       -> 0 
    Sylvester_InvBinConv    -> 0 
    Sylvester_PolyRow3      -> 0 
    Sylvester_PolyCol3      -> 0 
    Sylvester_RevToff11     -> 0 
    Sylvester_RevTrev11     -> 0 
    Sylvester_RevTantidiag  -> 0 
    Sylvester_RevTacc       -> 0 
    Sylvester_RevTalt       -> 0 
    Sylvester_RevTder       -> 0 
    Sylvester_RevEvenSum    -> 0 
    Sylvester_RevAccRevSum  -> 0 
    Sylvester_RevAntiDSum   -> 0 
    Sylvester_RevColMiddle  -> 0 
    Sylvester_RevCentralO   -> 0 
    Sylvester_RevTransNat0  -> 0 
    Sylvester_RevTransNat1  -> 0 
    Sylvester_RevTransSqrs  -> 0 
    Sylvester_RevPolyDiag   -> 0 
    Sylvester_TablCol0      -> https://oeis.org/A7
    Sylvester_AltSum        -> https://oeis.org/A27
    Sylvester_RevPolyRow2   -> https://oeis.org/A27
    Sylvester_TablGcd       -> https://oeis.org/A34
    Sylvester_TablDiag0     -> https://oeis.org/A79
    Sylvester_TablCol1      -> https://oeis.org/A142
    Sylvester_TablSum       -> https://oeis.org/A522
    Sylvester_AbsSum        -> https://oeis.org/A522
    Sylvester_TablDiag1     -> https://oeis.org/A1788
    Sylvester_PolyRow1      -> https://oeis.org/A5843
    Sylvester_RevNegHalf    -> https://oeis.org/A7466
    Sylvester_PolyRow2      -> https://oeis.org/A7742
    Sylvester_RevOddSum     -> https://oeis.org/A38155
    Sylvester_RevPolyRow1   -> https://oeis.org/A55642
    Sylvester_PolyCol2      -> https://oeis.org/A81923
    Sylvester_RevPosHalf    -> https://oeis.org/A81923
    Sylvester_PosHalf       -> https://oeis.org/A84262
    Sylvester_RevPolyRow3   -> https://oeis.org/A137882
    Sylvester_PolyDiag      -> https://oeis.org/A295183
    Sylvester_Triangle      -> https://oeis.org/A341101
    Sylvester_Talt          -> https://oeis.org/A341101
    Sylvester_RevPolyCol3   -> https://oeis.org/A346258

    Sylvester: Distinct: 19, Hits: 22, Misses: 43
'''
