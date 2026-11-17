import pandas as pd
import random as r
import os

# === SEPARATORE ===
'moltip il char ► _______________________________________________'

def s(l=60, c="_", n=0):
    print(c * l) if not n else print(f"{c * l}\n")
    return c * l if not n else f"{c * l}\n"

# === TITOLO ===
'txt("parola") ► ◄===== PAROLA =====►'

def txt(t="", u=1):
    print(f"◄===== {t} =====►".upper()) if u else  print(f"◄===== {t} =====►")
    return f"◄===== {t} =====►".upper() if u else f"◄===== {t} =====►"

def tst(t):
    return f"{s()}\n{txt(t)}"


def p(*args, **kwargs):
    print(*args, **kwargs)