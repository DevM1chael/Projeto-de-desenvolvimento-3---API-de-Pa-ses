from decimal import InvalidOperation
import json
import sys

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

def contagem_de_paises():
    resposta = requisicao(url_all)
    if resposta:
        lista_de_paises = parsing(resposta)
        return len(lista_de_paises)
#________________________________________________

def mostrar_populacao(nome_do_pais):
    resposta = requisicao("{}/{}".format(url_nome, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            for pais in lista_de_paises:
                print("{}: {} habitantes".format(pais['name']['common'], pais['population']))
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

def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("Erro: Você precisa informar o nome do país.")
        return None


if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Bem vindo ao sistema de países ##")
        print("Uso: python paises.py <acao> <nome do país>")
        print("Ações disponíveis: contagem, moeda, populacao")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
           numero_de_listar_paises = contagem_de_paises()
           print("Existem {} países no mundo todo.".format(numero_de_paises))
        elif argumento1 == "moeda":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("Argumento inválido")