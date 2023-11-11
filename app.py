from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import subprocess
import os
import numpy as np
import load_features
 
app = Flask(__name__)
 
upload_folder = os.path.join('static', 'uploads')

# Loading pre-processed features
global hsv_features
hsv_features = load_features.load_array()
print(hsv_features)


app.config['UPLOAD'] = upload_folder
 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        return render_template('index.html', img=img)
    return render_template('index.html')


@app.route('/extract_features', methods=['POST'])
def extract_features():
    global hsv_features
    load_features.del_hsv()
    result = subprocess.check_output(['python', 'feature_extraction.py'], stderr=subprocess.STDOUT)
    result = result.decode('utf-8')
    hsv_features = load_features.load_array()
    print(hsv_features)
    print("NORMAL")
    return render_template('index.html',extracted_notice=result)
 
if __name__ == '__main__':
    app.run(debug=True)