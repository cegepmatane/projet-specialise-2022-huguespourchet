from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os

#création d'une application Flask
app = Flask(__name__)

#configuration des dossiers d'upload du serveur
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#gestion de l'autorisation des types de fichiers
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Routes
@app.route('/')
def index():
    return redirect(url_for('hello'))
#route par défault
@app.route('/hello/')
def hello(error= None):
    return render_template('hello.html', error=error)
#route upload via page web
@app.route('/upload/',methods = ['POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return render_template('liste_file.html', files=os.listdir('./uploads'))
    return hello(error='yes')
#route d'upload via API
@app.route('/upload_API/',methods = ['POST'])
def upload_file_api():
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp
#route download, fonctionne par page web et API
@app.route('/download/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name, as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000)