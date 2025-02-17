from functools import cache
from _tabltypes import Table

"""Fubini triangle.

[0]  1;
[1]  0,  1;
[2]  0,  1,    2;
[3]  0,  1,    6,     6;
[4]  0,  1,   14,    36,    24;
[5]  0,  1,   30,   150,   240,    120;
[6]  0,  1,   62,   540,  1560,   1800,    720;
[7]  0,  1,  126,  1806,  8400,  16800,  15120,  5040;
[8]  0,  1,  254,  5796, 40824, 126000, 191520, 141120, 40320;
"""


@cache
def fubini(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return fubini(n - 1)[k] if k <= n - 1 else 0

    row = [0] + fubini(n - 1)
    for k in range(1, n + 1):
        row[k] = k * (r(k - 1) + r(k))
    return row


Fubini = Table(
    fubini,
    "Fubini",
    ["A131689", "A019538", "A090582", "A278075"],
    "",
    r"k! \ {n \brace k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Fubini)




''' OEIS
    Fubini_AltSum        -> https://oeis.org/A-999999
    Fubini_Trev          -> 0 
    Fubini_Tinvrev11     -> 0 
    Fubini_Tacc          -> 0 
    Fubini_Tder          -> 0 
    Fubini_TablLcm       -> 0 
    Fubini_RevToff11     -> 0 
    Fubini_RevTrev11     -> 0 
    Fubini_RevTantidiag  -> 0 
    Fubini_RevTacc       -> 0 
    Fubini_RevTalt       -> 0 
    Fubini_RevTder       -> 0 
    Fubini_RevOddSum     -> 0 
    Fubini_RevAntiDSum   -> 0 
    Fubini_RevColMiddle  -> 0 
    Fubini_RevTransNat0  -> 0 
    Fubini_RevTransSqrs  -> 0 
    Fubini_TablCol0      -> https://oeis.org/A7
    Fubini_TablCol1      -> https://oeis.org/A12
    Fubini_RevPolyRow1   -> https://oeis.org/A12
    Fubini_PolyRow1      -> https://oeis.org/A27
    Fubini_RevPolyRow2   -> https://oeis.org/A27
    Fubini_TablDiag0     -> https://oeis.org/A142
    Fubini_BinConv       -> https://oeis.org/A312
    Fubini_RevNegHalf    -> https://oeis.org/A629
    Fubini_TablSum       -> https://oeis.org/A670
    Fubini_AbsSum        -> https://oeis.org/A670
    Fubini_TablCol2      -> https://oeis.org/A918
    Fubini_TablCol3      -> https://oeis.org/A1117
    Fubini_TablDiag1     -> https://oeis.org/A1286
    Fubini_TablMax       -> https://oeis.org/A2869
    Fubini_PolyCol2      -> https://oeis.org/A4123
    Fubini_RevPosHalf    -> https://oeis.org/A4123
    Fubini_AccRevSum     -> https://oeis.org/A5649
    Fubini_TransNat1     -> https://oeis.org/A5649
    Fubini_NegHalf       -> https://oeis.org/A9006
    Fubini_PolyRow2      -> https://oeis.org/A14105
    Fubini_Toff11        -> https://oeis.org/A19538
    Fubini_TablGcd       -> https://oeis.org/A27760
    Fubini_RevPolyRow3   -> https://oeis.org/A28872
    Fubini_PolyCol3      -> https://oeis.org/A32033
    Fubini_RevEvenSum    -> https://oeis.org/A32109
    Fubini_TablDiag2     -> https://oeis.org/A37960
    Fubini_TablDiag3     -> https://oeis.org/A37961
    Fubini_EvenSum       -> https://oeis.org/A52841
    Fubini_TransNat0     -> https://oeis.org/A69321
    Fubini_TransSqrs     -> https://oeis.org/A83411
    Fubini_OddSum        -> https://oeis.org/A89677
    Fubini_Trev11        -> https://oeis.org/A90582
    Fubini_PolyDiag      -> https://oeis.org/A94420
    Fubini_PolyRow3      -> https://oeis.org/A94421
    Fubini_AntiDSum      -> https://oeis.org/A105795
    Fubini_AccSum        -> https://oeis.org/A120368
    Fubini_RevAccRevSum  -> https://oeis.org/A120368
    Fubini_RevTransNat1  -> https://oeis.org/A120368
    Fubini_PosHalf       -> https://oeis.org/A122704
    Fubini_Triangle      -> https://oeis.org/A131689
    Fubini_Talt          -> https://oeis.org/A131689
    Fubini_CentralE      -> https://oeis.org/A210029
    Fubini_RevCentralO   -> https://oeis.org/A233734
    Fubini_RevPolyCol3   -> https://oeis.org/A255927
    Fubini_RevPolyDiag   -> https://oeis.org/A331690
    Fubini_InvBinConv    -> https://oeis.org/A344053
    Fubini_Tantidiag     -> https://oeis.org/A344392
    Fubini_ColMiddle     -> https://oeis.org/A344397
    Fubini_CentralO      -> https://oeis.org/A367392

    Fubini: Distinct: 43, Hits: 50, Misses: 16
'''
