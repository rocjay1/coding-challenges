def index_all(lst, ans, coords, s):
    for item_pos, item in enumerate(lst):
        if type(item) == list: # if item is list, update coords and recursively call on new list
            coords = coords + [item_pos]
            index_all(item, ans, coords, s)
            del coords[-1] # when pop out, remove last coord
        elif item == s: 
            # if found, append item coords to answer list
            coords_app = coords + [item_pos] # new coords list to avoid del
            ans.append(coords_app)
    return 

lst = [[[1,2,[1,2,[1,2,3]]],2,[1,[1,3]]],[1,2,3]]
ans, coords = [], []
index_all(lst, ans, coords, 2)
print(ans)