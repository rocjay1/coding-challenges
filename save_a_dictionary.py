def save_dict(dict, path):
    s = str(dict) 
    with open(path, "w") as f:
        f.write(s)

d = {0 : {0 : 'a'}, 1 : 'b'}
save_dict(d, "./saved_dict.txt")

def retrieve_dict(path):
    with open(path, "r") as f:
        contents = f.read()
        return eval(contents) # eval does the hard conversion

print(retrieve_dict("./saved_dict.txt"))
