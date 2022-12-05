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
Each line gives the password policy and then the password. The password policy indicates the lowest and 
highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means 
that the password must contain a at least 1 time and at most 3 times.

How many passwords are valid according to their policies?
"""
ans = 0
with open(fip) as f:
    for idx, line in enumerate(f.readlines()):
        freq, letter, pw = line.strip().replace(":", "").split()
        # print(freq, letter, pw)
        a,b = map(int, freq.split("-"))
        if a <= Counter(pw)[letter] <= b:
            ans += 1 



    print(f'p1 ans: {ans}')

"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means 
the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant 
for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
"""
ans = 0
with open(fip) as f:
    for idx, line in enumerate(f.readlines()):
        freq, letter, pw = line.strip().replace(":", "").split()
        a,b = map(lambda x: int(x)-1, freq.split("-"))
        # print(a,b)
        ans += Counter(pw[a]+pw[b])[letter] == 1 



    print(f'p2 ans: {ans}')


