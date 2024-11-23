#include <stdio.h> 
#include "obrazky.h"

// Potřeba kompilovat oboje! gcc obrazky.c test.c -o test
int main(){
    obrazek a;
    a = cerny(3, 3);
    printf("%s\n", chyba);
    nastav_prvek(a, 0, 0, 1);
    zobraz(a);
    return 0;
}