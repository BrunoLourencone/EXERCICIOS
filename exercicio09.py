import json
import os 
data = "funcionarios.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]

funcionarios = carregar_dados()
for funcionario in funcionarios:
    print("_"*40)
    print(f"nome do funcionario: {funcionario["nome"]}")
    print(f"o salario dele é: {funcionario["salario"]}")
          
