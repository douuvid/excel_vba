
import datetime
from transaction import Transaction
from utils import limit_transaction


class TransactionBook:
    


    
    """
    Représente un carnet de transactions.

    Méthodes:
    - load_transactions(transactions): Charge des transactions dans le carnet.
    - netting(): Réalise une compensation par contrepartie et renvoie le résultat sous forme de dictionnaire.
    - add_transaction(transaction): Ajoute une nouvelle transaction au carnet.
    - delete_transaction(**kwargs): Supprime des transactions basées sur des arguments de filtrage.
    - update_transaction(filter_args, update_args): Met à jour des transactions selon des critères de filtrage et des arguments de mise à jour.
    - get_transactions_between_dates(start, end): Récupère les transactions entre deux dates spécifiées.
    - get_invalid_transactions(): Identifie les transactions considérées comme invalides.
    - get_sorted_transactions(*args): Récupère les transactions triées selon des attributs spécifiés.
    - get_all_transactions(): Récupère l'ensemble des transactions.
    - get_transactions(): Récupère un nombre limité de transactions en utilisant le décorateur limit_transaction.
    """
    
    
    
    def __init__(self, country_mapping=None):
        """
        Initialise une nouvelle instance de la classe TransactionBook.
        
        Cette méthode est le constructeur de la classe TransactionBook. Elle initialise une nouvelle instance de la classe en créant une liste vide pour stocker les transactions.
        
        Exemple d'utilisation :
        ```python
        carnet = TransactionBook()
        ```
        
        Entrées : 
        - Aucune
        
        Déroulement :
        1. La méthode __init__ est appelée lorsqu'une nouvelle instance de la classe TransactionBook est créée.
        2. Elle initialise l'attribut transaction_list comme une liste vide.
        
        Sorties :
        - Aucune
        """
      
    
        self.transaction_list = []
        self.country_mapping = country_mapping or {}  # On utilise un dictionnaire vide par défaut si rien n'est fourni


    def is_valid_transaction_format(self, transaction: Transaction) -> bool:
    # Remarque : Vous pourriez vouloir ajouter plus de vérifications ici en fonction de vos critères de validité
        if not transaction.transaction_date:
            return False
        if transaction.amount <= 0:  # par exemple, si vous considérez un montant négatif ou nul comme invalide
            return False
        # Ajoutez d'autres vérifications si nécessaire...
        return True


        
    

    
    def load_transactions(self, transactions):
        
    
        for transaction in transactions:
            index, id_counterpart, country_id, rating, industry, transaction_date, amount = transaction

            country_name = self.get_country_name_by_id(str(country_id)) 
            self.transaction_list.append(Transaction(index, id_counterpart, country_id, rating, industry, transaction_date, amount, country_name))




    def netting(self):
        """
        Effectue une compensation par contrepartie.

        Returns:
        - Un dictionnaire avec pour clés les identifiants des contreparties et pour valeurs les montants nets.
        """
        result = {}
        for tx in self.transaction_list:
            if tx.id_counterpart not in result:
                result[tx.id_counterpart] = 0
            result[tx.id_counterpart] += tx.amount
        return result


    def add_transaction(self, transaction_data):
        index, id_counterpart, country_id, rating, industry, transaction_date, amount = transaction_data

        country_name = self.get_country_name_by_id(str(country_id))
        transaction = Transaction(index, id_counterpart, country_id, rating, industry, transaction_date, amount, country_name)
     
        if self.is_valid_transaction_format(transaction):
         self.transaction_list.append(transaction)
        else:
            print(f"Transaction invalide : {transaction_data[0]}")





    def delete_transaction(self, **kwargs):
        """
        Supprime des transactions basées sur des arguments de filtrage.

        Args:
        - kwargs : Arguments de filtrage pour spécifier les transactions à supprimer.
        """
        self.transaction_list = [tx for tx in self.transaction_list if not all([getattr(tx, key) == value for key, value in kwargs.items()])]

    def update_transaction(self, filter_args, update_args):
        """
        Met à jour des transactions selon des critères de filtrage et des arguments de mise à jour.

        Args:
        - filter_args : Critères pour identifier les transactions à mettre à jour.
        - update_args : Arguments indiquant quels attributs mettre à jour et leurs nouvelles valeurs.
        """
        for tx in self.transaction_list:
            if all([getattr(tx, key) == value for key, value in filter_args.items()]):
                for key, value in update_args.items():
                    setattr(tx, key, value)

    def get_transactions_between_dates(self, start: datetime.date, end: datetime.date):
        """
        Récupère les transactions entre deux dates.

        Args:
        - start : Date de début.
        - end : Date de fin.

        Returns:
        - Une liste des transactions entre les dates spécifiées.
        """
        return [tx for tx in self.transaction_list if tx.transaction_date and start <= tx.transaction_date <= end]

    def get_invalid_transactions(self):
        """
        Identifie les transactions considérées comme invalides.

        Returns:
        - Une liste de transactions invalides, selon certains critères.
        """
        return [tx for tx in self.transaction_list if not self.is_valid_transaction_format(tx)]

    def get_sorted_transactions(self, *attributes):
        valid_attributes = ["index", "id_counterpart", "country", "rating", "industry", "transaction_date", "amount"]
        attributes = [attr for attr in attributes if attr in valid_attributes]
        if not attributes:
            print("Aucun attribut valide fourni pour le tri.")
            return self.transaction_list
        return sorted(self.transaction_list, key=lambda x: tuple(getattr(x, attr) for attr in attributes))
    
    


    def get_all_transactions(self):
        """
        Récupère l'ensemble des transactions.

        Returns:
        - Une liste contenant toutes les transactions.
        """
        return self.transaction_list

    def __str__(self):
        """
        Représente le carnet de transactions sous forme de chaîne de caractères.
        
        Returns:
        - Une représentation sous forme de chaîne de caractères des transactions.
        """
        return "\n".join(str(tx.__dict__) for tx in self.transaction_list)
    
    def get_country_name_by_id(self, country_id):
        try:
            return self.country_mapping[country_id]
        except KeyError:
            print(f"ID de pays non trouvé : {country_id}. Utilisation de 'Inconnu' comme nom de pays.")
            return 'Inconnu'



  # Assurez-vous que self.country_mapping est initialisé avec la correspondance appropriée

    
    @limit_transaction(100)
    def get_transactions(self):
        """
        Récupère un nombre limité de transactions.

        Returns:
        - Une liste de transactions limitée à un certain nombre.
        """
        return self.transaction_list