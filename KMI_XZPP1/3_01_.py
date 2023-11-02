cislo = int(input('Zadej přirozené číslo: '))

compute = True
next = True
candidate = 2

je_prvocislo = True
test_number = 2    # lower bound

while compute:
    while je_prvocislo == True and next:
        
        neco = True
        while neco:
            if candidate % test_number == 0:
                je_prvocislo = False
                candidate += 1
            else:
                je_prvocislo = True
                aktualni_prvocislo = test_number
                neco = 0
        next = 0

    if (cislo % aktualni_prvocislo == 0) and (cislo / aktualni_prvocislo != 1.0):
        cislo = cislo / aktualni_prvocislo
        print(aktualni_prvocislo, end=" ")
    
    elif cislo / aktualni_prvocislo == 1.0:
        compute = 0
        print(aktualni_prvocislo)
    
    else:
        test_number += 1
        next = 1


