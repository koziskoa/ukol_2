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
        