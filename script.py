import requests, re, os


if os.path.exists("../../Téléchargements/upload.txt"):
    os.remove("../../Téléchargements/upload.txt")

files = {'file': open('/home/hugues/upload.txt','rb')}




values = {'upload_file' : 'upload.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}





req = requests.post('http://127.0.0.1:5000/upload_API/', files=files, data=values)
print(req.text, req.status_code)
print()





req2 = requests.get('http://127.0.0.1:5000/download/upload.txt', allow_redirects=True)
print('download: ')
print(req2)


filename = re.findall("filename=(.+)", req2.headers['content-disposition'])
url = '../../Téléchargements/'+filename[0]
fichier = open(url, "w")
fichier.write(req2.text)
fichier.close()



print('fichier disponible dans les téléchargements')

delete = input("Supprimer les fichiers nouvellement créés ? : ")
if delete == "yes":
    os.remove("../../Téléchargements/upload.txt")
    rmv = "uploads/" + filename[0]
    os.remove(rmv)