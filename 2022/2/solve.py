from sys import path
from os.path import join
# from pathlib import Path

dir_path = path[0]  ## get cwd
fi = "input.in"
print(dir_path)
fip = join(dir_path, fi)
print(fip)

"""
The winner of the whole tournament is the player with the highest score. Your total score is the sum 
of your scores for each round. The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 
3 if the round was a draw, and 6 if you won).
"""

shape_score = {move:score for move,score in zip('XYZ', (1,2,3))}
score2shape = {score:move for move,score in zip('XYZ', (1,2,3))}
def result(x,y):
    if x+y in ('AX','BY', 'CZ'):
        return 3
    if x+y in ('AY','BZ', 'CX'):
        return 6
    return 0
print(shape_score)
ans = 0
with open(fip) as f:
    for turn in f.readlines():
        opp, mine = turn.split()
        ans += shape_score[mine] + result(opp, mine)
    print(ans)

"""
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how 
the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means 
you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose 
so the round ends as indicated. The example above now goes like this:s
"""
ans = 0
with open(fip) as f:
    for turn in f.readlines():
        opp, outcome = turn.split()
        if outcome == "X":  ## loss
            ans += 0
            if opp == "A":
                ans += shape_score["Z"]
            elif opp == "B":
                ans += shape_score["X"]
            else:
                ans += shape_score["Y"]

        elif outcome == "Y": ## draw
            ans += 3
            if opp == "A":
                ans += shape_score["X"]
            elif opp == "B":
                ans += shape_score["Y"]
            else:
                ans += shape_score["Z"]

        else:   ## win
            ans += 6
            if opp == "A":
                ans += shape_score["Y"]
            elif opp == "B":
                ans += shape_score["Z"]
            else:
                ans += shape_score["X"]
            
        # ans += shape_score[mine] + result(opp, mine)
    print(ans)
