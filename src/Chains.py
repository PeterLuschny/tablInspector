from functools import cache
from _tabltypes import Table

"""Chains of length k in partially ordered set 
formed from subsets of n-set by inclusion.

0  [  1]
1  [  2,    1]
2  [  4,    5,     2]
3  [  8,   19,    18,     6]
4  [ 16,   65,   110,    84,    24]
5  [ 32,  211,   570,   750,   480,   120]
6  [ 64,  665,  2702,  5460,  5880,  3240,   720]
7  [128, 2059, 12138, 35406, 57120, 52080, 25200, 5040]
"""


@cache
def chains(n: int) -> list[int]:
    if n == 0:
        return [1]

    ch = chains(n - 1) + [0]
    row = ch.copy()
    row[0] = 2 * ch[0]
    row[n] = n * ch[n - 1]

    for k in range(n - 1, 0, -1):
        row[k] = k * ch[k - 1] + (k + 2) * ch[k]

    return row


Chains = Table(
    chains, 
    "Chains", 
    ["A038719"], 
    "",
    r"\left({n+2 \brace k+2} -  {n+1 \brace k+2} \right)\, k!"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Chains)






''' OEIS
    Chains_Trev          -> 0 
    Chains_Toff11        -> 0 
    Chains_Trev11        -> 0 
    Chains_Tantidiag     -> 0 
    Chains_Tacc          -> 0 
    Chains_Tder          -> 0 
    Chains_TablCol3      -> 0 
    Chains_TablDiag2     -> 0 
    Chains_TablDiag3     -> 0 
    Chains_TablLcm       -> 0 
    Chains_TablMax       -> 0 
    Chains_AccSum        -> 0 
    Chains_AntiDSum      -> 0 
    Chains_ColMiddle     -> 0 
    Chains_CentralE      -> 0 
    Chains_CentralO      -> 0 
    Chains_PosHalf       -> 0 
    Chains_TransNat0     -> 0 
    Chains_TransSqrs     -> 0 
    Chains_InvBinConv    -> 0 
    Chains_PolyRow3      -> 0 
    Chains_PolyDiag      -> 0 
    Chains_RevToff11     -> 0 
    Chains_RevTrev11     -> 0 
    Chains_RevTantidiag  -> 0 
    Chains_RevTacc       -> 0 
    Chains_RevTalt       -> 0 
    Chains_RevTder       -> 0 
    Chains_RevEvenSum    -> 0 
    Chains_RevOddSum     -> 0 
    Chains_RevAccRevSum  -> 0 
    Chains_RevAntiDSum   -> 0 
    Chains_RevColMiddle  -> 0 
    Chains_RevCentralO   -> 0 
    Chains_RevTransNat0  -> 0 
    Chains_RevTransNat1  -> 0 
    Chains_RevTransSqrs  -> 0 
    Chains_RevPolyRow3   -> 0 
    Chains_RevPolyCol3   -> 0 
    Chains_RevPolyDiag   -> 0 
    Chains_TablGcd       -> https://oeis.org/A12
    Chains_AltSum        -> https://oeis.org/A12
    Chains_PolyRow1      -> https://oeis.org/A27
    Chains_TablCol0      -> https://oeis.org/A79
    Chains_TablDiag0     -> https://oeis.org/A142
    Chains_BinConv       -> https://oeis.org/A272
    Chains_EvenSum       -> https://oeis.org/A629
    Chains_TablCol1      -> https://oeis.org/A1047
    Chains_OddSum        -> https://oeis.org/A2050
    Chains_RevPolyRow1   -> https://oeis.org/A5408
    Chains_TablSum       -> https://oeis.org/A7047
    Chains_AbsSum        -> https://oeis.org/A7047
    Chains_Triangle      -> https://oeis.org/A38719
    Chains_Talt          -> https://oeis.org/A38719
    Chains_TablDiag1     -> https://oeis.org/A38720
    Chains_TablCol2      -> https://oeis.org/A38721
    Chains_RevNegHalf    -> https://oeis.org/A52841
    Chains_RevPolyRow2   -> https://oeis.org/A54552
    Chains_PolyRow2      -> https://oeis.org/A84849
    Chains_NegHalf       -> https://oeis.org/A119881
    Chains_AccRevSum     -> https://oeis.org/A162509
    Chains_TransNat1     -> https://oeis.org/A162509
    Chains_PolyCol2      -> https://oeis.org/A368319
    Chains_RevPosHalf    -> https://oeis.org/A368319
    Chains_PolyCol3      -> https://oeis.org/A368322

    Chains: Distinct: 21, Hits: 25, Misses: 40
'''
