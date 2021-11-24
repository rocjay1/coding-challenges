def alpha_sort(st):
    lst = [sub_st for sub_st in st.split()]
    start_st = st 
    i = 0
    # Consider pairs of words, moving up 1 place each time
    while (i < len(lst) - 1):
        # First sort the words by length
        item_1, item_2 = lst[i], lst[i + 1]
        if (len(item_1) > len(item_2)):
            lst[i], lst[i + 1] = item_2, item_1
        j = 0
        comp_len = min(len(item_1), len(item_2))
        # Comparing the letters one index at a time, alphabetize
        while (j < comp_len):
            if (lst[i][j].lower() > lst[i + 1][j].lower()): # if they're out of order, switch them
                item_1, item_2 = lst[i], lst[i + 1]
                lst[i], lst[i + 1] = item_2, item_1
                break
            elif (lst[i][j].lower() < lst[i + 1][j].lower()): break # if this happens, they're in order
            j = j + 1
        i = i + 1
    st = " ".join(lst)
    if (st != start_st): return alpha_sort(st)
    return st

# Easier implementation using the sorted function
def sort_words(st):
    return " ".join(sorted(st.split(), key=str.lower))

print(alpha_sort("alley allay ally all"))
print(alpha_sort("banana ORANGE apple"))
print(alpha_sort("String of words"))

print(sort_words("alley allay ally all"))
print(sort_words("banana ORANGE apple"))
print(sort_words("String of words"))