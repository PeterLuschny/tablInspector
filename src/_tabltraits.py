"""
This module provides various functions to analyze and transform integer triangles (Table objects).
It includes functions to compute different traits of tables, such as dot products, polynomials, table columns, diagonals, rows, and various transformations and convolutions of tables. Additionally, it provides functions to compute lcm, gcd, sums, and other properties of table rows and columns. 
"""

from Binomial import Binomial, InvBinomial
from _tabltypes import Table, RevTable, rowgen, Trait
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
    """
    Calculate the dot product of two vectors.

    Args:
        vec (list[int]): The first vector.
        tor (list[int]): The second vector.

    Returns:
        int: The dot product of the two vectors.

    Raises:
        ValueError: If the input vectors are not of the same length.

    Example:
        >>> dotproduct([1, 2, 3], [4, 5, 6])
        32
    """
    """Returns the dot product of the two vectors."""
    return sum(map(operator.mul, vec, tor))


def Triangle(T: Table, size: int = 7) -> list[int]:
    """
    Generates an integer triangle (a regular lower triangular table) as a list of rows.

    Args:
        T (Table): The table referencing the generating function.
        size (int, optional): The number of rows requested. Defaults to 7.

    Returns:
        list[int]: The rows flattened to a list of integers.
    
    Example:
        >>> Triangle(Abel, 4)
        [1, 0, 1, 0, 2, 1, 0, 9, 6, 1]
        A137452
    """
    return T.flat(size)


def Trev(T: Table, size: int = 7) -> list[int]:
    """
    Generates an integer triangle by reversing the rows of the given table.

    Args:
        T (Table): The table with the generating function of the original object.
        size (int, optional): The number of rows to reverse. Defaults to 7.

    Returns:
        list[int]: A flattened list of the reversed rows.
    
    Example:
        >>> Trev(StirlingSet, 4)
        [1, 1, 0, 1, 1, 0, 1, 3, 1, 0]
        A106800
    """
    return list(flatten([T.rev(n) for n in range(size)]))


def Tinv(T: Table, size: int = 7) -> list[int]:
    """
    Inverts the given table (matrix inversion) and flattens the resulting table.

    Args:
        T (Table): The table to be inverted.
        size (int, optional): The desired number of rows. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers representing the inverted table.
    
    Example:
        >>> Tinv(Abel, 4)
        [1, 0, 1, 0, -2, 1, 0, 3, -6, 1]
        A059297
    """
    return list(flatten(T.inv(size)))


def Tinvrev(T: Table, size: int = 7) -> list[int]:
    """
    First reverse the table and then invert the reversed table.

    Args:
        T (Table): The table to be inverted and reversed.
        size (int, optional): The desired number of rows. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers after reversing and inverting the table.
    
    Example:
        >>> Tinvrev(FallingFactorial, 4)
        [1, -1, 1, 0, -2, 1, 0, 0, -3, 1]
        A132013
    """
    return list(flatten(T.invrev(size)))


def Trevinv(T: Table, size: int = 7) -> list[int]:
    """
    First invert the table and then revert the rows of the inverted table.

    Args:
        T (Table): The table to be inverted and reversed.
        size (int, optional): The desired number of rows. Defaults to 7.

    Returns:
        list[int]: A flattened table after inverting and reversing the table.
    
    Example:
        >>> Trevinv(DyckPaths, 4)
        [1, 1, -1, 1, -3, 1, 1, -5, 6, -1]
        A054142
    """
    return list(flatten(T.revinv(size)))


def Toff11(T: Table, size: int = 7) -> list[int]:
    """
    Creates a new Table object offset by 1 row and 1 column from the original table,
    and returns a flattened list of rows of the new table.

    Args:
        T (Table): The original table object.
        size (int, optional): The desired number of rows. Defaults to 7.

    Returns:
        list[int]: A flattened list of rows from the shifted table.
    
    Example:
        >>> T = Abel
        >>> T11 = Table(T.off(1, 1), T.id + "off11")

        >>> print(T.id); T.show(4); 
        >>> print(T11.id); T11.show(4)
        
        >>> print("Inverse of T:"); print(T.inv(4))
        >>> print("Inverse of T11:"); print(T11.inv(4))

        >>> print(f"PolyRows of {T.id}:")
        >>> for n in range(4): print(PolyRow(T, n, 5))
        >>> print(f"PolyRows of {T11.id}:")
        >>> for n in range(4): print(PolyRow(T11, n, 5))

        Abel
        [0] [1] 
        [1] [0, 1] 
        [2] [0, 2, 1] 
        [3] [0, 9, 6, 1] 

        Abeloff11
        [0] [1] 
        [1] [2, 1] 
        [2] [9, 6, 1] 
        [3] [64, 48, 12, 1] 

        Inverse of T:
        [[1], [0, 1], [0, -2, 1], [0, 3, -6, 1]]
        Inverse of T11:
        []

        PolyRows of Abel:
        [1, 1, 1, 1, 1]
        [0, 1, 2, 3, 4]
        [0, 3, 8, 15, 24]
        [0, 16, 50, 108, 196]
        
        PolyRows of Abeloff11:
        [1, 1, 1, 1, 1]
        [2, 3, 4, 5, 6]
        [9, 16, 25, 36, 49]
        [64, 125, 216, 343, 512]
    """
    T11 = Table(T.off(1, 1), T.id + "off11")
    return T11.flat(size)


def Trev11(T: Table, size: int = 7) -> list[int]:
    """
    Generate a flattened list of reversed rows from a Table object with
    offset by 1 row and 1 column.

    Args:
        T (Table): The Table object containing the data.
        size (int, optional): The number of rows to reverse. Defaults to 7.

    Returns:
        list[int]: A flattened list of reversed elements of the shifted table.
    
    Example:
        >>> Trev11(Eulerian, 4)
        [1, 1, 1, 1, 4, 1, 1, 11, 11, 1]
        A008292
        
        >>> Trev(Eulerian, 4)
        [1, 1, 0, 1, 1, 0, 1, 4, 1, 0]
        A173018
    """
    return list(flatten([T.rev11(n) for n in range(size)]))


def Tinv11(T: Table, size: int = 7) -> list[int]:
    """
    Compute the inverse of the table with offset 1 row and 1 column 
    and flatten the rows of the result.

    Args:
        T (Table): The table object which has the inv11 method.
        size (int, optional): The desired number of rows of the shifted table. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers representing the rows of the shifted table.
    """
    InvT11 = T.inv11(size)
    return list(flatten(InvT11))


def Tinvrev11(T: Table, size: int = 7) -> list[int]:
    """
    First fix the new offset, next reverse and then invert the reversed table.

    Args:
        T (Table): The table object that contains the `invrev11` method.
        size (int, optional): The desired number of rows. Defaults to 7.

    Returns:
        list[int]: A flattened list of the rows of the generated table.
    
    Example:
        >>> Tinvrev11(Eulerian, 4)
        [1, -1, 1, 3, -4, 1, -23, 33, -11, 1]
        A055325
    """
    InvrevT11 = T.invrev11(size)
    return list(flatten(InvrevT11))


def Trevinv11(T: Table, size: int = 7) -> list[int]:
    """
    First fix the new offset, next inverse and then reverse the rows.

    Args:
        T (Table): The table object to be processed.
        size (int, optional): The desired number of rows. Defaults to 7.

    Returns:
        list[int]: A flattened list of the rows of the generated table.
    
    Example:
        >>> Trevinv11(Eulerian, 4)
        [1, 1, -1, 1, -4, 3, 1, -11, 33, -23]
    """
    RevinvT11 = T.revinv11(size)
    return list(flatten(RevinvT11))


def Talt(T: Table, size: int = 7) -> list[int]:
    """
    Generate a list of alternative values of the rows of the given table.

    Args:
        T (Table): The Table object from which to generate alternating rows.
        size (int, optional): The desired number of rows. Defaults to 7.

    Returns:
        list[int]: A flattened list of the rows of the generated table.
        
    Example:
        >>> Talt(Binomial, 4)
        [1, 1, -1, 1, -2, 1, 1, -3, 3, -1]
        A130595
    """
    return list(flatten([T.alt(n) for n in range(size)]))


def Tacc(T: Table, size: int = 7) -> list[int]:
    """
    Accumulate values of the values of the rows of the given table.

    Args:
        T (Table): The table from which to accumulate the row values.
        size (int, optional): The desired number of rows. Defaults to 7.

    Returns:
        list[int]: A flattened list of the rows of the generated table.
    
    Example:
        >>> Tacc(Binomial, 4)
        [1, 1, 2, 1, 3, 4, 1, 4, 7, 8]
        A008949
    """
    return list(flatten([T.acc(n) for n in range(size)]))


def Tder(T: Table, size: int = 7) -> list[int]:
    """
    Generate a list of rows representing the derivatives of the polynomials interpreting the row values as the coefficients of the polynomials.

    Args:
        T (Table): The Table object to process.
        size (int, optional): The desired number of rows. Defaults to 7.

    Returns:
        list[int]: A flattened list of the rows of the generated table.
    
    Example:
        >>> Tder(Abel, 5)
        [0, 1, 2, 2, 9, 12, 3, 64, 96, 36, 4]
        A225465
    """
    return list(flatten([T.der(n) for n in range(size)]))


def Tantidiag(T: Table, size: int = 9) -> list[int]:
    """
    Generate the flattened table of the antidiagonals of the given table.

    Args:
        T (Table): The table from which to generate the antidiagonals.
        size (int, optional): The number of antidiagonals. Defaults to 9.

    Returns:
        list[int]: A flattened list of the first `size` antidiagonals of the table.
        
    Example:
        >>> Tantidiag(Motzkin, 6)
        [1, 1, 2, 1, 4, 2, 9, 5, 1, 21, 12, 3]
        A106489
    """
    return list(flatten([T.antidiag(n) for n in range(size)]))


def TablCol(T: Table, col: int, size: int = 28) -> list[int]:
    """
    Extract a column from the given table and return it as a list of integers.

    Args:
        T (Table): The table from which to extract the column.
        col (int): The index of the column to extract.
        size (int, optional): The number of elements to extract from the column. Defaults to 28.

    Returns:
        list[int]: A list of integers representing the extracted column.
    """
    return [T(col + n, col) for n in range(size)]


def TablCol0(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Retrieve column 0 of a table.

    Args:
        T (Table): The table from which to retrieve the column.
        size (int, optional): The number of elements to retrieve. Defaults to 28.
        rev (bool, optional): If True, retrieve the diagonal instead of the column. Defaults to False.

    Returns:
        list[int]: A list of integers representing the first column or the diagonal of the table.
    """
    if rev:
        return TablDiag0(T, size)
    else:
        return [T(n, 0) for n in range(size)]


def TablCol1(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Retrieve column 1 of a table.

    Args:
        T (Table): The table from which to extract the column.
        size (int, optional): The number of elements in the column. Defaults to 28.
        rev (bool, optional): If True, return the diagonal elements instead of the column. Defaults to False.

    Returns:
        list[int]: A list of integers representing the column or diagonal elements.
    """
    if rev:
        return TablDiag1(T, size)
    else:
        return [T(1 + n, 1) for n in range(size)]


def TablCol2(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Retrieve column 2 of a table.

    Args:
        T (Table): The table from which to extract the column.
        size (int, optional): The size of the list to generate. Defaults to 28.
        rev (bool, optional): If True, generates the list using the TablDiag2 function. Defaults to False.

    Returns:
        list[int]: A list of integers representing column 2 
        or diagonal 2 of the given table.
    """
    if rev:
        return TablDiag2(T, size)
    else:
        return [T(2 + n, 2) for n in range(size)]


def TablCol3(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Retrieve column 3 of a table.

    Args:
        T (Table): The table object from which to extract the column.
        size (int, optional): The number of elements to retrieve. Defaults to 28.
        rev (bool, optional): If True, use the TablDiag3 function to generate the list. Defaults to False.

    Returns:
        list[int]: A list of integers generated from the Table object.
    """
    if rev:
        return TablDiag3(T, size)
    else:
        return [T(3 + n, 3) for n in range(size)]


def TablDiag(T: Table, diag: int, size: int = 28) -> list[int]:
    """
    Extracts a diagonal from a table.

    Args:
        T (Table): The table from which to extract the diagonal.
        diag (int): The row index where the diagonal starts.
        size (int, optional): The number of terms of the diagonal. Defaults to 28.

    Returns:
        list[int]: A list of integers representing the diagonal elements.
    """
    return [T(diag + k, k) for k in range(size)]


def TablDiag0(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generate a list of diagonal elements from a table.

    Args:
        T (Table): The table from which to extract diagonal elements.
        size (int, optional): The number of terms of the diagonal. Defaults to 28.
        rev (bool, optional): If True, extract elements from the first column instead of the diagonal. Defaults to False.

    Returns:
        list[int]: A list of integers representing the diagonal or the first column.
    """
    if rev:
        return TablCol0(T, size)
    else:
        return [T(k, k) for k in range(size)]


def TablDiag1(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generates the subdiagonal or column 1 of the provided table depending on `rev`.

    Args:
        T (Table): A table function that takes two integer arguments.
        size (int, optional): The number of terms of the diagonal. Defaults to 28.
        rev (bool, optional): A flag to determine which list generation method to use. Defaults to False.

    Returns:
        list[int]: A list of integers representing the subdiagonal or the second column.
    """
    if rev:
        return TablCol1(T, size)
    else:
        return [T(1 + k, k) for k in range(size)]


def TablDiag2(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generates the diagonal or the column starting at row 2 of the provided table depending on `rev`.

    If `rev` is True, the function returns the result of `TablCol2(T, size)`.
    Otherwise, it returns a list of integers generated by calling the Table
    function `T` with parameters (2 + k, k) for k in the range of `size`.

    Args:
        T (Table): A function that takes two integers and returns an integer.
        size (int, optional): The number of terms of the diagonal. Defaults to 28.
        rev (bool, optional): A flag to determine which list generation method to use. Defaults to False.

    Returns:
        list[int]: A list of integers representing the third diagonal or the third column.
    """
    if rev:
        return TablCol2(T, size)
    else:
        return [T(2 + k, k) for k in range(size)]


def TablDiag3(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generates the diagonal or the column starting at row 3 of the provided table depending on `rev`.

    If `rev` is True, the function returns the result of `TablCol3(T, size)`.
    Otherwise, it returns a list of integers generated by calling the Table function `T`
    with parameters (3 + k, k) for k in the range of `size`.

    Args:
        T (Table): A function that takes two integer arguments and returns an integer.
        size (int, optional): The number of terms of the diagonal. Defaults to 28.
        rev (bool, optional): A flag to determine which list to return. Defaults to False.

    Returns:
        list[int]: A list of integers representing the fourth diagonal or the fourth column.
    """
    if rev:
        return TablCol3(T, size)
    else:
        return [T(3 + k, k) for k in range(size)]


def PolyRow(T: Table, row: int, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values for a given row in a table.

    Args:
        T (Table): The table object containing the polynomial coefficients.
        row (int): The row index for which to generate polynomial values.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values for the specified row.

    Example:
        >>> print(PolyRow(Abel, 3, 7))
        [0, 16, 50, 108, 196, 320, 486]
    """
    return [T.poly(row, x) for x in range(size)]


def PolyRow1(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values for the first row of a table.

    Args:
        T (Table): The table object containing the polynomial coefficients.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values for row 1.
    """
    return [T.poly(1, x) for x in range(size)]


def PolyRow2(T: Table, size: int = 28) -> list[int]:
    """
    Generates a list of polynomial values of row 2 for a given table.

    Args:
        T (Table): The table object containing the polynomial coefficients.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values for row 2.
    """
    return [T.poly(2, x) for x in range(size)]


def PolyRow3(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of row 3 for a given table.

    Args:
        T (Table): The table object containing the polynomial coefficients.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values for row 3.
    """
    return [T.poly(3, x) for x in range(size)]


def PolyCol(T: Table, col: int, size: int = 28) -> list[int]:
    """
    Generates a list of polynomial values for a specified column in the table generated 
    by the polynomials with coefficients from the rows of the given table.

    Args:
        T (Table): The table object containing the polynomial coefficients.
        col (int): The column index for which polynomial values are to be generated.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values for the specified column.

    Example:
        >>> print(PolyCol(Abel, 3, 7))
        [1, 3, 15, 108, 1029, 12288, 177147]
        A362354
    """
    return [T.poly(x, col) for x in range(size)]


def PolyCol1(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 1 for a given table.

    Args:
        T (Table): The table object containing the polynomial coefficients.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values in column 1.
    """
    return [T.poly(x, 1) for x in range(size)]


def PolyCol2(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 2 for a given table.

    Args:
        T (Table): The table object containing the polynomial coefficients.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values in column 2.

    Example:
        >>> PolyCol2(Abel, 7)
        [1, 2, 8, 50, 432, 4802, 65536]
        A007334
    """
    return [T.poly(x, 2) for x in range(size)]


def PolyCol3(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 3 for a given table.

    Args:
        T (Table): The table object containing the polynomial coefficients.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values in column 3.
    """
    return [T.poly(x, 3) for x in range(size)]


def PolyDiag(T: Table, size: int = 28) -> list[int]:
    """
    Generates a list of polynomial diagonal values from a given Table object.

    Args:
        T (Table): The table object containing the polynomial coefficients.
        size (int, optional): The number of diagonal values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial diagonal values.
    
    Example:
        >>> PolyDiag(Abel, 6)
        [1, 1, 8, 108, 2048, 50000]
        A193678
    """
    return [T.poly(n, n) for n in range(size)]


def RowLcmGcd(g: rowgen, row: int, lg: bool) -> int:
    """
    Calculate the least common multiple (LCM) or greatest common divisor (GCD) of 
    non-trivial elements in a row generated by a given row generator function.
    Note our convention to exclude 0 and 1 from the terms.

    Args:
        g (rowgen): A row generator function that takes an integer row index and 
                    returns an iterable of integers.
        row (int): The index of the row to process.
        lg (bool): If True, calculate the LCM of the elements; if False, calculate the GCD.

    Returns:
        int: The LCM or GCD of the non-trivial elements in the row. If the row contains 
             only trivial elements (-1, 0, 1), returns 1.
    """
    Z = [v for v in g(row) if v not in [-1, 0, 1]]
    if Z == []:
        return 1
    return lcm(*Z) if lg else gcd(*Z)


def TablLcm(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the least common multiple (LCM) for each row in a table.
    Note our convention to exclude 0 and 1 from the terms.

    Args:
        T (Table): The table containing rows for which the LCM is to be calculated.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of LCM values for each row in the table.
    
    Example:
        >>> TablLcm(Leibniz, 8)
        [1, 2, 6, 12, 60, 60, 420, 840]
        A003418
    """
    return [RowLcmGcd(T.row, n, True) for n in range(size)]


def TablGcd(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the greatest common divisor (GCD) for each row in a table.
    Note our convention to exclude 0 and 1 from the terms.

    Args:
        T (Table): The table containing rows to process.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of GCD values for each row in the table.
        
    Example:
        >>> TablGcd(Fubini, 6)
        [1, 1, 2, 6, 2, 30]
        A141056, A027760
    """
    return [RowLcmGcd(T.row, n, False) for n in range(size)]


def TablMax(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the maximum absolute value in each row of a table.
    Note our convention to use the abs value.

    Args:
        T (Table): The table from which to calculate the maximum values.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of maximum absolute values for each row.
    
    Example:
        >>> TablMax(BinaryPell, 6)
        [1, 2, 4, 12, 32, 80]
        A109388
    """
    return [reduce(max, (abs(t) for t in T.row(n))) for n in range(size)]


def TablSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of the elements of the first `size` rows.

    Args:
        T (Table): The table object containing the data.
        size (int, optional): The number of rows to sum. Defaults to 28.

    Returns:
        list[int]: A list of sums for each element in the specified range.
    
    Example:
        >>> TablSum(Binomial, 6)
        [1, 2, 4, 8, 16, 32]
        A000079
    """
    return [T.sum(n) for n in range(size)]


def EvenSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of the even-indexed elements of the first `size` rows.

    Args:
        T (Table): The table object containing rows of data.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of sums of even-indexed elements for each row.
    
    Example:
        >>> EvenSum(Binomial, 6)
        [1, 1, 2, 4, 8, 16]
        A011782
    """
    return [sum(T.row(n)[::2]) for n in range(size)]


def OddSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of the odd-indexed elements of the first `size` rows.

    Args:
        T (Table): The table object containing rows of data.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of sums of elements at odd indices for each row.
    
    Example:
        >>> OddSum(Binomial, 6)
        [0, 1, 2, 4, 8, 16]
        A131577
    """
    return [sum(T.row(n)[1::2]) for n in range(size)]


def AltSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the alternating sum of elements in each row of a table.

    Args:
        T (Table): The table from which rows are taken.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of the alternating sums of the rows.
    
    Example:
        >>> AltSum(Binomial, 6)
        [1, 0, 0, 0, 0, 0]
        A000007
    """
    return [sum(T.row(n)[::2]) - sum(T.row(n)[1::2]) for n in range(size)]


def AbsSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the absolute sum of each row in a table.

    Args:
        T (Table): The table from which to calculate the absolute sums.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of absolute sums of the rows.
    
    Example:
        >>> AbsSum(EulerTan, 6)
        [0, 1, 2, 5, 12, 41, 142]
        A009739
    """
    return [sum(abs(t) for t in T.row(n)) for n in range(size)]


def AccSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the accumulated sum for the first 'size' rows of the table.

    Args:
        T (Table): The table the accumulated sums should be calculated.
        size (int, optional): The number of rows to calculate the accumulated sums. Defaults to 28.

    Returns:
        list[int]: A list of accumulated sums for each index from 0 to size-1.
    
    Example:
        >>> AccSum(Binomial, 6)
        [1, 3, 8, 20, 48, 112]
        A001792
    """
    return [sum(T.acc(n)) for n in range(size)]


def AccRevSum(T: Table, size: int = 28) -> list[int]:
    """
    Return the accumulated sums of the reversed rows for the given table.

    Args:
        T (Table): The table object containing revenue data.
        size (int, optional): The number of periods to calculate the accumulated sums for. Defaults to 28.

    Returns:
        list[int]: A list of accumulated sums of the reversed rows
    
    Example:
        >>> AccRevSum(StirlingCycle, 6)
        [1, 2, 5, 17, 74, 394]
        A000774
    """
    return [sum(accumulate(T.rev(n))) for n in range(size)]


def AntiDSum(T: Table, size: int = 28) -> list[int]:
    """
    Return the sum of the antidiagonals of a table.

    Args:
        T (Table): The table from which to calculate the antidiagonal sums.
        size (int, optional): The number of antidiagonals to sum. Defaults to 28.

    Returns:
        list[int]: A list of sums of the antidiagonals.
    
    Example:
        >>> AntiDSum(Binomial, 6)
        [1, 1, 2, 3, 5, 8]
        A000045
    """
    return [sum(T.antidiag(n)) for n in range(size)]


def ColMiddle(T: Table, size: int = 28) -> list[int]:
    """
    Return the middle column of a table.

    Args:
        T (Table): The table object from which to extract the column.
        size (int, optional): The number of elements to generate in the list. Defaults to 28.

    Returns:
        list[int]: A list of the middle terms of the given table.
    
    Example:
        >>> ColMiddle(Binomial, 6)
        [1, 1, 2, 3, 6, 10]
        A001405
    """
    return [T(n, n // 2) for n in range(size)]


def CentralE(T: Table, size: int = 28) -> list[int]:
    """
    Return the central column (terms of the form T(2n, n)) of a table.

    Args:
        T (Table): The table object from which to extract the column.
        size (int, optional): The number of elements to generate. Defaults to 28.

    Returns:
        list[int]: A list of the central terms of the given table.
        
    Example:
        >>> CentralE(Binomial, 6)
        [1, 2, 6, 20, 70, 252]
        A000984
    """
    return [T(2 * n, n) for n in range(size)]


def CentralO(T: Table, size: int = 28) -> list[int]:
    """
    Return the central column (terms of the form T(2n + 1, n)) of a table.

    Args:
        T (Table): The table object from which to extract the column.
        size (int, optional): The number of elements to generate. Defaults to 28.

    Returns:
        list[int]: A list of the central terms of the given table.
        
    Example:
        >>> CentralO(Binomial, 6)
        [1, 3, 10, 35, 126, 462]
        A001700
    """
    return [T(2 * n + 1, n) for n in range(size)]


def ColLeft(T: Table, size: int = 28) -> list[int]:
    """
    Extracts the leftmost column from a table.

    Args:
        T (Table): The table from which to extract the column.
        size (int, optional): The number of rows to extract. Defaults to 28.

    Returns:
        list[int]: A list containing the values from the leftmost column of the table.
    
    Example:
        >>> ColLeft(Nicomachus, 6)
        [1, 2, 4, 8, 16, 32]
        A000079
    """
    return [T(n, 0) for n in range(size)]


def ColRight(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of integers by applying the function T to each integer in the range from 0 to size-1.

    Args:
        T (Table): A function that takes two integer arguments and returns an integer.
        size (int, optional): The number of elements to generate. Defaults to 28.

    Returns:
        list[int]: A list of integers generated by applying T to each integer in the specified range.
    
    Example:
        >>> ColRight(Nicomachus, 6)
        [1, 3, 9, 27, 81, 243]
        A000244
    """
    return [T(n, n) for n in range(size)]


def PolyFrac(row: list[int], x: int) -> int:
    """
    Evaluate a polynomial with integer coefficients at a given point x.

    This function takes a list of coefficients representing a polynomial
    and evaluates the polynomial at the given value of x. The coefficients
    are assumed to be in descending order of powers.

    Args:
        row (list[int]): A list of integers representing the coefficients of the polynomial.
        x (int): The value at which to evaluate the polynomial.

    Returns:
        int: The result of the polynomial evaluation at x.
    """
    n = len(row) - 1
    return sum(c * x**(n - k) for (k, c) in enumerate(row))


def PosHalf(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial fractions for the first half of the rows in the table.

    Args:
        T (Table): The table from which rows are taken.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of polynomial fractions for the specified rows.
    
    Example:
        >>> PosHalf(FallingFactorial, 6)
        [1, 3, 10, 38, 168, 872]
        A010842
    """
    return [PolyFrac(T.row(n), 2) for n in range(size)]


def NegHalf(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial fractions with a negative half exponent.

    Args:
        T (Table): The table from which rows are taken.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of polynomial fractions with a -2 exponent.
        
        Example:
        >>> NegHalf(FallingFactorial, 7)
        [1, -1, 2, -2, 8, 8, 112]
        A000023
    """
    return [PolyFrac(T.row(n), -2) for n in range(size)]


def TransNat0(T: Table, size: int = 28) -> list[int]:
    """
    Transforms the nonnegative numbers by the linear transformation represented by the table.

    Args:
        T (Table): The table to be transformed.
        size (int, optional): The size parameter for the transformation. Defaults to 28.

    Returns:
        list[int]: A list of the transformed nonnegative integers.
    
    Example:
        >>> TransNat0(Binomial, 6)
        [0, 1, 4, 12, 32, 80]
        A001787
    """
    return T.trans(lambda k: k, size)


def TransNat1(T: Table, size: int = 28) -> list[int]:
    """
    Transforms the positive numbers by the linear transformation represented by the table.

    Args:
        T (Table): The table to be transformed.
        size (int, optional): The length of the returned list. Defaults to 28.

    Returns:
        list[int]: A list of the transformed positive integers.
    
    Example:
        >>> TransNat1(Binomial, 6)
        [1, 3, 8, 20, 48, 112]
        A001792
    """
    return T.trans(lambda k: k + 1, size)


def TransSqrs(T: Table, size: int = 28) -> list[int]:
    """
    Transforms the squares by the linear transformation represented by the table.

    Args:
        T (Table): The table considered as a linear transformation.
        size (int, optional): The length of the returned list. Defaults to 28.

    Returns:
        list[int]: The list of the transformed squares.
    
    Example:
        >>> TransSqrs(Lah, 6)
        [0, 1, 6, 39, 292, 2505]
        A103194
    """
    return T.trans(lambda k: k * k, size)


def BinConv(T: Table, size: int = 28) -> list[int]:
    """
    Transforms the table by computing the dot product of the n-th row of T with the n-th row of the binomial triangle.

    Args:
        T (Table): The input table with the rows to be transformed.
        size (int, optional): The number of rows th be processed. Defaults to 28.

    Returns:
        list[int]: A list of integers representing the binomial convolution of the given table.
    
    Example:
        >>> BinConv(FallingFactorial, 6)
        [1, 2, 7, 34, 209, 1546]
        A002720
    """
    return [dotproduct(Binomial.row(n), T.row(n)) for n in range(size)]


def InvBinConv(T: Table, size: int = 28) -> list[int]:
    """
    Transforms the table by computing the dot product of the n-th row of T with the n-th row of the inverse binomial triangle.

    Args:
        T (Table): The input table with the rows to be transformed.
        size (int, optional): The number of rows th be processed. Defaults to 28.

    Returns:
        list[int]: A list of integers representing the inverse binomial convolution of the given table.
    
    Example:
        >>> InvBinConv(FallingFactorial, 6)
        [1, 0, -1, -4, -15, -56]
        A009940
    """
    return [dotproduct(InvBinomial.row(n), T.row(n)) for n in range(size)]

#------

def Rev_Toff11(t: Table, size: int = 7) -> list[int]:
    """
    Generates a list of integers by reversing the given table, offsetting it by (1, 1), 
    and flattening the result to the specified size.

    Args:
        t (Table): The input table to be reversed and processed.
        size (int, optional): The size of the flattened list to be returned. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers from the processed table.
    """
    T = RevTable(t)
    T11 = Table(T.off(1, 1), T.id + "off11")
    return T11.flat(size)


def Rev_Trev11(t: Table, size: int = 7) -> list[int]:
    """
    Generates a list of integers by applying the rev11 method of the RevTable class to a given Table object.

    Args:
        t (Table): The Table object to be processed.
        size (int, optional): The number of times to apply the rev11 method. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers resulting from the rev11 method applied to the Table object.
    """
    T = RevTable(t)
    return list(flatten([T.rev11(n) for n in range(size)]))


def Rev_Tinv11(t: Table, size: int = 7) -> list[int]:
    """
    Computes the inverse of the table `t` and flattens the result.

    Args:
        t (Table): The table to be inverted.
        size (int, optional): The size parameter for the inversion. Defaults to 7.

    Returns:
        list[int]: A flattened list of the inverted table.
    """
    T = RevTable(t)
    InvT11 = T.inv11(size)
    return list(flatten(InvT11))


def Rev_Talt(t: Table, size: int = 7) -> list[int]:
    """
    Generate a list of integers by reversing the table and flattening the alternates.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of alternates to consider. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers from the alternates of the reversed table.
    """
    T = RevTable(t)
    return list(flatten([T.alt(n) for n in range(size)]))


def Rev_Tacc(t: Table, size: int = 7) -> list[int]:
    """
    Generate a list of accumulated values from a reversed table.

    Args:
        t (Table): The table to be reversed and processed.
        size (int, optional): The number of accumulations to perform. Defaults to 7.

    Returns:
        list[int]: A flattened list of accumulated values from the reversed table.
    """
    T = RevTable(t)
    return list(flatten([T.acc(n) for n in range(size)]))


def Rev_Tder(t: Table, size: int = 7) -> list[int]:
    """
    Generate a list of derivatives from a reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of derivatives to compute. Defaults to 7.

    Returns:
        list[int]: A flattened list of derivatives from the reversed table.
    """
    T = RevTable(t)
    return list(flatten([T.der(n) for n in range(size)]))


# Needs 9 rows
def Rev_Tantidiag(t: Table, size: int = 9) -> list[int]:
    """
    Generates a list of integers from the reversed table's antidiagonals.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of antidiagonals to consider. Defaults to 9.

    Returns:
        list[int]: A flattened list of integers from the reversed table's antidiagonals.
    
    Example:
        >>> Rev_Tantidiag(Leibniz, 5)
        [1, 2, 3, 2, 4, 6, 5, 12, 3]
        A128502
    """
    T = RevTable(t)
    return list(flatten([T.antidiag(n) for n in range(size)]))


def Rev_PolyRow1(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values from a reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 1 from the reversed table.
    """
    T = RevTable(t)
    return [T.poly(1, x) for x in range(size)]


def Rev_PolyRow2(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 2 from a reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 2.
    """
    T = RevTable(t)
    return [T.poly(2, x) for x in range(size)]


def Rev_PolyRow3(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 3 for a given table.

    This function takes a table `t` and generates a list of polynomial values
    of degree 3 for each element in the range of `size`. The table is first
    reversed using the `RevTable` function, and then the polynomial values
    are computed.

    Args:
        t (Table): The input table to be reversed and processed.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 3.
    """
    T = RevTable(t)
    return [T.poly(3, x) for x in range(size)]


def Rev_PolyCol3(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 3 from a reversed table.

    Args:
        t (Table): The input table.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 3.
    """
    T = RevTable(t)
    return [T.poly(x, 3) for x in range(size)]


def Rev_PolyDiag(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial diagonal values from a reversed table.

    Args:
        t (Table): The input table.
        size (int, optional): The number of diagonal values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial diagonal values.
    
    Example:
        >>> Rev_PolyDiag(Narayana, 6)
        [1, 1, 3, 19, 185, 2426]
        A242369
    """
    T = RevTable(t)
    return [T.poly(n, n) for n in range(size)]


def Rev_EvenSum(t: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of even-indexed elements in each row of the reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of sums of even-indexed elements for each row.
    """
    T = RevTable(t)
    return [sum(T.row(n)[::2]) for n in range(size)]


def Rev_OddSum(t: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of odd-indexed elements in each row of the reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list containing the sum of odd-indexed elements for each row.
    """
    T = RevTable(t)
    return [sum(T.row(n)[1::2]) for n in range(size)]


def Rev_AccRevSum(t: Table, size: int = 28) -> list[int]:
    """
    Calculate the accumulated row sums of the reversed table.

    Args:
        t (Table): The input table.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of accumulated sums for each row in the reversed table.
    """
    T = RevTable(t)
    return [sum(accumulate(T.rev(n))) for n in range(size)]


def Rev_AntiDSum(t: Table, size: int = 28) -> list[int]:
    """
    Calculate the sums of the antidiagonals of the reversed table.

    Args:
        t (Table): The input table.
        size (int, optional): The number of antidiagonals to sum. Defaults to 28.

    Returns:
        list[int]: A list of sums of the antidiagonals of the reversed table.
    
    Example:
        >>> Rev_AntiDSum(Narayana, 6)
        [1, 1, 1, 2, 4, 8]
        A004148
    """
    T = RevTable(t)
    return [sum(T.antidiag(n)) for n in range(size)]


def Rev_ColMiddle(t: Table, size: int = 28) -> list[int]:
    """
    Generates a list of integers by reversing the table and selecting the middle column.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of elements to generate. Defaults to 28.

    Returns:
        list[int]: A list of integers from the middle column of the reversed table.
    """
    T = RevTable(t)
    return [T(n, n // 2) for n in range(size)]


def Rev_CentralO(t: Table, size: int = 28) -> list[int]:
    """
    Generate the central elements T(2n + 1, n) of the reversed table.

    Args:
        t (Table): The input table.
        size (int, optional): The number of elements to generate in the list. Defaults to 28.

    Returns:
        list[int]: The list of the central elements of the reversed table.
    """
    T = RevTable(t)
    return [T(2 * n + 1, n) for n in range(size)]


def Rev_PosHalf(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial fractions for reversed elements of a table.

    Args:
        t (Table): The table object containing elements to be reversed.
        size (int, optional): The number of elements to process. Defaults to 28.

    Returns:
        list[int]: A list of polynomial fractions for the reversed elements.
    
    Example:
        >>> Rev_PosHalf(Narayana, 6)
        [1, 2, 6, 22, 90, 394]
        A152681
    """
    return [PolyFrac(t.rev(n),  2) for n in range(size)]


def Rev_NegHalf(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial fractions with a negative half exponent.

    This function takes a Table object and generates a list of polynomial fractions
    with an exponent of -2 for each element in the table, reversed up to the specified size.

    Args:
        t (Table): The table object containing the elements to be processed.
        size (int, optional): The number of elements to process. Defaults to 28.

    Returns:
        list[int]: A list of polynomial fractions with a negative half exponent.
        
    Example:
        Rev_NegHalf(Narayana, 6)
        [1, -2, 2, 2, -10, 6]
        A152681
    """
    return [PolyFrac(t.rev(n), -2) for n in range(size)]


def Rev_TransNat0(t: Table, size: int = 28) -> list[int]:
    """
    Reverse the given table and transform its elements.

    This function takes a table `t`, reverses it using the `RevTable` function,
    and then applies a transformation to its elements using the `trans` method.
    The transformation applied is the identity function (i.e., each element is
    mapped to itself).

    Args:
        t (Table): The table to be reversed and transformed.
        size (int, optional): The size parameter to be passed to the `trans` method. Defaults to 28.

    Returns:
        list[int]: A list of integers resulting from the transformation.
    
    Example:
        >>> Rev_TransNat0(StirlingCycle, 6)
        [0, 0, 1, 7, 46, 326]
        A067318
    """
    T = RevTable(t)
    return T.trans(lambda k: k, size)


def Rev_TransNat1(t: Table, size: int = 28) -> list[int]:
    """
    Reverse the given table and transform its elements by adding 1.

    Args:
        t (Table): The table to be reversed and transformed.
        size (int, optional): The size parameter for the transformation. Defaults to 28.

    Returns:
        list[int]: A list of integers resulting from the transformation.
    
    Example:
        >>> Rev_TransNat1(StirlingCycle, 6)
        [1, 1, 3, 13, 70, 446]
        A121586
    """
    T = RevTable(t)
    return T.trans(lambda k: k + 1, size)


def Rev_TransSqrs(t: Table, size: int = 28) -> list[int]:
    """
    Applies a transformation to the given table by reversing it and then squaring each element.

    Args:
        t (Table): The input table to be transformed.
        size (int, optional): The size parameter for the transformation. Defaults to 28.

    Returns:
        list[int]: A list of integers resulting from the transformation.
    
    Example:
        >>> Rev_TransSqrs(Binomial, 6)
        [0, 1, 6, 24, 80, 240]
        A001788
    """
    T = RevTable(t)
    return T.trans(lambda k: k * k, size)


# sum((-1)**(n-k)*Binomial(n,k)*Trev(n, k) for k in range(n+1)) for n in range(size)])


"""The basic construction is a map
    (Table:Class, Trait:Function) -> (Anum:Url, TreatInfo:TeXString)
"""

# Useful for the LaTeX titels: https://latexeditor.lagrida.com/

TraitInfo: TypeAlias = Tuple[Trait, int, str]

'''The dictionary of all traits with their respective functions and TeX strings.
   The size of the table is set to 7, 9 or 28 rows for the default case.
   It is mandatory that this dictionary starts with the key 'Triangle'!
'''
AllTraits: dict[str, TraitInfo] = {
    "Triangle     ": (Triangle,  7, r"\(T_{n,k}\)"),
    "Tinv         ": (Tinv,      7, r"\(T^{-1}_{n,k}\)"),
    "Trev         ": (Trev,      7, r"\(T_{n,n-k}\)"),
    "Tinvrev      ": (Tinvrev,   7, r"\((T_{n,n-k})^{-1}\)"),
    "Trevinv      ": (Trevinv,   7, r"\((T_{n,n-k})^{-1}\)"),
    "Toff11       ": (Toff11,    7, r"\(T_{n+1,k+1} \)"),
    "Trev11       ": (Trev11,    7, r"\(T_{n+1,n-k+1} \)"),
    "Tinv11       ": (Tinv11,    7, r"\(T^{-1}_{n+1,k+1}\)"),
    "Tinvrev11    ": (Tinvrev11, 7, r"\((T_{n+1,n-k+1})^{-1}\)"),
    "Trevinv11    ": (Trevinv11, 7, r"\((T^{-1}_{n+1,n-k+1})\)"),
    "Tantidiag    ": (Tantidiag, 9, r"\(T_{n-k,k}\ \ (k \le n/2)\)"),
    "Tacc         ": (Tacc,      7, r"\(\sum_{j=0}^{k} T_{n,j}\)"),
    "Talt         ": (Talt,      7, r"\(T_{n,k}\ (-1)^{k}\)"),
    "Tder         ": (Tder,      7, r"\(T_{n,k+1}\ (k+1) \)"),
    "TablCol0     ": (TablCol0,  28, r"\(T_{n  ,0}\)"),
    "TablCol1     ": (TablCol1,  28, r"\(T_{n+1,1}\)"),
    "TablCol2     ": (TablCol2,  28, r"\(T_{n+2,2}\)"),
    "TablCol3     ": (TablCol3,  28, r"\(T_{n+3,3}\)"),
    "TablDiag0    ": (TablDiag0, 28, r"\(T_{n  ,n}\)"),
    "TablDiag1    ": (TablDiag1, 28, r"\(T_{n+1,n}\)"),
    "TablDiag2    ": (TablDiag2, 28, r"\(T_{n+2,n}\)"),
    "TablDiag3    ": (TablDiag3, 28, r"\(T_{n+3,n}\)"),
    "TablLcm      ": (TablLcm,   28, r"\(\text{lcm} \{ \ \| T_{n,k} \| : k=0..n \} \)"),
    "TablGcd      ": (TablGcd,   28, r"\(\text{gcd} \{ \ \| T_{n,k} \| : k=0..n \} \)"),
    "TablMax      ": (TablMax,   28, r"\(\text{max} \{ \ \| T_{n,k} \| : k=0..n \} \)"),
    "TablSum      ": (TablSum,   28, r"\(\sum_{k=0}^{n} T_{n,k}\)"),
    "EvenSum      ": (EvenSum,   28, r"\(\sum_{k=0}^{n} T_{n,k}\ ( 2 \mid k) \)"),
    "OddSum       ": (OddSum,    28, r"\(\sum_{k=0}^{n} T_{n,k}\ (1 - (2 \mid k)) \)"),
    "AltSum       ": (AltSum,    28, r"\(\sum_{k=0}^{n} T_{n,k}\ (-1)^{k}\)"),
    "AbsSum       ": (AbsSum,    28, r"\(\sum_{k=0}^{n} \| T_{n,k} \| \)"),
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
    "RevEvenSum   ": (Rev_EvenSum,   28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ (2 \mid k) \)"),
    "RevOddSum    ": (Rev_OddSum,    28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ (1- (2 \mid k)) \)"),
    "RevAccRevSum ": (Rev_AccRevSum, 28, r"\(\sum_{k=0}^{n} \sum_{j=0}^{k}T_{n,n-j}\)"),
    "RevAntiDSum  ": (Rev_AntiDSum,  28, r"\(\sum_{k=0}^{n/2}T_{n-k,n-k}\)"),
    "RevColMiddle ": (Rev_ColMiddle, 28, r"\(T_{n, n/2}\)"),
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
