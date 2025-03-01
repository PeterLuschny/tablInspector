<img src="imag/IntegerTrianglesPy.png" width="300" alt="The tabl Inspector"/>

# The tabl Inspector

No, the name has no typo. 'tabl' is a keyword in the Online Encyclopedia of Integer Sequences (OEIS). It classifies a sequence as a regular triangular array of numbers.

This library can be used in four ways:

- As a library of Python implementations of lower triangular matrices with integer values, which can be integrated into your programs.

- The tblInspector can also be considered an app that works like an add-on when displaying some HTML pages of the OEIS (those implemented in this library). However, you do not have to load an app or add an add-on to your browser; you just need to access these pages via this link:

  [Index](https://peterluschny.github.io/tablInspector/index.html)

  The entire infrastructure for creating such pages with cross-references is implemented in the library. This allows you to generate an overview of a cluster of related OEIS sequences  in just a couple of minutes.

- A Jupyter [notebook](src/InteractiveTableInspector.ipynb) is based on the library, with which you can interactively study the more than 8000 defined relationships between sequences in the OEIS database.

- The fourth application is more theoretical. It tries to identify semantically meaningful clusters of sequences generated by a fixed pool of elementary transformations mapping the integer triangles to straight sequences. Such transformations are called 'table traits'. Conversely, the number of sequences of a particular trait implemented in the database can be used to infer the significance of these characteristics.

  The relationships between triangles and traits often give new interpretations of sequences or point out gaps in the OEIS database that are easy to close.

# Some examples

The implementations are written in annotated Python and refer to a uniform interface. An integer triangle is a list of integer lists (list[list[int]]). As usual in Python, all lists are 0-based; in particular, all triangles have offset = 0.

This allows us to identify an integer triangle with a list whose indexing is like this:

```
[ [(0,0)], [(1,0), (1,1)], [(2,0), (2,1), (2,2)], ..., [(n,0), (n,1), ... (n,k), ... (n,n)] ]
```

For example, G. W. Leibniz wrote down a number triangle in his "Dissertatio de arte combinatoria", Leipzig in 1666, that will be displayed:

```
    [0]    [0]
    [1]    [0,   1]
    [2]    [0,   2,    2]
    [3]    [0,   3,    4,   3]
    [4]    [0,   4,    6,   6,    4]
    [5]    [0,   5,    8,   9,    8,    5]
    [6]    [0,   6,   10,  12,   12,   10,    6]
    [7]    [0,   7,   12,  15,   16,   15,   12,    7]
    [8]    [0,   8,   14,  18,   20,   20,   18,   14,   8]
    [9]    [0,   9,   16,  21,   24,   25,   24,   21,  16,  9]
```

The first (left) column indicates the row number and is not part of the triangle.

To use the library, put the file Tables.py in the same directory where your project is or where the interpreter can find it elsewhere.
Make sure your Python has the "more_itertools" package installed. The other Python files are not needed as long as you do not want to add new triangles.

### Example 1

```
    from Tables import TablesListPreview
    TablesListPreview()
```

This shows the list of the sequences implemented.

To use a Table from the library:

### Example 2

```
    from Tables import Abel, InspectTable
    InspectTable(Abel)
```

Use the Table as an iterable:

### Example 3

```
    AbelRows = Abel.itr(7)
    for row in AbelRows:
        print(row, 'sum:', sum(row))
```

### ... or add your own table:

Go to the file "Template.py". It describes how you can add your own Table class to the library in three simple steps.

# The methods

Currently, 116 triangles are included in this library, implementing the class `Table` that provides the following methods:

<pre>
    __call__(self, n: int, k: int) -> int | T(n, k)
    val (n:int, k:int)   -> int  | T(n, k)
    row (n: int)         -> tblrow | n-th row of table
    itr (size: int)      -> Iterator[list[int]] | traverse the first 'size' rows
    flat (size: int)     -> list[int] | flattened form of the first size rows
    diag(n, size: int)   -> list[int] | diagonal starting at the left side
    col (k, size: int)   -> list[int] | k-th column starting at the main diagonal
    sum (size: int)      -> list[int] | sums of the first size rows
    antidiag (size: int) -> list[int] | upward anti-diagonals
    rev (size: int)      -> tblrow | reversed rows
    acc (size: int)      -> tblrow | accumulated row
    alt (size: int)      -> tblrow | alternating signs
    diff (size: int)     -> tblrow | first difference of row
    der (size: int)      -> tblrow | derivative of row
    tab (size: int)      -> tabl | table with size rows
    mat (size: int)      -> tabl | matrix form of lower triangular array
    inv (size: int)      -> tabl | inverse table
    revinv (size: int)   -> tabl | row reversed inverse
    invrev (size: int)   -> tabl | inverse of row reversed
    off (N: int, K: int) -> rowgen | new offset (N, K)
    revinv11 (size: int) -> tabl | revinv from offset (1, 1)
    invrev11 (size: int) -> tabl | invrev from offset (1, 1)
    poly(n: int, x: int) -> int  | sum(T(n, k) * x^j for j=0..n)
    trans(s: seq, size)  -> list[int] | linear transformation induced by T
    invtrans(s: seq, size) -> list[int] | inverse transformation induced by T
    show (size: int)     -> None | prints the first 'size' rows with row-numbers
</pre>

These methods provide various ways for manipulating and generating integer triangles. For example, the row method returns the n-th row of the triangle, the rev method returns the reversed row of the triangle, and the antidiag method returns the n-th antidiagonal of the triangle.

# Triangles as semantically meaningful clusters in the database.

This project aimed to identify the crucial triangles without relying on subjective assessment. For this, a metric had to be developed. We based the ranking on the number of distinct sequences generated by a fixed pool of elementary transformations mapping the triangles to other sequences. These transformations are called 'table traits' and are implemented in the module '\_tabltraits'. These simple transformations occur everywhere in the OEIS but are not always recognized as such and often lead to unnecessarily complicated formulas.

In the table below, the two columns on the right are _examples_ of thousands of similar identities that can be generated with the module. We give some examples here; many more examples can be found in the notebook [Examples](src/ExamplesTableInspector.ipynb), where you can also find a table with the traits currently implemented.

| Name         |  Formula | Triangle   | Trait  |
| :---         | :---     | :---       | :---   |
| Tinv         | $ (T^{-1})_{n,k} $ | Abel  | A059297  |
| Tantidiag    | $ T_{n-k,k}\ \ (k \le n/2) $ | Motzkin  | A106489  |
| Tder         | $ T_{n,k+1}\ (k+1)  $ | Abel | A225465 |
| TablCol2     | $ T_{n+2,2} $ | WardCycle | A000276 |
| TablDiag0    | $ T_{n  ,n} $ | WardSet | A001147 |
| TablLcm      | $ \text{lcm} \{ \ \| T_{n,k} \| : k=0..n \} $ | Binomial | A002944 |
| TablGcd      | $ \text{gcd} \{ \ \| T_{n,k} \| : k=0..n \} $ | Fubini | A141056 |
| AntiDSum     | $ \sum_{k=0}^{n/2} T_{n-k, k} $ | Binomial | A000045 |
| TransSqrs    | $ \sum_{k=0}^{n}T_{n,k}\ k^{2} $ | Lah | A103194  |
| BinConv      | $ \sum_{k=0}^{n}T_{n,k}\ \binom{n}{k}  $ | FallingFactorial | A002720  |
| InvBinConv   | $ \sum_{k=0}^{n}T_{n,k}\ (-1)^{n-k}\ \binom{n}{k} $ | FallingFactorial | A009940  |
| PolyCol2     | $ \sum_{k=0}^{n}T_{n,k}\ 2^k $ | Abel | A007334 |

Note that references to OEIS-Ids are approximate. They often differ in signs and offset, sometimes also in the first few values. In Visual Studio Code, the TeX formulas are displayed correctly.

# Looking up the traits in the OEIS

The module provides a central function that extracts the traits from tables and simultaneously searches for further information in the OEIS database. In particular, the function returns the A-number of the sequence, provided it is in the database.

<pre>
    def LookUp(t: Table, tr: Trait, info: bool = True) -> int:
        """
        Look up the A-number in the OEIS database based on a trait of a table.

        Args:
            t (Table):  The table to be analyzed.
            tr (Trait): A function that extracts a trait from the table.
            info (bool, optional): If True, information about the matching
                        will be displayed. Defaults to True.

        Returns:
            int: The A-number of the sequence if found, otherwise 0.

        Raises:
            Exception: If the OEIS server cannot be reached after multiple attempts.
            Currently -999999 is returned if the OEIS server cannot be reached.

        Example:
            >>> LookUp(Fubini, PolyDiag)
            *** Found: A094420 Generalized ordered Bell numbers Bo(n,n).
        """
</pre>

With 70 implemented traits and 100 triangles currently out of the box, 7000 queries can be made this way. This systematically links the triangles with sequences to a network and often reveals previously unnoticed connections.

# Ranking of triangles.

In this way, we found that each of the 50 most highly ranked triangles generates, on average, 35 distinct related sequences registered in the OEIS. Thus, a high rank means the triangle is a significant structural component in the OEIS database and binds seemingly unrelated sequences into a semantically meaningful cluster.

Currently, 118 triangles are included in this ranking. The top 20 triangles are listed below. (Note that some links have not yet been implemented.) The full list can be seen in [Ranking.md](data/Ranking.md).

|     | Name             |  OEIS   | Distinct | Hits |                              Traits                              |                                      Links                                       |
| :-: | :--------------- | :-----: | :------: | :--: | :--------------------------------------------------------------: | :------------------------------------------------------------------------------: |
|  1  | StirlingSet      | A048993 |    53    |  63  | [All](https://peterluschny.github.io/tabl/StirlingSet.html)      | [OEIS](https://peterluschny.github.io/tablInspector/StirlingSetTraits.html)    |
|  2  | FallingFactorial | A008279 |    48    |  60  | [All](https://peterluschny.github.io/tabl/FallingFactorial.html) | [OEIS](https://peterluschny.github.io/tablInspector/FallingFactorialTraits.html) |
|  3  | StirlingCycle    | A132393 |    47    |  63  | [All](https://peterluschny.github.io/tabl/StirlingCycle.html)    | [OEIS](https://peterluschny.github.io/tablInspector/StirlingCycleTraits.html)   |
|  4  | BinaryPell       | A038207 |    46    |  57  | [All](https://peterluschny.github.io/tabl/BinaryPell.html)       | [OEIS](https://peterluschny.github.io/tablInspector/BinaryPellTraits.html)    |
|  5  | Lah              | A271703 |    46    |  56  | [All](https://peterluschny.github.io/tabl/Lah.html)              | [OEIS](https://peterluschny.github.io/tablInspector/LahTraits.html)        |
|  6  | Lucas            | A029635 |    45    |  59  | [All](https://peterluschny.github.io/tabl/Lucas.html)            | [OEIS](https://peterluschny.github.io/tablInspector/LucasTraits.html)       |
|  7  | DyckPathsInv     | A085478 |    43    |  55  | [All](https://peterluschny.github.io/tabl/DyckPathsInv.html)     | [OEIS](https://peterluschny.github.io/tablInspector/DyckPathsInvTraits.html)   |
|  8  | Fubini           | A131689 |    43    |  50  | [All](https://peterluschny.github.io/tabl/Fubini.html)           | [OEIS](https://peterluschny.github.io/tablInspector/FubiniTraits.html)      |
|  9  | Partition        | A072233 |    43    |  55  | [All](https://peterluschny.github.io/tabl/Partition.html)        | [OEIS](https://peterluschny.github.io/tablInspector/PartitionTraits.html)     |
| 10  | CatalanInv       | A128908 |    42    |  49  | [All](https://peterluschny.github.io/tabl/CatalanInv.html)       | [OEIS](https://peterluschny.github.io/tablInspector/CatalanInvTraits.html)    |
| 11  | BesselInv        | A122848 |    41    |  48  | [All](https://peterluschny.github.io/tabl/BesselInv.html)        | [OEIS](https://peterluschny.github.io/tablInspector/BesselInvTraits.html)     |
| 12  | Ordinals         | A002262 |    41    |  66  | [All](https://peterluschny.github.io/tabl/Ordinals.html)         | [OEIS](https://peterluschny.github.io/tablInspector/OrdinalsTraits.html)     |
| 13  | DyckPaths        | A039599 |    39    |  51  | [All](https://peterluschny.github.io/tabl/DyckPaths.html)        | [OEIS](https://peterluschny.github.io/tablInspector/DyckPathsTraits.html)     |
| 14  | Powers           | A004248 |    39    |  49  | [All](https://peterluschny.github.io/tabl/Powers.html)           | [OEIS](https://peterluschny.github.io/tablInspector/PowersTraits.html)      |
| 15  | Motzkin          | A064189 |    38    |  48  | [All](https://peterluschny.github.io/tabl/Motzkin.html)          | [OEIS](https://peterluschny.github.io/tablInspector/MotzkinTraits.html)      |
| 16  | Catalan          | A128899 |    37    |  44  | [All](https://peterluschny.github.io/tabl/Catalan.html)          | [OEIS](https://peterluschny.github.io/tablInspector/CatalanTraits.html)      |
| 17  | Divisibility     | A113704 |    37    |  58  | [All](https://peterluschny.github.io/tabl/Divisibility.html)     | [OEIS](https://peterluschny.github.io/tablInspector/DivisibilityTraits.html)   |
| 18  | Eulerian         | A173018 |    37    |  56  | [All](https://peterluschny.github.io/tabl/Eulerian.html)         | [OEIS](https://peterluschny.github.io/tablInspector/EulerianTraits.html)     |
| 19  | Monotone         | A059481 |    37    |  52  | [All](https://peterluschny.github.io/tabl/Monotone.html)         | [OEIS](https://peterluschny.github.io/tablInspector/MonotoneTraits.html)     |
| 20  | Abel             | A137452 |    36    |  42  | [All](https://peterluschny.github.io/tabl/Abel.html)             | [OEIS](https://peterluschny.github.io/tablInspector/AbelTraits.html)       |
