from flask import Flask, render_template,request,jsonify
import os

current_dir = os.path.dirname(os.path.abspath(__file__))



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    cars = [
        {
            'img': '01.avif', 
            'title': 'CUPRA Terramar MID 204к.с DSG 4Drive', 
            'descriptin': 'CUPRA Terramar MID 204к.с DSG 4Drive опис'
        },
        {
            'img': '02.jpeg', 
            'title': 'CUPRA Terramar VZ 265к.с DSG 4Drive', 
            'descriptin': 'CUPRA Terramar VZ 265к.с DSG 4Drive опис'
        },
        {'img': '03.jpeg', 'title': 'Formentor VZ 2.0 TSI 333кс DSG 4Drive', 'descriptin': 'Formentor VZ 2.0 TSI 333кс DSG 4   Drive опис'}
    ]
    
    cars_for_sale = [
        {
            'img': 'CUPRATerramarMID204к.с.DSG4Drive.jpg',
            'title': 'CUPRA Terramar MID 204к.с DSG 4Drive',
            'descriptin': 'CUPRA Terramar MID 204к.с DSG 4Drive опис'
        },
        {
            'img': 'CUPRATerramarVZ265к.с.DSG4Drive.jpg', 
            'title': 'CUPRA Terramar VZ 265к.с DSG 4Drive',
            'descriptin': 'CUPRA Terramar VZ 265к.с DSG 4Drive опис',            
        },
        {
            'img': 'FormentorVZ2.0TSI333ксDSG4Drive.jpg',
            'title': 'Formentor VZ 2.0 TSI 333кс DSG 4Drive',
            'descriptin': 'Formentor VZ 2.0 TSI 333кс DSG 4 Drive опис' 
        }
    ]
    return render_template('index.html', cars=cars, cars_for_sale=cars_for_sale)

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