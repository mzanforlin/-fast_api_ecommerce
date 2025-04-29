import sqlite3

## Criação do meu banco de dados fast-api-ecommerce.db que vai estar no meu files
def conectar():
    return sqlite3.connect('fast-api-ecommerce.db')

## Criar tabelas

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    #criar as tabelas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            data_registro TEXT NOT NULL,
            sexo TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            preco INTEGER NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    criar_tabelas()