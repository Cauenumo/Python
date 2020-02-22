def listar_todos(lista_cli):
    lista_cli = ['Cauê','Gabriel','Lucas','Júlia','José']
    return lista_cli

def cadastrar_cliente(id_cli,nome_cli,email_cli):
    # id_cli = id_cli 
    # nome_cli = nome_cli 
    # email_cli = email_cli

    cli = {'id': {id_cli}, 'nome':{nome_cli}, 'email':{email_cli}}
    print(cli)


print(cadastrar_cliente(3,'caue','caue'))

