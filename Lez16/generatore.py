import csv
import random

def crea_file_sporco():
    righe = [
        ["id", "nome", "email", "eta", "spesa", "data"],
        ["1", "Mario", "mario@test.com", "25", "100.50", "2024-01-01"],
        ["2", "Luigi", "luigi@test.com", "abc", "50,00", "2024-01-02"], # eta errata, spesa con virgola
        ["3", "Peach", "peach@test.com", "-5", "200", "2024/01/03"], # eta negativa, data errata
        ["", "", "", "", "", ""], # riga vuota
        ["4", "Yoshi", "yoshi@test.com", "30", "0", "2024-01-04"], # spesa zero
        ["5", "Bowser", "bowser@test.com", "40", "999999", "2024-01-05"], # spesa enorme
        ["2", "Luigi", "luigi@test.com", "abc", "50,00", "2024-01-02"], # duplicato esatto
        ["6", "Toad", "", "35", "75.00", "2024-13-45"], # email vuota, data impossibile
        ["7", "Wario", "wario@test.com", "130", "120.00", "2024-01-07"] # eta impossibile
    ]
    
    with open("dati_sporchi.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(righe)
    
if __name__ == "__main__":
    crea_file_sporco()