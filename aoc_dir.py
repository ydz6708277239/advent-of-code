from sys import path, argv
import os
from string import ascii_lowercase as a2z
from pathlib import Path
from datetime import datetime

currentDateTime = datetime.now()
date = currentDateTime.date()
current_yr = (date.strftime("%Y"))
print(current_yr)

dir_path = path[0]  ## get cwd
print(dir_path)
template_path = '/Users/wdanni/kyopro/AOC/solve_template.py'


years = argv[1:]
if not years:
    print('no inputs provided')
print(years)

for year in years:
    # try:
        if not year.isnumeric():
            print(f'{year} is not numeric')
            continue
        if not ('2015' <= year <= current_yr):
            print(f'skipping {year}: not valid AOC year')
            continue
        yp = os.path.join(dir_path, year)
        if not os.path.exists(yp):
            os.mkdir(yp)
        for day in range(1,len(a2z)):
            dp = os.path.join(yp, str(day))
            if not os.path.exists(dp):
                os.mkdir(dp)
                # input_path = os.path.join(dp, 'input.in')
            ex1_path = Path(os.path.join(dp, 'ex1.txt'))
            ex1_path.touch(exist_ok=True)            
            input_path = Path(os.path.join(dp, 'input.txt'))
            input_path.touch(exist_ok=True)            
            sol_path = os.path.join(dp, 'solve.py')
            # sol_path = Path(os.path.join(dp, 'solve.py'))
            if not os.path.exists(sol_path) or not os.path.getsize(sol_path):
                print(f'creating solve.py in {dp}')
                src = open(template_path, "r")
                dest = open(sol_path, "w")
                dest.writelines(l for l in src)
                # with open(sol_path, "w") as dest: 
                #     dest.writelines(l for l in src)
                dest.close()
                src.close()
    # except Exception:
    #     print('invalid year value')



    

