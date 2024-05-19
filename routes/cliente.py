from flask import Blueprint, render_template, request
from database.models.cliente import Cliente


cliente_route = Blueprint('cliente', __name__)

"""
ROTA DE CLIENTES

    -/clientes/ (GET) - listar clientes
    -/clientes/ (POST) - inserir cliente no servidor
    -/clientes/new (GET) - renderizar form para cliente
    -/clientes/<id> (GET) - obter dados de cliente
    -/clientes/<id>/edit (GET) - renderizar dados para editar um cliente
    -/clientes/<id>/update (PUT) - editar cliente
    -/clientes/<id>/delete (DELETE) - deletar cliente
    
"""


@cliente_route.route('/')
def lista_cliente():
    """listar os clientes"""
    conn, cursor = Cliente.conectarDb()
    consulta = ('SELECT * FROM clientes')
    cursor.execute(consulta)

    resultados = cursor.fetchall()
    print(resultados)

    # Convertendo tuplas em dicionários
    colunas = [desc[0] for desc in cursor.description]
    clientes = [dict(zip(colunas, linha)) for linha in resultados]

    conn.close()

    return render_template('lista_clientes.html', clientes=clientes)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """inserir dados do cliente"""
    dados = request.json
    nome = dados.get('nome')
    email = dados.get('email')

    novoCliente = Cliente(nome, email)
    novo_id = novoCliente.inserirCliente()

    conn, cursor = Cliente.conectarDb()
    cursor.execute('SELECT id FROM clientes ORDER BY id DESC LIMIT 1')
    ultimo_id = cursor.fetchone()[0]

    novoUsuario = {
        "id": ultimo_id,
        "nome": nome,
        "email": email,
    }

    return render_template('item_cliente.html', cliente=novoUsuario)


@cliente_route.route('/new')
def form_cliente():
    """formulado para cadastrar cliente"""
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """exibir detalhes de cliente"""

    conn, cursor = Cliente.conectarDb()
    cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
    cliente = cursor.fetchone()

    print(cliente_id)
    

    return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """formulario para editar cliente"""
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c

    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """atualizar informacoes do cliente"""
    cliente_editado = None
    # obter dados form de edição
    data = request.json

    # obter usuario pelo id
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']

            cliente_editado = c
    # editar o usuario
    return render_template('item_cliente.html', cliente=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """deletar cliente"""
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]

    return 's'
