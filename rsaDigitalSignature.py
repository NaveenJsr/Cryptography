def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  

    if gcd(e, phi) != 1:
        raise Exception("e and phi(n) are not coprime.")

    d = mod_inverse(e, phi)
    if d is None:
        raise Exception("No modular inverse for e.")

    return ((e, n), (d, n))

def sign(message, private_key):
    d, n = private_key
    signature = pow(message, d, n)
    return signature

def verify(message, signature, public_key):
    e, n = public_key
    decrypted_signature = pow(signature, e, n)
    return decrypted_signature == message

# Example usage
p = 61
q = 53

public_key, private_key = generate_keypair(p, q)
message = 6274
print("Message: ", message)
signature = sign(message, private_key)
print("Generated Signature:", signature)

is_verified = verify(message, signature, public_key)
print("Signature Verification:", is_verified)
