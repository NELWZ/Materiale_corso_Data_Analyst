from chat_manager import avvia_chat_semplice, analizza_csv_con_ai, chiedi_pulizia_csv
def s():
    print('_' * 60)

def main():
    while True:
        s()
        print('1-Chat\n2-Analizza CSV\n3-Pulizia CSV\n4-Esci')
        scelta = input("► ").strip()
        while scelta not in ['1','2','3','4']:
            print("SCELTA NON VALIDA")
            print('1-Chat\n2-Analizza CSV\n3-Pulizia CSV\n4-Esci')
            scelta = input("► ").strip()
            s()
        if scelta == '1':
            avvia_chat_semplice()
        elif scelta == '2':
            percorso = input("Nome o percorso file: ")
            analizza_csv_con_ai(percorso)
        elif scelta == '3':
            percorso = input("Nome o percorso file: ")
            chiedi_pulizia_csv(percorso)
        else:
            break

if __name__ == '__main__':
    main()

