from sys import path
from os.path import join
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from string import ascii_letters as letters, ascii_lowercase as az, ascii_uppercase as AZ

dir_path = path[0]  ## get cwd

"""
In how many assignment pairs does one range fully contain the other?
"""
exf = 1
fi = "input.in" if exf else "ex1"
fip = join(dir_path, fi)

flag = 0
pad = ['\n'] if flag else []

ans = 0
with open(fip) as f:
    for idx, line in enumerate(f.readlines() + pad):
        a,b = line.strip().split(",")
        a1,a2 = map(int,a.split("-"))
        b1,b2 = map(int,b.split("-"))
        if a1<=b1<=b2<=a2 or b1<=a1<=a2<=b2:
            ans += 1


    print(f'p1 ans: {ans}')

"""
In how many assignment pairs do the ranges overlap?
"""
exf = 1
fi = "input.in" if exf else "ex1"
fip = join(dir_path, fi)

flag = 0
pad = ['\n'] if flag else []

ans = 0
with open(fip) as f:
    cnt = 0
    for idx, line in enumerate(f.readlines() + pad):
        xs = line.strip()
        a,b = line.strip().split(",")
        a1,a2 = map(int,a.split("-"))
        b1,b2 = map(int,b.split("-"))
        if a2 < b1 or b2 < a1:
            ans += 1
        cnt += 1



    print(f'p2 ans: {cnt - ans}')


