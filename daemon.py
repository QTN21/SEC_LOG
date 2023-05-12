import sys
import os

# Récupération de la liste des paramètres
param = sys.argv[1::]

if len(param) != 3:
    print("Veuillez entrer le bon nombre de paramètres")
    exit(1)

# Verification de l'existence des fichiers de CSV
if not os.path.exists("./daemon_status.csv"):
    with open("./daemon_status.csv", "w") as f:
        f.write("SOFTWARE;STATE\n")

if not os.path.exists("./daemon_history.csv"):
    with open("./daemon_history.csv", "w") as f:
        f.write("DATE;SOFTWARE;STATE\n")


# Data contient le contenu du fichier daemon_status
# software contient la liste des soft présent dans daemon_status
data, software = [], []

with open("./daemon_status.csv", "r") as f:
    data = f.readlines()
    software = [i.split(";")[0] for i in data]

# Traitement pour modifier l'état du soft dans daemon_status
for i, content in enumerate(data):
    content = content.split(";")
    if param[1] not in software:
        data.append(f"{param[1]};{param[2]}\n")
        break
  
    if content[0] == param[1]:
        data[i] = f"{param[1]};{param[2]}\n"
        break

# Ecrire des nouvelles données dans daemon_status
with open("./daemon_status.csv", "w") as f:
    f.writelines(data)

# Ajout simple dans l'historique
with open("./daemon_history.csv", "a") as f:
    f.write(f"{';'.join(param)}\n")
            