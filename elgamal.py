import math
from function import *


class ElGamal :

    n_char_encrypt = 1

    def __init__(self, p, g, x, y=0):
        print(f"p : {p}")
        print(f"g : {g}")
        print(f"x : {x}")
        print(f"y : {y}")

        if not is_prime(p) :
            print("p must be a prime number")
        if g >= p :
            print("g must be smaller than p")
        if (x < 1) or (x > (p-2)) :
            print("x must be in 1 =< x =< p-2")

        self.p = p
        self.g = g
        self.x = x
        self.y = y

        print(f"p : {p}")
        print(f"g : {g}")
        print(f"x : {x}")
        print(f"y : {y}")

    def public_key(self) :
        print("Kunci public :")
        print(f"y : {self.y} \ng : {self.g} \np : {self.p}")
        return self.y, self.g, self.p

    def private_key(self) :
        print("Kunci private :")
        print(f"x : {self.x} \np : {self.p}")
        return self.x, self.p

    def generate_key(self) :
        self.y = (self.g ** self.x) % self.p

        ElGamal.writeKey(self)
        ElGamal.public_key(self)
        ElGamal.private_key(self)

    def set_plain(self, plain):
        self.plain = plain
        print("Plain teks : ", self.plain)
        
    def set_cipher(self, cipher):
        self.cipher = cipher
        print("Cipher teks : ", self.cipher)

    def writeKey(self):
        data_public_key = str(self.y) + "," + str(self.g) + "," + str(self.p)
        data_private_key = str(self.x) + "," + str(self.p)
        
        writeFileText('elgamal.pub', data_public_key)
        writeFileText('elgamal.pri', data_private_key)

    def encrypt(self, k) :

        if (k < 1) or (k > (self.p-2)) :
            print("k must be in 1 =< k =< p-2")

        self.k = k

        m = ''
        for i in self.plain :
            m += str(ord(i)).zfill(3)

        list_m = split_string_into_list_of_length_n(m, 3*self.n_char_encrypt)
 
        list_cipher = []
        for i in list_m :
            a = (self.g ** self.k) % self.p
            a = str(a).zfill(len(str(self.p)))
            b = ((self.y ** self.k) * int(i)) % self.p
            b = str(b).zfill(len(str(self.p)))
            list_cipher.append([a, b])

        #print("List cipher : ", list_cipher)
        c = ''
        for i in list_cipher :
            c += str(i[0]) + str(i[1])
        
        print(f"Cipher hasil enkripsi : {c}")
        self.cipher = c
        return c

    def decrypt(self) :
        list_c_raw = split_string_into_list_of_length_n(self.cipher, len(str(self.p)))

        i = 0
        list_c = []
        while i < len(list_c_raw) :
            list_c.append([int(list_c_raw[i]), int(list_c_raw[i+1])])
            i += 2

        #print("List_c : ", list_c)

        list_plain = []
        for i in list_c :
            ax_inverse = (i[0] ** (self.p - 1 - self.x)) % self.p
            m = i[1] * ax_inverse % self.p
            list_plain.append(m)
        
        #print("List_plain : ", list_plain)
        
        plain = ''
        for i in list_plain :
            plain += chr(i)

        print(f"Plain hasil dekripsi : {plain}")
        self.plain = plain
        return plain



if __name__ == "__main__":
    elgamal = ElGamal(2357, 2, 1751)
    elgamal.set_plain("HELLO ALICE")
    elgamal.generate_key()
    cipher = elgamal.encrypt(1520)
    plain = elgamal.decrypt()

