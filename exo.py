import datetime
import pandas as pd
import json
from transaction import Transaction
from transaction_book import TransactionBook
from utils import get_transformed_dataframe, transform_csv_with_json
import os


transformed_df = get_transformed_dataframe()


if __name__ == "__main__":
    try:
        # Charger le fichier JSON pour obtenir les correspondances
        with open("referential.json", 'r') as jf:
            json_content = json.load(jf)

        # Obtenir la correspondance des pays
        country_mapping = json_content["country"]

        # Créer une instance de TransactionBook avec la correspondance des pays
        transaction_book = TransactionBook(country_mapping)

        # Charger les transactions à partir du CSV dans une liste
        transactions_list = pd.read_csv(r"data.csv", sep=";", decimal=",").values.tolist()

        # Charger les transactions dans le TransactionBook
        transaction_book.load_transactions(transactions_list)

        # Ajouter une nouvelle transaction à TransactionBook
        transaction_to_add = [2001, "1", "10", "11", "58", "01/02/2023", 48919]
        transaction_book.add_transaction(transaction_to_add)

        # Afficher un nombre limité de transactions
        print(transaction_book.get_transactions())

        # Mettre à jour et supprimer des transactions
        transaction_book.update_transaction(
            {"country": "FR"}, {"country": "FRA"})
        transaction_book.delete_transaction(rating="F")

        # # Afficher les transactions entre deux dates
        print(transaction_book.get_transactions_between_dates(
            datetime.date(2023, 1, 1), datetime.date(2023, 12, 1)))

        # Afficher les transactions invalides
        print(transaction_book.get_invalid_transactions())

        # # # Afficher le solde des transactions par contrepartie
        print(transaction_book.netting())

        # #Afficher la liste des transactions
        print(transaction_book)

        # Afficher les transactions triées
        print(transaction_book.get_sorted_transactions(*["country", "rating"]))

        # Afficher uniquement les transactions avec un montant de 0,00 €
        zero_transactions = [
            tx for tx in transaction_book.get_all_transactions() if tx.amount == 0.0]
        for tx in zero_transactions:
            print(tx)
        print(
            f"Il y a {len(zero_transactions)} transactions avec un montant de 0.0 €.")

        # Afficher toutes les transactions
        for tx in transaction_book.get_all_transactions():
            print(tx)

    except FileNotFoundError:
        print("Le fichier referential.json n'a pas été trouvé.")
