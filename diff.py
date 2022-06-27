import random
import os
import aes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512

class Participant:
    def __init__(self, name):
        self.name = name
        print(self.name)
    
    def diff(self):
        self.prime = 13
        self.g = 2
        self.friend.usePrime(self.prime, self.g)
        
        self.private_key = random.randint(0, self.prime - 1)
        
        self.public_key = self.g
        for i in range(1, self.private_key):
            self.public_key = self.public_key * self.g % self.prime
            
        self.friend_public_key = self.friend.use_public_key(self.public_key)
        
        self.K = self.friend_public_key

        for i in range(1, self.private_key):
            self.K = self.K * self.friend_public_key % self.prime
        print(self.name, self.K)
        
        # Use K to generate a 16byte key
        self.sixteenb_key = PBKDF2(self.K, id(self)%256, 16, count=1000000, hmac_hash_module=SHA512)
    
    def use_public_key(self, key):
        self.K = key
        for i in range(1, self.private_key):
            self.K = self.K * key % self.prime
        print(self.name, self.K)
        
        # Use K to generate a 16byte key
        self.sixteenb_key = PBKDF2(self.K, id(self.friend)%256, 16, count=1000000, hmac_hash_module=SHA512)

        return self.public_key
    
    def set_friend(self, friend):
        self.friend = friend

    def usePrime(self, p, g):
        self.prime = p
        self.g = g
        
        self.private_key = random.randint(0, self.prime - 1)
        
        self.public_key = self.g
        for i in range(1, self.private_key):
            self.public_key = self.public_key * self.g % self.prime
            
    def sendAESKeys(self, key1, key2):
        self.key1 = key1
        self.key2 = key2
        
        print("I am", self.name, "I know the keys", key1, key2)
        
        tuple1 = aes.encrypt(self.sixteenb_key, key1)
        tuple2 = aes.encrypt(self.sixteenb_key, key2)
        
        print("I am", self.name, "I send the ciphers", tuple1[1], tuple2[1])
        
        self.friend.receiveAESKeys(tuple1, tuple2)
    
    
    def receiveAESKeys(self, tuple1, tuple2):
        print("I am", self.name, "I received the ciphers", tuple1[1], tuple2[1])

        self.key1 = aes.decrypt(tuple1[0], tuple1[1], tuple1[2], self.sixteenb_key)
        self.key2 = aes.decrypt(tuple2[0], tuple2[1], tuple2[2], self.sixteenb_key)
        
        print("I am", self.name, "I know the keys", self.key1, self.key2)
        

if __name__ == "__main__" :
    alice = Participant("Alice")
    bob = Participant("Bob")
    
    alice.set_friend(bob)
    bob.set_friend(alice)
    
    alice.diff()
    
    first_key = b"Sixteen byte key"
    second_key = b"What is love bae"
    
    alice.sendAESKeys(first_key, second_key)
    
    
    
    
    