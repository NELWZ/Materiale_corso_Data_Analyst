# pip install groq
# pip3 install groq
# python -m pip install groq
# python3 -m pip install groq

def get_api():
    file_api = "C:\\Users\\avare\\Desktop\\groqapi.txt"
    # apri il file e leggilo
    with open (file_api, 'r', encoding='utf-8') as panda:
        api = panda.read().strip()

    return api

if __name__ == "__main__":
    from groq import Groq

    client = Groq(api_key=get_api())
    while True:
        try:
            chat = client.chat.completions.create(
                messages=[
                    {'role': 'user', 'content': input("Prompt: ")}
                ],
                model="openai/gpt-oss-120b"
            )
            print(chat.choices[0].message.content)

        except Exception as er:
            print(f"Errore: {er}")


