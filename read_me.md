<p>Program počítá průměr sedmidenních (týdenních) a ročních průtoků.</p>
Zajišťuje případné chyby v průtocích a informuje o tom uživatele v konzoli.

Příkladem vstupu pro správné fuungování programu mohou být data, která zaznamenává ČHMÚ:

https://www.chmi.cz/historicka-data/hydrologie/denni_data/denni-data-dle-z.-123-1998-Sb# 
    
Výstupem programu jsou 2 CSV soubory.
    První soubor **vystup_7dni.csv** vypisuje průměr sedmidenních průtoků.
        Řádek nese informaci o datu prvního dne (rok, měsíc a den), pro který se začíná počítat týdenní průměr.
    Druhý soubor **vystup_rok.csv** vypisuje  průměr ročních průtoků.
        Řádek nese informaci o prvním dnu v roce, pro který se počítá roční průměr.