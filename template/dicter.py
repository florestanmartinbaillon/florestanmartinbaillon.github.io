"""
Un format très simple pour
stocker des list de dict:
une suite de ligne de la forme
key1:value1
key2:value2

séparé par des 
---

"""

def list_split(l, s):
    """
    découpe une liste
    en bloc séparer par l'élement s
    """
    L = []
    cur = []
    for it in l:
        if it == s:
            L.append(cur)
            cur = []
        else:
            cur.append(it)
    L.append(cur)
    return L

def line_parser(line, sep):
    """
    découper un string en 2
    selon la première occurence de sep
    """
    sp = line.split(sep)
    key = sp[0]
    value = sep.join(sp[1:])
    return (key, value)

def dicter_parser(txt, sepl="---", sepkey=":"):
    lines = txt.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    sp = list_split(lines, sepl)
    L = []
    for bloc in sp:
        d = {}
        for line in bloc:
            k,v = line_parser(line, sepkey)
            d[k] = v
        L.append(d)
    return L
