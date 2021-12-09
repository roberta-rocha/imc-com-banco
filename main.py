import sqlite3

def inserirCalculoEfetuado(valor):
    conn = sqlite3.connect('imc.db')
    cursor = conn.cursor()
    valor = round(valor,2)
    cursor.execute("INSERT INTO IMC(imc) VALUES(?)",(valor,))
    conn.commit()
    conn.close()
    print ("O calculo do IMC ",valor," inserido com sucesso")

def imprimirValores():
    conn = sqlite3.connect('imc.db')
    cursor = conn.cursor()
    cursor.execute("""select * from imc;""")
    for i in cursor.fetchall():
        print(i)
    conn.close()


def imc(peso, altura):
    return (peso / altura ** 2) * 10000


if __name__ == '__main__':
    opcao = input("Digite 1 se quer calcular o IMC ou 2 para ver os IMCs armazenados\n")
    if opcao == "1":
        peso = float(input("Digite o peso\n"))
        altura = float(input("Digite a altura\n"))
        calculado = imc(peso, altura)
        print("O imc é : %.2f" % calculado)
        guardar = input("Gostaria de guardar no banco de dados (S ou N)\n")
        if guardar == "S":
            inserirCalculoEfetuado(calculado)
    else:
        imprimirValores()
