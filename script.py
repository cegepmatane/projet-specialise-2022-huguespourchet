import requests

files = {'file': open('/home/hugues/upload.txt','rb')}
values = {'upload_file' : 'upload.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}

req = requests.post('http://127.0.0.1:5000/upload_API/', files=files, data=values)
print(req.text, req.status_code)

req2 = requests.get('http://127.0.0.1:5000/download/upload.txt', allow_redirects=True)
print(req2)
fichier = open('../../Téléchargements/upload.txt', "w")
fichier.write(req2.text)
fichier.close()
