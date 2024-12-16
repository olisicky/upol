#include "obrazky.h"

int chyba;

// funkční prototypy (jen pro vyzkoušení ať jsou pomocné fce schované dole)
short** alokuj_pamet(int h, int w);
void uvolni_pamet(short** data, int h);
char prvek(obrazek obr, int i, int j);
int sirka(obrazek obr);
int vyska(obrazek obr);

obrazek inicializace(int h, int w){
    obrazek obr;
    short** data;
    obr.h = h;
    obr.w = w;

    data = alokuj_pamet(h, w);
    if (chyba != BEZ_CHYBY){
        return obr;    // Jestli alokace neprošla, tak nechci nikam vkládat
    };
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            data[i][j] = (j < 4) ? j : 4;
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
    if (chyba != BEZ_CHYBY){
        return obr;    // Jestli alokace neprošla, tak nechci nikam vkládat
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
    uvolni_pamet(obr.data, obr.h);

    if (obr.data[0]){
        chyba = CHYBA_JINA;
        return;
    }
    chyba = BEZ_CHYBY;
    return;
}

void zobraz(obrazek obr){
    int i, j;

    for (i = 0; i < obr.h; i++){
        for (j = 0; j < obr.w; j++){
            switch (prvek(obr, i, j)){
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
                    chyba = CHYBA_JINA;
                    return;
            }
        }
        printf("\n");
    }
    chyba = BEZ_CHYBY;
    return;
}

obrazek otoc90(obrazek obr){
    obrazek rotated;
    short** data;

    rotated.h = obr.w;
    rotated.w = obr.h;

    data = alokuj_pamet(rotated.h, rotated.w);

    if (chyba != BEZ_CHYBY){
        return obr;    // Jestli alokace neprošla, tak nechci nikam vkládat
    };
    for (int i = 0; i < obr.h; i++) {
        for (int j = 0; j < obr.w; j++) {
            data[obr.w - j - 1][i] = prvek(obr, i, j);
        }
    }

    rotated.data = data;
    return rotated;
}

obrazek morfing(obrazek obr1, obrazek obr2){
    obrazek morph;
    short** data;

    if ( (obr1.h != obr2.h) || (obr1.w != obr2.w)){
        chyba = CHYBA_TYPU;
        return morph;    // Tohle nevím, zda bylo tak myšleno, ale jinak bych dostal segmentation error
    }
    chyba = BEZ_CHYBY;

    morph.h = obr1.h;
    morph.w = obr1.w;
    data = alokuj_pamet(morph.h, morph.w);

    if (chyba != BEZ_CHYBY){
        return morph;    // Jestli alokace neprošla, tak nechci nikam vkládat
    };
    for (int i = 0; i < obr1.h; i++){
        for (int j = 0; j < obr1.w; j++){
            data[i][j] = (prvek(obr1, i, j) + prvek(obr2, i, j) + 1) / 2;
        }
    }
    morph.data = data;
    return morph;

}

short min(obrazek obr){
    short min = 4;

    for (int i = 0; i < obr.h; i++){
        for (int j = 0; j < obr.w; j++){
            if (obr.data[i][j] < min){
                min = prvek(obr, i, j);
            }
        }
    }
    chyba = BEZ_CHYBY;
    return min;
}

short max(obrazek obr){
    short max = 0;

    for (int i = 0; i < obr.h; i++){
        for (int j = 0; j < obr.w; j++){
            if (obr.data[i][j] > max){
                max = prvek(obr, i, j);
            }
        }
    }
    chyba = BEZ_CHYBY;
    return max;
}

obrazek jasova_operace(obrazek obr, operace o, ...){
    va_list parametry;
    va_start(parametry, o);
    obrazek novy;
    short** data;

    novy.h = obr.h;
    novy.w = obr.w;

    data = alokuj_pamet(novy.h, novy.w);
    if (chyba != BEZ_CHYBY){
        return obr;    // Jestli alokace neprošla, tak nechci nikam vkládat
    };
    switch(o){
        case 0:{
            for (int i = 0; i < novy.h; i++){
                for (int j = 0; j < novy.w; j++){
                    data[i][j] = 4 - prvek(obr, i, j);
                }
            };
            break;
        }
        case 1:{
            int k = va_arg(parametry, int);
            short new_val;
            for (int i = 0; i < novy.h; i++){
                for (int j = 0; j < novy.w; j++){
                    new_val = prvek(obr, i, j) + k;
                    if (k > 0){
                        data[i][j] = (new_val < 4) ? new_val : 4;
                    }
                    else{
                        data[i][j] = (new_val > 0) ? new_val : 0;
                    }
                }
            };
            break;
        }
        case 2:{
            double k1 = va_arg(parametry, double);
            int k2 = va_arg(parametry, int);
            float new_val;

            if (k1 < 0){
                chyba = CHYBA_JINA;
                return novy;
            }

            for (int i = 0; i < novy.h; i++){
                for (int j = 0; j < novy.w; j++){
                    new_val = k1 * prvek(obr, i, j) + k2;
                    if (k2 > 0){
                        data[i][j] = (new_val < 4) ? (int)(new_val + 0.5)  : 4;
                    }
                    else{
                        data[i][j] = (new_val > 0) ? (int)(new_val + 0.5)  : 0;
                    }
                }
            };
            break;
        }
    };
    novy.data = data;
    return novy;
}

obrazek nacti_ze_souboru(const char *soubor){
    FILE *f;
    obrazek ze_souboru;
    char line[MAXIMALNI_DELKA];
    short** temp_array = NULL;
    int row_count = 0;
    int col_count = 0;

    f = fopen(soubor, "r");
    if (f == NULL){
        chyba = CHYBA_OTEVRENI;
        return ze_souboru;
    }
    // for each line in a file extracts numberics and convert them into integer to form array
    while (fgets(line, sizeof(line), f)){
        short temp_row[MAXIMALNI_DELKA];
        int current_col = 0;
        int line_position = 0;
        
        while (line[line_position] != '\0' && line[line_position] != '\n'){
            // ignore spaces and increase position in current line
            while (line[line_position] == ' '){
                line_position++;
            }
            if (line[line_position] >= '0' && line[line_position] <= '9'){    // is numeric?
                // Convert consecutive numerics from ASCII into an integer 
                // (we work with 0-4 but this is for more general usage)
                short num = 0;
                while (line[line_position] >= '0' && line[line_position] <= '9'){
                    num = num * 10 + (line[line_position] - '0');    // shift by tenths
                    line_position++;
                }
                temp_row[current_col++] = num;
            }
            else{
                line_position++;
            }
        }
        // re-allocate memory according to the new known row (row pointers)
        temp_array = realloc(temp_array, (row_count + 1) * sizeof(short*));
        if (!temp_array){
            chyba = CHYBA_ALOKACE;
            return ze_souboru;
        }

        // in the new row allocate memory for columns
        temp_array[row_count] = malloc(current_col * sizeof(short*));
        if (!temp_array[row_count]){
            chyba = CHYBA_ALOKACE;
            return ze_souboru;
        }

        for (int i = 0; i < current_col; i++){
            temp_array[row_count][i] = temp_row[i];
        }
        row_count++;
        if (col_count < current_col){
            col_count = current_col;
        }
    }

    if (fclose(f) == EOF){
        chyba = CHYBA_ZAVRENI;
        return ze_souboru;
    }

    ze_souboru.h = row_count;
    ze_souboru.w = col_count;
    ze_souboru.data = temp_array;
    return ze_souboru;
}

void uloz_do_souboru(obrazek obr, const char *soubor){
    FILE *f;

    f = fopen(soubor, "w");
    if (f == NULL){
        chyba = CHYBA_OTEVRENI;
        return;
    }

    for (int i = 0; i < obr.h; i++){
        for (int j = 0; j < obr.w; j++){
            switch (prvek(obr, i, j)){
                case 0: 
                    fprintf(f, " ");
                    break;
                case 1:
                    fprintf(f, ".");
                    break;
                case 2:
                    fprintf(f, ":");
                    break;
                case 3:
                    fprintf(f, "+");
                    break;
                case 4:
                    fprintf(f, "#");
                    break;
                default:
                    chyba = CHYBA_JINA;
                    return;
            }
        }
        fprintf(f, "\n");
    }

    if (fclose(f) == EOF){
        chyba = CHYBA_ZAVRENI;
        return;
    }
    return;
}

// // Pomocné funkce

short** alokuj_pamet(int h, int w){
    // allocate memory for image
    short** data = malloc(h * sizeof(short*));    // alloc for row pointers

    if (!data){
        chyba = CHYBA_ALOKACE;
        return data;
    }

    for (int i = 0; i < h; i++){
        data[i] = malloc(w * sizeof(short*)); // alloc for rows
        if (!data[i]) {
            chyba = CHYBA_ALOKACE;
            return data;
        }
    }
    chyba = BEZ_CHYBY;
    return data;
}

// void uvolni_pamet(short*** data, int h){
//     for (int i = 0; i < h; i++){
//         free((*data)[i]);    // vnitřní uvolnění pro každý řádek
//         (*data)[i] = NULL;
//     }
//     free(*data);    // Vnější uvolnění paměti
//     *data = NULL;    // viz skripta
// }

void uvolni_pamet(short** data, int h){
    for (int i = 0; i < h; i++){
        free(data[i]);    // vnitřní uvolnění pro každý řádek
        data[i] = NULL;
    }
    free(data);    // Vnější uvolnění paměti
}


int vyska(obrazek obr){
    return obr.h;
}

int sirka(obrazek obr){
    return obr.w;
}

char prvek(obrazek obr, int i, int j){
    return obr.data[i][j];
}

void nastav_prvek(obrazek obr, int i, int j, short hodnota){
    if (!obr.data){
        chyba = CHYBA_JINA;
        return;
    }
    obr.data[i][j] = hodnota;
    return;
}