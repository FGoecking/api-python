from flask import Flask

app = Flask(__name__)

@app.route('/')
def cumprimentar():
    return jsonify({"resp": "Olá, Mundo!"})

@app.route ("/testes/1")
def teste_GET_implicito ():
    return jsonify ({"resp": "Teste 1: método GET implícito."})

@app.route ("/testes/2", methods=['GET'])
def teste_GET_explicito ():
    return jsonify ({"resp": "Teste 2: método GET explícito."})

@app.route ("/testes/3", methods=['POST'])
def teste_POST ():
    return jsonify ({"resp": "Teste 3: método POST."})

@app.route ("/testes/4", methods=['GET', 'POST'])
def teste_GET_POST ():
    return jsonify ({"resp": "Teste 4: método GET ou POST."})

@app.route('/testes/1')
def teste_query_string_1_agurmento_get():
    linguagem = request.args.get('linguagem')
    return '''<h1>Linguagem informada: {}</h1>'''.format(linguagem)

@app.route('/testes/2')
def teste_query_string_2_agurmentos_get():
    linguagem = request.args.get('linguagem')
    framework = request.args.get('framework')
    return '''<h1>Linguagem informada: {}</h1><h1>Framework informado: {}</h1>'''.format(linguagem, framework)

@app.route('/testes/2')
def teste_query_string_2_agurmentos_get():
    linguagem = request.args.get('linguagem')
    framework = request.args.get('framework')
    return '''<h1>Linguagem informada: {}</h1><h1>Framework informado: {}</h1>'''.format(linguagem, framework)

@app.route('/atividade_16/1')
def transformaCelsiusFahrenheit_post():
    tempCelsious = request.args.get('tempCelsious')
    tempFahrenheit = (tempCelsious * 1.8) + 32
    return tempFahrenheit

@app.route('/atividade_16/1')
def calculaMedia_get():
    nota1 = request.args.get('nota1')
    nota2 = request.args.get('nota2')
    nota3 = request.args.get('nota3')
    media = (nota1 + nota2 + nota3)/3
    if(media < 3 ):
        return "reprovado"
    elif(media >= 3 & media < 7):
        return "exame"
    elif(media >= 7):
        return "aprovado"

if __name__ == "__main__":
    app.run ()

#if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    #app.run(debug = True, port = 5000)