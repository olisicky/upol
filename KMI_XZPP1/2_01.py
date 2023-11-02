a = float(input('Zadej kvadratický koeficient a: '))
b = float(input('Zadej lineární koeficient b: '))
c = float(input('Zadej konstantu c: '))

diskriminant = b**2 - 4*a*c

x1 = (-b + diskriminant**(1/2)) / (2 * a)
x2 = (-b - diskriminant**(1/2)) / (2 * a)

if diskriminant > 0:
    print(f'Rovnice má dva reálné kořeny {x1} a {x2}')

elif diskriminant == 0:
    print(f'Rovnice má dva stejné reálné kořeny {x1}')

else:
    print(f'Rovnice má řešení v oboru komplexních čísel s kořeny {x1} a {x2}.')

