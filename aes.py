from Crypto.Cipher import AES

def encrypt(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext
    except ValueError:
        print("Key incorrect or message corrupted")


if __name__ == "__main__" :

    key = bytes(input("Choose a key(press enter for default 'Sixteen byte key'): "), "UTF-8")
    data = bytes(input("Text to encrypt (press enter for default 'Hello World'): "), "UTF-8")
    
    key = b'Sixteen byte key' if key == b"" else key
    data = b"Hello World" if data == b"" else data
    (a, b, c) = encrypt(key, data)
    
    print("Encrypt: ", a)
    print("Decrypt: ", decrypt(a,b,c, key))