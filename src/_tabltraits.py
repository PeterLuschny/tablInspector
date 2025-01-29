"""
This module provides various functions to analyze and transform integer triangles (Table objects).
It includes functions to compute different traits of tables, such as dot products, polynomials, table columns, diagonals, rows, and various transformations and convolutions of tables. Additionally, it provides functions to compute LCM, GCD, sums, and other properties of table rows and columns.
"""

from Binomial import Binomial, InvBinomial
from _tabltypes import Table, RevTable, rowgen, trait
from _tablutils import SeqToString
from typing import Tuple, TypeAlias
from itertools import accumulate
from more_itertools import flatten
from functools import reduce
from math import lcm, gcd
import operator


# #@

# use the defaults for size: 7 rows for tables or 28 terms


def dotproduct(vec: list[int], tor: list[int]) -> int:
    """Returns the dot product of the two vectors."""
    return sum(map(operator.mul, vec, tor))


def Triangle(T: Table, size: int = 7) -> list[int]:
    return T.flat(size)


def Trev(T: Table, size: int = 7) -> list[int]:
    return list(flatten([T.rev(n) for n in range(size)]))


def Tinv(T: Table, size: int = 7) -> list[int]:
    return list(flatten(T.inv(size)))


def Tinvrev(T: Table, size: int = 7) -> list[int]:
    return list(flatten(T.invrev(size)))


def Toff11(T: Table, size: int = 7) -> list[int]:
    T11 = Table(T.off(1, 1), T.id + "off11")
    return T11.flat(size)


def Trev11(T: Table, size: int = 7) -> list[int]:
    return list(flatten([T.rev11(n) for n in range(size)]))


def Tinv11(T: Table, size: int = 7) -> list[int]:
    InvT11 = T.inv11(size)
    return list(flatten(InvT11))


def Tinvrev11(T: Table, size: int = 7) -> list[int]:
    InvrevT11 = T.invrev11(size)
    return list(flatten(InvrevT11))


def Talt(T: Table, size: int = 7) -> list[int]:
    return list(flatten([T.alt(n) for n in range(size)]))


def Tacc(T: Table, size: int = 7) -> list[int]:
    return list(flatten([T.acc(n) for n in range(size)]))


def Tder(T: Table, size: int = 7) -> list[int]:
    return list(flatten([T.der(n) for n in range(size)]))


# Needs 9 rows
def Tantidiag(T: Table, size: int = 9) -> list[int]:
    return list(flatten([T.antidiag(n) for n in range(size)]))


def TablCol(T: Table, col: int, size: int = 28) -> list[int]:
    return [T(col + n, col) for n in range(size)]


def TablCol0(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    if rev:
        return TablDiag0(T, size)
    else:
        return [T(n, 0) for n in range(size)]


def TablCol1(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    if rev:
        return TablDiag1(T, size)
    else:
        return [T(1 + n, 1) for n in range(size)]


def TablCol2(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    if rev:
        return TablDiag2(T, size)
    else:
        return [T(2 + n, 2) for n in range(size)]


def TablCol3(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    if rev:
        return TablDiag3(T, size)
    else:
        return [T(3 + n, 3) for n in range(size)]


def TablDiag(T: Table, diag: int, size: int = 28) -> list[int]:
    return [T(diag + k, k) for k in range(size)]


def TablDiag0(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    if rev:
        return TablCol0(T, size)
    else:
        return [T(k, k) for k in range(size)]


def TablDiag1(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    if rev:
        return TablCol1(T, size)
    else:
        return [T(1 + k, k) for k in range(size)]


def TablDiag2(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    if rev:
        return TablCol2(T, size)
    else:
        return [T(2 + k, k) for k in range(size)]


def TablDiag3(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    if rev:
        return TablCol3(T, size)
    else:
        return [T(3 + k, k) for k in range(size)]


def PolyRow(T: Table, row: int, size: int = 28) -> list[int]:
    return [T.poly(row, x) for x in range(size)]


def PolyRow1(T: Table, size: int = 28) -> list[int]:
    return [T.poly(1, x) for x in range(size)]


def PolyRow2(T: Table, size: int = 28) -> list[int]:
    return [T.poly(2, x) for x in range(size)]


def PolyRow3(T: Table, size: int = 28) -> list[int]:
    return [T.poly(3, x) for x in range(size)]


def PolyCol(T: Table, col: int, size: int = 28) -> list[int]:
    return [T.poly(x, col) for x in range(size)]


def PolyCol1(T: Table, size: int = 28) -> list[int]:
    return [T.poly(x, 1) for x in range(size)]


def PolyCol2(T: Table, size: int = 28) -> list[int]:
    return [T.poly(x, 2) for x in range(size)]


def PolyCol3(T: Table, size: int = 28) -> list[int]:
    return [T.poly(x, 3) for x in range(size)]


def PolyDiag(T: Table, size: int = 28) -> list[int]:
    return [T.poly(n, n) for n in range(size)]


# Note our convention to exclude 0 and 1.
def RowLcmGcd(g: rowgen, row: int, lg: bool) -> int:
    Z = [v for v in g(row) if v not in [-1, 0, 1]]
    if Z == []:
        return 1
    return lcm(*Z) if lg else gcd(*Z)


def TablLcm(T: Table, size: int = 28) -> list[int]:
    return [RowLcmGcd(T.row, n, True) for n in range(size)]


def TablGcd(T: Table, size: int = 28) -> list[int]:
    return [RowLcmGcd(T.row, n, False) for n in range(size)]


# Note our convention to use the abs value.
def TablMax(T: Table, size: int = 28) -> list[int]:
    return [reduce(max, (abs(t) for t in T.row(n))) for n in range(size)]


def TablSum(T: Table, size: int = 28) -> list[int]:
    return [T.sum(n) for n in range(size)]


def EvenSum(T: Table, size: int = 28) -> list[int]:
    return [sum(T.row(n)[::2]) for n in range(size)]


def OddSum(T: Table, size: int = 28) -> list[int]:
    return [sum(T.row(n)[1::2]) for n in range(size)]


def AltSum(T: Table, size: int = 28) -> list[int]:
    return [sum(T.row(n)[::2]) - sum(T.row(n)[1::2]) for n in range(size)]


def AbsSum(T: Table, size: int = 28) -> list[int]:
    return [sum(abs(t) for t in T.row(n)) for n in range(size)]


def AccSum(T: Table, size: int = 28) -> list[int]:
    return [sum(T.acc(n)) for n in range(size)]


def AccRevSum(T: Table, size: int = 28) -> list[int]:
    return [sum(accumulate(T.rev(n))) for n in range(size)]


def AntiDSum(T: Table, size: int = 28) -> list[int]:
    return [sum(T.antidiag(n)) for n in range(size)]


def ColMiddle(T: Table, size: int = 28) -> list[int]:
    return [T(n, n // 2) for n in range(size)]


def CentralE(T: Table, size: int = 28) -> list[int]:
    return [T(2 * n, n) for n in range(size)]


def CentralO(T: Table, size: int = 28) -> list[int]:
    return [T(2 * n + 1, n) for n in range(size)]


def ColLeft(T: Table, size: int = 28) -> list[int]:
    return [T(n, 0) for n in range(size)]


def ColRight(T: Table, size: int = 28) -> list[int]:
    return [T(n, n) for n in range(size)]


def PolyFrac(row: list[int], x: int) -> int:
    n = len(row) - 1
    return sum(c * x**(n - k) for (k, c) in enumerate(row))


def PosHalf(T: Table, size: int = 28) -> list[int]:
    return [PolyFrac(T.row(n), 2) for n in range(size)]


def NegHalf(T: Table, size: int = 28) -> list[int]:
    return [PolyFrac(T.row(n), -2) for n in range(size)]


def TransNat0(T: Table, size: int = 28) -> list[int]:
    return T.trans(lambda k: k, size)


def TransNat1(T: Table, size: int = 28) -> list[int]:
    return T.trans(lambda k: k + 1, size)


def TransSqrs(T: Table, size: int = 28) -> list[int]:
    return T.trans(lambda k: k * k, size)


def BinConv(T: Table, size: int = 28) -> list[int]:
    return [dotproduct(Binomial.row(n), T.row(n)) for n in range(size)]


def InvBinConv(T: Table, size: int = 28) -> list[int]:
    return [dotproduct(InvBinomial.row(n), T.row(n)) for n in range(size)]

#------

def Rev_Toff11(t: Table, size: int = 7) -> list[int]:
    T = RevTable(t)
    T11 = Table(T.off(1, 1), T.id + "off11")
    return T11.flat(size)


def Rev_Trev11(t: Table, size: int = 7) -> list[int]:
    T = RevTable(t)
    return list(flatten([T.rev11(n) for n in range(size)]))


def Rev_Tinv11(t: Table, size: int = 7) -> list[int]:
    T = RevTable(t)
    InvT11 = T.inv11(size)
    return list(flatten(InvT11))


def Rev_Talt(t: Table, size: int = 7) -> list[int]:
    T = RevTable(t)
    return list(flatten([T.alt(n) for n in range(size)]))


def Rev_Tacc(t: Table, size: int = 7) -> list[int]:
    T = RevTable(t)
    return list(flatten([T.acc(n) for n in range(size)]))


def Rev_Tder(t: Table, size: int = 7) -> list[int]:
    T = RevTable(t)
    return list(flatten([T.der(n) for n in range(size)]))


# Needs 9 rows
def Rev_Tantidiag(t: Table, size: int = 9) -> list[int]:
    T = RevTable(t)
    return list(flatten([T.antidiag(n) for n in range(size)]))


def Rev_PolyRow1(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [T.poly(1, x) for x in range(size)]


def Rev_PolyRow2(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [T.poly(2, x) for x in range(size)]


def Rev_PolyRow3(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [T.poly(3, x) for x in range(size)]


def Rev_PolyCol3(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [T.poly(x, 3) for x in range(size)]


def Rev_PolyDiag(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [T.poly(n, n) for n in range(size)]


def Rev_EvenSum(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [sum(T.row(n)[::2]) for n in range(size)]


def Rev_OddSum(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [sum(T.row(n)[1::2]) for n in range(size)]


def Rev_AccRevSum(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [sum(accumulate(T.rev(n))) for n in range(size)]


def Rev_AntiDSum(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [sum(T.antidiag(n)) for n in range(size)]


def Rev_ColMiddle(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [T(n, n // 2) for n in range(size)]


def Rev_CentralO(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return [T(2 * n + 1, n) for n in range(size)]


def Rev_PosHalf(t: Table, size: int = 28) -> list[int]:
    return [PolyFrac(t.rev(n),  2) for n in range(size)]


def Rev_NegHalf(t: Table, size: int = 28) -> list[int]:
    return [PolyFrac(t.rev(n), -2) for n in range(size)]


def Rev_TransNat0(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return T.trans(lambda k: k, size)


def Rev_TransNat1(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return T.trans(lambda k: k + 1, size)


def Rev_TransSqrs(t: Table, size: int = 28) -> list[int]:
    T = RevTable(t)
    return T.trans(lambda k: k * k, size)


# sum((-1)**(n-k)*Binomial(n,k)*Trev(n, k) for k in range(n+1)) for n in range(size)])


"""The basic construction is a map
    (Table:Class, Trait:Function) -> (Anum:Url, TreatInfo:TeXString)
"""

# Useful for the LaTeX titels: https://latexeditor.lagrida.com/

TraitInfo: TypeAlias = Tuple[trait, int, str]

'''The dictionary of all traits with their respective functions and TeX strings.
   The size of the table is set to 7, 9 or 28 rows for the default case.
   It is mandatory that this dictionary starts with the key 'Triangle'!
'''
AllTraits: dict[str, TraitInfo] = {
    "Triangle     ": (Triangle,  7, r"\(T_{n,k}\)"),
    "Tinv         ": (Tinv,      7, r"\(T^{-1}_{n,k}\)"),
    "Trev         ": (Trev,      7, r"\(T_{n,n-k}\)"),
    "Tinvrev      ": (Tinvrev,   7, r"\((T_{n,n-k})^{-1}\)"),
    "Toff11       ": (Toff11,    7, r"\(T_{n+1,k+1} \)"),
    "Trev11       ": (Trev11,    7, r"\(T_{n+1,n-k+1} \)"),
    "Tinv11       ": (Tinv11,    7, r"\(T^{-1}_{n+1,k+1}\)"),
    "Tinvrev11    ": (Tinvrev11, 7, r"\((T_{n+1,n-k+1})^{-1}\)"),
    "Tantidiag    ": (Tantidiag, 9, r"\(T_{n-k,k}\ \ (k \le n/2)\)"),
    "Tacc         ": (Tacc,      7, r"\(\sum_{j=0}^{k} T_{n,j}\)"),
    "Talt         ": (Talt,      7, r"\(T_{n,k}\ (-1)^{k}\)"),
    "Tder         ": (Tder,      7, r"\(T_{n+1,k+1}\ (k+1) \)"),
    "TablCol0     ": (TablCol0,  28, r"\(T_{n  ,0}\)"),
    "TablCol1     ": (TablCol1,  28, r"\(T_{n+1,1}\)"),
    "TablCol2     ": (TablCol2,  28, r"\(T_{n+2,2}\)"),
    "TablCol3     ": (TablCol3,  28, r"\(T_{n+3,3}\)"),
    "TablDiag0    ": (TablDiag0, 28, r"\(T_{n  ,n}\)"),
    "TablDiag1    ": (TablDiag1, 28, r"\(T_{n+1,n}\)"),
    "TablDiag2    ": (TablDiag2, 28, r"\(T_{n+2,n}\)"),
    "TablDiag3    ": (TablDiag3, 28, r"\(T_{n+3,n}\)"),
    "TablLcm      ": (TablLcm,   28, r"\(\text{lcm}_{k=0}^{n}\ |T_{n,k}|\ (T_{n,k}>1)\)"),
    "TablGcd      ": (TablGcd,   28, r"\(\text{gcd}_{k=0}^{n}\ |T_{n,k}|\ (T_{n,k}>1)\)"),
    "TablMax      ": (TablMax,   28, r"\(\text{max}_{k=0}^{n}\ |T_{n,k}|\)"),
    "TablSum      ": (TablSum,   28, r"\(\sum_{k=0}^{n} T_{n,k}\)"),
    "EvenSum      ": (EvenSum,   28, r"\(\sum_{k=0}^{n} T_{n,k}\ [2|k]\)"),
    "OddSum       ": (OddSum,    28, r"\(\sum_{k=0}^{n} T_{n,k}\ (1-[2|k])\)"),
    "AltSum       ": (AltSum,    28, r"\(\sum_{k=0}^{n} T_{n,k}\ (-1)^{k}\)"),
    "AbsSum       ": (AbsSum,    28, r"\(\sum_{k=0}^{n} | T_{n,k} |\)"),
    "AccSum       ": (AccSum,    28, r"\(\sum_{k=0}^{n} \sum_{j=0}^{k} T_{n,j}\)"),
    "AccRevSum    ": (AccRevSum, 28, r"\(\sum_{k=0}^{n} \sum_{j=0}^{k} T_{n,n-j}\)"),
    "AntiDSum     ": (AntiDSum,  28, r"\(\sum_{k=0}^{n/2} T_{n-k, k}\)"),
    "ColMiddle    ": (ColMiddle, 28, r"\(T_{n, n / 2}\)"),
    "CentralE     ": (CentralE,  28, r"\(T_{2 n, n}\)"),
    "CentralO     ": (CentralO,  28, r"\(T_{2 n + 1, n}\)"),
    "PosHalf      ": (PosHalf,   28, r"\(\sum_{k=0}^{n}T_{n,k}\ 2^{n-k} \)"),
    "NegHalf      ": (NegHalf,   28, r"\(\sum_{k=0}^{n}T_{n,k}\ (-2)^{n-k} \)"),
    "TransNat0    ": (TransNat0, 28, r"\(\sum_{k=0}^{n}T_{n,k}\ k\)"),
    "TransNat1    ": (TransNat1, 28, r"\(\sum_{k=0}^{n}T_{n,k}\ (k+1)\)"),
    "TransSqrs    ": (TransSqrs, 28, r"\(\sum_{k=0}^{n}T_{n,k}\ k^{2}\)"),
    "BinConv      ": (BinConv,   28, r"\(\sum_{k=0}^{n}T_{n,k}\ \binom{n}{k} \)"),
    "InvBinConv   ": (InvBinConv, 28, r"\(\sum_{k=0}^{n}T_{n,k}\ (-1)^{n-k}\ \binom{n}{k}\)"),
    "PolyRow1     ": (PolyRow1,  28, r"\(\sum_{k=0}^{1}T_{1,k}\ n^k\)"),
    "PolyRow2     ": (PolyRow2,  28, r"\(\sum_{k=0}^{2}T_{2,k}\ n^k\)"),
    "PolyRow3     ": (PolyRow3,  28, r"\(\sum_{k=0}^{3}T_{3,k}\ n^k\)"),
    "PolyCol2     ": (PolyCol2,  28, r"\(\sum_{k=0}^{n}T_{n,k}\ 2^k\)"),
    "PolyCol3     ": (PolyCol3,  28, r"\(\sum_{k=0}^{n}T_{n,k}\ 3^k\)"),
    "PolyDiag     ": (PolyDiag,  28, r"\(\sum_{k=0}^{n}T_{n,k}\ n^k\)"),
    "RevToff11    ": (Rev_Toff11,    7, r"\(T_{n+1,n-k} \)"),
    "RevTrev11    ": (Rev_Trev11,    7, r"\(T_{n+1,n-k} \)"),
    "RevTinv11    ": (Rev_Tinv11,    7, r"\(T^{-1}_{n+1,n-k}\)"),
    "RevTantidiag ": (Rev_Tantidiag, 9, r"\(T_{n-k,n-2k}\ \ (k \le n/2)\)"),
    "RevTacc      ": (Rev_Tacc,      7, r"\(\sum_{j=0}^{n-k}T_{n,n-j}\)"),
    "RevTalt      ": (Rev_Talt,      7, r"\(T_{n,n-k}\ (-1)^{n-k}\)"),
    "RevTder      ": (Rev_Tder,      7, r"\(T_{n+1,n-k}\ (n-k+1) \)"),
    "RevEvenSum   ": (Rev_EvenSum,   28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ [2|k]\)"),
    "RevOddSum    ": (Rev_OddSum,    28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ (1-[2|k])\)"),
    "RevAccRevSum ": (Rev_AccRevSum, 28, r"\(\sum_{k=0}^{n} \sum_{j=0}^{k}T_{n,n-j}\)"),
    "RevAntiDSum  ": (Rev_AntiDSum,  28, r"\(\sum_{k=0}^{n/2}T_{n-k,n-k}\)"),
    "RevColMiddle ": (Rev_ColMiddle, 28, r"\(T_{n,n/2}\)"),
    "RevCentralO  ": (Rev_CentralO,  28, r"\(T_{2n+1,n}\)"),
    "RevPosHalf   ": (Rev_PosHalf,   28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ 2^{n-k} \)"),
    "RevNegHalf   ": (Rev_NegHalf,   28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ (-2)^{n-k} \)"),
    "RevTransNat0 ": (Rev_TransNat0, 28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ k\)"),
    "RevTransNat1 ": (Rev_TransNat1, 28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ (k + 1)\)"),
    "RevTransSqrs ": (Rev_TransSqrs, 28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ k^{2}\)"),
    "RevPolyRow1  ": (Rev_PolyRow1,  28, r"\(\sum_{k=0}^{1}T_{1,n-k}\ n^k\)"),
    "RevPolyRow2  ": (Rev_PolyRow2,  28, r"\(\sum_{k=0}^{2}T_{2,n-k}\ n^k\)"),
    "RevPolyRow3  ": (Rev_PolyRow3,  28, r"\(\sum_{k=0}^{3}T_{3,n-k}\ n^k\)"),
    "RevPolyCol3  ": (Rev_PolyCol3,  28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ 3^k\)"),
    "RevPolyDiag  ": (Rev_PolyDiag,  28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ n^k\)"),
}


def TableTraits(T: Table) -> None:
    """
    Processes and prints traits of a given table.

    Args:
        T (Table): The table object whose traits are to be processed.

    Iterates over all traits in the AllTraits dictionary, constructs a name
    for each trait by combining the table's ID and the trait ID, and prints
    the name and the corresponding trait's TeXed formula. Additionally, converts the
    trait's sequence to a string and prints it.

    The name can be used as a key into the dictionary of T.
    The sequence is converted to a string with a maximum line length of 60 and
    a maximum of 20 terms.

    Returns:
        None
    """
    for trait_id, tr in AllTraits.items():
        name = (T.id + '_' + trait_id).ljust(9 + len(T.id), " ")
        tex = tr[2]
        seq = tr[0](T, tr[1])
        print(name, tex)
        # print(FNVhash(SeqToString(seq, 180, 50, ",", 3, True)))
        print(SeqToString(seq, 60, 20))


if __name__ == "__main__":

    from Abel import Abel                # type: ignore
    from AbelInv import AbelInv          # type: ignore
    from LahInv import LahInv            # type: ignore

    def test(T: Table, LEN: int) -> None:
        print("TablCol")
        for n in range(4):
            print(TablCol(T, n, LEN))
        print("TablDiag")
        for n in range(4):
            print(TablDiag(T, n, LEN))
        print("PolyRow")
        for n in range(4):
            print(PolyRow(T, n, LEN))
        print("PolyCol")
        for n in range(4):
            print(PolyCol(T, n, LEN))
        print()
    
    #test(Abel, 10)
    TableTraits(Abel)
