def symetricEncryption(input):
    str = ""
    for ch in input:
        new_ch = chr((ord(ch) - ord('a') + 19) % 26 + ord('a'))
        str += new_ch
    return str

def symetricDecryption(input):
    str = ""
    for ch in input:
        new_ch = chr((ord(ch) - ord('a') - 19) % 26 + ord('a'))
        str += new_ch
    return str


user_input = input("Enter your message: ")
print("User input Message: " + user_input)
encMessage = symetricEncryption(user_input)
print("Encrypted Message: " + encMessage)

decMessage = symetricDecryption(encMessage)
print("Decrypted Message: " + decMessage)