# ==============================================================================
# UNIDADE CURRICULAR: PROJETO APLICADO I
# EMPRESA PARCEIRA: SCHULZ S.A.
# SCRIPT PYTHON PARA CONECTAR AO SQLITE E EXECUTAR O ARQUIVO 03_banco.sql
# Prof. MSc. Hugo Menezes Barra | Prof. Rodrigo Losina
# Equipe: Marx Braga Camilo, Gladson Goulart, Carla Tayna, Yorman Hernandez
# ==============================================================================

import sqlite3

NOME_BANCO = "schulz_calibracao.db"
ARQUIVO_SQL = "03_banco.sql"

conexao = None
try:
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    with open(ARQUIVO_SQL, "r", encoding="utf-8") as f:
        script_sql = f.read()

    cursor.executescript(script_sql)
    conexao.commit()

    # Confirma quais tabelas foram criadas no banco
    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'")
    tabelas = [linha[0] for linha in cursor.fetchall()]

    print("=" * 60)
    print(f"SUCESSO: Banco de dados '{NOME_BANCO}' gerado com sucesso!")
    print(f"Tabelas criadas: {', '.join(tabelas)}")
    print("=" * 60)
except Exception as e:
    print(f"ERRO ao executar o script DDL: {e}")
finally:
    if conexao is not None:
        conexao.close()
