import math
from math import gcd as bltin_gcd


def is_prime(number):   # check prime or not
    if (number==2):
        return True
    if (number%2==0):
        return False
    for i in range(3, math.floor(math.sqrt(number))+1, 2):
        if (number%i == 0):
            return False
    return True


def bilangan_prima_ke(n):   # get n-th prime 
    prime_count = 0
    i = 1
    while prime_count < n:
        i += 1
        if (is_prime(i)):
            prime_count += 1
    return i


def coprime2(a, b):     # chech relative prime or not
    return bltin_gcd(a, b) == 1


def split_string_into_list_of_length_n(string, n):
    return [string[i:i + n] for i in range(0, len(string), n)]


def readFile(filename):
    f = open(filename, "rb")
    data = f.read()
    f.close()
    return data.decode('iso8859-1')


def writeFile(filename, data):
    f = open(filename, "wb")
    bytearray = data.encode('iso8859-1')
    result = f.write(bytearray)
    f.close()
    if (result):
        print("Write file success")
        

def writeFileText(filename, data):
    f = open(filename, "w+")
    result = f.write(data)
    f.close()
    if (result):
        print("Write file success")
        
        
def readPublicPrivateKey(filename):
    f = open(filename, "r+")
    data = f.read()
    data = data.split(',')
    f.close()
    if len(data) == 2 :
        return data[0], data[1]
    if len(data) == 3 :
        return data[0], data[1], data[2]
