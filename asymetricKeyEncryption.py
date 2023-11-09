import math

def encryption(e, n, plaintext):
    ciphertext = []
    for char in plaintext:
        pt = ord(char)
        c = pow(pt, e, n)
        ciphertext.append(c)
    return ciphertext

def decryption(d, n, ciphertext):
    plaintext = ""
    for c in ciphertext:
        pt = pow(c, d, n)
        char = chr(pt)
        plaintext += char
    return plaintext

def generate_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    e = 65537  
    d = pow(e, -1, phi_n)  
    print(d)

    return (e, n), (d, n)

p = 103   
q = 107   

public_key, private_key = generate_keys(p, q)

user_input = input("Enter your message: ")
ciphertext = encryption(public_key[0], public_key[1], user_input)
print("Encrypted Message: " + str(ciphertext))
plaintext = decryption(private_key[0], private_key[1], ciphertext)
print("Decrypted Message: " + plaintext)
