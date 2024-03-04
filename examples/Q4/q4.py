print("part A: C>>>>>>>F\npart B: F>>>>>>>C")
ch=input("please choose A or B :")
a=float(input("enter temperature: "))
if ch=='A':
    print(1.8*a+32)
elif ch=='B':
    print((a-32)/1.8)