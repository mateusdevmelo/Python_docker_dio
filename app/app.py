from flask import Flask, render_template
import pymysql
import random
import socket

app = Flask(__name__)

# Configurações do banco de dados
DB_HOST = "54.234.153.24"
DB_USER = "root"
DB_PASSWORD = "Senha123"
DB_NAME = "meubanco"


@app.route("/")
def index():
    try:
        # Conectar ao banco de dados
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        with connection.cursor() as cursor:
            # Gerar valores randômicos
            valor_rand1 = random.randint(1, 999)
            valor_rand2 = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
            host_name = socket.gethostname()

            # Inserir dados na tabela
            query = """
            INSERT INTO dados (AlunoID, Nome, Sobrenome, Endereco, Cidade, Host)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (valor_rand1, valor_rand2, valor_rand2, valor_rand2, valor_rand2, host_name))
            connection.commit()

        return render_template("index.html", message="Novo registro criado com sucesso!")

    except Exception as e:
        return render_template("index.html", message=f"Erro: {str(e)}")

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4500)
