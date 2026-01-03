
import subprocess
from flask import Flask, render_template, request
import uuid

from werkzeug.utils import secure_filename
import os


UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []
        for key, value in request.files.items():
            print(key, value)
            #upload the file
            file = request.files[key]
            if file :
                filename = secure_filename(file.filename)
                if(not (os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, filename))
                input_files.append(file.filename)
            #capture the description and save it a file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"),"w") as f:
                    f.write(desc)
        for fl in input_files:
             with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"), "a") as f:
                  f.write(f"file '{fl}'\nduration 1 \n")
                  
             


    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html",reels=reels)

if __name__ == "__main__":
    # Start background generate_process.py
    subprocess.Popen(["python", "generate_process.py"], shell=True)
    print("✅ Background process started: generate_process.py")
    
    # Start Flask server
    app.run(debug=True)