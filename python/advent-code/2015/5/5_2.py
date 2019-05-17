'''
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a 
string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping,
like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

It contains at least one letter which repeats with exactly one letter between them, like xyx, 
abcdefeghi (efe), or even aaa.

For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
'''

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

lines = (line for line in open(os.path.join(__location__, 'input.txt')))
line_list = (line.rstrip() for line in lines)
input_elements = list(line_list)

#input_elements = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'aaabfbaamvaa', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']

total_good = 0

for element in input_elements:
    rule_1_count = False
    rule_2_count = 0
    my_dict = {}
    size = len(element)
    for index, char in enumerate(element):
        if index > 1 and char == element[index - 2]:
            rule_2_count += 1
        
        if index > 0:
            if index + 1 < size and element[index-1] is char and element[index+1] is char:
                continue
            else:
                item = element[index-1] + char
                if item in my_dict:
                    my_dict[item] = my_dict[item] + 1
                else:
                    my_dict[item] = 1
    for _, v in my_dict.items():
        if v >= 2:
            rule_1_count = True
            break    
    if rule_1_count and rule_2_count >= 1:
        total_good += 1

    #print(element, ' - ', rule_1_count, ',', rule_2_count)

print('Nice Strings = ', total_good)
