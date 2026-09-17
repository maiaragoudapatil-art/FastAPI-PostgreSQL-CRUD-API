from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:Nihonviji%40553@localhost:5432/students"
)

try:
    conn = engine.connect()
    print("Connected Successfully!")
    conn.close()
except Exception as e:
    print(e)