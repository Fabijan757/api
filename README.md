[README_API.txt](https://github.com/user-attachments/files/23563835/README_API.txt)
Analiza TV serija – projekt (API + MySQL + Tableau)

Ovaj projekt prikazuje kompletan proces obrade i analize podataka o TV serijama korištenjem API-ja, MySQL baze podataka i Tableau vizualizacija. Cilj je bio automatski preuzeti podatke o najpopularnijim i najlošije ocijenjenim serijama, pohraniti ih u relacijsku bazu, obraditi SQL upitima te vizualizirati rezultate kroz interaktivni dashboard.

1. Preuzimanje podataka (API)
Podaci o serijama preuzeti su putem javnog API-ja (bez API ključa).
Prikupljeni podaci uključivali su:
- naziv serije
- ocjenu (rating)
- žanrove
- jezik serije

API je korišten u Python skripti i spremljen u CSV datoteke:
- najbolje_ocijenjeno.csv
- najgore_ocijenjeno.csv

2. Uvoz podataka u MySQL
Podaci su učitani u MySQL u tablicu 'tv_shows' s kolonama:
- id
- name
- rating
- genres
- language

3. SQL analize
Napravljene analize uključuju:
- prosječna ocjena po žanru
- broj serija po žanru
- sortiranje najboljih i najgorih serija
- filtriranje serija po žanru

4. Vizualizacije (Tableau Dashboard)
Izrađena su tri grafikona:
- Najgore ocijenjene serije
- Najbolje ocijenjene serije
- Analiza broja i prosječne ocjene žanrova

5. Rezultat
Projekt prikazuje cijeli Data Engineering proces:
API → CSV → MySQL → SQL analize → Tableau Dashboard
