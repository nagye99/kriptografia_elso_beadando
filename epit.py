from Merkle_tree import findMerkleRoot
from POW import POW
import random

def epit(tranzakiok, lanc):
    csucs = findMerkleRoot(tranzakiok)
    if(len(lanc) == 0):
        utolso = random.getrandbits(256)
    else:
        utolso = lanc[-1]
    uj_elem = POW(csucs, utolso)
    return uj_elem