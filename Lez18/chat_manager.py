from groq_client import client
from config import MODEL

def chatta(messaggi):
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=messaggi,
            temperature=0.7,
            max_completion_tokens=2048,
            stream=False,
        )
        return completion.choices[0].message.content
    except Exception as e: print(f"Errore: {e}")
    
def avvia_chat_semplice():
    messaggi = [{'role': 'system', 'content': 'Sei un assistente utile e coiciso. Rispondi in Italiano.'}]
    while True:
        testo = input("Tu: ").strip()
        if testo == "ferma_chat": break
        if not testo: continue
        messaggi.append({'role': 'user', 'content': testo})
        risposta = chatta(messaggi)
        print(f"AI: {risposta}")
        messaggi.append({'role': 'assistant', 'content': risposta})

def analizza_csv_con_ai(percoso):
    from csv_analyzer import leggi_csv, prepara_contesto_per_ai
    
    df = leggi_csv(percoso)
    if df is None: return 
    contesto = prepara_contesto_per_ai(df, percoso)
    print("Contesto estratto. Invio all'AI...")
    
    messaggi = [
        {'role': 'system', 'content': 'Sei un assistente utile e coiciso. Rispondi in Italiano.'},
        {'role': 'user', 'content': f'Analizza questo Dataframe e dimmi cosa vedi. Evidenzia problemi, pattern interessanti e possibili analisi da fare.\n\n{contesto}'},
    ]
    risposta = chatta(messaggi)
    print("=== ANALISI AI ===")
    print(risposta)
    

def chiedi_pulizia_csv(percorso):
    from csv_analyzer import leggi_csv, chiedi_pulizia_a_ai
    
    df = leggi_csv(percorso)
    if df is None: return
    
    prompt = chiedi_pulizia_a_ai(df)
    messaggi = [
        {'role': 'system','content': 'Sei un data engineer esperto di pandas. Fornisci codice concreto e spiegazioni  brevi.'},
        {'role': 'user', 'content': prompt},
    ]
    risposta = chatta(messaggi)
    print(risposta)
    
