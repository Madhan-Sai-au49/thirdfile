m = input("ENTER A NUMBER = M : ")
n = input("ENTER A NUMBER = N : ")
o = input("ENTER A NUMBER = 0 : ")
p = input("ENTER A NUMBER = P : ")

if (m>n and m>o and m>p):
    print(" M IS GREATER THAN N,O,P")
elif (n>m and n>o and n>p):
    print("N IS GREATER THAN M,O,P")
elif (o>m and o>n and o>p):
    print("O IS GREATER THAN M,N,P")
else:
    print("P IS GREATER THAN M,N,O")
