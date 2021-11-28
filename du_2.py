import csv

# otevírání souboru pro týdny
with open("priklad_vstupu.csv", encoding="utf-8") as csvfile,\
    open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csv_outfile_tyden:
    reader = csv.reader(csvfile, delimiter=",")
    writer = csv.writer(csv_outfile_tyden)

    # inicializace proměnných
    prumer_tyden = 0
    suma_prutoku_tyden = 0
    radky = 1
    prutok = 0
    chyba = 0
    max = 0
    min = 999999
    tydenni = []

    # procházení souboru cyklem
    for row in reader:
        # když se nacházím v prvním dnu týdne
        if (radky == 1):
            tydenni = row

        # načtení průtoku daného dne a přičítání do proměnné suma_prutoku_tyden
        try:
            prutok = float(row[5])
            suma_prutoku_tyden += prutok

            if prutok > max:
                max = prutok
            if prutok < min:
                min = prutok
        # když nastane špatný vtup započítá ho do proměnné chyba a vytiskne do konzole informaci o chybě
        except ValueError:
            chyba += 1  
            print(f"Pro den {row[4]}. {row[3]}. {row[2]} není možné započítat průtok")

        # když přijde sedmý den (řádek), sečtené průtoky se zprůměrují
        if radky == 7: 
            # pokud je aspoň jeden platný průtok
            if radky != chyba:
                prumer_tyden = suma_prutoku_tyden/(7-chyba)
                tydenni[5] = f"    {prumer_tyden:.4f}"
                print(f"{prumer_tyden:.4f}")
            else:
                print("Daný týden nemá validní data")
                tydenni[5] = "    Pro daný týden nemá validní data"

            writer.writerow(tydenni)

            # vynulování prměnných na další nový týden
            suma_prutoku_tyden = 0        
            prumer_tyden = 0              
            radky = 0
            chyba = 0

        # řeší případy, kdy se vyskytne chyba na prvním řádku nového týdne
        # vytiskne průměr zbylých sečtených průtoků -> tzn. řádky, které už nedojdou do konce týdne
        # kdyby byl elif pryč, do průměru se mi načte chyba, kdyby se následující 2 řádky přesunuly do ifu na konci,
        # číslo neodpovídá průměru hodnot
        elif radky != chyba: 
            
            prumer_tyden = suma_prutoku_tyden/(radky - chyba)
            tydenni[5] = f"    {prumer_tyden:.4f}"

        radky += 1

    # průměr na konci souboru v případě, kdy poslední týden nebude mít záznam ze všech dní 
    if radky < 8:
        print(f"{prumer_tyden:.4f}")
        writer.writerow(tydenni)

# otevírání souboru pro roky
with open("priklad_vstupu_rok.csv", encoding="utf-8") as csvfile,\
     open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csv_outRok:
    reader = csv.reader(csvfile, delimiter=",")
    writer = csv.writer(csv_outRok)

    # inicializace proměnných
    prumer_rok = 0
    chyba = 0
    suma_prutok_rok = 0
    radky_rok = 1
    rok = 0

    # procházení cyklu souborem
    for row in reader:
        # načtení průtoku daného dne a přičítání do proměnné suma_prutok_rok
        try:
            prutok = float(row[5])
            suma_prutok_rok = suma_prutok_rok + prutok
        # když nastane špatný vtup vytiskne informaci, na kterém řádku nastala chyba
        except ValueError:
            print(f"Pro den {row[4]}. {row[3]}. {row[2]} není možné započítat průtok")
            # pokud proměnná rok neodpovídá třetímu sloupci (rok) v aktuálním řádku
            # chyba se nastaví na 1
            if rok != int(row[2]):
                chyba = 1          # pokrývá jen možnost, kdy se rok = 0
                # pokud nastane nový rok
                if rok != 0:
                    prumer_rok = suma_prutok_rok/(radky_rok-chyba)
                    print(prumer_rok)
                    prvni_den[5] = f"   {prumer_rok:.4f}"
                    writer.writerow(prvni_den)

                    rok = int(row[2]) # nese informaci o aktuálním roku v řádku v cyklu
                    print(f"Rok {rok}")
                    radky_rok = 1
                    continue
            # pokud se vyskytne chyba během načítání průtoků v rámci jednoho roku
            else:  
                chyba += 1
        # pokud rok neodpovídá  třetímu sloupci v aktuálním řádku
        if rok != int(row[2]):
            # nastává nový rok 
            if rok != 0:
                print(prumer_rok)
                prumer_rok = suma_prutok_rok/(radky_rok-chyba)
                prvni_den[5] = f"   {prumer_rok:.4f}"
                writer.writerow(prvni_den)
                radky_rok = 1
                suma_prutok_rok = float(row[5])

            rok = int(row[2])
            print(f"Rok {rok}")

        # když se nacházím v prvním dnu nového roku
        if radky_rok == 1:
            prvni_den = row
            
        radky_rok += 1

    # tisk pro poslední rok v souboru
    prumer_rok = suma_prutok_rok/(radky_rok-chyba)
    print(prumer_rok)
    prvni_den[5] = f"   {prumer_rok:.4f}"
    writer.writerow(prvni_den)

    print(f"Minimální průtok řeky je {min} a maximální průtok řeky je {max}.")
