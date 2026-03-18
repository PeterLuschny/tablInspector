# tablInspector — Project Summary

> Generated: 2026-03-08

---

## 1. Purpose and Overview

**tablInspector** is a Python library and research tool for the systematic study of integer triangular arrays — sequences classified with the keyword `tabl` in the [OEIS](https://oeis.org) (Online Encyclopedia of Integer Sequences). The project pursues two intertwined goals:

1. **Library** — Provide clean, uniform Python implementations of lower-triangular integer matrices (called *tables*) that can be imported and used directly in other programs.
2. **Research tool** — Identify semantically meaningful clusters of OEIS sequences by applying a fixed inventory of elementary transformations (*traits*) to each table and cross-referencing the resulting sequences with the OEIS database. This yields an objective, metric-based *ranking* of triangles by their structural importance in the OEIS.

The project also exposes the data via static HTML pages, a Jupyter notebook, and an interactive SageMath/HTML page — all without requiring the user to install anything beyond Python.

---

## 2. Repository Layout

```
tablInspector/
├── src/               # All Python source code
│   ├── _tabltypes.py        # Core Table class and type aliases
│   ├── _tablinverse.py      # Lower-triangular matrix inversion
│   ├── _tabltraits.py       # ~70 trait functions
│   ├── _tabloeis.py         # OEIS HTTP query interface
│   ├── _tablutils.py        # Utilities (hashing, timing, formatting)
│   ├── _tabldatabase.py     # JSON database, HTML generation, ranking I/O
│   ├── _tablstats.py        # Ranking computation and occurrence analysis
│   ├── _tablmake.py         # Code generator: produces Tables.py
│   ├── _tablinteractive.py  # Jupyter / SageMath interactive helpers
│   ├── _htmlsources.py      # HTML/CSS templates for generated pages
│   ├── Tables.py            # Auto-generated mega-file (all tables combined)
│   ├── Template.py          # Starter template for adding new triangles
│   ├── InteractiveTableInspector.ipynb   # Jupyter notebook
│   ├── Abel.py … Worpitzky.py            # ~116 individual triangle modules
│   └── NumBell.py … NumRiordan.py        # Sequence-only "Num*" modules
├── data/
│   ├── AllTraits.json       # Cached trait ↔ OEIS A-number mappings
│   ├── Ranking.md           # Full ranking table (118 triangles)
│   └── csv/                 # (CSV exports, currently sparse)
├── docs/                    # Static HTML published to GitHub Pages
│   ├── index.html
│   ├── InteractiveTablInspector.html
│   ├── CodeCruiser.css
│   └── <Name>Traits.html   # One file per triangle (~116 files)
├── imag/                    # Images (project logo, screenshot)
├── README.md
├── SUMMARY.md               # This file
└── LICENSE
```

---

## 3. Core Architecture

### 3.1 The `Table` Class (`_tabltypes.py`)

The central abstraction is the `Table` class. Every triangle is an instance of this class, constructed with:

| Parameter | Type | Meaning |
|---|---|---|
| `gen`   | `rowgen` (callable) | `gen(n)` returns the n-th row as `list[int]` |
| `id`    | `str`       | Human-readable name, e.g. `"Abel"` |
| `oeis`  | `list[str]` | OEIS A-numbers of closely related sequences |
| `invid` | `str`       | A-number of the inverse triangle (empty if non-invertible) |
| `tex`   | `str`       | LaTeX formula for the triangle |

The class provides **30 methods** covering every standard operation on a lower-triangular array:

| Category | Methods |
|---|---|
| Element access    | `val`, `__call__`, `__getitem__` |
| Row operations    | `row`, `rev`, `alt`, `acc`, `diff`, `der`, `rev11` |
| Table views       | `tab`, `mat`, `flat`, `itr` |
| Structural        | `antidiag`, `diag`, `col`, `sum` |
| Inversion         | `inv`, `revinv`, `invrev`, `inv11`, `revinv11`, `invrev11` |
| Offset / sub-triangle | `off` |
| Polynomial        | `poly` |
| Linear transforms | `trans`, `invtrans` |
| Display           | `show`, `showarray` |

Type aliases used throughout the library:

- `trow = list[int]` — a single row
- `tabl = list[list[int]]` — a full triangle
- `seq = Callable[[int], int]` — a sequence
- `rowgen = Callable[[int], trow]` — a row generator
- `tblgen = Callable[[int, int], int]` — a cell generator
- `trait = Callable[[Table, int], list[int]]` — a trait function

### 3.2 Triangle Modules

Each of the ~116 triangle files follows the same three-step pattern illustrated in `Template.py`:

1. Define a cached row generator function (decorated with `@cache`).
2. Instantiate a `Table` object with the generator and metadata.
3. Optionally include an `if __name__ == "__main__":` block that calls `InspectTable`.

Example (Abel polynomials):

```python
@cache
def abel(n: int) -> list[int]:
    if n == 0: return [1]
    b = binomial(n - 1)
    return [b[k-1] * n**(n-k) if k > 0 else 0 for k in range(n+1)]

Abel = Table(abel, "Abel", ["A137452", "A061356", "A139526"],
             "A059297", r"is(k=0)\ ?\ 0^n : \binom{n-1}{k-1}(-n)^{n-k}")
```

Many triangles cross-reference each other (e.g. `Abel.py` imports `Binomial`).

**Included triangles (selected):** Abel, AbelInv, Andre, Baxter, Bell, Bessel, BesselInv, BinaryPell, Binomial, Catalan, CatalanInv, ChebyshevS/T/U, Delannoy, DyckPaths, Entringer, Euler, Eulerian, FallingFactorial, Fibonacci, Fubini, Gaussq2, HermiteE/H, Jacobsthal, Laguerre, Lah, Leibniz, Lucas, Moebius, Motzkin, Narayana, Partition, Pascal, Rencontres, Schroeder, Sierpinski, StirlingCycle, StirlingSet, WardCycle, WardSet, Worpitzky, and many more.

### 3.3 Trait Functions (`_tabltraits.py`)

A *trait* is a function `(T: Table, size: int) -> list[int]` that extracts a named integer sequence from a triangle. Approximately **70 traits** are implemented, grouped as:

| Group | Examples |
|---|---|
| Triangle variants  | `Triangle`, `Trev`, `Tinv`, `Tinvrev`, `Trevinv`, `Talt`, `Tacc`, `Tder`, `Tantidiag` |
| Offset variants    | `Toff11`, `Trev11`, `Tinv11`, `Tinvrev11`, `Trevinv11` |
| Columns            | `TablCol0/1/2/3` |
| Diagonals          | `TablDiag0/1/2/3` |
| Row summaries      | `TablSum`, `TablLcm`, `TablGcd`, `TablMax`, `EvenSum`, `OddSum`, `AltSum` |
| Polynomial evaluations | `PolyRow1/2/3`, `PolyCol1/2/3`, `PolyDiag` |
| Convolutions       | `BinConv`, `InvBinConv`, `TransNat0`, `TransNat1`, `TransSqrs` |
| Anti-diagonal sums | `AntiDSum` |

With 70 traits × ~118 triangles, the library can generate over **8 000** OEIS sequence candidates.

### 3.4 OEIS Integration (`_tabloeis.py`)

`QueryOEIS(seqlist, maxnum, info, minlen)` submits sequences to the OEIS JSON API and returns matching A-numbers. The module includes:

- Retry logic with delays to handle server unavailability.
- A longest-common-substring matcher to align offsets between candidate and stored sequences.
- A JSON schema for validating OEIS API responses.
- FNV-1a hashing (`FNVhash`) for fast local deduplication.

### 3.5 Database and HTML Generation (`_tabldatabase.py`)

- `ReadJsonDict` / `WriteJsonDict` — load/save `data/AllTraits.json`, a nested dict mapping `{triangle_name → {trait_name → A-number}}`.
- `AnumberDict(T)` — queries OEIS for all traits of a given table and returns the mapping.
- `DictToHtml(T, dict)` — generates `docs/<Name>Traits.html` (found sequences) and `docs/<Name>Missing.html` (sequences not yet in OEIS).
- `RefreshDatabase()` — regenerates all HTML and JSON data for all triangles in `TablesList`.
- `InspectTable(T)` — prints a formatted trait/A-number overview for a single table.

### 3.6 Ranking (`_tablstats.py`)

`Ranking()` reads `AllTraits.json` and scores each triangle by the number of **distinct** OEIS sequences it generates (sequences with A-number ≠ 0 and no duplicates). The top triangles from the full ranking of 118 entries:

| Rank | Triangle | OEIS | Distinct |
|---|---|---|---|
| 1 | StirlingSet      | A048993 | 53 |
| 2 | FallingFactorial | A008279 | 48 |
| 3 | StirlingCycle    | A132393 | 47 |
| 4 | BinaryPell       | A038207 | 46 |
| 5 | Lah              | A271703 | 46 |
| … | … | … | … |

`ListOccurences()` finds A-numbers that appear across more than 10 different triangles — the most "universal" sequences.

### 3.7 Code Generation (`_tablmake.py`)

`_tablmake.py` reads each source module listed in `tabl_files`, strips import headers and `__main__` blocks, and concatenates everything into the single self-contained `Tables.py`. This file is the only import needed in external projects:

```python
from Tables import Abel, InspectTable
InspectTable(Abel)
```

### 3.8 Interactive Interfaces

| Interface | File | Description |
|---|---|---|
| Jupyter notebook | `src/InteractiveTableInspector.ipynb` | Dropdown widgets for table/trait selection; plots |
| SageMath HTML | `docs/InteractiveTablInspector.html` | Browser-based SageMath cells, no installation needed |
| GitHub Pages | `docs/index.html` | Static index linking all per-triangle HTML pages |

---

## 4. Data Flow

```
Individual triangle .py files
        │
        ▼
_tablmake.py  ──────→  Tables.py  (auto-generated, all-in-one)
        │
        ▼
_tabldatabase.py::RefreshDatabase()
        │
        ├──→  data/AllTraits.json    (trait → A-number cache)
        │
        └──→  docs/<Name>Traits.html (per-triangle HTML pages)
                        │
                        ▼
                GitHub Pages (public website)
```

---

## 5. Dependencies

| Package | Purpose |
|---------|---------|
| `requests`        | OEIS HTTP API queries |
| `ipywidgets`      | Dropdown selectors in Jupyter |
| `functools.cache` | Memoisation of row generators |
| `more_itertools`  | `flatten`, `difference` (used in traits and Table methods) |
| Standard library  | `math`, `itertools`, `pathlib`, `json`, `time`, `typing` |

> **Note:** `sympy`, `numpy`, and `scipy` are deliberately excluded from `Tables.py` to keep it self-contained.

---

## 6. How to Use

### As a library

```python
# Minimal usage: import the combined file
from Tables import Abel, InspectTable, TablesListPreview

TablesListPreview()          # list all triangles
InspectTable(Abel)           # print all traits of Abel triangle
row3 = Abel.row(3)           # [0, 9, 6, 1]
flat = Abel.flat(5)          # first 5 rows flattened
print(Abel(4, 2))            # T(4,2) = 48
```

### Adding a new triangle

1. Copy `src/Template.py` to `src/MyTriangle.py`.
2. Implement the `@cache` row generator.
3. Instantiate a `Table` object with name, OEIS references, and TeX formula.
4. Add the filename to `tabl_files` and the class to `tabl_dict` in `_tablmake.py`.
5. Run `_tablmake.py` to regenerate `Tables.py`.

### OEIS lookup for a single trait

```python
from Tables import LookUp, Fubini, PolyDiag
LookUp(Fubini, PolyDiag)
# *** Found: A094420 Generalized ordered Bell numbers Bo(n,n).
```
