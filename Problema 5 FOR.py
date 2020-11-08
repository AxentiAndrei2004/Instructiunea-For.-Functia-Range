n=eval(input('Introduceti numarul n= '))
s=0
for i in range (1,n+1):
    if (i%3==0) and (i%5==0):
        s+=i
print('suma numerelor de la 1 la {n}, care se imparte la 3 si la 5',s)