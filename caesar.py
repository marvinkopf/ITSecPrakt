alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def encrypt(alphabet, key, message):
    return "".join([alphabet[(alphabet.find(c) + key) % len(alphabet)]
        if alphabet.find(c) != -1 else c for c in message])
    

def decrypt(alphabet, key, message):
    return "".join([alphabet[(alphabet.find(c) - key) % len(alphabet)]
        if alphabet.find(c) != -1 else c for c in message])

if __name__ == "__main__" :
    input_alphabet = input("Choose alphabet (default A-Z, a-z, 0-9):")
    alphabet = alphabet if input_alphabet == "" else input_alphabet
    
    input_key = input("Choose key (default 1):")
    key = 1 if input_key == "" else int(input_key)
  
    isEncrypt = input("Do you want to encrypt or decrypt (e/d)?:")
    
    message = ""
    if isEncrypt == "e":
        message = input("Message:")
        message = encrypt(alphabet, key, message)
    else:
        message = input("Cipher:")
        message = decrypt(alphabet, key, message)
    
    print(message)