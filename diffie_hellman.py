import math
from function import *


class Diffie_Hellman:
    def __init__(self, n, g, x, y):
        if g >= n:
            print("g must be smaller than n")
        if not is_prime(n):
            print("n must be a prime numner")
        if not is_prime(g):
            print("g must be a prime number")
            
        self.n = n
        self.g = g
        self.x = x
        self.y = y
        
        print(f"n : {n}")
        print(f"g : {g}")
        print(f"x : {x}")
        print(f"y : {y}\n")
        
        
    def generate_X(self):
        return (self.g**self.x) % self.n
    
    def generate_Y(self):
        return (self.g**self.y) % self.n
    
    def count_K(self):
        return (self.generate_Y()**self.x) % self.n
    
    def count_K_dash(self):
        return (self.generate_X()**self.y) % self.n 
        
        
    def generate_key(self):
        X = self.generate_X()
        Y = self.generate_Y()
        K = self.count_K()
        K_dash = self.count_K_dash()
        
        print(f"X : {X}")
        print(f"Y : {Y}")
        print(f"K : {K}")
        print(f"K_dash : {K_dash}")
        
        return X, Y, K, K_dash
            
        

if __name__ == "__main__":
    dh = Diffie_Hellman(97, 5, 36, 58)
    dh.generate_key()