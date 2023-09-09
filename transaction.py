import datetime
class Transaction:
    """
    Représente une transaction unique avec divers attributs tels que l'index, l'ID de la contrepartie, le pays, la notation, le secteur, la date de la transaction et le montant.
    """

    def  __init__(self, index: int, id_counterpart: str, country: str, rating: str, industry: str, transaction_date: str, amount: float, country_name: str = None):
        """
        Initialise un nouvel objet Transaction avec les attributs fournis.

        Args:
            index (int): L'index de la transaction.
            id_counterpart (str): L'ID de la contrepartie de la transaction.
            country (str): Le pays de la transaction.
            rating (str): La notation de la transaction.
            industry (str): Le secteur de la transaction.
            transaction_date (str): La date de la transaction au format "%d/%m/%Y".
            amount (float): Le montant de la transaction.
            country_name (str, optionnel): Le nom du pays. Par défaut, None.

        Lève:
            ValueError: Si la transaction_date ne peut pas être convertie en un objet datetime.date valide.
            ValueError: Si le montant ne peut pas être converti en float.
        """
        self.index = index
        self.rating = str(rating)
        self.industry = industry

        self.id_counterpart = id_counterpart
        self.country = country_name or country

        if isinstance(transaction_date, str):
            try:
                self.transaction_date = datetime.datetime.strptime(transaction_date, "%d/%m/%Y").date()
            except ValueError:
                print(f"Date non valide : {transaction_date}. La transaction sera considérée comme invalide.")
                self.transaction_date = None
        else:
            print(f"Format de date non conforme : {transaction_date}. La transaction sera considérée comme invalide.")
            self.transaction_date = None

        try:
            self.amount = float(amount)
        except ValueError:
            print(f"Valeur de montant non valide : {amount} pour la transaction {index}. La transaction sera considérée comme invalide.")
            self.amount = 0.0

    def __str__(self):
        date_str = self.transaction_date.strftime('%d/%m/%Y') if self.transaction_date else "Date Invalide"
        return (
        f"Transaction Index: {self.index}\n"
        f"Contrepartie ID: {self.id_counterpart}\n"
        f"Pays: {self.country}\n"
        f"Date: {date_str}\n"
        f"Montant: {self.amount:.2f} €\n"  # suppose que le montant est en euros
        "-------------------------------------"  # juste pour séparer chaque transaction
    )
        
    def __repr__(self):
        return f"Transaction({self.index}, {self.id_counterpart}, {self.country}, {self.transaction_date}, {self.amount})"
