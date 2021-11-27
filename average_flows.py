import csv
with open("priklad_vstupu.csv", encoding="utf-8") as csvfile,\
     open ("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csv_outfile:
    reader = csv.reader(csvfile, delimiter =",") 
    writer = csv.writer(csv_outfile)
    
    prumer = 0
    suma_prutoku = 0
    lines = 1
    prutok = 0
    chyba = 0
    tydenni = []

    for row in reader:
        if (lines == 1):
            tydenni = row
        print(lines)
        try:
            prutok = float(row[5])
            suma_prutoku += prutok
        except ValueError:
            chyba += 1  # když nastane špatný vtup započítá ho do proměnné chyba
                  
        if lines %7==0:  # když přijde sedmý den (řádek), sečtené průtoky se zprůměrují 
            #print(suma_prutoku)
            if lines != chyba:
                prumer = suma_prutoku/(7-chyba)
                tydenni[5] = f"    {prumer:.4f}"
                print(f"{prumer:.4f}")
                writer.writerow(tydenni)                
            else:
                print("Daný týden nemá validní data") 
                tydenni[5]= "    Pro daný týden nemá validní data"
                writer.writerow(tydenni)

            suma_prutoku = 0        # pak se všechny proměnné vynulují, 
            prumer = 0              # aby začaly počítat znovu od dalšího týdne
            lines = 0
            chyba = 0
        
        elif lines != chyba: 
            prumer = suma_prutoku/(lines - chyba) #vytiskne průměr zbylých sečtených průtoků -> 
                                                   #tzn. řádky, které už nedojdou do konce týdne
            tydenni[5]=f"    {prumer:.4f}"
        lines += 1
    if lines < 8:
        print(f"{prumer:.4f}")
        writer.writerow(tydenni)

with open("vstup_6dni.csv", encoding="utf-8") as csvfile,\
     open ("vystup_rok.csv", "w", newline="", encoding="utf-8") as csv_outRok:
    reader = csv.reader(csvfile, delimiter =",") 
    writer = csv.writer(csv_outRok)     

    suma_prutok_rok = 0
    lines = 1
    rocni = []
    rok = 0 
    for row in reader:
        rocni = row         # nese informaci o celém aktuálním řádku v cyklu
        try:
            prutok = float(row[5])
            suma_prutok_rok = suma_prutok_rok + prutok
        except ValueError:
            pass
        if rok == int(row[2]):
            print(lines)
            prumer = suma_prutok_rok/lines
            #print(prumer)        
        if rok != int(row[2]):                
            if rok == 0:
                rok = int(row[2])   # nese informaci o aktuálním roku v řádku v cyklu
                print(f"Nový rok {rok}")
                print(lines)
            else:
                print(prumer)
                prvni_den[5] = f"   {prumer:.4f}" 
                writer.writerow(prvni_den)
                rok = int(row[2])   # nese informaci o aktuálním roku v řádku v cyklu
                print(f"Nový rok {rok}")
                lines = 1
                print(lines)
                suma_prutok_rok = float(row[5])
        if lines == 1:
            prvni_den = row
        lines += 1
    print(prumer)
    prvni_den[5] = f"   {prumer:.4f}" 
    writer.writerow(prvni_den)