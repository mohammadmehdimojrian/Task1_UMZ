a=input()
n=len(a)-1
if a[0]=='[' and a[n]==']':
    print(type(eval(a)))
    exit()
if ord(a[0])==34 or ord(a[0])==39:
    print(type(a))
    exit()
for i in a:
    if ord(i)>=65 and ord(i)<=122:
        print(type(a))
        exit()
if type(eval(a)=='int' or eval(a)=='float'):
    print(type(eval(a)),'number')