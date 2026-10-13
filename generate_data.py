
# ============================================================
# 1. IMPORTATION DES BIBLIOTHÈQUES
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
# 2. INITIALISATION DU GÉNÉRATEUR ALÉATOIRE
# ============================================================

# Fixer la graine aléatoire pour garantir la reproductibilité
np.random.seed(42)


# ============================================================
# 3. GÉNÉRATION DES DONNÉES DES CLIENTS
# ============================================================

# Nombre de clients fictifs à générer
n = 500

# Création du DataFrame contenant les caractéristiques des clients
data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    "salaire": np.random.randint(1200, 8000, n),
    "abonnement": np.random.choice(
        ["Basique", "Standard", "Premium"], n
    ),
    "anciennete": np.random.randint(0, 15, n),
    "consommation": np.random.randint(0, 100, n)
})


# ============================================================
# 4. CRÉATION DE LA VARIABLE CIBLE : CHURN
# ============================================================

# Un client est considéré comme étant à risque de départ si :
# - sa consommation est inférieure à 30 ;
# - son ancienneté est inférieure à 2 ans.
#
# churn = 1 : client à risque de départ
# churn = 0 : client qui ne répond pas à cette règle

data["churn"] = (
    (data["consommation"] < 30) &
    (data["anciennete"] < 2)
).astype(int)


# ============================================================
# 5. SAUVEGARDE DES DONNÉES
# ============================================================

# Enregistrement du DataFrame dans un fichier CSV
# index=False permet de ne pas ajouter l'index comme colonne.
data.to_csv("churn_data.csv", index=False)


# ============================================================
# 6. AFFICHAGE ET VÉRIFICATION DES RÉSULTATS
# ============================================================

# Afficher les cinq premières lignes
print("Aperçu des données :")
print(data.head())

# Afficher les dimensions du DataFrame
print("\nDimensions du jeu de données :")
print(data.shape)

# Afficher les noms des colonnes
print("\nColonnes disponibles :")
print(data.columns.tolist())

# Calculer et afficher le taux de churn
taux_churn = data["churn"].mean()

print(f"\nTaux de churn : {taux_churn:.1%}")

# Vérifier le nombre de clients dans chaque catégorie
print("\nRépartition des clients selon le churn :")
print(data["churn"].value_counts())
