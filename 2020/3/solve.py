from functools import reduce
from operator import mul, add
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
Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a 
map (your puzzle input) of the open squares (.) and trees (#) you can see.

The locations you'd check in the above example are marked here with O where there was an open square and X 
where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees 
would you encounter?
"""
ans = 0
with open(fip) as f:
    col = 0
    for idx, line in enumerate(f.readlines()):
        xs = line.strip()
        if xs[col] == '#':
            ans += 1
        col = (col + 3) % len(xs)
        print(col)




    print(f'p1 ans: {ans}')

"""
Determine the number of trees you would encounter if, for each of the following slopes, you start at the 
top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, 
these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""
ans = 0

with open(fip) as f:
    a,b,c,d,e = 0,0,0,0,0
    cnt = Counter()
    for idx, line in enumerate(f.readlines()):
        xs = line.strip()
        if xs[a] == "#":
            cnt['a'] += 1
        a = (a + 1) % len(xs) 
        if xs[b] == "#":
            cnt['b'] += 1
        b = (b + 3) % len(xs) 
        if xs[c] == "#":
            cnt['c'] += 1
        c = (c + 5) % len(xs) 
        if xs[d] == "#":
            cnt['d'] += 1
        d = (d + 7) % len(xs) 
        if not idx & 1:
            if xs[e] == "#":
                # print('hit tree on `e`-slope')
                cnt['e'] += 1
            e = (e + 1) % len(xs) 

    ans = reduce(mul, cnt.values())    

    print(f'p2 ans: {ans}')


