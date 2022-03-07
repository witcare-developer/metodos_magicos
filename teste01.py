class Model:
    def __getattr__(self, name):
        def funcao():
            print("O método chamado é: {}".format(name) )
        return funcao()

    def __setattr__(self, name, value):
        def funcao():
            print("O método chamado é: {} e o valor: {}".format(name, value) )
        return funcao()

    def setData(self, nome):
        setattr(self, "set_{}".format(nome[0]), nome[1] )

if __name__ == '__main__':
    model = Model()
    data = ['nome_cliente', 42.0]
    print(model.setData(data))