import os
import socket
import requests


def liste_fichiers():
    nom_ordinateur = socket.gethostname()
    dir = "uploads!"+ nom_ordinateur
    if not os.path.isdir(dir.replace("!", "/")):
        os.makedirs(dir.replace("!", "/"))

    url = 'http://127.0.0.1:5000/files_list/'+dir
    req = requests.get(url, allow_redirects=True)

    return req.text.split(',')

def upload(path, filename):
    nom_ordinateur = socket.gethostname()
    dir = nom_ordinateur + "/"
    if not os.path.isdir(dir):
        os.makedirs(dir)
    files = {'file': open(path, 'rb')}
    values = {'upload_file': filename, 'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

    req = requests.post('http://127.0.0.1:5000/upload_API/', files=files, data=values)
    return req

def download(filename):
    req = requests.get('http://127.0.0.1:5000/download/'+filename, allow_redirects=True)
    print('download: ')
    user = os.getlogin()
    url = '/home/'+user+'/Téléchargements/' + filename
    fichier = open(url, "w")
    fichier.write(req.text)
    fichier.close()
    return req