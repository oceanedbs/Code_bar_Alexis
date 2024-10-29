import pandas as pd

#constants
conversion_page_cm = 10/1000 #épaisseur pour 1 page

#load data
data_livre = pd.read_csv("4_chomage/livres.txt", sep=' ', header=None)
data_livre.columns=['Titre', 'hauteur_cm', 'nb_pages']
data_meubles = pd.read_csv("4_chomage/meubles.txt", sep=' ', header=None)
data_meubles.columns=['Nom', 'hauteur_cm', 'largeur_cm', 'prix']

#associer à chaque libre le meuble de hauteur correspondante
def find_meuble_for_book(book_height, meubles):
    suitable_meubles = meubles[meubles['hauteur_cm'] >= book_height]
    if not suitable_meubles.empty:
        suitable_meubles = suitable_meubles.sort_values(by='hauteur_cm').head(1)
        return suitable_meubles.iloc[0]['Nom']
    return None

#calucler le nombre de meubles nécessaires
def calculate_items_needed(row, meubles):
    meuble = meubles[meubles['Nom'] == row['meuble']]
    if not meuble.empty:
        meuble_width = meuble.iloc[0]['largeur_cm']
        return (row['max_largeur_cm'] // meuble_width) + (1 if row['max_largeur_cm'] % meuble_width > 0 else 0)
    return 0

#calculier le prix total
def calculate_total_price(row, meubles):
    meuble = meubles[meubles['Nom'] == row['meuble']]
    if not meuble.empty:
        meuble_price = meuble.iloc[0]['prix']
        return row['items_needed'] * meuble_price
    return 0

#trouver le meuble optimal pour chaque livre
data_livre['meuble'] = data_livre['hauteur_cm'].apply(lambda x: find_meuble_for_book(x, data_meubles))
#calculer la largeur de chaque livre
data_livre['largeur_cm'] = data_livre['nb_pages'] * conversion_page_cm
print(data_livre)

#calculer la largeur nécessaire de chaque meuble pour y mettre tous les livres
max_widths = data_livre.groupby('meuble')['largeur_cm'].sum().reset_index()
max_widths.columns = ['meuble', 'max_largeur_cm']
#calculer le nombre de meubles nécessaire correspondant à la largeur maximale
max_widths['items_needed'] = max_widths.apply(lambda row: calculate_items_needed(row, data_meubles), axis=1)
#calculer le prix total pour n items de chaque meuble
max_widths['total_price'] = max_widths.apply(lambda row: calculate_total_price(row, data_meubles), axis=1)
print(max_widths)
print(max_widths.sum())

