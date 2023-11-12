from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import subprocess
import os
import load_features
import extraction_func
import time
 
app = Flask(__name__)
 
upload_folder = os.path.join('static', 'uploads')

# Loading pre-processed features
global hsv_features
hsv_features = load_features.load_array()
print(hsv_features)

try:
    uploadedFilename
except:
    imgExist = False
else:
    imgExist = True

app.config['UPLOAD'] = upload_folder
 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global uploadedFilename
    if request.method == 'POST':
        file = request.files['img']
        uploadedFilename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], uploadedFilename))
        img = os.path.join(app.config['UPLOAD'], uploadedFilename)
        return render_template('index.html', img=img)
    return render_template('index.html')


@app.route('/extract_features', methods=['GET', 'POST'])
def extract_features():
    global hsv_features
    load_features.del_hsv()
    result = subprocess.check_output(['python', 'feature_extraction.py'], stderr=subprocess.STDOUT)
    result = result.decode('utf-8')
    hsv_features = load_features.load_array()
    print(hsv_features)
    print("NORMAL")
    return render_template('index.html',extracted_notice=result)

@app.route('/image_color_search', methods=['GET','POST'])
def image_color_search():
    global hsv_features
    global uploadedFilename
    start_time = time.time()
    img = os.path.join(app.config['UPLOAD'], uploadedFilename)
    imgHist = extraction_func.getHistogramFromUpload(uploadedFilename)
    key = extraction_func.colorSimilarityValueAndFilename(hsv_features,imgHist)
    end_time = time.time()
    timer = end_time-start_time
    timer = round(timer,3)
    search_result = str(len(key))+" results in "+str(timer)+" seconds"
    # search_result = search_result.decode('utf-8')
    return render_template('index.html',key=key,img=img,search_result=search_result)
 
if __name__ == '__main__':
    app.run(debug=True)