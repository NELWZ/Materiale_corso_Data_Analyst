fame = True
soldi = 8

if fame and soldi >= 7:
    print(f"ho €{soldi} mi compro una pizza")
    soldi -= 7
    print(f"mi sono rimasti €{int(soldi)}")

elif fame and soldi < 7:
    print("Ho fame ma non ho i soldi per la pizza")