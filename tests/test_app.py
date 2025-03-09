def test_hello_word(cliente):
    status = 200
    requisicao = cliente.get('/')
    assert requisicao.status_code == status


def test_criar_usuario(cliente):
    usuario_a_criar = {
        'name': 'Joao',
        'email': 'joao@teste.com',
        'password': '1q2w3',
    }
    status = 201
    requisicao = cliente.post('/user', json=usuario_a_criar)
    usuario_a_criar.update({'name': 'joao0', 'email': 'joao0@test.com'})
    requisicao2 = cliente.post('/user', json=usuario_a_criar)
    assert requisicao.status_code == status
    assert requisicao2.status_code == status


def test_mostrar_usuarios(cliente):
    usuarios = cliente.get('/users')
    print(usuarios.json())
    status = 200
    assert usuarios.status_code == status
