import os
import socket
import requests


def liste_fichiers():
    nom_ordinateur = socket.gethostname()
    dir = "uploads!"+ nom_ordinateur
    if not os.path.isdir(dir.replace("!", "/")):
        os.makedirs(dir.replace("!", "/"))

    url = 'http://huguespourchet.pythonanywhere.com/files_list/'+dir
    req = requests.get(url, allow_redirects=True)

    return req.text.split(',')

def upload(path, filename):
    nom_ordinateur = socket.gethostname()
    dir = nom_ordinateur + "/"
    if not os.path.isdir(dir):
        os.makedirs(dir)
    files = {'file': open(path, 'rb')}
    values = {'upload_file': filename, 'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

    req = requests.post('http://huguespourchet.pythonanywhere.com/upload_API/', files=files, data=values)
    return req

def download(filename):
    req = requests.get('https://huguespourchet.pythonanywhere.com/download/'+filename, allow_redirects=True)
    print('download: ')
    print(req.text)
    user = os.getlogin()
    url = '/home/'+user+'/Téléchargements/' + filename
    fichier = open(url, "w")
    fichier.write(req.text)
    fichier.close()
    return req
