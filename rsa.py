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

def is_prime(value):
    for i in range(2, int(value**(1/2))+1):
        if value % i == 0:
            return False
    return True

def gen_keys():
    import random
    
    p = 4
    while(is_prime(p) is False):
        p = random.randint(10,50)
    print("p", p)
        
    q = 4
    while(is_prime(q) is False or q == p):
        q = random.randint(10, 50)
    print("q", q)

    N = p * q
    print("N", N)
    
    
    phi_N = (p-1)*(q-1)
    
    e = N
    while(eeA(phi_N, e)[0] != 1):
        e = random.randint(2, N)
        
    print("e", e)
    public_rsa = (e, N)
    a, d, k = eeA(e, phi_N)
    private_rsa = (d, N)
    return public_rsa, private_rsa

def eeA(a, b):
    if a == 0 :
        return b,0,1
             
    (t,x1,y1) = eeA(b%a, a)
     
    x = y1 - (b//a) * x1
    y = x1
     
    return (t,x,y)

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