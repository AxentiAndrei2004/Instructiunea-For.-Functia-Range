a=int(input('Introduceti numarul a='))
b=int(input('introduceti numarul b='))
b=b+1
for i in range(a,b,2):
     if(i%2!=0):
          print(i,end=' ')