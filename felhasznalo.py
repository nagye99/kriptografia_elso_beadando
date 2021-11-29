import rsa
from rsa.key import newkeys


class Felhasznalo:
    pass

A = Felhasznalo()
A.azon = "A"
A.penz = 100
A.publicKey, A.privateKey = rsa.newkeys(1024)
A.publicKey, a = rsa.newkeys(256)

B = Felhasznalo()
B.azon = "B"
B.penz = 100
B.publicKey, B.privateKey = rsa.newkeys(1024)
B.publicKey, a = rsa.newkeys(256)

C = Felhasznalo()
C.azon = "C"
C.penz = 100
C.publicKey, C.privateKey = rsa.newkeys(1024)
C.publicKey, a = rsa.newkeys(256)

D = Felhasznalo()
D.azon = "D"
D.penz = 100
D.publicKey, D.privateKey = rsa.newkeys(1024)
D.publicKey, a = rsa.newkeys(256)