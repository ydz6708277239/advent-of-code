from functools import reduce, cache, lru_cache
from operator import mul, add
from itertools import accumulate, product
from pprint import pprint
from random import sample, choice, choices
from sys import path
from os.path import join
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from string import ascii_letters as letters, ascii_lowercase as az, ascii_uppercase as AZ

dir_path = path[0]  ## get cwd

## graph-related problems
mov = [-1,0,1]
mv = [-1,0,1,0,-1]

# adj8 = lambda i,j: [(i+di,j+dj) for di,dj in [*(product(mov,mov))] if di|dj]
# adj4 = [(i,j) for i,j in adj8 if i^j]
# adj4 = lambda i,j: [(i+di,j+dj) for di,dj in zip(mv[:-1], mv[1:])]
def adj8(i,j):
    yield from ((i+di,j+dj) for di,dj in [*(product(mov,mov))] if di|dj)
def adj4(i,j):
    yield from ((i+di,j+dj) for di,dj in zip(mv[:-1], mv[1:]))

"""

"""
test = 0
fi = "input.txt" if not test else "ex1.txt"
fip = join(dir_path, fi)

padding = 0
pad = ['\n'] if padding else []

a, b = 0, 0
with open(fip) as f:
    for idx, line in enumerate(f.readlines() + pad):
        xs = line.strip()
        print(xs)



    print(f'p1 ans: {a}')

    print(f'p2 ans: {b}')

