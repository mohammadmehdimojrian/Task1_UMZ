a=input()
n=len(a)-1
if a[0]=='[' and a[n]==']':
    print("list")
    exit()
if ord(a[0])==34 or ord(a[0])==39:
    print("string")
    exit()
for i in a:
    if ord(i)>=65 and ord(i)<=122:
        print("string")
        exit()
if type(eval(a)=='int' or eval(a)=='float'):
    print("number")