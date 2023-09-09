import pandas as pd
import json


def transform_csv_with_json(csv_path, json_path):
    # Ici on ouvre fichier JSON
    with open(json_path, 'r') as jf:
        json_content = json.load(jf)

    # Lecture du fichier CSV 
    df = pd.read_csv(csv_path, delimiter=";", decimal=",")

    #  Vérifiez si le remplacement de la virgule par le point fonctionne correctement.
    df['amount'] = df['amount'].str.replace(',', '.')
    

    # Convertir les valeurs de la colonne 'amount' en numérique
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # Afficher les entrées avec des montants non valides
    invalid_amounts = df[df['amount'].isnull()]
    for _, row in invalid_amounts.iterrows():
        print(f"Ligne {row['index']} a une valeur de montant non valide.")

    # Remplacer NaN par 0
    df['amount'].fillna(0, inplace=True)

    # Remplacer les indices par leurs valeurs correspondantes pour chaque colonne
    try:
        for col, mapping in json_content.items():
            if col in df.columns:
                if col == "country":
                    # Pour le pays, nous conservons l'ID et ajoutons également le nom
                    df["country_name"] = df[col].map(mapping)
                else:
                    df[col] = df[col].map(mapping)
    except KeyError:
        print(f"Erreur: La colonne '{col}' n'a pas de correspondance dans le fichier JSON.")
        
    # Enregistrement du DataFrame transformé dans un nouveau fichier CSV
    transformed_csv_path = csv_path.replace(".csv", "_transformed.csv")
    df.to_csv(transformed_csv_path, sep=";", decimal=",", index=False)
    
    print(f"\nFichier sauvegardé à l'emplacement {transformed_csv_path}")
    return df


def limit_transaction(n):
   
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result[:n]
        return wrapper
    return decorator

import os

def get_transformed_dataframe(csv_filename="data.csv", json_filename="referential.json"):
    """
    Génère les chemins relatifs pour les fichiers CSV et JSON et renvoie le DataFrame transformé.

    Args:
    - csv_filename (str, optional): Nom du fichier CSV. Par défaut à "data.csv".
    - json_filename (str, optional): Nom du fichier JSON. Par défaut à "referential.json".

    Returns:
    - DataFrame: Le DataFrame transformé.
    """

    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_directory, csv_filename)
    json_file_path = os.path.join(current_directory, json_filename)

    # Transforme le fichier CSV en utilisant le fichier JSON et renvoie le DataFrame
    return transform_csv_with_json(csv_file_path, json_file_path)

# Utilisation de la fonction:
transformed_df = get_transformed_dataframe()
