import csv
import math
with open("priklad_vstupu.csv", encoding="utf-8") as csvfile,\
     open ("vystup_7dni.csv", encoding="utf-8") as csv_outfile:
    reader = csv.reader(csvfile, delimiter =",") 
    writer = csv.writer(csv_outfile, delimiter = ",")
    
    prumer = 0
    suma_prutoku = 0
    celkem = 0
    lines = 1
    prutok = 0

    for row in reader:
        #lines += int(len(list(row))/6)
        print(lines)
        try:
            prutok = float(row[5])
        except ValueError:
            prutok = 0
        if lines %7!=0:  # tady to načítá a tiskne průtoky
            suma_prutoku += prutok
        if lines %7==0:
            print(suma_prutoku)
            suma_prutoku += prutok
            prumer = suma_prutoku/7
            print(f"{prumer:.4f}")
            suma_prutoku = 0
            prumer = 0
        else:
            print(suma_prutoku/(lines%7))
        lines += 1