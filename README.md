Le module Python présenté ci-dessus met en œuvre un carnet de transactions, une collection qui rassemble des opérations financières individuelles.

Comprendre les Transactions
Chaque transaction est représentée par la classe Transaction avec les attributs suivants :

index: Identifiant unique de la transaction.
id_counterpart: ID de la contrepartie avec laquelle la transaction a eu lieu.
country: Pays de la contrepartie.
rating: Notation de la contrepartie.
industry: Secteur d'activité de la contrepartie.
transaction_date: Date de la transaction.
amount: Montant de la transaction.
Découverte du Carnet de Transactions (TransactionBook)
La classe TransactionBook symbolise un ensemble de transactions. Elle offre plusieurs méthodes pour gérer ces transactions, dont :

load_transactions: Charger des transactions à partir d'une liste.
add_transaction: Ajouter une transaction au carnet.
delete_transaction: Supprimer une transaction du carnet.
update_transaction: Mettre à jour une transaction existante.
get_transactions: Récupérer toutes les transactions du carnet.
get_transactions_between_dates: Récupérer les transactions effectuées entre deux dates précises.
get_invalid_transactions: Identifier les transactions non valides.
netting: Équilibrer les transactions par contrepartie.
get_sorted_transactions: Récupérer les transactions triées selon certains attributs.
Comment utiliser le Carnet de Transactions
Pour exploiter les fonctionnalités de ce carnet de transactions, suivez ces étapes :

Créez un objet TransactionBook.
Chargez vos transactions avec la méthode load_transactions.
Gérez vos transactions (ajoutez, supprimez, mettez à jour) grâce aux méthodes fournies.
Interrogez votre carnet de transactions en fonction de vos besoins, en utilisant par exemple get_transactions_between_dates pour récupérer des transactions sur une période précise.

Exemple d'utilisation
Voici un exemple simple d'utilisation de ce carnet :

# Création d'une instance du carnet de transactions
book = TransactionBook()

# Chargement des transactions
book.load_transactions(liste_transactions) # `liste_transactions` est une liste de vos transactions

# Affichage des transactions entre le 1er janvier et le 31 décembre 2023
print(book.get_transactions_between_dates(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))

# Suppression des transactions avec un montant négatif
book.delete_transaction(amount='<0')

# Ajout d'une nouvelle transaction
new_transaction = (2024, 'ID100', 'FR', 'A', 'Tech', '15/05/2023', 5000.0)
book.add_transaction(new_transaction)
