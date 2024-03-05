num=int(input("how much money? "))
while(True):
    print("A:variz pool\nB:bardasht pool\nC:mujudi\nD:payan")
    ch=input("enter your activty with A,B,C,D: ")
    if ch=='A':
        a=int(input("please enter your money for variz: "))
        num+=a
    elif ch=='B':
        b=int(input("please enter your money for bardasht: "))
        if b>num:
            print("mujudit kameh baraye bardasht!!!\n")
        else:
            num-=b
    elif ch=='C':
        print("mujudi is %i\n"%num)
    elif(ch=='D'):
        break

    