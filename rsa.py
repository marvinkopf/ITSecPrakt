def encrypt(public_rsa, c):
    return __crypt(c, public_rsa[0], public_rsa[1])

def decrypt(private_rsa, c):
    return __crypt(c, private_rsa[0], private_rsa[1])
    
def __crypt(c, exponent, N):
    return ''.join([my_pow(ord(char), exponent, N) for char in c])
    
def my_pow(value, exponent, modulo):
    buffer = value
    for i in range(1, exponent):
        buffer = buffer * value % modulo
    return chr(buffer)


def gen_keys():
    e = 23
    p = 11
    q = 13
    N = p * q
    public_rsa = (e, N)
    phi_N = (p-1)*(q-1)
    a, d, k = eeA(e, phi_N)
    private_rsa = (d, N)
    return public_rsa, private_rsa

def eeA(a, b):
    if a == 0 :
        return b,0,1
             
    (t,x1,y1) = eeA(b%a, a)
     
    x = y1 - (b//a) * x1
    y = x1
     
    return (0,x,y)

if __name__ == "__main__" :
    public_rsa, private_rsa = gen_keys()
    
    f = open("message.txt")
    message = f.read()
    f.close()
    
    cipher = encrypt(public_rsa, message)
    f = open ("decrypted.txt", "w")
    f.write(cipher)
    f.close()
    
    decrypted = decrypt(private_rsa, cipher)
    f = open ("decrypted.txt", "w")
    f.write(decrypted)
    f.close()
    print(decrypted)