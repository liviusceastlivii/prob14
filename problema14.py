a=int(input("Numarul de linii:"))
b=[]
dp=0
ds=0
sdp=0
jdp=0
sds=0
jds=0
for i in range(0, a):
    c=[]
    for j in range(0,a):
        c.append(int(input('>')))
    b.append(c)
for i in range(0,a):
    for j in range(0,a):
        print(b[i][j], end=" ")
    print()
for i in range(0,a):
    dp+=b[i][i]
print('Suma elementelor de pe diagonala principala=', dp)
h=0
for i in b[::-1]:
    ds+=i[h]
    h+=1
print("Suma elementelor de pe diagonala secundara", ds)
for i in range(0,a):
    for j in range(0,a):
        if i<j:
            sds+=b[i][j]
        if i>j:
            jdp+=b[i][j]
print("Suma elementelor aflate mai jos de diagonala principala=", jdp)
print("Suma elementelor aflate mai sus de diagonnala principala=", sds)
for i in range(0,a):
     if(i+j)<(a-1):
         sds+=b[i][j]
     if (i+j)>(a-1):
        jds+=b[i][j]
print("Suma elementelor aflate mai jos de diagonala secundara=", jds)
print("Suma elementelor aflate mai sus de diagonala secundara=", sds) 
        
           