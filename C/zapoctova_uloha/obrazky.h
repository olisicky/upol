#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>

#define BEZ_CHYBY "nedošlo k žádné chybě"
#define CHYBA_ALOKACE "chyba při alokaci paměti"
#define CHYBA_OTEVRENI "chyba při otevření souboru"
#define CHYBA_ZAVRENI "chyba při zavření souboru"
#define CHYBA_TYPU "nesprávně nadefinovaný obrázek"
#define CHYBA_JINA "něco je špatně"

typedef struct{
    int h;
    int w;
    short** data;
} obrazek;

typedef enum{
    NEGATIV, ZMENA_JASU, ZMENA_KONTRASTU
} operace;

// externs
extern const char* chyba;
extern obrazek inicializace(int h, int w);
extern obrazek cerny(int h, int w);
extern void odstran(obrazek obr);
extern void zobraz(obrazek obr);
// extern obrazek otoc90(obrazek obr);
// extern obrazek morphing(obrazek obr1, obrazek obr2);
// extern short min(obrazek obr);
// extern short max(obrazek obr);
// extern obrazek jasova_operace(obrazek obr, operace o, ...);
// extern obrazek nacti_ze_souboru(const char *soubor);
// extern void uloz_do_souboru(obrazek obr, const char *soubor);
extern void nastav_prvek(obrazek obr, int i, int j, short hodnota);
// extern char prvek(obrazek obr, int i, int j);
// extern int sirka(obrazek obr);
// extern int vyska(obrazek obr);

// helper prototypes
short** alokuj_pamet(int h, int w);
void uvolni_pamet(short*** data, int h);
