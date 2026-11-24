import pandas as pd

from utili import *


def pulsici_dati(df):
    tst("pulizia dei dati")

    # elimino i duplicati
    righe_prima = len(df)
    df = df.drop_duplicates()
    righe_dopo = len(df)
    print(f"Duplicati rimossi: {righe_prima - righe_dopo}")

    # eliminiamo le righe vuote
    df = df.dropna(how="all")
    print("Tutte le righe vuote sono state rimosse")

    # sistemiamo i numeri con la virgola (50,56)
    if "spesa" in df.columns:
        df["spesa"] = df["spesa"].astype(str).str.strip().str.replace(",", ".", regex=False)
        df["spesa"] = pd.to_numeric(df["spesa"], errors="coerce")
        df.loc[df["spesa"] < 0, "spesa"] = float("nan")

    # convertiamo i numeri "sporchi" (abc) in NaN
    tst("convertiamo i numeri sporchi")
    if "eta" in df.columns:
        df["eta"] = df["eta"].astype(str).str.strip().str.replace(",", ".", regex=False)
        df["eta"] = pd.to_numeric(df["eta"], errors="coerce")
        df.loc[(df["eta"] < 18) | (df["eta"] > 100), "eta"] = float("nan")

    if "data" in df.columns:
        df["data"] = df["data"].astype(str).str.strip().str.replace("/", "-", regex=False)
        df["data"] = df["data"].apply(lambda x: x if x.count("-") == 2 else None)

    if "email" in df.columns:
        df = df.dropna(subset=["email"])
        df = df[df["email"].astype(str).str.strip() != ""]

    if "nome" in df.columns:
        df["nome"] = df["nome"].astype(str).str.strip().str.capitalize()

    # Riempiamo i NaN con la media
    for col in ["spesa", "eta"]:
        if col in df.columns:
            media = df[col].mean()
            df[col] = df[col].fillna(media if not pd.isna(media) else 0)

    df = df.dropna(axis=1, how="all")
    print(f"Pulizia completata, righe rimaste: {len(df)}")
    return df
