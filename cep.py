# script retorna os dados sobre um CEP digitado pelo usuário utilizando a biblioteca requests

import requests

cep = input("Digite aqui o CEP para consulta: ")

resp = requests.get(f"http://cep.republicavirtual.com.br/web_cep.php?cep={cep}&formato=json").json()

print(f"Cidade: {resp["cidade"]} \nBairro: {resp["bairro"]} \nLogradouro: {resp["logradouro"]}")

