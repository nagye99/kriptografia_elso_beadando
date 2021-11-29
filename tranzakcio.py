import rsa
import datetime
import hashlib

def doubleSha256(input):
    return hashlib.sha256(hashlib.sha256(input).hexdigest().encode('utf-8')).hexdigest()

def tranzakcio(ki, kinek, mennyit):
    ido = datetime.datetime.now().timestamp()
    adat=ki.azon + kinek.azon + str(mennyit) + str(ido) + str(kinek.publicKey)
    titkos = rsa.encrypt(str.encode(adat), ki.privateKey)
    hashelt = doubleSha256(titkos)
    return hashelt