import csv
with open("QD_200550_Data.csv", encoding="utf-8") as csvfile,\
     open ("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csv_outfile_tyden:
    reader = csv.reader(csvfile, delimiter =",") 
    writer = csv.writer(csv_outfile_tyden)
    
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
            chyba += 1  # když nastane špatný vtup započítá ho do proměnné chyba a vytiskne do konzole informaci o chybě
            print(f"Pro den {row[4]}. {row[3]}. {row[2]} není možné započítat průtok")
        if lines %7==0:  # když přijde sedmý den (řádek), sečtené průtoky se zprůměrují 
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

with open("QD_200550_Data.csv", encoding="utf-8") as csvfile,\
     open ("vystup_rok.csv", "w", newline="", encoding="utf-8") as csv_outRok:
    reader = csv.reader(csvfile, delimiter =",") 
    writer = csv.writer(csv_outRok)     

    chyba = 0
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
            if rok != int(row[2]):
                chyba = 1
                if rok != 0:
                    #sem narvat vše pro nový rok
                    prumer = suma_prutok_rok/(lines-chyba)
                    print(prumer)
                    prvni_den[5] = f"   {prumer:.4f}" 
                    writer.writerow(prvni_den)
                    rok = int(row[2])   # nese informaci o aktuálním roku v řádku v cyklu
                    print(f"Nový rok {rok}")
                    lines = 1
                    print(lines)
                    continue
            else: #rok == int(row[2]):
                chyba += 1
            
        if rok == int(row[2]): # takže tenhle if vůbec nepotřebuju?
            print(lines)
            #prumer = suma_prutok_rok/(lines-chyba)
            #print(prumer)        
        if rok != int(row[2]):                
            if rok == 0:
                rok = int(row[2])   # nese informaci o aktuálním roku v řádku v cyklu
                print(f"Rok {rok}")
                print(lines)
            else:
                print(prumer)
                prumer = suma_prutok_rok/(lines-chyba)
                prvni_den[5] = f"   {prumer:.4f}" 
                writer.writerow(prvni_den)
                rok = int(row[2])   # nese informaci o aktuálním roku v řádku v cyklu
                print(f"Rok {rok}")
                lines = 1
                print(lines)
                suma_prutok_rok = float(row[5])
                
        if lines == 1:
            prvni_den = row
        lines += 1
    prumer = suma_prutok_rok/(lines-chyba)
    print(prumer)
    prvni_den[5] = f"   {prumer:.4f}" 
    writer.writerow(prvni_den)