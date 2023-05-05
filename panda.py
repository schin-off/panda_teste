import pandas as pd

calendario = {}

def adicionar(tarefa, data):
    calendario.update({tarefa: data})

tarefa_var = input("Qual tarefa deseja adicionar?")
data_var = input(f"Em que data será '{tarefa_var}'?")

adicionar(tarefa_var, data_var)

x = pd.DataFrame(calendario, index=["Data"])

print(x)