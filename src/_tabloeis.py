"""
This module provides functionality to query the OEIS (Online Encyclopedia of Integer Sequences) 
for a given sequence and determine if it is present in the database. 

  QueryOEIS(seqlist: list[int], maxnum: int = 1, info: bool = False, minlen: int = 24) -> int:
    Queries the OEIS for a given sequence to check if it is present in the database.
      maxnum: Maximum number of sequences to be returned. Defaults to 1.
      info: If True, prints details; otherwise, is quiet except for warnings. Defaults to False.
      minlen: Minimum length of the sequence required for the query. Defaults to 24.
      The A-number of the sequence if found, 0 if the sequence was not found, 
      or -999999 if the OEIS server cannot be reached.

The module also includes a function to find the longest common substring between two strings. 
The function 'lcsubstr' is CC BY-SA 4.0 and taken from the Algorithm Implementation Wikibook.
https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring
"""

from typing import TypeAlias
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from _tabltypes import Table, Trait
from _tablutils import SeqToString


oeis_schema = '''{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": [
      {
        "type": "object",
        "properties": {
          "greeting": {
            "type": "string"
          },
          "query": {
            "type": "string"
          },
          "count": {
            "type": "integer"
          },
          "start": {
            "type": "integer"
          },
          "results": {
            "type": "array",
            "items": [
              {
                "type": "object",
                "properties": {
                  "number": {
                    "type": "integer"
                  },
                  "id": {
                    "type": "string"
                  },
                  "data": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "comment": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "reference": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "link": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "formula": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "maple": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "mathematica": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "program": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "xref": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "keyword": {
                    "type": "string"
                  },
                  "offset": {
                    "type": "string"
                  },
                  "author": {
                    "type": "string"
                  },
                  "ext": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "references": {
                    "type": "integer"
                  },
                  "revision": {
                    "type": "integer"
                  },
                  "time": {
                    "type": "string"
                  },
                  "created": {
                    "type": "string"
                  }
                }
              }
            ]
          }
        }
      }
    ]
  }'''

OEISdata: TypeAlias = dict[str, int | str | list[str] ]

testdata: dict[str, int | str | list[str] ] = {"number": 367025, "data": "1,4,1,9,9,2,16,36,32,5,25,100,200,125,14,36,225,800,1125,504,42,49,441,2450,6125,6174,2058,132,64,784,6272,24500,43904,32928,8448,429,81,1296,14112,79380,222264,296352,171072,34749,1430", "name": "Triangle read by rows, T(n, k) = [x^k] p(n), where p(n) = (1 - hypergeom([-1/2, -n - 1, -n - 1], [1, 1], 4*x)) / (2*x).", "formula": ["T(n,k) = binomial(n+1,n-k)^2*binomial(2*k,k)/(k+1). - _Detlef Meya_, Nov 19 2023"], "example": ["Triangle T(n, k) starts:", "  [0]   1;", "  [1]   4,    1;", "  [2]   9,    9,     2;", "  [3]  16,   36,    32,      5;", "  [4]  25,  100,   200,    125,     14;", "  [5]  36,  225,   800,   1125,    504,      42;", "  [6]  49,  441,  2450,   6125,   6174,    2058,     132;", "  [7]  64,  784,  6272,  24500,  43904,   32928,    8448,    429;", "  [8]  81, 1296, 14112,  79380, 222264,  296352,  171072,  34749,   1430;", "  [9] 100, 2025, 28800, 220500, 889056, 1852200, 1900800, 868725, 143000, 4862;"], "maple": ["p := n -> (1 - hypergeom([-1/2, -n-1, -n-1], [1, 1], 4*x)) / (2*x):", "T := (n, k) -> coeff(simplify(p(n)), x, k):", "seq(seq(T(n, k), k = 0..n), n = 0..9);"], "mathematica": ["T[n_,k_]:=Binomial[n+1,n-k]^2*Binomial[2*k,k]/(k+1);Flatten[Table[T[n,k],{n,0,9},{k,0,n}]] (* _Detlef Meya_, Nov 19 2023 *)"], "xref": ["Cf. A000290 (first column), A000108 (main diagonal).", "Cf. A367022, A367023, A387024."], "keyword": "nonn,tabl", "offset": "0,2", "author": "_Peter Luschny_, Nov 07 2023", "references": 0, "revision": 14, "time": "2023-11-20T11:52:33-05:00", "created": "2023-11-07T14:43:14-05:00"}

# #@



def format_anum(number: int) -> str:
    """
    Format an integer as a zero-padded OEIS A-number string.

    Replaces the ad-hoc pattern ``f"A{(6 - len(str(n))) * '0' + str(n)}"``
    found elsewhere in this module with the standard format-spec idiom.
    Works correctly for numbers with more than 6 digits.

    Args:
        number: The non-negative integer to format.

    Returns:
        A string of the form ``"A000001"`` (minimum 6 digits, left-padded with
        zeros; wider for numbers >= 1_000_000).

    Examples:
        >>> format_anum(12)
        'A000012'
        >>> format_anum(1000000)
        'A1000000'
    """
    return f"A{number:06d}"


def lcsubstr(s: str, t: str) -> tuple[int, int]:
    """
    Finds the longest contiguous common substring of *s* and *t* using
    O(min(|s|, |t|)) working space instead of the O(|s| × |t|) matrix
    allocated by the original.  The interface is identical.

    Args:
        s: The first string.
        t: The second string.

    Returns:
        ``(start, length)`` where the matched substring begins at index
        *start* in *s* and has the given *length*.
    """
    # Keep t as the shorter string for minimal memory use.
    if len(s) < len(t):
        s, t = t, s
        swapped = True
    else:
        swapped = False

    lt = len(t)
    prev = [0] * (lt + 1)
    longest, x_longest = 0, 0

    for i in range(1, len(s) + 1):
        curr = [0] * (lt + 1)
        for j in range(1, lt + 1):
            if s[i - 1] == t[j - 1]:
                curr[j] = prev[j - 1] + 1
                if curr[j] > longest:
                    longest = curr[j]
                    x_longest = i
        prev = curr

    start = x_longest - longest
    if swapped:
        # start was computed in the (possibly swapped) s; map back to the
        # original first argument via the matched substring value.
        orig_start = s[start:start + longest]  # the common substring itself
        start = t.find(orig_start) if orig_start else 0  # t is original s
    return (start, longest)


def QueryOEIS(
        seqlist: list[int], 
        maxnum: int = 1,
        info: bool = False, 
        minlen: int = 24 
    ) -> int:
    """
    Query if a given sequence is present in the OEIS. At least 24 terms 
    of the sequence must be given. The first three terms and signs are disregard. 
    Sequences with huge terms might have to few terms to give reliable results. 
    This is a heuristic function, understand it's limited reach.

    Args:
        seqlist: The sequence to search. Must have at least 24 terms.

        maxnum: max number of sequences to be returned. Defaults to 1.

        info: Prints details, otherwise is quiet except for warnings. Defaults to False.
        
        minlen: At least {minlen} terms are required.

    Returns:
        Returns anum is the A-number of the sequence, 
        Returns 0 if the sequence was not found.
        If sl < 5 and dl > 12, then anum probably matches the sequence,
        modulo a couple of first terms and the signs.

    Raises:
        Exception: If the OEIS server cannot be reached after multiple attempts.
        Currently, the function will return -999999 if the OEIS server cannot be reached.
    """
    if len(seqlist) < minlen:
      print(f"Sequence is too short! We require at least {minlen} terms.")
      print("You provided:", seqlist)
      return 0

    if seqlist == [0 for _ in range(minlen)]: return 4  # XXXXX dont search for the all zeros sequence
    off = 0 if 0 == sum(seqlist[3:minlen]) else 3  # XXXXX dont skip leading terms if the rest is zero
    seqstr = SeqToString(seqlist, 160, 36, ",", off, True)
    url = f"https://oeis.org/search?q={seqstr}&fmt=json"

    _retry = Retry(
        total=4,
        backoff_factor=1,           # waits: 0s, 1s, 2s, 4s
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    _session = requests.Session()
    _session.mount("https://", HTTPAdapter(max_retries=_retry))

    for _ in range(4):
        # if debug: print(f"connecting: [{_}]")
        try:
            jdata = _session.get(url, timeout=(10, 60)).json()
            if jdata == None:
                if ((0 == sum(seqlist[::2]) or 
                  (0 == seqlist[1] and 0 == seqlist[3] and 0 == seqlist[6] 
                   and 0 == seqlist[10] and 0 == seqlist[15]))): 
                    seqlist = Table.zeroless(seqlist)
                    seqstr = SeqToString(seqlist, 160, 36, ",", 3, True)
                    if info:
                        print("Searching without zeros:", seqstr)
                    url = f"https://oeis.org/search?q={seqstr}&fmt=json"
                    raise ValueError('Try again')
                if info:
                    print("Sorry, no match found for:", seqstr)
                return 0

            number = dl = ol = 0
            for j in range(min(maxnum, len(jdata))):
                seq = jdata[j]
                number = seq["number"]
                anumber = f"A{(6 - len(str(number))) * '0' + str(number)}"
                name = seq["name"]
                data = seq["data"].replace('-', '')         # type: ignore
                seqstr = SeqToString(seqlist, 160, 25, ",", 0, True)
                start, length = lcsubstr(data, seqstr)      # type: ignore
                ol = data.count(",")                        # type: ignore
                sl = data.count(",", 0, start)              # type: ignore
                dl = data.count(",", start, start + length) # type: ignore
                if dl < 12:
                    print(f"\n*** WARNING! Only {dl} out of {ol} terms match! ***\n")
                if info or dl < 12:
                    print("You searched:", seqstr)
                    print("OEIS-data is:", data)          # type: ignore
                    # print(f"Info: Starting at index {sl} the next {dl} 
                    # consecutive terms match.\nThe matched substring starts 
                    # at byte {start} and has length {length}.")
                    print("*** Found:", anumber, name)
                if dl > 12:
                    break

            return int(number)  

        except ValueError: 
            continue
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    #raise Exception(f"Could not open {url}.")
    print(f"Exception! Could not open {url}.")
    return -999999


def LookUp(t: Table, tr: Trait, info: bool = True) -> int:
    """
    Look up the A-number in the OEIS database based on a trait of a table.

    Args:
        t (Table): The table to be analyzed.
        tr (Trait): A function that extracts a trait from the table.
        info (bool, optional): If True, information about the matching will be displayed. Defaults to True.

    Returns:
        int: The A-number of the sequence if found, otherwise 0.
    
    Raises:
        Exception: If the OEIS server cannot be reached after multiple attempts.
        Currently, the function will return -999999 if the OEIS server cannot be reached.
    
    Example:
        >>> LookUp(Fubini, PolyDiag)
        You searched: 1,1,10,219,8676,...
        OEIS-data is: 1,1,10,219,8676,...
        *** Found: A094420 Generalized ordered Bell numbers Bo(n,n).
        Returns the int 94420.
    """
    return QueryOEIS(tr(t, 24), 1, info)


if __name__ == "__main__":
    from Tables import Lehmer, TablesList, TablSum
    from Tables import Fubini, PolyDiag

    data1 = [1, 4, 1, 9, 9, 2, 16, 36]
    data2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,19,20,21,22,23,24,25,26,27]
    data3 = [36,32,5,25,100,200,125,14,36,225,800,1125,504,42,49,441,2450,6125,6174,2058,132,64,784,6272]
    data4 = [1,0,1,0,2,0,2,0,4,0,4,0,8,0,10,0,20,0,30,0,56,0,94,0,180,0,316,0,596,0, 1096,0,2068,0,3856,0]
    data5 = [1,-1,1,0,-2,1,1,1,-3,1,-1,2,3,-4,1,0,-4,2,6,-5,1,1,2,-9,0,10,-6,1]

    def test() -> None:
        print(QueryOEIS(data1, 1, True)); print()
        print(QueryOEIS(data2, 1, True)); print()
        print(QueryOEIS(data3, 1, True)); print()

    def testQuerySum() -> None:
        for tabl in TablesList[:5]:
            print(f"Searching row sums of {tabl.id} {tabl.oeis}.")
            sumlist = [tabl.sum(n) for n in range(30)]
            anum = QueryOEIS(sumlist)
            print('A' + str(anum).rjust(6, "0"))

    #test()
    #testQuerySum()
    LookUp(Fubini, PolyDiag)  # type: ignore
    LookUp(Lehmer, TablSum)    # type: ignore
    print(QueryOEIS(data5, 1, True)) # -> A104562 AND A101950