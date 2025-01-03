from functools import cache
from _tabltypes import Table

"""The hyperharmonic numbers.

[0]    1;
[1]    1,     1;
[2]    2,     3,    1;
[3]    6,    11,    5,    1;
[4]   24,    50,   26,    7,   1;
[5]  120,   274,  154,   47,   9,   1;
[6]  720,  1764, 1044,  342,  74,  11,  1;
[7] 5040, 13068, 8028, 2754, 638, 107, 13, 1;
"""


@cache
def hyperharmonic(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = hyperharmonic(n - 1) + [1]

    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n

    return row


HyperHarmonic = Table(
    hyperharmonic,
    "HyperHarmonic",
    ["A165675", "A093905", "A105954", "A165674"],
    "A000000",
    r"(n - k + 1)! \ \text{HyperHarmonic}(k, n - k)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(HyperHarmonic)


''' OEIS
    HyperHarmonic_Tinv          -> 0 
    HyperHarmonic_Tinv11        -> 0 
    HyperHarmonic_Tantidiag     -> 0 
    HyperHarmonic_Tacc          -> 0 
    HyperHarmonic_Tder          -> 0 
    HyperHarmonic_TablLcm       -> 0 
    HyperHarmonic_EvenSum       -> 0 
    HyperHarmonic_OddSum        -> 0 
    HyperHarmonic_AltSum        -> 0 
    HyperHarmonic_AccSum        -> 0 
    HyperHarmonic_AccRevSum     -> 0 
    HyperHarmonic_AntiDSum      -> 0 
    HyperHarmonic_ColMiddle     -> 0 
    HyperHarmonic_CentralE      -> 0 
    HyperHarmonic_CentralO      -> 0 
    HyperHarmonic_PosHalf       -> 0 
    HyperHarmonic_NegHalf       -> 0 
    HyperHarmonic_TransNat0     -> 0 
    HyperHarmonic_TransNat1     -> 0 
    HyperHarmonic_TransSqrs     -> 0 
    HyperHarmonic_BinConv       -> 0 
    HyperHarmonic_InvBinConv    -> 0 
    HyperHarmonic_PolyRow3      -> 0 
    HyperHarmonic_PolyCol2      -> 0 
    HyperHarmonic_PolyCol3      -> 0 
    HyperHarmonic_PolyDiag      -> 0 
    HyperHarmonic_RevToff11     -> 0 
    HyperHarmonic_RevTrev11     -> 0 
    HyperHarmonic_RevTantidiag  -> 0 
    HyperHarmonic_RevTacc       -> 0 
    HyperHarmonic_RevTder       -> 0 
    HyperHarmonic_RevEvenSum    -> 0 
    HyperHarmonic_RevOddSum     -> 0 
    HyperHarmonic_RevAccRevSum  -> 0 
    HyperHarmonic_RevAntiDSum   -> 0 
    HyperHarmonic_RevColMiddle  -> 0 
    HyperHarmonic_RevNegHalf    -> 0 
    HyperHarmonic_RevTransNat0  -> 0 
    HyperHarmonic_RevTransNat1  -> 0 
    HyperHarmonic_RevTransSqrs  -> 0 
    HyperHarmonic_RevPolyRow3   -> 0 
    HyperHarmonic_RevPolyCol3   -> 0 
    HyperHarmonic_RevPolyDiag   -> 0 
    HyperHarmonic_TablDiag0     -> https://oeis.org/A12
    HyperHarmonic_TablGcd       -> https://oeis.org/A12
    HyperHarmonic_PolyRow1      -> https://oeis.org/A27
    HyperHarmonic_RevPolyRow1   -> https://oeis.org/A27
    HyperHarmonic_TablCol0      -> https://oeis.org/A142
    HyperHarmonic_TablCol1      -> https://oeis.org/A254
    HyperHarmonic_TablMax       -> https://oeis.org/A254
    HyperHarmonic_RevPolyRow2   -> https://oeis.org/A384
    HyperHarmonic_TablCol2      -> https://oeis.org/A1705
    HyperHarmonic_TablCol3      -> https://oeis.org/A1711
    HyperHarmonic_PolyRow2      -> https://oeis.org/A2378
    HyperHarmonic_TablDiag1     -> https://oeis.org/A5408
    HyperHarmonic_RevCentralO   -> https://oeis.org/A58806
    HyperHarmonic_TablDiag2     -> https://oeis.org/A80663
    HyperHarmonic_TablSum       -> https://oeis.org/A93345
    HyperHarmonic_AbsSum        -> https://oeis.org/A93345
    HyperHarmonic_Trev11        -> https://oeis.org/A93905
    HyperHarmonic_Trev          -> https://oeis.org/A105954
    HyperHarmonic_RevTalt       -> https://oeis.org/A105954
    HyperHarmonic_Toff11        -> https://oeis.org/A165674
    HyperHarmonic_Triangle      -> https://oeis.org/A165675
    HyperHarmonic_Talt          -> https://oeis.org/A165675
    HyperHarmonic_TablDiag3     -> https://oeis.org/A165676

    HyperHarmonic: Distinct: 18, Hits: 23, Misses: 43
'''
