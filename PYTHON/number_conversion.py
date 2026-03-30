num=int(input("enter a decimal number:"))
base=int(input("enter the base(2/8/16):"))
digits="0123456789ABCDEF"
result=""

while num>0:
    result=digits[num%base]+result
    num=num//base
print("converted number:",result)