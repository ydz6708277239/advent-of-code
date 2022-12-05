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

"""
ans = 0
with open(fip) as f:
    for idx, line in enumerate(f.readlines()):
        xs = line.strip()



    print(f'p1 ans: {ans}')

"""

"""
ans = 0
with open(fip) as f:
    for idx, line in enumerate(f.readlines()):
        xs = line.strip()



    print(f'p2 ans: {ans}')


