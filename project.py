from flask import Flask, render_template,request,jsonify, redirect, url_for, session
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

current_dir = os.path.dirname(os.path.abspath(__file__))

USER = {
    'useremail': 'test@gmail.com',
    'password': '123345678'
}

app = Flask(__name__)
app.secret_key = 'my_secret_text'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def home():
    user = ''
    if 'keyuser' in session:
        user = f"""
        <h2>Вітаю {session['keyuser']}! Ви увійшли в систему.</h2>
        """

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
    return render_template('index.html', cars=cars, cars_for_sale=cars_for_sale, user=user)

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

@app.route('/register', methods=['GET'])
def register():
    if request.method == 'POST':
        useremail = request.form.get('email')
        password = request.form.get('password')


        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(email=useremail, password=hashed_password) 
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home'))
    


            

    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        useremail = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=useremail).first()
        if user and check_password_hash(user.password, password):            
            
            session['keyuser'] = useremail
            return redirect(url_for('home'))
        else:
            return 'Непвельні дані'
    return render_template('login.html')

@app.route('/car_buy', methods=['GET'])
def car_buy():
    return render_template('car_buy.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('keyuser', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)