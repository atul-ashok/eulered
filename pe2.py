#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
'''
a=1
b=2
total=a+b
f_total=2
while True:
    print ("total= ", total)
    b=total
    total=total+b
    print(total)
    print ("a= ", a, "b= ",b)
    if total%2==0:
        f_total+=total
        print(f_total)
    if total==89:
        break
print (a, b, total, f_total)
'''
f_seq=[]
final=0
a,b=1,2
print (a,b)
f_seq.append(a)
f_seq.append(b)
while True:
    if b%2==0:
        final+=b
    a,b=b,a+b
    if b<4000000:
        f_seq.append(b)
        print (b)
    else:
        print(f_seq)
        print(final)
        break

