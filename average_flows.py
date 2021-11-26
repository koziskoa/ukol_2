import csv
import math
with open("priklad_vstupu.csv", encoding="utf-8") as csvfile,\
     open ("vystup_7dni.csv", encoding="utf-8") as csv_outfile:
    reader = csv.reader(csvfile, delimiter =",") 
    writer = csv.writer(csv_outfile, delimiter = ",")
    
    prumer = 0
    suma_prutoku = 0
    lines = 1
    prutok = 0
    chyba = 0

    for row in reader:
        #lines += int(len(list(row))/6)
        print(lines)
        try:
            prutok = float(row[5])
            suma_prutoku += prutok
        except ValueError:
            chyba += 1  # když nastane špatný vtup započítá ho do proměnné chyba
            pass        # a pokračuje dál
                  
        if lines %7==0:  # když přijde sedmý den (řádek), sečtené průtoky se zprůměrují 
            #print(suma_prutoku)
            prumer = suma_prutoku/(7-chyba)
            print(f"{prumer:.4f}")
            suma_prutoku = 0        # pak se všechny proměnné vynulují, 
            prumer = 0              # aby začaly počítat znovu od dalšího týdne
            lines = 0
            chyba = 0
        elif lines == chyba:  # řeší případy, kdy se bude počst řádků rovnat počtu chyb
            print (f"Řádek {row} není validní, přeskakuji")
            pass
        else: 
            prumer = suma_prutoku/(lines - chyba) #vytiskne průměr zbylých sečtených průtoků -> 
                                                   #tzn. řádky, které už nedojdou do konce týdne
        lines += 1
    if lines < 8:
        print(f"{prumer:.4f}")

    #writer.writerow(row)