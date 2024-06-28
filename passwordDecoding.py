import hashlib
from hashlib import sha3_512
password = "cbfe4a6d948b4c1fc7c05ac4ba1a5b91c145e7bb88ea7d34cf2b10f28eafd1318477ff0e5dd679432e3b7b3763c6d3424037221addb68568b9215df83014f877"

s = hashlib.sha3_512()
s.update(b"abbild")
dic = {}
with open("Lernfeld_8_Hashmap_-bung\de-1296-v1.txt") as f:
    for line in f.read().splitlines():
        s = sha3_512(line.encode())
        dic[s.hexdigest()] = line
print(dic[password])


