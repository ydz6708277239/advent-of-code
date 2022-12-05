from functools import reduce
from operator import mul, add
from pprint import pprint
from sys import path
from os.path import join
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from string import ascii_letters as letters, ascii_lowercase as az, ascii_uppercase as AZ

dir_path = path[0]  ## get cwd

"""
After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
test = 0
fi = "input.txt" if not test else "ex1.txt"
fip = join(dir_path, fi)

padding = 0
pad = ['\n'] if padding else []

ans = 0
with open(fip) as f:
    pic = []
    st = defaultdict(list)
    for idx, line in enumerate(f.readlines() + pad):
        xs = line
        if idx < 8:
            pic += [xs]
        ## build stacks
        elif idx == 8:
            # cols = [pic[-1].find(i) for i in '123456789']   
            # print(cols)    
            for i,x in enumerate(xs):
                # print(x)
                if x.isnumeric():
                    # print(i,x)
                    j = len(pic) - 1
                    while j>=0 and pic[j][i] in letters:
                        st[int(x)] += [pic[j][i]]
                        j -= 1

            pprint(st)

        elif idx > 9:
            print(xs)
            # _,cnt,_,src,_,dest = xs.strip().split()
            # cnt, src, dest = map(int, (cnt, src, dest))
            # for _ in range(cnt):
            #     st[dest].append(st[src].pop())

    pprint(st)
    ans = reduce(add, [x[-1] for x in st.values()])



    print(f'p1 ans: {ans}')

"""
After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
test = 0
fi = "input.txt" if not test else "ex1.txt"
fip = join(dir_path, fi)

padding = 0
pad = ['\n'] if padding else []

ans = 0
with open(fip) as f:
    pic = []
    st = defaultdict(list)
    for idx, line in enumerate(f.readlines() + pad):
        xs = line
        # print(idx, line)
        if idx < 8:
            pic += [xs]
        ## build stacks
        elif idx == 8:
            for i,x in enumerate(xs):
                if x.isnumeric():
                    j = len(pic) - 1
                    while j>=0 and pic[j][i] in letters:
                        # print(pic[j][i])
                        st[x] += [pic[j][i]]
                        j -= 1

            # pprint(st)

        elif idx > 9:
            xs = line.strip()
            # print(xs)
            # if xs:
            cnt,src,dest = filter(str.isnumeric, xs.split())
            # print(f"transferring {cnt} blocks from {src} -> {dest}")
            tmp = []
            for _ in range(int(cnt)):
                tmp = [st[src].pop()] + tmp
            st[dest].extend(tmp)
                
        

    pprint(st)
    ans = reduce(add, [x[-1] for x in st.values()])
            



    print(f'p2 ans: {ans}')


