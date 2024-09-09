from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def coletar_informacoes_pet():
    nome_pet = request.form['nome_pet']
    nome_tutor = request.form['nome_tutor']
    endereco = request.form['endereco']
    numero_tutor = request.form['numero_tutor']
    idade = request.form['idade']
    peso = request.form['peso']

    return render_template('resultado.html', 
                           nome_tutor=nome_tutor, endereco=endereco, 
                           numero_tutor=numero_tutor, nome_pet=nome_pet, 
                           idade=idade, peso=peso)

if __name__ == '__main__':
    app.run(debug=True)
