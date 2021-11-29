import hashlib

def doubleSha256(input):
    input= input.encode('utf-8')
    return hashlib.sha256(hashlib.sha256(input).hexdigest().encode('utf-8')).hexdigest()


def makeLeaf(transactions):
    leafHash = []
    for trans in transactions:
        leafHash.append(doubleSha256(trans))
    return leafHash



def findMerkleRoot(transactions):
    leafHash = makeLeaf(transactions)
    hash = []
    hash2 = []
    if len(leafHash) % 2 != 0:                             ##if not even, repeat the last element
        leafHash.extend(leafHash[-1:])

    for leaf in sorted(leafHash):
        hash.append(leaf)
        if len(hash) % 2 == 0:
            hash2.append(doubleSha256(hash[0]+hash[1]))
            hash == []
    if len(hash2) == 1:
        return hash2
    else:
        return findMerkleRoot(hash2)