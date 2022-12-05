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
The automatic passport scanners are slow because they're having trouble detecting which passports have all 
required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of 
key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your 
batch file, how many passports are valid?
"""
ans = 0
with open(fip) as f:
    missing_facts = {'byr','iyr','eyr','hgt', 'hcl', 'ecl','pid','cid'}
    passport = 1
    for idx, line in enumerate(f.readlines()):
        xs = line.strip().split()
        for stat in xs:
            k,v = stat.split(":")
            missing_facts.discard(k)
        if not xs:
            re = (f'passport {passport} omitted {missing_facts}\n')
            if not missing_facts or missing_facts == {'cid'}:
                re += (f'passport {passport} is valid\n')
                ans += 1
            print(re)
            missing_facts |= {'byr','iyr','eyr','hgt', 'hcl', 'ecl','pid','cid'}
            passport += 1


    print(f'p1 ans: {ans}')

"""
The line is moving more quickly now, but you overhear airport security talking about how passports with 
invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid 
for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Count the number of valid passports - those that have all required fields and valid values. Continue to treat 
cid as optional. In your batch file, how many passports are valid?
"""
def ok(k,v):
    if k == 'byr': return v.isnumeric() and len(v) == 4 and '1920'<=v<='2002'
    if k == 'iyr': return v.isnumeric() and len(v) == 4 and '2010'<=v<='2020'
    if k == 'eyr': return v.isnumeric() and len(v) == 4 and '2020'<=v<='2030'
    if k == 'hgt':
        q,m = v[:-2],v[-2:]
        if q.isnumeric() and m in ('cm','in'):  
            return True if ('150'<=q<='193' and m == 'cm' or '59'<=q<='76' and m == 'in') else False
        return False
    if k == 'hcl': return len(v) == 7 and v[0] == '#' and all(c in '0123456789abcdef' for c in v[1:])
    if k == 'ecl': return v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if k == 'pid': return v.isnumeric() and len(v) == 9
    if k == 'cid': return True

ans = 0
with open(fip) as f:
    missing_facts = {'byr','iyr','eyr','hgt', 'hcl', 'ecl','pid','cid'}
    passport = 1
    for idx, line in enumerate(f.readlines()):
        xs = line.strip().split()
        for stat in xs:
            k,v = stat.split(":")
            if ok(k,v):
                missing_facts.discard(k)
        if not xs:
            re = (f'passport {passport} omitted {missing_facts}\n')
            if not missing_facts or missing_facts == {'cid'}:
                re += (f'passport {passport} is valid\n')
                ans += 1
            print(re)
            missing_facts |= {'byr','iyr','eyr','hgt', 'hcl', 'ecl','pid','cid'}
            passport += 1



    print(f'p2 ans: {ans}')


