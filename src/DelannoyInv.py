from functools import cache
from _tabltypes import Table

"""
Inverse of the Delannoy triangle, unsigned version.

[0]     1;
[1]     1,     1;
[2]     2,     3,     1;
[3]     6,    10,     5,     1;
[4]    22,    38,    22,     7,    1;
[5]    90,   158,    98,    38,    9,    1;
[6]   394,   698,   450,   194,   58,   11,   1;
[7]  1806,  3218,  2126,   978,  334,   82,  13,   1;
[8]  8558, 15310, 10286,  4942, 1838,  526, 110,  15,  1;
"""

@cache
def delannoyinv(n: int) -> list[int]:
    if n == 0:
        return [1]

    d = delannoyinv(n - 1)
    row = [sum(d)] + d
    for k in range(n - 1, 0, -1):
        row[k] = row[k + 1] + d[k - 1] + d[k]

    return row


DelannoyInv = Table(
    delannoyinv,
    "DelannoyInv",
    ["A132372", "A103136", "A033878"],
    "A008288",
    r"%%",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(DelannoyInv)




''' OEIS
    DelannoyInv_Tinv          -> https://oeis.org/A-999999
    DelannoyInv_Trevinv       -> https://oeis.org/A-999999
    DelannoyInv_Tinv11        -> https://oeis.org/A-999999
    DelannoyInv_Trevinv11     -> https://oeis.org/A-999999
    DelannoyInv_Toff11        -> 0 
    DelannoyInv_Trev11        -> 0 
    DelannoyInv_Tantidiag     -> 0 
    DelannoyInv_Tacc          -> 0 
    DelannoyInv_Tder          -> 0 
    DelannoyInv_TablCol2      -> 0 
    DelannoyInv_TablCol3      -> 0 
    DelannoyInv_TablDiag3     -> 0 
    DelannoyInv_TablLcm       -> 0 
    DelannoyInv_AccSum        -> 0 
    DelannoyInv_AntiDSum      -> 0 
    DelannoyInv_ColMiddle     -> 0 
    DelannoyInv_CentralO      -> 0 
    DelannoyInv_PosHalf       -> 0 
    DelannoyInv_TransSqrs     -> 0 
    DelannoyInv_BinConv       -> 0 
    DelannoyInv_PolyRow3      -> 0 
    DelannoyInv_PolyCol2      -> 0 
    DelannoyInv_PolyDiag      -> 0 
    DelannoyInv_RevToff11     -> 0 
    DelannoyInv_RevTrev11     -> 0 
    DelannoyInv_RevTantidiag  -> 0 
    DelannoyInv_RevTder       -> 0 
    DelannoyInv_RevAccRevSum  -> 0 
    DelannoyInv_RevColMiddle  -> 0 
    DelannoyInv_RevCentralO   -> 0 
    DelannoyInv_RevPosHalf    -> 0 
    DelannoyInv_RevTransNat0  -> 0 
    DelannoyInv_RevTransNat1  -> 0 
    DelannoyInv_RevTransSqrs  -> 0 
    DelannoyInv_RevPolyCol3   -> 0 
    DelannoyInv_RevPolyDiag   -> 0 
    DelannoyInv_AltSum        -> https://oeis.org/A7
    DelannoyInv_TablDiag0     -> https://oeis.org/A12
    DelannoyInv_TablGcd       -> https://oeis.org/A12
    DelannoyInv_PolyRow1      -> https://oeis.org/A27
    DelannoyInv_RevPolyRow1   -> https://oeis.org/A27
    DelannoyInv_InvBinConv    -> https://oeis.org/A247
    DelannoyInv_RevPolyRow2   -> https://oeis.org/A384
    DelannoyInv_EvenSum       -> https://oeis.org/A1003
    DelannoyInv_OddSum        -> https://oeis.org/A1003
    DelannoyInv_AccRevSum     -> https://oeis.org/A1003
    DelannoyInv_TransNat1     -> https://oeis.org/A1003
    DelannoyInv_RevEvenSum    -> https://oeis.org/A1003
    DelannoyInv_RevOddSum     -> https://oeis.org/A1003
    DelannoyInv_PolyRow2      -> https://oeis.org/A2378
    DelannoyInv_TablDiag1     -> https://oeis.org/A5408
    DelannoyInv_TablCol0      -> https://oeis.org/A6318
    DelannoyInv_TablSum       -> https://oeis.org/A6318
    DelannoyInv_AbsSum        -> https://oeis.org/A6318
    DelannoyInv_RevTacc       -> https://oeis.org/A33877
    DelannoyInv_Trev          -> https://oeis.org/A33878
    DelannoyInv_RevTalt       -> https://oeis.org/A33878
    DelannoyInv_TablDiag2     -> https://oeis.org/A90288
    DelannoyInv_TablCol1      -> https://oeis.org/A103138
    DelannoyInv_TablMax       -> https://oeis.org/A103138
    DelannoyInv_RevAntiDSum   -> https://oeis.org/A110110
    DelannoyInv_RevNegHalf    -> https://oeis.org/A114710
    DelannoyInv_Triangle      -> https://oeis.org/A132372
    DelannoyInv_Talt          -> https://oeis.org/A132372
    DelannoyInv_TransNat0     -> https://oeis.org/A238112
    DelannoyInv_RevPolyRow3   -> https://oeis.org/A272378
    DelannoyInv_PolyCol3      -> https://oeis.org/A321574
    DelannoyInv_NegHalf       -> https://oeis.org/A330803
    DelannoyInv_CentralE      -> https://oeis.org/A367393

    DelannoyInv: Distinct: 23, Hits: 37, Misses: 32
'''
