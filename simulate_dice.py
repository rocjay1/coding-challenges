import random

# Create an init dict with entries corresponding to different possible outcomes
def construct_tbl(*dice):
    max_outcome, min_outcome = 0, 0
    for die in dice: 
        max_outcome = max_outcome + die
        min_outcome = min_outcome + 1
    return {i : 0 for i in range(min_outcome, max_outcome + 1)}

def print_tbl(tbl, num_samples):
    for key in tbl:
        prob = (tbl[key] / num_samples) * 100
        tbl[key] = prob
        print("{}\t{:0.2f}%".format(key, prob))
    return tbl

def roll_dice(num_samples, *dice):
    tbl = construct_tbl(*dice)
    # for each trial, roll each of the dice and compute the final outcome
    for trial in range(0, num_samples): 
        outcome = 0
        for die in dice:
            outcome = outcome + random.randint(1,die)
        tbl[outcome] = tbl[outcome] + 1 
    return print_tbl(tbl, num_samples) # return table in probability form
            
roll_dice(1000000, 4, 6, 6, 20)