import hashlib
import random
import sys

def doubleSha256(input):
    input= input.encode('utf-8')
    hexa = hashlib.sha256(hashlib.sha256(input).hexdigest().encode('utf-8')).hexdigest()
    return bin(int(hexa, 16))[3:]


def POW(csúcsHASH, utolso_elem):
    while(True):
        meret= random.randint(1, 10)
        rand = random.getrandbits(meret)
        konkat = str(csúcsHASH)+str(utolso_elem)+str(rand)
        h = doubleSha256(konkat)
        if(h[:4] == "0000"):
            break
    return h