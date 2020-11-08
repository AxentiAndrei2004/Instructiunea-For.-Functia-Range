#6.1
s1=0
n=eval(input('Introduceti numarul n='))
for i in range (1,n+1):
    s1+=i
print('suma este', s1)

#6.2
s2=0
n=eval(input('Introduceti numarul n='))
for i in range (2,n+1):
    s2=(i-1)*i
print('Suma numerelor este',s2)

#6.3
s3=0
n=eval(input('Introduceti numarul n='))
p=1
for t in range (1,n+1):
    p=p*t
    s3=s3+p
    print('Suma este',s3)

#6.4
s4=0
n=eval(input('Introducetu numarul n='))
for i in range (12,n*10+3,10):
    s4+=i
print('Suma numerelor este',s4)