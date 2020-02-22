def novo_decorador(func):
    def funcao_interna():
        print("Código executado antes da função!")
        func()
        print("Código executado depois da função!")
    return funcao_interna

def precisa_decorar():
    print("Essa funcao precisa de decorador!")

precisa_decorar = novo_decorador(precisa_decorar)

@novo_decorador
def precisa_decorar():
    print("Essa função precisa de decorador!")
print(precisa_decorar())
