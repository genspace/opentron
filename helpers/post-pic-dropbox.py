from flask import Flask, request
import dropbox
from PIL import Image  
import PIL
import io
import os

dbx = dropbox.Dropbox(os.environ['DBox']) 
app = Flask(__name__) 

@app.route("/")
def hello():
  return "Hello World!" 
  
@app.route('/img', methods = ['POST'])
def index2():
  if request.method == 'POST':
    image = request.files['media']
    fname = image.filename
    im1 = Image.open(image)
    img_bytes = io.BytesIO()
    im1.save(img_bytes, format = 'PNG')
    img_bytes_arr = img_bytes.getvalue()
    path_partial = "experiment/"
    path = path_partial + fname
    dbx.with_path_root(dropbox.common.PathRoot.namespace_id("<name-id>")).files_upload(img_bytes_arr, path)
    
  return "Hello World!"

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port)
