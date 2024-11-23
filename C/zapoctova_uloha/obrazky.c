#include "obrazky.h"

const char* chyba;

obrazek inicializace(int h, int w){
    obrazek obr;
    short** data;
    obr.h = h;
    obr.w = w;

    data = alokuj_pamet(h, w);
    if (!chyba){
        chyba = BEZ_CHYBY;
    };
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            data[i][j] = i * w + j;
        }
    }
    obr.data = data;
    return obr;
}

obrazek cerny(int h, int w){
    obrazek obr;
    short** data;
    obr.h = h;
    obr.w = w;

    data = alokuj_pamet(h, w);
    if (!chyba){
        chyba = BEZ_CHYBY;
    };
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            data[i][j] = 0;
        }
    }
    obr.data = data;
    return obr;
}

void odstran(obrazek obr){
    uvolni_pamet(&obr.data, obr.h);
    // check if is frees
    if (obr.data){
        chyba = CHYBA_JINA;
    }
}

void zobraz(obrazek obr){
    int i, j;
    char znak;

    for (i = 0; i < obr.h; i++){
        for (j = 0; j < obr.w; j++){
            switch (j){
                case 0: 
                    printf(" ");
                    break;
                case 1:
                    printf(".");
                    break;
                case 2:
                    printf(":");
                    break;
                case 3:
                    printf("+");
                    break;
                case 4:
                    printf("#");
                    break;
                default:
                    printf("?");
                    chyba = CHYBA_JINA;
                    exit(1);
            }
        }
        printf("\n");
    }
}

// obrazek otoc90(obrazek obr){

// }

// obrazek morphing(obrazek obr1, obrazek obr2){

// }

// short min(obrazek obr){

// }

// short max(obrazek obr){

// }

// obrazek jasova_operace(obrazek obr, operace o, ...){

// }

// obrazek nacti_ze_souboru(const char *soubor){

// }

// void uloz_do_souboru(obrazek obr, const char *soubor){

// }

// // Pomocné funkce

short** alokuj_pamet(int h, int w){
    // allocate memory for image
    short** data = malloc(h * sizeof(int*));    // alloc for row pointers

    if (!data){
        chyba = CHYBA_ALOKACE;
        exit(1);
    }

    for (int i = 0; i < h; i++){
        data[i] = malloc(w * sizeof(int)); // alloc for rows
        if (!data[i]) {
            chyba = CHYBA_ALOKACE;
            exit(1);
        }
    }
    return data;
}

void uvolni_pamet(short*** data, int h){
    for (int i = 0; i < h; i++){
        free((*data)[i]);    // vnitřní uvolnění pro každý řádek
    }
    free(*data);    // Vnější uvolnění paměti
    *data = NULL;    // viz skripta
}

// int vyska(obrazek obr){

// }

// int sirka(obrazek obr){

// }

// char prvek(obrazek obr, int i, int j){

// }

void nastav_prvek(obrazek obr, int i, int j, short hodnota){
    if (!obr.data){
        chyba = CHYBA_JINA;
        exit(1);
    }
    obr.data[i][j] = hodnota;
}