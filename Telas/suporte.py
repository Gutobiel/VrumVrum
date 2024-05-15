# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import sqlite3

# app = FastAPI()

# # Configurando o banco de dados SQLite
# def init_sqlite_db():
#     conn = sqlite3.connect('database.db')
#     conn.execute('CREATE TABLE IF NOT EXISTS suporte (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, regiao TEXT, mensagem TEXT)')
#     conn.close()

# init_sqlite_db()

# class Suporte(BaseModel):
#     nome: str
#     email: str
#     regiao: str
#     mensagem: str

# @app.post("/api/suporte")
# async def add_message(suporte: Suporte):
#     try:
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO suporte (nome, email, regiao, mensagem) VALUES (?, ?, ?, ?)", 
#                        (suporte.nome, suporte.email, suporte.regiao, suporte.mensagem))
#         conn.commit()
#         conn.close()
#         return {"success": True, "message": "Mensagem enviada com sucesso!"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
