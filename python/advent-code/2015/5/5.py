'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or 
aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part 
of one of the other requirements.

For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
'''

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

lines = (line for line in open(os.path.join(__location__, 'input.txt')))
line_list = (line.rstrip() for line in lines)
input_elements = list(line_list)

total_good = 0

for element in input_elements:
    vowal_count = 0
    appear_twice = False
    not_contains = True
    for index, char in enumerate(element):
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowal_count += 1
        
        if index > 0 and not appear_twice:
            if char == element[index-1]:
                appear_twice = True
        
        if index > 0 and not_contains:
            item = element[index-1]+char
            if item == 'ab' or item == 'cd' or item == 'pq' or item == 'xy':
                not_contains = False
    if vowal_count >= 3 and appear_twice and not_contains:
        total_good += 1

print('Nice Strings = ', total_good)
