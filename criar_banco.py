import sqlite3

def iniciaBanco():
    conn = sqlite3.connect('imc.db')
    # definindo um cursor
    cursor = conn.cursor()

    # criando a tabela (schema)
    cursor.execute("""
    CREATE TABLE imc (
            id INTEGER PRIMARY KEY,
            imc REAL NOT NULL
    );
    """)

    print('Tabela criada com sucesso.')
    # desconectando...
    conn.close()

iniciaBanco()