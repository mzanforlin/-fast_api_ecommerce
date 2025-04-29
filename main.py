from fastapi import FastAPI
from vendas import vendas
from user import user

app = FastAPI()


@app.get("/")
def home():
    return 'minha api esta no ar'

@app.get("/qtd_produtos")
def qtd_produtos():
    return {"Total de Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:    
        return vendas[id_venda]
    else:
        return {"Erro": "Id de venda não encontrado"}
    
@app.get('/user/{user_id}')
def pegar_user(user_id: int):
    if user_id in user:
        return user[user_id]
    else:
        return {"Erro"}
    