nume=input("cum te cheama?")
varsta=int(input("ce varsta ai?"))
inaltime=float(input("ce inaltime ai?"))
print("salut",nume)
print("ai ",varsta, "de ani")
print("ai ",inaltime,"m inaltime")

a=int(input("primul nr: "))
b=int(input("al doilea nr: "))
suma=a+b
diferenta=a-b
produs=a*b
impartire=a/b
print(suma)
print(diferenta)
print(produs)
print(impartire)

prenume=input("care este prenumele tau? ")
nume=input("care este numele tau? ")
nume_total=prenume+" "+nume
print("numele tau este:", nume_total)

# exercitii test
numar_zecimal=float(input("introduceti un numar zecimal: "))
print(numar_zecimal)
print(int(numar_zecimal))
print(str(numar_zecimal))

nume=(input("cum te cheama?"))
varsta=int(input("ce varsta ai?"))
noua_varsta=varsta+5
print("salut", nume, "peste 5 ani vei avea",varsta+5,"de ani!")

x=int(input("nr 1= "))
y=int(input("nr 2= "))
print(x+y)
print(x-y)
print(x*y)
print(x/y)

a,b,c=10,20,30
print(a,b,c)
x=a
a=c
c=b
b=x
print(a,b,c)

nume=input("cum te cheama? ")
varsta=int(input("ce varsta aveti? "))
salariu=float(input("ce salariu aveti pe luna? "))
print("salut ",nume,"aveti ",varsta,"de ani si aveti un salariu de",salariu,"de lei pe luna.")