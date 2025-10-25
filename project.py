
from flask import Flask, render_template,request,jsonify
import os

current_dir = os.path.dirname(os.path.abspath(__file__))



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def handle_form():
    user_text = request.form.get('user-text')
    user_number = request.form.get('user-number')
    return f'Надісланоб текст: [{user_text}], число: [{user_number}]'

@app.route('/save-data', methods=['POST'])
def save_data():
    mytext = request.get_json()
    text = mytext.get('mytext')

    filename = current_dir + '/saved_text.txt'
    with open(filename, 'a') as f:
        f.write(text + '\n')
    return '', 200

@app.route('/get-data', methods=['POST'])
def get_data():
    filename = current_dir + '/saved_text.txt'
    with open(filename,'r') as f:
        lines = f.readlines()

    text = [line + 'br' for line in lines]
    return jsonify({'data': text}), 200

if __name__ == '__main__':
    app.run(debug=True)