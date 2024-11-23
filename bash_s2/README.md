## Příklad 1 - zápočet
Skript vypíše seznam složek a souborů aktuálního adresáře, případně adresáře, který mu je zadán jako argument. Skript přímá přepínač `-a`, čímž jsou zobrazeny také skrité soubory.

Skript vypisuje: `název` `typ` `práva`
```
/home/ondrejlisicky/personal directory (0755/drwxr-xr-x)
/home/ondrejlisicky/test directory (0755/drwxr-xr-x)
```

* v případě, kdy se jedná o symlink, tak je to zobrazeno v názvu a typu
 
Volání:

```bash
./pr_1.sh    # vypíše z aktuální složky bez skrytých souborů/složek
./pr_1.sh -a    # vypíše z aktuální složky se skrytými soubory/složkami
./pr_1.sh -a ~    # vypíše z domovské cesty i se skrytými soubory/složkami
```


## Příklad 2
Skript vytvoří soubory, do kterých jsou náhodně zapsány DD/MM/YYYY. Je řízen přes dva přepínaše `-a`, který vygeneruje soubory a `-b`, který přímá argument cesty k souborům, který poukládá soubory do podadresářů podle roku, měsíce a dne.

Příklad:

```bash
./pr_2.sh -a    # vygeneruj soubory do aktuálního adresáře
./pr_2.sh -b files    # poukládá soubory ze složky files (zde byly soubory nakopírovány ručně pro test) postupně do podakresářů

```