# ================================= #
# variabile chiamata "num1" con un valore numerico int
num1 = 1
# variabile chiamata "num2" con un valore numerico int
num2 = 1
# variabile chiamata "num3" con un valore numerico int
num3 = 1

x = num2 > num1 and num2 > num3
print(x)

# SE la variabile "num1" è maggiore della variabile "num2" AND variabile "num1" è maggiore della variabile "num3"
if (num1 > num2) and (num1 > num3):
    print(f"numero più grande è {num1}")
    
# ALTRIMENTI SE la variabile "num2" è maggiore della variabile num1 AND la variabile "num2" è maggiore della variabile "num3"
elif x:print(f"numero più grande è {num2}")

# ALTRIMENTI SE la variabile "num3" è maggiore della variabile "num1 AND la variabile "num3" è maggiore della variabile "num2"
elif num3 > num1 and num3 > num2:
        print(f"numero più grande è {num3}")

# ALTRIMENTI
else: #elif num1 == num2 == num3:
    print("Tutti i numeri sono uguali")

