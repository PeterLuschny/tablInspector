from functools import cache
from _tabltypes import Table

"""Binary Pell triangle

[0] [  1]
[1] [  2,    1]
[2] [  4,    4,    1]
[3] [  8,   12,    6,    1]
[4] [ 16,   32,   24,    8,    1]
[5] [ 32,   80,   80,   40,   10,   1]
[6] [ 64,  192,  240,  160,   60,  12,   1]
[7] [128,  448,  672,  560,  280,  84,  14,  1]
[8] [256, 1024, 1792, 1792, 1120, 448, 112, 16, 1]
"""


@cache
def binarypell(n: int) -> list[int]:

    if n == 0:
        return [1]

    arow = binarypell(n-1)
    row = arow + [1]
    for k in range(n-1, 0, -1):
        row[k] = arow[k - 1] + 2 * arow[k]
    row[0] = 2 * arow[0]
    return row


BinaryPell = Table(
    binarypell,
    "BinaryPell",
    ["A038207"],
    "A065109",  # involutory 
    r"\binom{n}{k} \, 2^{n-k}"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(BinaryPell)


''' OEIS
    BinaryPell_Toff11        -> 0 
    BinaryPell_Trev11        -> 0 
    BinaryPell_Tinv11        -> 0 
    BinaryPell_Tacc          -> 0 
    BinaryPell_Tder          -> 0 
    BinaryPell_TablLcm       -> 0 
    BinaryPell_ColMiddle     -> 0 
    BinaryPell_TransSqrs     -> 0 
    BinaryPell_InvBinConv    -> 0 
    BinaryPell_RevTrev11     -> 0 
    BinaryPell_RevTacc       -> 0 
    BinaryPell_RevTder       -> 0 
    BinaryPell_RevNegHalf    -> https://oeis.org/A7
    BinaryPell_TablDiag0     -> https://oeis.org/A12
    BinaryPell_AltSum        -> https://oeis.org/A12
    BinaryPell_PolyRow1      -> https://oeis.org/A27
    BinaryPell_TablCol0      -> https://oeis.org/A79
    BinaryPell_AntiDSum      -> https://oeis.org/A129
    BinaryPell_TablSum       -> https://oeis.org/A244
    BinaryPell_AbsSum        -> https://oeis.org/A244
    BinaryPell_NegHalf       -> https://oeis.org/A244
    BinaryPell_PolyDiag      -> https://oeis.org/A272
    BinaryPell_PolyRow2      -> https://oeis.org/A290
    BinaryPell_PolyCol2      -> https://oeis.org/A302
    BinaryPell_PosHalf       -> https://oeis.org/A351
    BinaryPell_PolyCol3      -> https://oeis.org/A351
    BinaryPell_RevPolyCol3   -> https://oeis.org/A420
    BinaryPell_PolyRow3      -> https://oeis.org/A578
    BinaryPell_RevAntiDSum   -> https://oeis.org/A1045
    BinaryPell_TablCol1      -> https://oeis.org/A1787
    BinaryPell_TablCol2      -> https://oeis.org/A1788
    BinaryPell_TablCol3      -> https://oeis.org/A1789
    BinaryPell_BinConv       -> https://oeis.org/A1850
    BinaryPell_OddSum        -> https://oeis.org/A3462
    BinaryPell_RevPolyRow1   -> https://oeis.org/A5408
    BinaryPell_TablDiag1     -> https://oeis.org/A5843
    BinaryPell_AccRevSum     -> https://oeis.org/A6234
    BinaryPell_TransNat1     -> https://oeis.org/A6234
    BinaryPell_EvenSum       -> https://oeis.org/A7051
    BinaryPell_Trev          -> https://oeis.org/A13609
    BinaryPell_RevTalt       -> https://oeis.org/A13609
    BinaryPell_RevPolyRow2   -> https://oeis.org/A16754
    BinaryPell_RevPolyRow3   -> https://oeis.org/A16755
    BinaryPell_TransNat0     -> https://oeis.org/A27471
    BinaryPell_Triangle      -> https://oeis.org/A38207
    BinaryPell_Tinv          -> https://oeis.org/A38207
    BinaryPell_Talt          -> https://oeis.org/A38207
    BinaryPell_TablDiag2     -> https://oeis.org/A46092
    BinaryPell_RevEvenSum    -> https://oeis.org/A46717
    BinaryPell_CentralE      -> https://oeis.org/A59304
    BinaryPell_RevTransSqrs  -> https://oeis.org/A62189
    BinaryPell_RevCentralO   -> https://oeis.org/A69720
    BinaryPell_CentralO      -> https://oeis.org/A69723
    BinaryPell_AccSum        -> https://oeis.org/A81038
    BinaryPell_RevAccRevSum  -> https://oeis.org/A81038
    BinaryPell_RevTransNat1  -> https://oeis.org/A81038
    BinaryPell_RevPolyDiag   -> https://oeis.org/A85527
    BinaryPell_RevColMiddle  -> https://oeis.org/A98660
    BinaryPell_TablMax       -> https://oeis.org/A109388
    BinaryPell_RevTantidiag  -> https://oeis.org/A128099
    BinaryPell_TablDiag3     -> https://oeis.org/A130809
    BinaryPell_RevOddSum     -> https://oeis.org/A152011
    BinaryPell_TablGcd       -> https://oeis.org/A171977
    BinaryPell_Tantidiag     -> https://oeis.org/A207538
    BinaryPell_RevTransNat0  -> https://oeis.org/A212697
    BinaryPell_RevToff11     -> https://oeis.org/A276985

    BinaryPell: Distinct: 45, Hits: 54, Misses: 12
'''
