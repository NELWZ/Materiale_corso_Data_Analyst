from chat_semplice import get_api
from groq import Groq

client = Groq(api_key=get_api())
DEFAULT_PROMPT_FILE = "C:/Users/avare/Desktop/A/addestrAICLD.txt"
model = "openai/gpt-oss-120b"
temperature = 0.5
max_tokens = 1024

def leggi_prompt(percorso=DEFAULT_PROMPT_FILE):
    try:
        with open(percorso, "r", encoding="utf-8") as file:
            return file.read()
    except OSError as errore:
        print(f"Impossibile leggere il file del prompt: {errore}")
        return ""

system_prompt = leggi_prompt()
termina = "esci"
print(f'Scrivi "{termina}" per fermare la chat')

def opzioni():
    global model, temperature, max_tokens, system_prompt
    while True:
        scelta = input("1-model\n2-temperature\n3-max_tokens\n4-ad\n5-Salva\n: ")
        if scelta == "1":
            model = input("Inserisci il modello: ").strip() or model
        elif scelta == "2":
            try:
                valore = float(input("Inserisci la temperatura (0.0-1.0): "))
                if 0.0 <= valore <= 1.0:
                    temperature = valore
                else:
                    print("Valore non valido")
            except ValueError:
                print("Inserisci un numero valido")
        elif scelta == "3":
            try:
                valore = int(input("Inserisci i Token Massimi: "))
                if 1 <= valore <= 4500:
                    max_tokens = valore
                else:
                    print("Valore non valido")
            except ValueError:
                print("Inserisci un numero intero valido")
        elif scelta == "4":
            tipo = input("1-carica file\n2-scrivi in breve\n: ")
            if tipo == "1":
                percorso = input("Nome o percorso file: ")
                system_prompt = leggi_prompt(percorso)
            elif tipo == "2":
                system_prompt = input("Scrivi le istruzioni: ")
        elif scelta == "5":
            return
        else:
            print("Scelta non valida")

def run_chat():
    messages = [{"role": "system", "content": system_prompt}]
    while True:
        user_input = input("Tu: ")
        if user_input.strip().lower() == termina:
            break
        messages.append({"role": "user", "content": user_input})
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            assistant_reply = completion.choices[0].message.content
        except Exception as e:
            print(f"Errore: {e}")
            messages.pop()
            continue
        messages.append({"role": "assistant", "content": assistant_reply})
        print(f"Bot: {assistant_reply}")

def main():
    while True:
        print("1-chat\n2-opzioni\n3-esci")
        scelta = input(": ")
        if scelta == "1":
            run_chat()
        elif scelta == "2":
            opzioni()
        elif scelta == "3":
            break
        else:
            print("Scelta non valida")

if __name__ == "__main__":
    main()