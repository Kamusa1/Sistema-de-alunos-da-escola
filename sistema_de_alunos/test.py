import os
from dotenv import load_dotenv
import libsql_client
import asyncio

load_dotenv()

url = os.getenv("TURSO_URL").strip()
token = os.getenv("TURSO_TOKEN").strip()
print(f"Conectando {url}")
async def main():
    if not url or not token:
        print("Erro: URL ou Token não encontrados no .env")
        return
    try:
        async with libsql_client.create_client(url = url, auth_token = token) as client:
            res = await client.execute("SELECT 'Conexão Segura!' as status")
            print(res.rows[0][0])
    except Exception as e:
        print(f"Erro ao conectar: {e}")
if __name__ == "__main__":
    asyncio.run(main())