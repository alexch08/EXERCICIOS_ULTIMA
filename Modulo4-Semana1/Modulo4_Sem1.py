import requests
def get_modelos(id_marca):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marca}/modelos'
    headers = {'user-agent': 'codigo_modelo'} # necessário criar header para fazer a requisição adequada na api
    resposta = requests.get(url,headers=headers)
    resposta_json = resposta.json()
    return resposta_json['modelos']

class Lista_fipe():

    def __init__(self, id_marca):
        self.id_marca = id_marca
        self.indice = 0
        self.modelos = []
    
    def __iter__(self):
        self.modelos = get_modelos(self.id_marca)
        return self

    def __next__(self):
        if self.indice >= len(self.modelos):
            print("Parar iteração")
            raise StopIteration 
        modelo = self.modelos[self.indice]
        self.indice += 1
        return modelo 


id_marca = 22 # pode ser qualquer id
lista_fipe = Lista_fipe(id_marca)
for veiculo in lista_fipe:
    print(f'Nome: {veiculo["nome"]}')
    print(f'ID: {veiculo["codigo"]}')

