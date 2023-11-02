cislo = int(input('Zadej přirozené číslo: '))

prvocisla = [2, 3, 5, 7, 11, 13, 17, 19]

index = 0
pocitej = 1
next = 1

upper_bound=100    # set limit for primary number search
je_prvocislo = True
test_number = 2    # lower bound

while pocitej:

    while test_number < upper_bound and je_prvocislo == True and next:
        for n in range(2, upper_bound):
            if n % test_number == 0:
                je_prvocislo = False
            else:
                je_prvocislo = True
                aktualni_prvocislo = test_number
                break
        next = 0

    if (cislo % aktualni_prvocislo == 0) and (cislo / aktualni_prvocislo != 1.0):
        cislo = cislo / aktualni_prvocislo
        print(aktualni_prvocislo, end=" ")
    elif cislo / aktualni_prvocislo == 1.0:
        pocitej = 0
        print(aktualni_prvocislo)
    else:
        test_number += 1
        next = 1


