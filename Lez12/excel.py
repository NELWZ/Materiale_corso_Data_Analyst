# WINDOWS
# pip install openpyxl
# python -m pip install openpyxl

# MAC & LINUX
# pip3 install openpyxl
# python3 -m pip install openpyxl

# === WORKBOOK === #
from openpyxl import Workbook

# Crea un file Excel VIRTUALE (in memoria)
wb = Workbook()

# Prendi il foglio attivo 
foglio = wb.active

# Rinomina il foglio
foglio.title = "Vendite"

# Scrivi in una cella
foglio['A1'] = "Categoria"
foglio['B1'] = "Fatturato"

foglio.append(['Elettronica', 15000])
foglio.append(['Casa', 8500])
foglio.append(['Sport', 4200])

# Salva
wb.save("vendite.xlsx")











