# get indices of squares that need to be filled in for each row
def get_inds(puz):
    inds = []
    for row in puz:
        l = []
        for ind, item in enumerate(row):
            if item == 0: l.append(ind)
        inds.append(l)
    return inds

def dup_test(lst):
    lst_nonzero = [x for x in lst if x != 0]
    if len(lst_nonzero) == len(set(lst_nonzero)): return True
    return False

def find_col(k, puz):
    cols = []
    for i in range(0,9):
        col = []
        for row in puz: col = col + [row[i]]
        cols.append(col)
    return cols[k]

def find_box(r, k, puz):
    puzz = [puz[0:3], puz[3:6], puz[6:9]]
    boxes = []
    for p in puzz:
        b1, b2, b3 = [], [], []
        for row in p:
            for i in range(0,len(row)):
                if 0 <= i < 3: b1 += [row[i]]
                elif 3 <= i < 6: b2 += [row[i]]
                else: b3 += [row[i]]
        boxes.append(b1)
        boxes.append(b2)
        boxes.append(b3)
    if 0 <= r < 3 and 0 <= k < 3: return boxes[0]
    elif 0 <= r < 3 and 3 <= k < 6: return boxes[1]
    elif 0 <= r < 3 and 6 <= k < 9: return boxes[2]
    elif 3 <= r < 6 and 0 <= k < 3: return boxes[3]
    elif 3 <= r < 6 and 3 <= k < 6: return boxes[4]
    elif 3 <= r < 6 and 6 <= k < 9: return boxes[5]
    elif 6 <= r < 9 and 0 <= k < 3: return boxes[6]
    elif 6 <= r < 9 and 3 <= k < 6: return boxes[7]
    elif 6 <= r < 9 and 6 <= k < 9: return boxes[8]

def main_test(r, k, puz):
    # row contains no duplicates, column has no duplicates, box has no duplicates
    if dup_test(puz[r]) and dup_test(find_col(k, puz)) and dup_test(find_box(r, k, puz)): return True
    return False

def solve_puz(puz):
    inds = get_inds(puz)
    r = 0 
    while r < 9:
        i = inds[r] 
        j = 0 # enumerates indices in i starting from 0
        k = i[j] # jth square in row that needs to be filled in
        while j < len(i):
            n = puz[r][k] + 1 # new value
            puz[r][k] = n
            # several cases, depending on where in row
            # new value works, valid, not in last column
            if main_test(r, k, puz) and n <= 9 and j < len(i) - 1: 
                j = j + 1
                k = i[j] # then keep going
            # new value works, valid, in the last column
            elif main_test(r, k, puz) and n <= 9 and j == len(i) - 1:
                j = j + 1 # next row
            # new value doesn't work, valid
            elif not main_test(r, k, puz) and n < 9:
                continue # try n + 1
            # new value doesn't work, is 9, not in first column
            # or, new value valid, not in first column
            elif (not main_test(r, k, puz) and n == 9 and j != 0) or (n > 9 and j != 0):
                puz[r][k] = 0
                j = j - 1
                k = i[j] # reset to 0, go back one column
            # new value doesn't work, is 9, in first column
            # or, new value invalid, in first column
            elif (not main_test(r, k, puz) and n == 9 and j == 0) or (n > 9 and j == 0):
                puz[r][k] = 0
                r = r - 1
                i = inds[r]
                j = len(i) - 1
                k = i[j] # reset to 0, go back a row, start in last column
        r = r + 1
    return puz

puz = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0], 
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
print(solve_puz(puz))