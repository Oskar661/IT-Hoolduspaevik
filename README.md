# IT Hoolduspäevik (CLI)

**Autor:** Oskar Lavrits  
**Keel:** Python  
**Kuupäev:** 2026  

---

## Projekti eesmärk

See projekt on **IT hoolduspäevik**, kuhu saab kirja panna IT-töid ja hooldusi, näiteks:  

- Arvuti parandamine  
- Tarkvara paigaldus  
- Võrgu probleemide lahendamine  

Projekti eesmärk on aidata IT-spetsialistil või kasutajal **jälgida tehtud töid**, nende staatust ja ajalugu, lihtsalt **konsooli kaudu**.  

---

## Failistruktuur

```text
IT-hoolduspäevik/
│
├─ main.py                # Programmi käivitamine CLI
├─ cli.py                 # CLI menüü ja funktsioonid
├─ import_csv.py          # CSV import ja vigade logimine
├─ sample_import.csv      # Näidis CSV fail vigade testimiseks
├─ README.md              # Projektikirjeldus
├─ models/
│   ├─ log_book.py        # LogBook klass, salvestamine, laadimine, otsing
│   └─ log_entry.py       # LogEntry klass, valideerimine, dict-konversioon
└─ errors/
    └─ import_errors.log  # Automaatne vigade logifail CSV importimisel
```
kuupäev;pealkiri;kirjeldus;staatus
2026-02-06 14:03:12;Printeri hooldus;Vahetasin toonerit ja puhastasin printeri;DONE
2026-02-06 14:06:30; ;Puudub pealkiri;OPEN


Kuidas käivitada - python main.py

1. Lisa kirje
2. Kustuta kirje
3. Muuda staatust
4. Otsi kirjeid
5. Filtreeri staatuse järgi
6. Näita kõiki kirjeid
7. Import CSV failist
0. Välju






**_Täiendatud omadused ja muudatused_**




CSV import vigade tuvastamine ja eraldi logimine.

Automaatne errors kausta loomine.

Kirjete pikkuse ja vigaste väljade kontroll (pealkiri ≥4, kirjeldus ≥10, staatus OPEN/DONE).

Pikemate kirjelduste lühendamine ekraanil kolme punktiga (...).

CLI küsib ENTER peale iga tegevuse lõpetamist, et kasutajal oleks aega infot lugeda.

Kasutamine GitHubis

Projekti struktuur peab olema selge.

Commitid peaksid näitama tööprotsessi, mitte ainult lõppversiooni.

README.md selgitab projekti eesmärki, struktuuri ja kasutamist.

Kõik tekstid kasutajaliideses on eesti keeles.

Kood (klassid, funktsioonid) on inglise keeles.