from flask import Flask,render_template,request,redirect,url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

dir_client = '~/download'
app.add_url_rule(
    "/download/<name>", endpoint=dir_client, build_only=True
)

@app.route('/')
def index():
    return redirect(url_for('hello'))

@app.route('/hello/')
def hello(error= None):
    return render_template('hello.html', error=error)

@app.route('/upload/',methods = ['GET','POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return render_template('liste_file.html', files=os.listdir('./uploads'))
    return hello(error='yes')


@app.route('/download/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name, as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000)