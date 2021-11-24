import string

def is_palindrome(st):
    # Remove all punctuation, whitespace and make all lowercase in most efficient way
    st = st.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ", "") 
    i = 0
    while (i <= len(st)//2 - 1):
        if (st[i] != st[len(st) - 1 - i]): return False
        i = i + 1
    return True

print(is_palindrome('Go Hang a Salami - I"m a lasagna hog.'))