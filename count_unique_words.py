import re

def count_words(fl):
    # dictionary with words as keys, values # of appearances of word
    d = {}
    tot_wds = 0
    with open(fl, "r") as f:
        lns = f.readlines()
        for l in lns:
            wds = re.findall(r"[a-zA-Z0-9\-\']+", l.lower())
            for w in wds:
                if w not in d.keys(): d[w] = 1
                else: d[w] += 1
                tot_wds += 1
    print("Total words:", tot_wds, "\n")
    # Sort according to value, the 2nd coord 
    s = sorted(d.items(), key=lambda x:x[1], reverse=True)
    print("Top 20 Words:")
    p = s[:20]
    for w in p: print(f'{w[0]:5} {w[1]:5d}') # formatting for consistent spacing

count_words("shakespeare.txt")