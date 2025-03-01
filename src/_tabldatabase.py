"""
This module provides functions to manage and manipulate tables and their traits, 
including reading and writing JSON dictionaries, filtering dictionaries, adding 
OEIS sections to source files, generating HTML files, and refreshing the database.

Functions:
    GetRoot(name: str = '') -> Path:
        Returns the root path of the project.
    ShowGlobalDict() -> None:
        Dumps the global dictionary to standard output.
    ReadJsonDict() -> Dict[str, Dict[str, int]]:
        Loads the file data/AllTraits.json into the global dictionary GlobalDict.
        Returns the global dictionary.
    FilterDict(olddict: Dict[str, int]) -> Dict[str, int]:
        Creates a new dictionary with unique A-numbers from the old dictionary.
        Returns the new dictionary.
    AddAnumsToSrcfile(name: str, dict: Dict[str, int] = {}) -> None:
        Adds an OEIS section to the source file of a table.
    AnumberDict(T: Table, info: bool = False, addtoglobal: bool = False) -> Dict[str, int]:
        Collects the A-numbers of the traits of the given table that are present in the OEIS.
        Returns a dictionary of traits and their A-numbers.
    DictToHtml(T: Table, dict: Dict[str, int], info: bool = False) -> tuple[int, int, int]:
        Transforms a dictionary {trait, anum} of the Table T into two HTML files: TNameTraits.html and TNameMissing.html.
        Returns a tuple of distinct A-numbers, hits, and misses.
    RefreshHtml(filter: bool = False) -> None:
        Refreshes the HTML files for all tables in TablesList.
    RefreshDatabase() -> None:
        Generates the traits for all tables in TablesList and writes them in HTML format to files in the docs directory.
        Saves the trait dictionaries in a JSON file in the data directory.
    AddTable(T: Table, dict: Dict[str, int] = {}) -> Dict[str, int]:
        Adds a table to the global dictionary and saves it to the JSON file.
        Returns the dictionary of traits and their A-numbers.
    InspectTable(T: Table, oeis: bool = False) -> None:
        Prints the table traits and optionally searches OEIS for A-numbers of the traits of the table.
"""

from Tables import TablesList
from _tabltypes import Table
from _tabloeis import QueryOEIS
from _tabltraits import TraitsDict, TableTraits
from _tablutils import TidToStdFormat, NumToAnum, TableGenerationTime
from pathlib import Path
from typing import Dict
import json


# #@

GlobalDict: Dict[str, Dict[str, int]] = {}


def GetRoot(name: str = '') -> Path:
    path = Path(__file__).parent.parent
    return (path / name).resolve()


def ShowGlobalDict() -> None:
    """Dump the global dictionary to std-out."""
    global GlobalDict
    for tabl, dict in GlobalDict.items():
        print(f"*** Table {tabl} ***")
        for trait in dict:
            print(f"    {trait} -> {dict[trait]}")


def ReadJsonDict() -> Dict[str, Dict[str, int]]:
    """Loaded the file data/AllTraits.json into the global dictionary GlobalDict.
    In case of a FileNotFoundError a new empty dictionary is created.

    Returns:
        Dict[str, Dict[str, int]]: A global dictionary containing traits dictionaries.
    """
    global GlobalDict
    jsonpath = GetRoot(f"data/AllTraits.json")
    try:
        with open(jsonpath, 'r') as file:
            GlobalDict = json.load(file)
    except FileNotFoundError:
        print("No file 'AllTraits.json' found.")
        GlobalDict = {}
        print("New GlobalDict created.")
        return GlobalDict

     # print("GlobalDict loaded with file AllTraits.json!")
    return GlobalDict


def FilterDict(olddict: Dict[str, int] )  -> Dict[str, int]:
    """Make a new dictionary with unique A-numbers.

    Args:
        olddict (Dict[str, int]): A-numbers can appear several times.

    Returns:
        Dict[str, int]: A-numbers can appear at most once.
    """
    anumlist: set[int] = set()
    newdict: Dict[str, int] = {}
    for k, v in olddict.items():
        if not v in anumlist: 
            newdict[k] = v
        anumlist.add(v)
    return newdict


def TruncateInfo(srcpath: Path) -> None:
    """
    The function reads the file line by line and writes back the content 
    up to (but not including) the line that starts with the OEIS marker 
    (''' OEIS). Once the marker is found, the file is truncated at that point.
    Args:
        srcpath (Path): The path to the file to be truncated.
    """
    oeis_marker = "''' OEIS"
    with open(srcpath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(srcpath, "w", encoding="utf-8") as f:
        for line in lines:
            if line.startswith(oeis_marker):
                f.truncate(f.tell())
                break
            f.write(line)


def AddAnumsToSrcfile(
    name: str, 
    dict: Dict[str, int] = {}
) -> None:
    """Add an OEIS section to the source file of a table.

    Args:
        name (str): name of the table
        dict (Dict[str, int], optional): where the OEIS infos are. 
        Defaults to {} which in turn triggers the use of the gloabl dictionary.

    Example:
       AddAnumsToSrcfile("Catalan") will add the following line to src/Catalan.py 
       indicatting the OEIS A-number of the row sums of the Catalan triangle.

       Catalan_TablSum -> https://oeis.org/A1700
    """
    
    global GlobalDict

    if dict == {}:
        ReadJsonDict()
        dict = GlobalDict[name]

    srcpath = GetRoot(f"src/{name}.py")
    TruncateInfo(srcpath)

    with open(srcpath, "a+", encoding="utf-8") as dest:
        d = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
        dest.write("\n\n" + r"'''" + " OEIS\n")
        for fullname, anum in d.items():
            if anum != 0:
                dest.write(f"    {fullname} -> https://oeis.org/A{anum}\n")
            else:
                dest.write(f"    {fullname} -> 0 \n")

        misses = len([v for v in d.values() if v == 0])
        hits = len(d.values()) - misses
        distincts = len(set(d.values()))

        dest.write(f"\n    {name}: Distinct: {distincts}, Hits: {hits}, Misses: {misses}")
        dest.write("\n" + r"'''" + "\n")


def AnumberDict(
    T: Table, 
    info: bool = False,
    addtoglobal: bool = False
) -> Dict[str, int]:
    """ Collects the A-numbers of the traits of the given table that are present in the OEIS.
    Requires online access to the OEIS database.

    Args:
        T (Table): table for which the OEIS data is seeked
        info (bool, optional): Prints infos while quering the OEIS database. Defaults to False.
        addtoglobal (bool, optional): add the generated dict to the global dict. Defaults to False.

    Returns:
        Dict[str, int]: _description_
    """
    
    global GlobalDict
    print(f"*** Table {T.id} under construction ***")

    trait_dict: Dict[str, int] = {}
    for trid, tr in TraitsDict.items():
        # the key of the dictionary is the table name + trait name.
        name = (T.id + '_' + trid).ljust(10 + len(T.id), ' ')
        if info: print(name)
        # generate the trait data for the query
        seq: list[int] = tr[0](T, tr[1])
        if seq != []:
            trait_dict[name] = QueryOEIS(seq, info)

    if addtoglobal:
        GlobalDict[T.id] = trait_dict
    return trait_dict


header = r'<!DOCTYPE html lang="en"><head><title>NAMEXXX</title><meta charset="utf-8"><meta name="viewport" content="width=device-width"><script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">window.MathJax={ loader:{ load: ["[tex]/bbox"]}, tex:{ packages:{ "[+]": ["bbox"]}}}</script><style type="text/css">table{ margin-top: 8px; display: inline-block;} table.rTable{ position: fixed; top: 0px; border: 2px solid #5949b3; background-color: #EEE7DB; text-align: center; border-collapse: collapse; font-family: "Segoe UI", sans-serif; font: 1em sans-serif; overflow-y: auto; max-height: 850px;} table.rTable td, table.rTable th{ border: 1px solid #AAAAAA; padding: 8px 2px;} table.rTable tbody td{ font-size: 16px;} table.rTable tr:nth-child(even){ background: #f3f1f0;} table.rTable thead{ background: #585ada;} table.rTable thead th{ font-size: 16px; font-weight: bold; color: #FFFFFF; text-align: center; border-left: 2px solid #A40808;} </style></head><body><iframe name="OEISframe" scrolling="yes" width="66%" height="850" align="left" title="Sequences" src=https://oeis.org/AXXXXXX></iframe><div style="height:850px; overflow:auto;"><table class="rTable"><thead><tr><th>OEIS</th><th>TRAIT</th><th>FORMULA</th></tr></thead><tbody><tr><td><a href="https://oeis.org/AXXXXXX" target="OEISframe">AXXXXXX</a></td><td style="color: darkgreen;font-weight:800">NAMEXXX</td><td style="color: darkgreen;font-weight:800">\(T_{n,k}\)</td></tr>'

def DictToHtml(
    T: Table, 
    dict: Dict[str, int],
    info: bool = False
)  -> int:
    """Transforms a dictionary {trait, anum} of the Table T
        into a html files: TNameTraits.html.
        A trait is 'missing' if the anum in the dictionary is 0.
    """

    hitpath = GetRoot(f"docs/{T.id}Traits.html")
    head = header.replace("NAMEXXX", T.id).replace("AXXXXXX", f"{T.oeis[0]}")

    hits = doubles = 0
    anumlist: set[int] = set()

    with open(hitpath, "w+", encoding="utf-8") as oeis:

        oeis.write(head)
        d = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}

        for fullname, anum in d.items():
            if info: print(f"    {fullname} -> {anum}") # prints sorted dict 
            traitfun, size, tex = TraitsDict[fullname.split('_')[1]] # type: ignore
            if anum == 0:
                continue
            if anum in anumlist: 
                doubles += 1
            Anum = 'A' + str(anum).rjust(6, "0")
            url = f"<a href='https://oeis.org/{Anum}' target='OEISframe'>{Anum}</a>"
            row = f"<tr><td>{url}</td><td>{fullname.split('_')[1]}</td><td>{tex}</td></tr>"
            oeis.write(row)
            hits += 1
            anumlist.add(anum)
            
        row = f"<tr><td colspan='3'><a href='https://peterluschny.github.io/tablInspector/index.html'>I N D E X</a></td></tr></tbody></table></div></body></html>"
        oeis.write(row)

    return hits


def RefreshHtml(filter: bool=False) -> None:
    """
    Refreshes the HTML representation of tables based on the global dictionary.

    This function reads the global dictionary from a JSON file, iterates over a list of tables,
    and converts each table's dictionary to HTML. If the `filter` parameter is set to True, 
    the dictionary multiple A-numbers are removed.

    Args:
        filter (bool): If True, multiple A-numbers are removed before conversion. Defaults to False.

    Raises:
        KeyError: If a table's ID is not found in the global dictionary.
    """
    global GlobalDict
    ReadJsonDict()
    
    indexpath = GetRoot(f"docs/index.html")
    with open(indexpath, "w+", encoding="utf-8") as index:
        index.write(indheader)

        for T in TablesList:
            try:
                dict = GlobalDict[T.id]
                if filter:
                    dict = FilterDict(dict)
                DictToHtml(T, dict)    # type: ignore
                index.write(
                    f"<tr><td align='left'><a href='{T.id}Traits.html'>{T.id}</a></td></tr>"
                )
                print(T.id, "dict length:", len(dict))
            except KeyError as e: 
                print("KeyError:", e)
                input()
                pass
        
        index.write("</tbody></table></body></html>")
        index.flush()


indheader = "<!DOCTYPE html><html lang='en'><head><title>Index</title><meta name='viewport' content='width=device-width,initial-scale=1'><style type='text/css'>body{ font-family: Calabri, Arial, sans-serif; font-size: 16px; background-color: #2f3332; color: #0f0f0f} a{ text-decoration: none;} tbody td:hover{ background-color: greenyellow;} table, td,th{ background-color: lightgrey; border: 2px solid black; border-collapse: collapse; margin-left: 16px; padding-left: 10px; padding-top: 4px;} </style><base href='https://peterluschny.github.io/tablInspector/' target='_blank'></head><body><table><thead><tr><th align='left'>Triangle Inspector</th></tr></thead><tbody><tr>"


def RefreshDatabase() -> None:
    """Generates the traits for all tables in TablesList and writes them 
        in html format to files in the docs directory. Furthermore, the
        trait dictionaries are saved in a dictionary in JSON format that
        is written to the data directory.
    """
    print("Warning: This will take some time.")

    global GlobalDict
    ReadJsonDict()

    indexpath = GetRoot(f"docs/index.html")
    with open(indexpath, "w+", encoding="utf-8") as index:
        index.write(indheader)

        for T in TablesList:
            dict = AnumberDict(T, True, True)  # type: ignore
            DictToHtml(T, dict, False)  # type: ignore
            index.write(
                f"<tr><td align='left'>{T.id}</td><td align='left'><a href='{T.id}Traits.html'>[online]</a></td></tr>"
            )
            AddAnumsToSrcfile(T.id, dict)

        index.write("</tbody></table></body></html>")
        index.flush()

    # Save to a JSON file
    jsonpath = GetRoot(f"data/AllTraits.json")
    with open(jsonpath, 'w') as fileson:
        json.dump(GlobalDict, fileson)


def AddTable(
    T: Table,
    dict: Dict[str, int] = {}
) -> Dict[str, int]:
    """
    Adds a table to a dictionary, i.e. it reads a JSON dictionary, 
    updates it with the provided table, and converts the dictionary to HTML.
    Args:
        T (Table): The table to be added.
        dict (Dict[str, int], optional): A dictionary to be updated. 
        Defaults to an empty dictionary.
    Returns:
        Dict[str, int]: The updated dictionary.
    """
    ReadJsonDict()

    if dict == {}:        #info, add2globalDict
        dict = AnumberDict(T, True, True)
    print("Dict length:", len(dict))
    DictToHtml(T, dict, True)
    jsonpath = GetRoot(f"data/AllTraits.json")
    with open(jsonpath, 'w+') as fileson:
        json.dump(GlobalDict, fileson)
    return dict


def TraitOccurences() -> Dict[str, set[int]]:
    """
    Generates a dictionary of traits with sets of A-numbers from the global dictionary. 
    Each key is a trait identifier and the value is a set of A-numbers associated 
    with that trait in some triangle.
    Returns:
        Dict[str, set[int]]: A dictionary where each key is a trait identifier 
        and the value is a set of A-numbers.
    """
    global GlobalDict
    ReadJsonDict()
    trdict: Dict[str, set[int]] = {trid: set() for trid in TraitsDict.keys()}

    for T in TablesList:
        for trid in TraitsDict.keys():
            # the key of the dictionary is the table name + trait name.
            key = (T.id + '_' + trid).ljust(10 + len(T.id), ' ')
            trdict[trid].add(GlobalDict[T.id].get(key, 1))
    return trdict


def TraitOccurence(trid: str) -> Dict[str, tuple[str, str]]:
    """
    Generates a dictionary of traits with A-numbers from the global dictionary.
    Each key is a trait identifier and the value is a tuple of the OEIS sequence.
    Returns:
        Dict[str, tuple[str, str]]: A dictionary where each key is the triangle identifier 
        and the value is the pair of A-numbers of the triangle and the trait. 
    """
    global GlobalDict
    ReadJsonDict()
    trdict: Dict[str, tuple[str, str]] = {}

    for T in TablesList:
        key = T.id + '_' + trid
        anum = NumToAnum(GlobalDict[T.id][key])
        trdict[T.id] = (T.oeis[0], anum)
    return trdict


def GetAnumOccurence(lookup: int) -> list[str]:
    """
    Generates a dictionary of traits 
    Returns:
        list[str]: A list where each key is a trait identifier 
        and the value is a set of A-numbers.
    """
    global GlobalDict
    ReadJsonDict()
    trdict: list[str] = []

    for T in TablesList:
        for trid in TraitsDict.keys():
            # the key of the dictionary is the table name + trait name.
            key = (T.id + '_' + trid).ljust(10 + len(T.id), ' ')
            anum = GlobalDict[T.id].get(key, 1)
            if anum == lookup:
                trdict.append(f"{trid.replace(' ', '') }({T.id})")
    return trdict


def InspectTable(T: Table, oeis: bool=False) -> None:
    """
    Prints the table traits. If the option oeis is True, 
    the A-numbers of the traits of T will be searched online
    and added to the global dictionary and also to the 
    file 'data/AllTraits.json'.
    
    Args:
        T, table to inspect

        oeis, search OEIS for A-numbers of the traits of T. 
        Defaults to False.

    Returns:
    None. 
    """
    print()
    TableTraits(T)
    print()
    print("NAME       ", T.id)
    print("Formula    ", T.tex)
    print("Similars   ", T.oeis)
    print("Inverse    ", T.invid if T.invQ else "None")
    print("Timing 100 rows:", end=''); TableGenerationTime(T)
    print()
    print("TABLE"); T.show(10)
    print()
    if oeis:
        print("Searching OEIS -- this will take some time!")
        AddTable(T)
        print()


if __name__ == "__main__":

    #for cmd in GetAnumOccurence(-999999):
    #    print(cmd)

    # RefreshDatabase()
    # RefreshHtml(True)

    # from SchroederInv import SchroederInv   # type: ignore
    #from MotzkinInv import MotzkinInv      # type: ignore
    #from DoublePochhammer import DoublePochhammer  # type: ignore

    #InspectTable(SchroederInv)

    # AddTable(SchroederInv) # type: ignore

    #for T in TablesList:
    #    print(T.id, T.tex)
    #    AddAnumsToSrcfile(T.id)

    #ReadJsonDict()

    #for k, v in GlobalDict.items():
    #    print(k, len(v.values()))

    # AddAnumsToSrcfile("DoublePochhammer")

    #for k, v in dict.items():
    #    print(k, v)
    
    #toc = TraitOccurences()
    #for k, v in toc.items(): print(k, v)
    
    # srcpath = GetRoot(f"src/Mist.py")
    # TruncateInfo(srcpath)

    for k, v in TraitOccurence("PosHalf").items():
        print(f"{TidToStdFormat(k)}  {v[0]} -> {v[1]}")
