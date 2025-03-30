from http import HTTPStatus


def test_hello_word(cliente):
    status = HTTPStatus.OK
    requisicao = cliente.get('/')
    assert requisicao.status_code == status


def test_capturar_token(cliente, usuario_teste):
    resposta_requisicao = cliente.post(
        '/token-access',
        data={
            'username': 'joao@teste.com',
            'password': usuario_teste.senha_limpa,
        },
    )
    token = resposta_requisicao.json()
    assert 'access_token' in token


def test_criar_usuario(cliente):
    usuario_a_criar = {
        'username': 'Joao',
        'email': 'joao@teste.com',
        'password': '1q2w3',
    }
    status = HTTPStatus.CREATED
    requisicao = cliente.post('/user', json=usuario_a_criar)
    usuario_a_criar.update({'username': 'joao0', 'email': 'joao0@test.com'})
    requisicao2 = cliente.post('/user', json=usuario_a_criar)
    assert requisicao.status_code == status
    assert requisicao2.status_code == status


def test_mostrar_usuarios(cliente):
    usuarios = cliente.get('/users')
    status = HTTPStatus.OK
    assert usuarios.status_code == status


def test_cadastrar_profissional(cliente):
    profissional_dados = {
        'nome': 'Joao',
        'numero_conselho': '12546',
        'data_desligamento': None,
    }
    status = HTTPStatus.CREATED
    requisicao = cliente.post('/criar_profissional', json=profissional_dados)
    assert requisicao.status_code == status


def test_profissionais_cadatrados(cliente):
    profissionais = cliente.get('/profissionais')
    status = HTTPStatus.OK
    assert profissionais.status_code == status
