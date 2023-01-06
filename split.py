import argparse
import csv

# Fonction qui découpe le texte en paragraphes de 500 mots
def split_into_paragraphs(text, max_words):
  words = text.split()
  num_words = len(words)
  paragraphs = []
  start_index = 0
  while start_index < num_words:
    end_index = start_index + max_words
    paragraph = words[start_index:end_index]
    paragraphs.append(' '.join(paragraph))
    start_index = end_index
  return paragraphs

# Configuration des arguments de ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument('input_filename', help='Nom du fichier de texte à lire')
parser.add_argument('output_filename', help='Nom du fichier CSV de sortie')
args = parser.parse_args()

# Lecture du fichier de texte
with open(args.input_filename, 'r') as f:
  text = f.read()

# Découpage du texte en paragraphes
paragraphs = split_into_paragraphs(text, 100)

# Ecriture des paragraphes dans un fichier CSV
with open(args.output_filename, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  for paragraph in paragraphs:
    writer.writerow([paragraph])
