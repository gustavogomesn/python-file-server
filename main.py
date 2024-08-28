from flask import Flask, request, send_file, send_from_directory, redirect, url_for, render_template
import os
import json
from datetime import datetime
import humanize
import magic
import shutil
import tempfile
from get_icon_by_type import GetIconByType
from ip_addr import IpAddr


running_on_windows = os.name == 'nt'
print(running_on_windows)
get_icon_by_type = GetIconByType()
ip_addr = IpAddr()
app = Flask(__name__)

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json'), 'r') as ini:
    content = json.load(ini)
    app.config['UPLOAD_FOLDER'] = content['UPLOAD_FOLDER']
    app.config['LOG_FILE'] = os.path.join(content['LOG_FOLDER'], 'file-server-activity.log')

@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect(url_for('files'))

@app.route('/files')
@app.route('/files/<path:dir>')
def files(dir = app.config['UPLOAD_FOLDER']):
    try:
        if running_on_windows:
            os.chdir(dir)
        else:
            os.chdir('/' + dir)
    except FileNotFoundError as e:
        print(e)
        os.chdir(app.config['UPLOAD_FOLDER'])
    
    folders = []
    for folder in os.listdir(os.getcwd()):
        if os.path.isdir(folder):
            aux = {}
            aux['is_file'] = False
            aux['name'] = folder
            aux['creation_date'] = datetime.fromtimestamp(os.path.getctime(folder)).strftime("%d/%m/%Y, %H:%M:%S")
            aux['modif_date'] = datetime.fromtimestamp(os.path.getmtime(folder)).strftime("%d/%m/%Y, %H:%M:%S")
            folders.append(aux)
    files = []
    for item in os.listdir(os.getcwd()):
        if os.path.isfile(item):
            aux = {}
            aux['is_file'] = True
            aux['name'] = item
            aux['size'] = humanize.naturalsize(os.path.getsize(item))
            aux['creation_date'] = datetime.fromtimestamp(os.path.getctime(item)).strftime("%d/%m/%Y, %H:%M:%S")
            aux['modif_date'] = datetime.fromtimestamp(os.path.getmtime(item)).strftime("%d/%m/%Y, %H:%M:%S")
            aux['type'] = get_icon_by_type.get_icon_by_type(magic.from_file(item, mime=True))
            files.append(aux)
    
    is_root_folder = os.getcwd() == app.config['UPLOAD_FOLDER']
    # print(ip_addr.get_domain_name(request.remote_addr))
    return render_template('index.html', files=files, folders=folders, os=os, is_root_folder=is_root_folder)

@app.route('/upload-file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file:
            filename = file.filename
            file.save(filename)
            return redirect(url_for('files', dir=os.getcwd()))

@app.route('/upload-folder', methods=['GET', 'POST'])
def upload_folder():
    if request.method == 'POST':
        if 'folder' not in request.files:
            return redirect(request.url)
        
        folder = request.files.getlist('folder')
        
        if folder == []:
            return redirect(request.url)

        for file in folder:
            filename = file.filename
            # filename has this format: path/to/file.txt, the line above get only the folder paths to create 
            folders_path = '/'.join(filename.split('/')[:-1])
            new_folder_manually(folders_path)
            file.save(os.path.join(os.getcwd(), filename))
        
        return redirect(url_for('files', dir=os.getcwd()))

@app.route('/open-file/<filename>')
def open_file(filename):
    return send_file(os.path.join(os.getcwd(), filename))

@app.route('/download/<filename>')
def download_file(filename):
    if os.path.isdir(filename):
        # this line is saving the file on temp dir, have to add function to clen the file after download
        shutil.make_archive(os.path.join(tempfile.gettempdir(), filename), 'zip', filename)
        return send_from_directory(tempfile.gettempdir(), f'{filename}.zip', as_attachment=True)
        
    return send_from_directory(os.getcwd(), filename, as_attachment=True)

@app.route('/previous-folder')
def previous_folder():
    previous_folder = os.path.split(os.getcwd())[0]
    return redirect(url_for('files', dir=previous_folder))

@app.route('/new-folder', methods=['GET', 'POST'])
def new_folder():
    new_folder = request.form['new-folder-name']
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
                
    return redirect(url_for('files', dir=os.getcwd()))

def new_folder_manually(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

@app.route('/delete/<filename>')
def delete(filename):
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        try:
            os.rmdir(filename)
        except OSError as e:
            shutil.rmtree(filename)
            
        
    return redirect(url_for('files', dir=os.getcwd()))

# @app.errorhandler(404)
# def page_not_found(e):
#     return redirect(url_for('upload_file'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
