from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Token da API Invertexto
API_TOKEN = "16202|KaCPY6S7We7rJU3hSbMrJ7F2mpWjXPaD"

# Endpoint da API
API_URL = "https://api.invertexto.com/v1/faker"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-person', methods=['GET'])
def generate_person():
    fields = "name,cpf,rg,birth_date,sex,sign,mother,father,email,phone,cellphone,cep,address,number,neighborhood,city,state,height,weight,blood_type,favorite_color,credit_card,gender,card_number,card_validity"

    response = requests.get(f"{API_URL}?token={API_TOKEN}&fields={fields}&locale=pt_BR")

    if response.status_code == 200:
        data = response.json()

        # Apenas devolver os campos que realmente existem
        return jsonify({key: value for key, value in data.items() if value is not None})
    
    return jsonify({"error": "Failed to fetch data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)