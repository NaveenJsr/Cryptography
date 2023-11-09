import hashlib
import math

def calculate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

def encryption(d, n, plaintext):
    ciphertext = []
    for char in plaintext:
        pt = ord(char)
        c = pow(pt, d, n)
        ciphertext.append(c)
    return ciphertext

def decryption(e, n, ciphertext):
    plaintext = ""
    for c in ciphertext:
        pt = pow(c, e, n)
        char = chr(pt)
        plaintext += char
    return plaintext

def generate_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    e = 65537  
    d = pow(e, -1, phi_n)  

    return (e, n), (d, n)


def sign(hashedMessage):
    return encryption(private_key[0], private_key[1], hashedMessage)

def verify(message,signedMessage):
    hashedMessage = calculate_hash(message)
    decryptedMessage = decryption(public_key[0], public_key[1], signedMessage)
    if hashedMessage == decryptedMessage:
        return True
    else:
        return False

p = 103   
q = 107  


public_key, private_key = generate_keys(p, q)

message = input("Enter message: ")
hashedMessage = calculate_hash(message)
signedMessage = sign(hashedMessage)
print("Signed message:", signedMessage)
verifyMessage = verify(message, signedMessage)
if verifyMessage :
    print("Message is verified.")
else:
    print("Message is not verified.")