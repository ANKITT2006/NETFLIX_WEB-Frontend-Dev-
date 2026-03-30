sentence=input("enter a sentence:")
letters=0
digits=0
for ch in sentence:
    if ch.isalpha():
        letters+=1
    elif ch.isdigit():
        digits+=1
print("letters:",letters)
print("digits:",digits)