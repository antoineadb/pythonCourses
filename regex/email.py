import re

text =  "contact@graven.yt"
pattern = r'^[a-zA-Z0-9_.-]+@[a-z]{2,}.[a-z]{2,}$'

# vérifier si le texte respecte le pattern

if re.match(pattern, text):
    print("Email valide")
else:
    print("Email invalide")