'''
Part 1 in 4.py file

--- Part Two ---
Now find one that starts with six zeroes.

'''

import hashlib

input_secret = 'iwrupvqb'
start_value = 1
min_val = None
can_continue = True

while can_continue:
    input_seq = input_secret+str(start_value)
    res = hashlib.md5(input_seq.encode())
    if res.hexdigest()[0:6] == '000000':
        min_val = start_value
        can_continue = False
        break
    start_value += 1
    if start_value % 10000 == 0:
        print('Index = ', start_value)

print(min_val)