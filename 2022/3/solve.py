from collections import Counter
from sys import path
from os.path import join
from string import ascii_letters as letters

dir_path = path[0]  ## get cwd
fi = "input.in"
print(dir_path)
fip = join(dir_path, fi)
print(fip)

"""
To help prioritize item rearrangement, every item type can be converted to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

The list of items for each rucksack is given as characters all on a single line. A given rucksack always 
has the same number of items in each of its two compartments, so the first half of the characters 
represent items in the first compartment, while the second half of the characters represent items in the 
second compartment.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities 
of those item types?
"""
priorities = {v:p for p,v in enumerate(letters, start=1)}
ans = 0
with open(fip) as f:
    for idx, line in enumerate(f.readlines()):
        rucksack = line.strip()
        sz = len(rucksack)//2
        c1, c2 = Counter(rucksack[:sz]), Counter(rucksack[sz:])
        for c in letters:
            if c in c1 and c in c2:
                # print(f'{idx}: {c} in both')
                ans += priorities[c]
    print(f'p1 ans: {ans}')

"""
Every set of three lines in your list corresponds to a single group, but each group can have a different 
badge item type. So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg

And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

"""
ans = 0
group = []
with open(fip) as f:
    for idx, line in enumerate(f.readlines()):
        rucksack = line.strip()
        z = idx % 3
        if not z:
            group = []
        # print(z)
        group += [rucksack]
        # try:
        #     group[z] = rucksack
        # except IndexError:
        #     print(f'index error: {z}')
        if z == 2:
            for c in letters:
                if c in group[0] and c in group[1] and c in group[2]:
                    # print(f'{idx}: {c} in all')
                    ans += priorities[c]
    print(f'p2 ans: {ans}')


