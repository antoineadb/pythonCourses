import re

text =  "https://www.youtube.com/watch?v=9hEGC3Mw7wQ"
pattern = r'^(https:\/\/)?(www.)?youtube.com\/watch\?v=([a-zA-Z0-9_-]+)$'

# vérifier si le texte respecte le pattern

match = re.search(pattern,text)

if match:
    print("C'est une vidéo youtube")
    print(match.group(3))
else:
    print("Ce n'est une vidéo youtube")