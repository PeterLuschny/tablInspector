"""
Classes:
    Table: A class that provides methods for generating and manipulating integer triangles.

    The class has the following parameter:
        row:   A function that generates the n-th row of the table for a given integer input n.
        id:    A string representing the name of the triangle.
        oeis:  A list of strings representing A-numbers of closely related OEIS triangles.
        invid: A string representing the ID of the inverse triangle.
        tex:   A TeX-string of the defining formula.
        invQ:  A boolean indicating whether the triangle is invertible, derived from whether invid, 
               the ID of the inverse triangle, is non-empty.

    The class provides the following 30 methods:

        __init__(self, gen: rowgen, id: str, oeis: list[str] = [''], invid: str = '', tex: str = '') -> None
        __getitem__(self, n: int) -> list[int]
        __call__(self, n: int, k: int) -> int

        val(self, n: int, k: int) -> int
        itr(self, size: int) -> Iterator[list[int]]
        tab(self, size: int) -> tabl
        mat(self, size: int) -> tabl
        row(self, n: int) -> trow
        rev(self, row: int) -> trow
        antidiag(self, n: int) -> list[int]
        alt(self, n: int) -> trow
        acc(self, row: int) -> trow
        diff(self, n: int) -> trow
        der(self, n: int) -> trow
        diag(self, n: int, size: int) -> list[int]
        col(self, k: int, size: int) -> list[int]
        sum(self, row: int) -> int
        flat(self, size: int) -> list[int]
        inv(self, size: int) -> tabl
        revinv(self, size: int) -> tabl
        invrev(self, size: int) -> tabl
        off(self, N: int, K: int) -> rowgen
        rev11(self, n: int) -> trow
        inv11(self, size: int) -> tabl
        revinv11(self, size: int) -> tabl
        invrev11(self, size: int) -> tabl
        poly(self, n: int, x: int) -> int
        trans(self, s: seq, size: int) -> list[int]
        invtrans(self, s: seq, size: int) -> list[int]
        show(self, size: int) -> None

    These methods provide various functionalities for manipulating and generating 
    integer triangles. For example, the row method returns the n-th row of the triangle, 
    the rev method returns the reversed row of the triangle, and the antidiag method 
    returns the n-th antidiagonal of the triangle.

Type Aliases:
    trow:  Type alias for a list of integers representing the row of a triangle.
    tabl:  Type alias for a list of rows representing a triangle.
    seq:   Type alias for a callable that takes an integer and returns an integer.
    rowgen:  Type alias for a callable that takes an integer and returns a row of a triangle.
    tblgen:  Type alias for a callable that takes two integers and returns an integer 
           (understood as the value of the triangle T(n,k)).
    trait: Type alias for a callable that takes a Table and an integer and returns a list of integers.

Functions:
    RevTable(T: Table) -> Table:
        Creates a new Table with reversed rows from the given Table.
    AltTable(T: Table) -> Table:
        Creates a new table with terms with alternating signs from the given Table.
    SubTriangle(T: Table, N: int, K: int) -> Table:
        Generates a sub-triangle of a given size from a given triangle.
"""

from typing import Callable, TypeAlias, Iterator
from itertools import accumulate, islice
from functools import cache
import operator
from more_itertools import difference
from _tablinverse import InvertMatrix

# #@

# TABLE T ENUMERATED AS A TRIANGLE
# Is always (0,0)-based!
#
# T(0,0)
# T(1,0)  T(1,1)
# T(2,0)  T(2,1)  T(2,2)
# T(3,0)  T(3,1)  T(3,2)  T(3,3)
# T(4,0)  T(4,1)  T(4,2)  T(4,3)  T(4,4)
# T(5,0)  T(5,1)  T(5,2)  T(5,3)  T(5,4)  T(5,5)
#
# A subtriangle of the standard triangle T as indexed above
# is given by a new root node [N, K].
# For some dimension size > 0 it is defined as
# T[N, K, size] = [[T(n, k) for k in range(K, N + n + 1)]
#                           for n in range(N, N + size)]
#
# Examples for the enumerations:
# row(4)     = [T(4,0), T(4,1), T(4,2), T(4,3), T(4,4)]
# col(2, 5)  = [T(2,2), T(3,2), T(4,2), T(5,2), T(6,2)]
# diag(2, 5) = [T(2,0), T(3,1), T(4,2), T(5,3), T(6,4)]


"""Type: row"""
trow: TypeAlias = list[int]

"""Type: triangle"""
tabl: TypeAlias = list[list[int]]

"""Type: sequence"""
seq: TypeAlias = Callable[[int], int]

"""Type: row generator"""
rowgen: TypeAlias = Callable[[int], trow]

"""Type: triangle generator"""
tblgen: TypeAlias = Callable[[int, int], int]


class Table:
    """Provides basic methods for manipulating integer triangles."""
    def __init__(
            self,
            gen: rowgen,
            id: str,
            oeis: list[str] = [''],
            invid: str = '',
            tex: str = ''
        ) -> None:
        """
        Provides basic methods for manipulating integer triangles.

        Args:
            gen:  Function gen(n:int) -> list[int], defined for all n >= 0.
            id:   The name of the triangle.
            oeis:  A list of A-numbers of closely related OEIS triangles.
            invid: The identifier for the inverse of the triangle.
            tex: Defining formula as a TeX-string. 
        """
        self.gen = gen
        self.id = id
        self.oeis = oeis
        self.invid = invid
        self.tex = tex
        self.invQ = invid != ''


    def __getitem__(self, n: int) -> trow:
        """
        Returns the n-th row of the triangle.

        Args:
            n: The index of the row.

        Returns:
            list[int]: The generated row.

        Raises:
            IndexError: if n < 0.
        """
        if n < 0:
            raise IndexError('0 <= n expected')
        return self.gen(n)


    def row(self, n: int) -> trow:
        """
        Return the n-th row of generated table

        Args:
            n, row index

        Returns:
            trow: The n-th row of the table.

        Raises:
            IndexError: if n < 0.
        """
        if n < 0:
            raise IndexError('0 <= n expected')
        return self.gen(n)


    def __call__(self, n: int, k: int) -> int:
        """
        Return term of table with index (n, k).

        Args:
            n, row index
            k, column index

        Returns:
            term of the table
        
        Raises:
            IndexError: if k > n, k < 0, or n < 0.
        """
        if k > n or k < 0 or n < 0:
            raise IndexError('0<=k<=n expected')
        return self.row(n)[k]

    def val(self, n: int, k: int) -> int:
        """
        Return the term of the table with index (n, k).

        Args:
            n, row index
            k, column index

        Returns:
            term of the table

        Raises:
            IndexError: if k > n, k < 0, or n < 0.
        """
        if k > n or k < 0 or n < 0:
            raise IndexError('0<=k<=n expected')
        return self.row(n)[k]


    def itr(self, size: int) -> Iterator[list[int]]:
        """
        Generate an iterator that yields a specified number of elements from the table.

        Args:
            size (int): The number of elements to yield.

        Returns:
            Iterator[list[int]]: An iterator that yields lists of integers.
            
        Example:
            >>> for r in Abel.itr(5): print(r, sum(r))
            [1] 1
            [0, 1] 1
            [0, 2, 1] 3
            [0, 9, 6, 1] 16
            [0, 64, 48, 12, 1] 125
        """
        return islice(iter(self.tab(size)), size)


    def tab(self, size: int) -> tabl:
        """
        Generates a table with the specified number of rows.

        Args:
            size, number of rows of the table to be generated

        Returns:
            A table generated with the specified number of rows.

        Example:
            >>> Abel.tab(5)
            [[1], [0, 1], [0, 2, 1], [0, 9, 6, 1], [0, 64, 48, 12, 1]]
        """
        return [list(self.row(n)) for n in range(size)]


    def mat(self, size: int) -> list[list[int]]:
        """
        Generates a size x size matrix with the table as the lower triangle.

        Args:
            size, number of rows and columns

        Returns:
            size x size matrix with the table as the lower triangle.
            
        Example:
            >>> Abel.mat(5)
            [[1,  0, 0,  0, 0], 
            [0,  1,  0,  0, 0], 
            [0,  2,  1,  0, 0], 
            [0,  9,  6,  1, 0], 
            [0, 64, 48, 12, 1]]
        """
        return [[self.row(n)[k] if k <= n else 0
                for k in range(size)] for n in range(size)]


    def rev(self, n: int) -> trow:
        """
        Reverses the elements of a specified row.

        Args:
            n index of the row to be reversed

        Returns:
            reversed row
        
        Example:
            >>> Abel.rev(4)
            [1, 12, 48, 64, 0]
        """
        return list(reversed(self.row(n)))


    def antidiag(self, n: int) -> list[int]:
        """
        Args:
            start index of the antidiagonal

        Returns:
            n-th antidiagonal

        Example:
            >>> [Motzkin.antidiag(n) for n in range(5)]
            [[1], [1], [2, 1], [4, 2], [9, 5, 1]]
            A106489
        """
        return [self.row(n - k)[k] for k in range((n + 2) // 2)]


    def alt(self, n: int) -> trow:
        """
        Generate an alternating sequence of terms.

        Args:
            n (int): The index of the row to be generated.

        Returns:
            trow: A list of terms with each term multiplied 
                  by (-1) raised to its row index.
        
        Example:
            >>> Abel.alt(4)
            [0, -64, 48, -12, 1]
        """
        return [(-1) ** k * term for k, term in enumerate(self.row(n))]


    def acc(self, n: int) -> trow:
        """
        Args:
            index of row to be accumulated.

        Returns:
            accumulated row
        
        Example:
            >>> Abel.acc(4)
            [0, 64, 112, 124, 125]
        """
        return list(accumulate(self.row(n)))


    def diff(self, n: int) -> trow:
        """
        Args:
            index of row the first differences is looked for

        Returns:
            first differences of row
            
        Example:
            >>> Abel.diff(4)
            [0, 64, -16, -36, -11]
            >>> list(accumulate(Abel.diff(5))) == Abel.row(5)
            True
        """
        return list(difference(self.row(n)))


    def der(self, n: int) -> trow:
        """
        Args:
            index of row-polynomial the derivative is looked for

        Returns:
            derivative of row-polynomial
        
        Example:
            >>> Abel.der(4)
            [64, 96, 36, 4]
        """
        if n == 0: return [0]
        powers = range(n + 1)
        coeffs = self.row(n)
        return list(map(operator.mul, coeffs, powers))[1:n+1]


    def diag(self, n: int, size: int) -> list[int]:
        """
        Args:
            n is the start index of the diagonal
            size, length of diagonal

        Returns:
            n-th diagonal starting at the left side
            
        Example:
            >>> Abel.diag(1, 5)
            [0, 2, 6, 12, 20]
        """
        return [self.row(n + k)[k] for k in range(size)]

    def col(self, k: int, size: int) -> list[int]:
        """
        Args:
            k, start at column k
            size, length of column

        Returns:
            k-th column starting at the main diagonal
        
        Example:
            >>> Abel.col(1, 5)
            [1, 2, 9, 64, 625]
        """
        return [self.row(k + n)[k] for n in range(size)]


    def sum(self, n: int) -> int:
        """
        Sums up the elements of a specified row.

        Args:
            n index (0-based) of the row to be summed up

        Returns:
            Sum of the elements in the specified row.

        Example:
            >>> Abel.sum(4)
            125
        """
        return sum(self.row(n))


    def flat(self, size: int) -> list[int]:
        """
        Flattens the table by reading the first size rows.

        Args:
            size, number of rows to be flattened

        Returns:
            generated table read by rows, flattened

        Example:
            >>> Abel.flat(5)
            [1, 0, 1, 0, 2, 1, 0, 9, 6, 1, 0, 64, 48, 12, 1]
        """
        return [self.row(n)[k] for n in range(size) for k in range(n + 1)]


    def inv(self, size: int) -> tabl:
        """
        Args:
            size, number of rows of the table to be inverted

        Returns:
            inverse table if it exists, otherwise the empty table

        Example:
            >>> Abel.inv(4)
            [[1], [0, 1], [0, -2, 1], [0, 3, -6, 1]]
        """
        if not self.invQ:
            return []

#       self.tab(size) = [list(self.row(n)) for n in range(size)]
        M = [[self.row(n)[k] for k in range(n + 1)] for n in range(size)]

        V = InvertMatrix(M)
        if V == []:
            self.invQ = False
            return []

        return V


    def revinv(self, size: int) -> tabl:
        """
        Args:
            size, number of reversed rows of the inverted table

        Returns:
            table with reversed rows of the inverse table if it exists, otherwise the empty table
        
        Example:
            >>> Abel.revinv(4)
            [[1], [1, 0], [1, -2, 0], [1, -6, 3, 0]]
        """
        V = self.inv(size)
        if V == []:
            return []

        return [[V[n][n - k] for k in range(n + 1)] for n in range(size)]


    def invrev(self, size: int) -> tabl:
        """
        Args:
            size, number of rows of the inverse table of reversed rows

        Returns:
            inverse table of reversed rows if it exists, otherwise the empty table
        
        Example:
            >>> Abel.invrev(4)
            []
        """
        M = [list(reversed(self.row(n))) for n in range(size)]

        return InvertMatrix(M)


    def off(self, N: int, K: int) -> rowgen:
        """
        Subtriangle based in (N, K).
        Args:
            N, shifts row-offset by N
            K, shifts column-offset by K

        Returns:
            row generator of shifted table
        
        Example:
            >>> [Abel.off(1, 1)(n) for n in range(4)]
            [[1], [2, 1], [9, 6, 1], [64, 48, 12, 1]]
        """
        def subgen(n: int) -> trow:
            return self.row(n + N)[K: N + n + 1]

        return subgen


    def rev11(self, n: int) -> trow:
        """
        Args:
            size, number of rows

        Returns:
            sub-table with offset (1,1) and reversed rows
        
        Example:
            >>> [Abel.rev11(n) for n in range(4)]
            [[1], [1, 2], [1, 6, 9], [1, 12, 48, 64]]
        """
        return list(reversed(self.off(1, 1)(n)))

    def inv11(self, size: int) -> tabl:
        """
        Args:
            size, number of rows

        Returns:
            inverse of the sub-table with offset (1,1) if it exists, otherwise the empty table
        
        Example:
            >>> Abel.inv11(4)
            [[1], [-2, 1], [3, -6, 1], [-4, 24, -12, 1]]
        """
        M = [list(self.off(1, 1)(n)) for n in range(size)]

        return InvertMatrix(M)


    def revinv11(self, size: int) -> tabl:
        """
        Args:
            size, number of rows

        Returns:
            reversed rows of the inverse sub-table with offset (1,1)
        
        Example:
            >>> Abel.revinv11(4)
            [[1], [1, -2], [1, -6, 3], [1, -12, 24, -4]]
        """
        M = self.inv11(size)
        return [list(reversed(row)) for row in M]


    def invrev11(self, size: int) -> tabl:
        """
        Args:
            size, number of rows

        Returns:
            sub-table with offset (1,1), reversed rows and inverted if it exists, otherwise the empty table

        Example:
            >>> Abel.invrev11(4)
            []
        """
        M = [list(reversed(self.off(1, 1)(n))) for n in range(size)]

        return InvertMatrix(M)


    def poly(self, n: int, x: int) -> int:
        """The rows seen as the coefficients of a polynomial in
        ascending order of powers. Evaluats the n-th row at x.

        Args:
            n, index of row
            x, argument of the polynomial

        Returns:
            sum(T(n, k) * x^j for j=0..n)
        
        Example:
            >>> Abel.poly(4, 2)
            432
        """
        return sum(c * (x ** j) for (j, c) in enumerate(self.row(n)))


    def trans(self, s: seq, size: int) -> list[int]:
        """
        Also called sumprod:
        [sum(T(n, k) * s(k) for 0 <= k <= n) for 0 <= n < size]
        For example, if T is the binomial then this is the
        'binomial transform'.

        Args:
            s, sequence. Recommended to be a cached function.
            size, length of the returned list

        Returns:
            Initial segment of length size of s transformed.

        Example:
            >>> Abel.trans(lambda n: n, 6)
            [0, 1, 4, 24, 200, 2160]
        """
        return [sum(self.row(n)[k] * s(k) for k in range(n + 1))
               for n in range(size)]


    def invtrans(self, s: seq, size: int) -> list[int]:
        """
        Also called inverse sumprod:
        [sum((-1)^(n-k) * T(n, k) * s(k) for 0 <= k <= n) for 0 <= n < size]
        For example, if T is the binomial then this is the
        'inverse binomial transform'.

        Args:
            s, sequence. Recommended to be cached function.
            size, length of the returned list

        Returns:
            Initial segment of length size of s transformed.

        Example:
            >>> Abel.invtrans(lambda n*n: n, 6)
            [0, 1, 2, -6, 36, -320]
        """
        return [sum((-1)**(n-k) * self.row(n)[k] * s(k) for k in range(n + 1))
               for n in range(size)]


    def show(self, size: int, total: bool = False) -> None:
        """
        Prints the first 'size' rows with the row-index in front and,
        optionally, the row sum at the end.

        Args:
            size: number of rows to print.
            total (optional): If True, print also the row sum. Defaults to False.
            
        Example:
            >>> Abel.show(5, True)
            [0] [1] [1]
            [1] [0, 1] [1]
            [2] [0, 2, 1] [3]
            [3] [0, 9, 6, 1] [16]
            [4] [0, 64, 48, 12, 1] [125]
        """
        for n in range(size):
            r = self.row(n)
            print([n], r, [sum(r)] if total else '')
 

def RevTable(T: Table) -> Table:
    """
    Create a new Table with reversed rows from the given Table.
    Args:
        T (Table): The original Table to reverse.
    Returns:
        Table: A new Table with rows in reverse order.
        The returned Table will have an identifier that appends ":Rev" 
        to the original table's identifier.
    """
    @cache
    def revgen(n: int) -> trow:
        return T.rev(n)
    return Table(revgen, T.id + ":Rev")


def AltTable(T: Table) -> Table:
    """
    Creates a new table with terms with alternating signs from the given Table.
    Args:
        T (Table): The original table to generate an alternating form.
    Returns:
        Table: A new table with a generation function of alternating terms.
        The returned Table will have an identifier that appends ":Alt" 
        to the original table's identifier.
    """
    @cache
    def altblgen(n: int) -> trow:
        return T.alt(n)
    return Table(altblgen, T.id + ":Alt")


def SubTable(T: Table, N: int, K: int) -> Table:
    """
    Generates a sub-triangle of a given size from a given triangle.

    Args:
        T (Table) 
        N (int): The starting row index of the sub-triangle.
        K (int): The starting column index of the sub-triangle.
        size (int): The size of the sub-triangle.

    Returns:
        tabl: The generated sub-triangle.

    """
    return Table(T.off(N, K), T.id + ":Off")


"""Type: trait"""
Trait: TypeAlias = Callable[[Table, int], list[int]]


if __name__ == "__main__":

    from functools import cache
    from _tabldict import InspectTable
    from more_itertools import flatten
    from StirlingSet import StirlingSet
    from Abel import Abel

    InspectTable(StirlingSet)

    print()
    print("Different ways to display a Table:")
    print()

    Abel.show(7)

    print()
    print(Abel.tab(7))

    print()
    print(list(flatten(Abel.itr(7))))

    print()

    # Use the Table as an iterable:
    rows = StirlingSet.itr(7)
    for r in rows:
        print(r, sum(r))

    print()
    print(Abel.val(8, 4) == Abel(8, 4))


""" IGNORE THIS PART

    A generator for an already existing table. For internal use only.

    Args:
        T, table to be wrapped
        max, size of the table

    Returns:
        table generator

    Error:
        If the requested size > size of given table then
        an emtpy list is returned.

def PseudoGenerator(T: tabl, max: int) -> rowgen:    
    def gen(n: int) -> trow:
        if n >= max:
            return []
        return T[n]
    return gen
"""