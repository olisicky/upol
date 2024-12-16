#include <stdio.h>
#include "obrazky.h"

int main (){
    obrazek obr1 , obr2 , obr3, obr4, obr5, obr6, obr7;

    obr1 = cerny(3 ,3);

    nastav_prvek(obr1, 0, 0, 0);
    nastav_prvek(obr1, 0, 1, 1);
    nastav_prvek(obr1, 0, 2, 2);
    nastav_prvek(obr1, 1, 0, 1);
    nastav_prvek(obr1, 1, 1, 2);
    nastav_prvek(obr1, 1, 2, 3);
    nastav_prvek(obr1, 2, 0, 2);
    nastav_prvek(obr1, 2, 1, 3);
    nastav_prvek(obr1, 2, 2, 4);

    printf("Obrazek obr1: \n");
    zobraz(obr1);
    printf("\n\n");

    obr2 = otoc90(obr1);
    printf("Otoceny obrazek obr1: \n");
    zobraz(obr2);
    printf("\n\n");

    printf("Minimalni intenzita obr2: %i \n", min(obr2));
    printf("Maximalni intenzita obr2: %i \n\n", max(obr2));

    obr3 = morfing(obr1, obr2);
    printf("Morfing obrazku obr1 + obr2: \n");
    switch(chyba){
        case CHYBA_TYPU:
            printf("Morfing nelze provest s ruzne velkymi obrazky.");
            break;
        case CHYBA_ALOKACE:
            printf("Nastala chyba alokace pameti.");
            break;
        case BEZ_CHYBY:
            zobraz(obr3);
            break;
    }
    printf("\n\n");
    obr4 = cerny(10 ,5);
    obr5 = morfing(obr1, obr5);

    switch(chyba){
        case CHYBA_TYPU:
            printf("Morfing nelze provest s ruzne velkymi obrazky.");
            break;
        case CHYBA_ALOKACE:
            printf("Nastala chyba alokace pameti.");
            break;
        case BEZ_CHYBY:
            zobraz(obr3);
            break;
    }
    printf("\n\n");

    obr5 = jasova_operace(obr1, NEGATIV);
    printf("Negativ obrazku obr1: \n");
    switch(chyba){
        case CHYBA_TYPU:
            printf("Chyba typu");
            break;
        case CHYBA_ALOKACE:
            printf("Nastala chyba alokace pameti.");
            break;
        case BEZ_CHYBY:
            zobraz(obr5);
            break;
    }
    printf("\n\n");

    obr6 = jasova_operace(obr1, ZMENA_KONTRASTU, 0.5, 1);
    printf("Zmena kontrastu obrazku obr1: \n");
    switch(chyba){
        case CHYBA_TYPU:
            printf("Chyba typu");
            break;
        case CHYBA_ALOKACE:
            printf("Nastala chyba alokace pameti.");
            break;
        case BEZ_CHYBY:
            zobraz(obr6);
            break;
    }
    printf("\n\n");

    printf("Nacteni ze souboru \n");
    obr7 = nacti_ze_souboru("soubor.txt");
    switch(chyba){
        case CHYBA_TYPU:
            printf("Chyba typu");
            break;
        case CHYBA_ALOKACE:
            printf("Nastala chyba alokace pameti.");
            break;
        case BEZ_CHYBY:
            zobraz(obr7);
            break;
    }
    printf("Ulozeni do souboru \n");
    uloz_do_souboru(obr1, "soubor_uloz.txt");
    switch(chyba){
        case CHYBA_TYPU:
            printf("Chyba typu");
            break;
        case CHYBA_ALOKACE:
            printf("Nastala chyba alokace pameti.");
            break;
        case BEZ_CHYBY:
            printf("Soubor uložen bez chyby");
            break;
    }

    printf("\n\n");
    odstran(obr1);
    switch(chyba){
        case CHYBA_TYPU:
            printf("Chyba typu");
            break;
        case CHYBA_ALOKACE:
            printf("Nastala chyba alokace pameti.");
            break;
        case CHYBA_JINA:
            printf("Jiná chyba");
            break;   
        case BEZ_CHYBY:
            printf("Obrázek byl smazán.");
            break;
    }
    return 0;
}