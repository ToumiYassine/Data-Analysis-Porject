from bs4 import BeautifulSoup
import requests
from io import BytesIO
import pandas as pd
# URL de la page web
url = "https://www.aduana.cl/exportacion-por-pais-y-codigo-arancelario/aduana/2018-12-14/101258.html"

# Effectuer une requête HTTP pour obtenir le contenu de la page
response = requests.get(url,verify=False)
response.raise_for_status()  # Vérifie que la requête a réussi

# Créer un objet BeautifulSoup pour analyser le HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver tous les liens (<a>) dans la page
links = soup.find_all('a', href=True)

# Filtrer les liens pour les années 2021 à 2024
selected_links = []
for link in links:
    # Vérifier si le texte du lien correspond aux années d'intérêt
    if link.text.strip() in ['2020','2021', '2022', '2023', '2024']:
        selected_links.append(link['href'])

# Afficher les liens extraits
for year, link in zip(['2020','2021', '2022', '2023', '2024'], selected_links):
    full_link = f"https://www.aduana.cl{link}"  # Compléter l'URL avec le domaine de base si nécessaire
    #print(f"Lien pour {year}: {full_link}")
    # Télécharger le contenu du lien
    try:
        content_response = requests.get(full_link, verify=False)
        content_response.raise_for_status()  # Vérifie que la requête a réussi

        # Sauvegarder le contenu dans un fichier (optionnel)
        filename = full_link.split('/')[-1]  # Utiliser le nom du fichier à partir de l'URL
        with open(filename, 'wb') as file:
            file.write(content_response.content)

        print(f"Téléchargé et sauvegardé : {filename}")

    except Exception as e:
        print(f"Erreur lors du téléchargement de {full_link}: {e}")

