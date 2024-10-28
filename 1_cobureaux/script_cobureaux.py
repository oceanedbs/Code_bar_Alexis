#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:37:15 2024

@author: oceane
"""

# Points pour les lettres en commun avec "Alexis"
points_alexis = {
    'a': 1, 'l': 2, 'e': 3, 'x': 4, 'i': 5, 's': 6
}

# Points pour les lettres en commun avec "Negatif"
points_negatif = {
    'n': 1, 'e': 2, 'g': 3, 'a': 4, 't': 5, 'i': 6, 'f': 7
}

# Fonction pour calculer les scores individuels
def calculer_score(nom, points):
    score = 0
    for lettre in nom.lower():
        score += points.get(lettre, 0)
    return score

# Fonction pour calculer le score total d'un nom/adjectif
def score_total(mot):
    score_alexis = calculer_score(mot, points_alexis)
    score_negatif = calculer_score(mot, points_negatif)
    return int(f"{score_alexis}{score_negatif}")

# Lecture des noms et adjectifs depuis les fichiers
with open('noms.txt', 'r', encoding='utf-8') as f:
    noms = [nom.strip() for nom in f.readlines()]

with open('adjectifs.txt', 'r', encoding='utf-8') as f:
    adjectifs = [adj.strip() for adj in f.readlines()]

# Calcul des scores totaux pour chaque prénom et chaque adjectif
scores_noms = [(nom, score_total(nom)) for nom in noms]
scores_adjectifs = [(adj, score_total(adj)) for adj in adjectifs]

# Tri des prénoms et adjectifs par score
scores_noms.sort(key=lambda x: x[1])
scores_adjectifs.sort(key=lambda x: x[1])

# Association des prénoms et adjectifs triés
associations = [(scores_noms[i][0], scores_adjectifs[i][0]) for i in range(len(scores_noms))]

# Recherche des associations pour les adjectifs demandés
resultats = {adj: nom for nom, adj in associations if adj in ["Capitaine", "Néofuturiste", "Beatnik", "Excesdevitesse"]}

# Affichage des résultats
for adj in ["Capitaine", "Néofuturiste", "Beatnik", "Excesdevitesse"]:
    print(f"{adj} : {resultats.get(adj)}")
