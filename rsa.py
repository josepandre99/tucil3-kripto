import math
from function import *



class RSA:
    
    # Enkripsi per n_char_encrypt character
    n_char_encrypt = 1
    
    def __init__(self, p=0, q=0, e=0, d=0, n=0):
        self.p = p
        # if not is_prime(p):
        #     print("p must be a prime number")
            
        self.q = q
        # if is_prime(q):
        #     print("q must be a prime number")
            
        if n == 0 :
            self.n = p * q
            if self.n < int(self.n_char_encrypt*'255'):
                print(f"p*q must be greater than {self.n_char_encrypt*'255'}")
        else:
            self.n = n
            

        self.e = e
            
        self.d = d
        
        self.plain = ''
        self.cipher = ''
        
        # print data
        print("Data :")
        print("p : ", self.p)
        print("q : ", self.q)
        print("n : ", self.n)
        print("e : ", self.e)
        print("d : ", self.d)
        print("toitent_euler(n) : ", self.toitent_euler())
        print("")
        
        
    
    def toitent_euler(self):
        return (self.p-1)*(self.q-1)
    
    
    def find_d(self):
        k = 0
        d_integer = False
        while d_integer == False:
            if ((1 + k*self.toitent_euler()) % self.e == 0):
                return (1 + k*self.toitent_euler()) // self.e
            k += 1
        
        
    def public_key(self):
        print("Kunci public :")
        print(f"e : {self.e} \nn : {self.n}")
        return self.e, self.n
        
        
    def private_key(self):
        print("Kunci private :")
        print(f"d : {self.d} \nn : {self.n}")
        return self.d, self.n
        
    
    def generate_key(self):
        list_error = []
        if coprime2(self.e, self.toitent_euler()):
            self.d = self.find_d()
        else:
            print(f"e must be coprime with toitent_euler(p*q) = {self.toitent_euler()}")
    
    
    def set_plain(self, plain):
        self.plain = plain
        print("Plain teks : ", self.plain)
        
    def set_cipher(self, cipher):
        self.cipher = cipher
        print("Cipher teks : ", self.cipher)
        
        
    def writeKey(self):
        data_public_key = str(self.e) + "," + str(self.n)
        data_private_key = str(self.d) + "," + str(self.n)
        
        writeFileText('rsa.pub', data_public_key)
        writeFileText('rsa.pri', data_private_key)
        
        
    def encrypt(self):
        m = ''
        for i in self.plain:
            m += str(ord(i)).zfill(3)
        
        list_m = split_string_into_list_of_length_n(m, 3*self.n_char_encrypt)
        
        c = ''
        for i in list_m:
            c += str((int(i)**self.e) % self.n).zfill(len(str(self.n)))
    
        print(f"Cipher hasil enkripsi : {c}")
        self.cipher = c
        return c


    def decrypt(self):
        list_c = split_string_into_list_of_length_n(self.cipher, len(str(self.n)))
        
        m = ''
        for i in list_c:
            m += str((int(i)**self.d) % self.n).zfill(3*self.n_char_encrypt)
            
        list_m = split_string_into_list_of_length_n(m, 3)
        
        m_teks = ''
        for i in list_m:
            m_teks += chr(int(i))
        
        
        print(f"Plain hasil dekripsi : {m_teks}")
        self.plain = m_teks
        return m_teks
        
        
        
        
        
if __name__ == "__main__":
    rsa = RSA(d=14431, n=286081)
    # rsa.generate_key()
    rsa.public_key()
    rsa.private_key()
    rsa.set_plain('HELLO')
    cipher =  rsa.encrypt()
    # print("==============================")
    # rsa.set_cipher('240205229859203623203623141282')
    # rsa.decrypt()
    