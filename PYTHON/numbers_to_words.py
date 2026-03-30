def number(num):
    dict={
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine",
        "0":"zero",       
    }
    for ch in str(num):
        print(dict[ch] ,end="")

print(number(input("enter the number:")))