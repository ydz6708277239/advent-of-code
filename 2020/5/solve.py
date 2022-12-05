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
Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be 
specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane 
(numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the 
whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back 
(64 through 127). The next letter indicates which half of that region the seat is in, and so on until 
you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the 
plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. 
L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat 
has ID 44 * 8 + 5 = 357.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
"""
ans = 0
with open(fip) as f:
    for idx, line in enumerate(f.readlines()):
        xs = line.strip()
        a,b = xs[:7], xs[7:] 
        lb, ub = 0, 127
        for c in a:
            m = (lb + ub) >> 1
            if c == 'B':
                lb = m+1    ## lowest row value for upper half
            else:
                ub = m      ## highest row value for lower half
            print(lb, ub)
        row = lb
        lb, ub = 0, 7
        for c in b:
            m = (lb + ub) >> 1
            if c == 'R':
                lb = m+1
            else:
                ub = m
            print(lb, ub)
        col = lb
        seat = row*8 + col
        ans = max(ans, seat)


    print(f'p1 ans: {ans}')

"""
It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, 
there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so 
they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your 
list.

What is the ID of your seat?
"""
ans = 0
with open(fip) as f:
    seats = []
    for idx, line in enumerate(f.readlines()):
        xs = line.strip()
        a,b = xs[:7], xs[7:] 
        lb, ub = 0, 127
        for c in a:
            m = (lb + ub) >> 1
            if c == 'B':
                lb = m+1    ## lowest row value for upper half
            else:
                ub = m      ## highest row value for lower half
            # print(lb, ub)
        row = lb
        lb, ub = 0, 7
        for c in b:
            m = (lb + ub) >> 1
            if c == 'R':
                lb = m+1
            else:
                ub = m
            # print(lb, ub)
        col = lb
        seat = row*8 + col
        if not seat:
            print(idx, line)
        seats += [seat]
        seats.sort()
        
    # print(seats)

    ans = set(range(seats[0], seats[-1])) - set(seats)

    print(f'p2 ans: {ans}')


