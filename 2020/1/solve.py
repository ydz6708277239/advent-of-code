from sys import path
from os.path import join
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from string import ascii_letters as letters, ascii_lowercase as az, ascii_uppercase as AZ

dir_path = path[0]  ## get cwd
fi = "input.in"
print(dir_path)
fip = join(dir_path, fi)
print(fip)

"""
Find the two entries that sum to 2020; what do you get if you multiply them together?
"""
ans = 0
s = set()
with open(fip) as f:
    for idx, line in enumerate(f.readlines()):
        xs = int(line.strip())
        if 2020 - xs in s:
            ans = (xs*(2020 - xs))
            break
        s |= {xs}


    print(f'p1 ans: {ans}')

"""

"""
ans = 0
with open(fip) as f:
    z = [int(line) for idx, line in enumerate(f.readlines())]
    z.sort()
    for i in range(len(z)-2):
        for j in range(i+1, len(z)-1):
            for k in range(j+1, len(z)):
                if sum((z[i],z[j],z[k])) == 2020:
                    ans = (z[i]*z[j]*z[k])



    print(f'p2 ans: {ans}')


