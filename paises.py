import json

import requests
#________________________________________________
url_all = "https://restcountries.com/v3.1/all"
url_nome = "https://restcountries.com/v3.1/name"
#________________________________________________

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text

    except Exception as e:
        print("Erro na requisição em: ", url)
#________________________________________________

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print("Erro no parsing")
#________________________________________________

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais["name"]["common"])
#________________________________________________

def contagem_de_paises(lista_de_paises):
    return len(lista_de_paises)
#________________________________________________

def mostrar_populacao(nome_do_pais):
    resposta = requisicao("{}/{}".format(url_nome, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            for pais in lista_de_paises:
                print("{}: {}".format(pais['name']['common'], pais['population']))
    else:
        print("País não encontrado.")
#________________________________________________

def mostrar_moedas(nome_do_pais):
    resposta = requisicao("{}/{}".format(url_nome, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            for pais in lista_de_paises:
                print("Moedas do", pais['name']['common'], ":")
                moedas = pais['currencies']
                for codigo, info in moedas.items():
                    print("{} - {}".format(info['name'], codigo))
    else:
        print("País não encontrado.")
#________________________________________________

if __name__ == "__main__":
    mostrar_moedas("Brazil")