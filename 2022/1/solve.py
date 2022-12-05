from sys import path
from os.path import join
# from pathlib import Path

dir_path = path[0]  ## get cwd
fi = "input.in"
print(dir_path)
fip = join(dir_path, fi)
print(fip)

# fp = os.path.realpath(__file__)
# dir_path = os.path.dirname(fp)
# print(dir_path)

"""
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to 
know how many Calories are being carried by the Elf carrying the most Calories. In the example above, 
this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""
with open(fip) as f:
    ans = 0
    curr = 0
    for idx,line in enumerate(f.readlines()):
        # s = ' '.join([str(ord(x)) for x in line])
        # print(s)
        z = line.strip()
        if not z:
            ans = max(ans, curr)
            curr = 0
        else: 
            curr += int(z)
    ans = max(ans, curr)
    print(ans)

"""
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

with open(fip) as f:
    ans = 0
    curr = 0
    q = []
    for idx,line in enumerate(f.readlines()):
        # s = ' '.join([str(ord(x)) for x in line])
        # print(s)
        z = line.strip()
        if not z:
            ans = max(ans, curr)
            q += [curr]
            curr = 0
        else: 
            curr += int(z)
    ans = max(ans, curr)
    q += [curr]
    q.sort()
    print(sum(q[-3:]))
