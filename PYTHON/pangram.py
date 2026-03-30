#it is a program that checks if a given sentence contains all 26 alphabet letters

def is_pangram(s):
    s=s.lower()
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in s:
            return False
    return True
print(is_pangram("my name is ankit nag"))
        