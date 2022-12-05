from sys import path
from os.path import join
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from string import ascii_letters as letters, ascii_lowercase as az, ascii_uppercase as AZ

dir_path = path[0]  ## get cwd
fi = "ex1"
print(dir_path)
fip = join(dir_path, fi)
print(fip)

"""
The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the 
questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take 
very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. 
For each of the people in their group, you write down the questions for which they answer "yes", one per line. 
For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers 
to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the 
plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each 
person's answers are on a single line. 

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
"""
flag = 1
pad = ['\n'] if flag else []

ans = 0
seen = set()
group = 1
with open(fip) as f:
    for idx, line in enumerate(f.readlines() + pad):
        xs = line.strip()
        seen |= set(xs)
        if not xs:
            # print(f'group {group}: {seen}')
            ans += len(seen)
            seen.clear()
            group += 1


    print(f'p1 ans: {ans}')

"""
For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""
fi = "ex1"
fip = join(dir_path, fi)

flag = 1
pad = ['\n'] if flag else []

ans = 0
group_size = 0
with open(fip) as f:
    seen = Counter()
    for idx, line in enumerate(f.readlines() + pad):
        xs = line.strip()
        for c in xs:
            seen[c] += 1
        print(seen)
        group_size += 1
        if not xs:
            ans += len([k for k in seen if seen[k] == group_size])
            seen.clear()
            group += 1
            group_size = 0



    print(f'p2 ans: {ans}')


