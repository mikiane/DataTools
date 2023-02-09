import argparse
import csv
import openai
import os

# Configuration des arguments de ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument('input_filename', help='Nom du fichier CSV d\'entrée')
parser.add_argument('output_filename', help='Nom du fichier CSV de sortie')
args = parser.parse_args()

# Chargement du modèle d'OpenAI
openai.api_key = os.environ.get('OPENAIAPI_KEY')
model_engine = "text-davinci-003"

# Lecture du fichier CSV d'entrée
with open(args.input_filename, 'r') as csvfile:
  reader = csv.reader(csvfile)
  rows = list(reader)


def process_text(text):
  # Traitement du texte (par exemple, extraction des 200 premiers mots)
  processed_text = ' '.join(text.split()[:300])  # Extraction des 200 premiers mots du texte

  return processed_text

# Traitement des lignes du fichier CSV
for row in rows:
  if len(row) >= 1:  # On vérifie que la ligne possède au moins une colonne
    text = row[0]  # On récupère le texte de la première colonne
    processed_text = process_text(text)  # Traitement du texte

    # Appel de l'API OpenAI
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Quelle est une question répondant au texte suivant : {processed_text}. Ne pas compéter le prompt. Juste poser la question. ",
      max_tokens=500,
      temperature=1
    )
    resultat = response["choices"][0]["text"]
    row.append(resultat)
    print(resultat)
    
    
# Gestion des erreurs de l'API
#if response.status_code != 200:
#    print(f"Erreur de l'API : {response.status_code}")
#else:
#	print(f"Ajout de la colonne suivante : {response.text}")
    # On ajoute la question trouvée à la deuxième colonne de la ligne
    #row.append(question)
    # On affiche le résultat dans le terminal
    
# Ecriture du fichier CSV de sortie
with open(args.output_filename, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  for row in rows:
    writer.writerow(row)

   
