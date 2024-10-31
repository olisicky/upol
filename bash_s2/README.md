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
