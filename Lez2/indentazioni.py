# ============================== #
'''
cartella_foto
    ╚→ cartella_audio
    |       ╚→ musica.mp3
    ╚→ compleanno.png
mouse = "cartella_audio"

if mouse == "cartella_foto": # A
    cartella = "musica"
    if cartella == "video":
        print("video.mp4")
    else:
        print("compleanno.png")

elif mouse == "cartella_audio": # B
    print("musica.mp3") # contenuto B

'''
if True: # A
    print('a') # contenuto A
if True: # B
    print() # contenuto B
    if True: # C → CB
        if True: # D → DC
            pass # contenuto D
        if True: # E → EC
            if True: # F → FE
                pass # contenuto F
    if True: # G → GB
        pass # contenuto G

'''
┌────────────────────────────────────────────────────────────┐
│                        LIVELLO 0                           │
│                                                            │
│  ┌─── if True: # A ───────────────────────────────────┐    │
│  │                                                    │    │
│  │     print('a')  # contenuto A                      │    │
│  │                                                    │    │
│  └────────────────────────────────────────────────────┘    │
│                                                            │
│  ┌─── if True: # B ───────────────────────────────────┐    │
│  │                                                    │    │
│  │     print()  # contenuto B                         │    │
│  │                                                    │    │
│  │     ┌─── if True: # C  (dentro B) ─────────────┐   │    │
│  │     │                                          │   │    │
│  │     │   ┌─── if True: # D  (dentro C) ─────┐   │   │    │
│  │     │   │                                  │   │   │    │
│  │     │   │     pass  # contenuto D          │   │   │    │
│  │     │   │                                  │   │   │    │
│  │     │   └──────────────────────────────────┘   │   │    │
│  │     │                                          │   │    │
│  │     │   ┌─── if True: # E  (dentro C) ─────┐   │   │    │
│  │     │   │                                  │   │   │    │
│  │     │   │   ┌── if True: # F (in E) ───┐   │   │   │    │
│  │     │   │   │                          │   │   │   │    │
│  │     │   │   │   pass # contenuto F     │   │   │   │    │
│  │     │   │   │                          │   │   │   │    │
│  │     │   │   └──────────────────────────┘   │   │   │    │
│  │     │   │                                  │   │   │    │
│  │     │   └──────────────────────────────────┘   │   │    │
│  │     │                                          │   │    │
│  │     └──────────────────────────────────────────┘   │    │
│  │                                                    │    │
│  │     ┌─── if True: # G  (dentro B) ────────────┐    │    │
│  │     │                                         │    │    │
│  │     │     pass  # contenuto G                 │    │    │
│  │     │                                         │    │    │
│  │     └─────────────────────────────────────────┘    │    │
│  │                                                    │    │
│  └────────────────────────────────────────────────────┘    │
│                                                            │
└────────────────────────────────────────────────────────────┘


A  ─ if True:                    ← livello 0
│
├── print('a')                   ← contenuto A          (1 indent)
│
B  ─ if True:                    ← livello 0
│
├── print()                      ← contenuto B          (1 indent)
│
├── C ─ if True:                 ← dentro B             (1 indent)
│   │
│   ├── D ─ if True:             ← dentro C             (2 indent)
│   │   │
│   │   └── pass                 ← contenuto D          (3 indent)
│   │
│   └── E ─ if True:             ← dentro C             (2 indent)
│       │
│       └── F ─ if True:         ← dentro E             (3 indent)
│           │
│           └── pass             ← contenuto F          (4 indent)
│
└── G ─ if True:                 ← dentro B             (1 indent)
    │
    └── pass                     ← contenuto G          (2 indent)

'''

