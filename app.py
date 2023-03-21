from pdf2docx import Converter
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    if request.method=="POST":
        print(request)
        file = request.files['file']
        str = file.filename.split(".")[0]
        f = open("temp.pdf",'wb')
        f.write(file.read())
        cv = Converter("temp.pdf")
        cv.convert("temp.docx",start=0,end=None)
        cv.close()
        return send_file("temp.docx",download_name=str+".docx",as_attachment=True)
    
    return render_template('index.html') 


if __name__ == "__main__":
    app.run(debug=True,port=8000)