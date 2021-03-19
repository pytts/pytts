from flask import Flask, send_file, render_template, request, redirect, url_for
import os
from io import BytesIO
from main import pytts

app = Flask(__name__, template_folder='server')
	
@app.route('/')
def index():
	return render_template('index.html')
		

@app.route('/generate', methods = ['POST', 'GET'])
def data():
  if request.method == 'GET':
    return redirect(url_for('index'))
  if request.method == 'POST':
    form_data = request.form
    text = form_data['text']
    
    fp = BytesIO()
    
    pytts.speak_to_fp(text, fp)
    
    return send_file(fp, attachment_filename='output.mp3', mimetype='audio/mpeg')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
