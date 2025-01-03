from functools import cache
from _tabltypes import Table

"""Bell (Peirce/Aitken) triangle, (see also A182930).

[0]     1;
[1]     1,     2;
[2]     2,     3,     5;
[3]     5,     7,    10,    15;
[4]    15,    20,    27,    37,    52;
[5]    52,    67,    87,   114,   151,   203;
[6]   203,   255,   322,   409,   523,   674,   877;
[7]   877,  1080,  1335,  1657,  2066,  2589,  3263,  4140;
[8]  4140,  5017,  6097,  7432,  9089, 11155, 13744, 17007, 21147;
[9] 21147, 25287, 30304, 36401, 43833, 52922, 64077, 77821, 94828, 115975;
"""


@cache
def bell(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [bell(n - 1)[n - 1]] + bell(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row


Bell = Table(
    bell, 
    "Bell", 
    ["A011971", "A011972", "A123346"], 
    "", # No inverse!
    r"\sum_{j=0}^{k} \binom{k}{j} Bell(n - k + j)"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Bell)


''' OEIS
    Bell_Trev11        -> 0 
    Bell_Tantidiag     -> 0 
    Bell_Tacc          -> 0 
    Bell_Tder          -> 0 
    Bell_TablLcm       -> 0 
    Bell_EvenSum       -> 0 
    Bell_OddSum        -> 0 
    Bell_AntiDSum      -> 0 
    Bell_TransNat0     -> 0 
    Bell_TransSqrs     -> 0 
    Bell_PolyRow2      -> 0 
    Bell_PolyRow3      -> 0 
    Bell_PolyCol3      -> 0 
    Bell_PolyDiag      -> 0 
    Bell_RevToff11     -> 0 
    Bell_RevTantidiag  -> 0 
    Bell_RevTacc       -> 0 
    Bell_RevTder       -> 0 
    Bell_RevEvenSum    -> 0 
    Bell_RevOddSum     -> 0 
    Bell_RevAntiDSum   -> 0 
    Bell_RevNegHalf    -> 0 
    Bell_RevTransSqrs  -> 0 
    Bell_RevPolyRow2   -> 0 
    Bell_RevPolyRow3   -> 0 
    Bell_RevPolyCol3   -> 0 
    Bell_RevPolyDiag   -> 0 
    Bell_TablGcd       -> https://oeis.org/A12
    Bell_InvBinConv    -> https://oeis.org/A12
    Bell_RevPolyRow1   -> https://oeis.org/A27
    Bell_TablCol0      -> https://oeis.org/A110
    Bell_TablDiag0     -> https://oeis.org/A110
    Bell_TablMax       -> https://oeis.org/A110
    Bell_PolyRow1      -> https://oeis.org/A5408
    Bell_TablDiag1     -> https://oeis.org/A5493
    Bell_TablSum       -> https://oeis.org/A5493
    Bell_AbsSum        -> https://oeis.org/A5493
    Bell_TablDiag2     -> https://oeis.org/A11965
    Bell_TablDiag3     -> https://oeis.org/A11966
    Bell_TablCol1      -> https://oeis.org/A11968
    Bell_TablCol2      -> https://oeis.org/A11969
    Bell_TablCol3      -> https://oeis.org/A11970
    Bell_Triangle      -> https://oeis.org/A11971
    Bell_Talt          -> https://oeis.org/A11971
    Bell_Toff11        -> https://oeis.org/A11972
    Bell_RevTrev11     -> https://oeis.org/A11972
    Bell_CentralO      -> https://oeis.org/A20556
    Bell_RevTransNat0  -> https://oeis.org/A92923
    Bell_CentralE      -> https://oeis.org/A94577
    Bell_PolyCol2      -> https://oeis.org/A95676
    Bell_Trev          -> https://oeis.org/A123346
    Bell_RevTalt       -> https://oeis.org/A123346
    Bell_AccSum        -> https://oeis.org/A124325
    Bell_RevAccRevSum  -> https://oeis.org/A124325
    Bell_RevTransNat1  -> https://oeis.org/A124325
    Bell_BinConv       -> https://oeis.org/A126390
    Bell_RevCentralO   -> https://oeis.org/A208782
    Bell_ColMiddle     -> https://oeis.org/A216078
    Bell_RevColMiddle  -> https://oeis.org/A216332
    Bell_AccRevSum     -> https://oeis.org/A278677
    Bell_TransNat1     -> https://oeis.org/A278677
    Bell_AltSum        -> https://oeis.org/A367775
    Bell_PosHalf       -> https://oeis.org/A367808
    Bell_NegHalf       -> https://oeis.org/A367809

    Bell: Distinct: 27, Hits: 37, Misses: 27
'''
