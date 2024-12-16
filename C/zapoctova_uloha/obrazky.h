#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>

#define BEZ_CHYBY 0
#define CHYBA_ALOKACE 1
#define CHYBA_OTEVRENI 2
#define CHYBA_ZAVRENI 3
#define CHYBA_TYPU 4
#define CHYBA_JINA 5
#define MAXIMALNI_DELKA 1024
#define MAXIMALNI_VYSKA 1024

//extern const char* chyba;
// #define BEZ_CHYBY "nedošlo k žádné chybě"
// #define CHYBA_ALOKACE "chyba při alokaci paměti"
// #define CHYBA_OTEVRENI "chyba při otevření souboru"
// #define CHYBA_ZAVRENI "chyba při zavření souboru"
// #define CHYBA_TYPU "nesprávně nadefinovaný obrázek"
// #define CHYBA_JINA "něco je špatně"

typedef struct{
    int h;
    int w;
    short** data;
} obrazek;

typedef enum{
    NEGATIV, ZMENA_JASU, ZMENA_KONTRASTU
} operace;

// externs
extern int chyba;
extern obrazek inicializace(int h, int w);
extern obrazek cerny(int h, int w);
extern void odstran(obrazek obr);
extern void zobraz(obrazek obr);
extern obrazek otoc90(obrazek obr);
extern obrazek morfing(obrazek obr1, obrazek obr2);
extern short min(obrazek obr);
extern short max(obrazek obr);
extern obrazek jasova_operace(obrazek obr, operace o, ...);
extern obrazek nacti_ze_souboru(const char *soubor);
extern void uloz_do_souboru(obrazek obr, const char *soubor);
extern void nastav_prvek(obrazek obr, int i, int j, short hodnota);
