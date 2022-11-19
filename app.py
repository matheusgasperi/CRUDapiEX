from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {
        'id': 1,
        'título': 'Notebook Acer',
        'preço': 'R$ 2500'
    },
    {
        'id': 2,
        'título': 'Headset Logitech',
        'preço': 'R$ 759'
    },
    {
        'id': 3,
        'título': 'Mouse sem fio Razer',
        'preço': 'R$ 399'
    },
]

# Consultar(todos)
@app.route('/produtos',methods=['GET'])
def obter_prod():
    return jsonify(produtos)

# Consultar(id)
@app.route('/produtos/<int:id>',methods=['GET'])
def obter_prod_por_id(id):
    for prod in produtos:
        if prod.get('id') == id:
            return jsonify(prod)
# Editar
@app.route('/produtos/<int:id>',methods=['PUT'])
def editar_prod_por_id(id):
    prod_alterado = request.get_json()
    for indice,prod in enumerate(produtos):
        if prod.get('id') == id:
            produtos[indice].update(prod_alterado)
            return jsonify(produtos[indice])
# Criar
@app.route('/produtos',methods=['POST'])
def incluir_novo_prod():
    novo_prod = request.get_json()
    produtos.append(novo_prod)
    
    return jsonify(produtos)
# Excluir
@app.route('/produtos/<int:id>',methods=['DELETE'])
def excluir_prod(id):
    for indice, prod in enumerate(produtos):
        if prod.get('id') == id:
            del produtos[indice]

    return jsonify(produtos)

app.run(port=5000,host='localhost',debug=True)