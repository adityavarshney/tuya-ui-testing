from itertools import product 
import string 
from sys import argv
import gzip 
import time 

start = time.time()
filename = argv[1] + '.gz'
length = int(argv[2])
all_chars = "ZE0123456789ABCDFGHIJKLMNOPQRSTUVWXY"

print(f"Starting program: Code format: {' '.join(['_']*length)}  ({all_chars})")
result = product(all_chars, repeat=length) 

print(f"Got the combinations in {(time.time()-start) // 60} minutes total. Writing to {filename}.")

with gzip.open(filename, 'wb') as wf: 
    for code in result:
        wf.write(str.encode(f"{''.join(code)}\n"))

print(f"Codes saved in {filename} in {(time.time()-start) // 60} minutes total")