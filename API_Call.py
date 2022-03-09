import os
import socket
import requests


def liste_fichiers():
    nom_ordinateur = socket.gethostname()
    print(nom_ordinateur)
    dir = "uploads!"+ nom_ordinateur
    if not os.path.isdir(dir.replace("!", "/")):
        os.makedirs(dir.replace("!", "/"))

    url = 'http://127.0.0.1:5000/files_list/'+dir
    req = requests.get(url, allow_redirects=True)

    return req.text.split(',')
