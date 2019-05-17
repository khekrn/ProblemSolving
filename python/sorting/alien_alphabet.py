'''
Aliens have visited earth and their alphabet is very weird. Its the same 26 letters (A to Z) but in a different order. They want your help to sort a string in the order of their alphabet.

For example, aliens might use the reversed alphabet of "zyxwvutsrqponmlkjihgfedcba" so when they sort "abc", it becomes "cba" and when they sort "apple" it becomes "pplea". When sorting capital/lowercase letters, the capital letters always come first (e.g. "camelCasE" -> "smlEeCcaa").

You will write a program that reads 2 lines from standard input - the first line is the alien's alphabet (letters a-z, all lowercase) and the second line is the string the aliens want you to sort. Your program will output only the sorted string (no other text should be printed by the program). Examples are provided below.

Example 1
input
abcdefghijklmnopqrstuvwxyz
cyxbza

output
abcxyz

Example 2
input
zyxwvutsrqponmlkjihgfedcba
cyxbza

output
zyxcba

Example 3
input
wvutsrqponmlkjihgfedcbaxyz
camelCasE

output
smlEeCcaa

'''

def alien_alphabet(A, tokens):
    my_dict = {}
    for index, value in enumerate(A):
        my_dict[value.upper()] = index + 1
        my_dict[value] = my_dict[value.upper()] + 1        

    result_dict = {}

    for token in tokens:
        result_dict[my_dict[token]] = token
    
    res = ''.join([str(result_dict[key]) for key in sorted(result_dict)])    
    return res

A = 'wvutsrqponmlkjihgfedcbaxyz'
tokens = 'camelCasE'

print(alien_alphabet(A, tokens))