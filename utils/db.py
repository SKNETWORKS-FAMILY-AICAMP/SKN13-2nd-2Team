
from sqlalchemy import create_engine

def get_engine():
    user = "admin"
    password = "13221322"
    host = "database-1.cqv4s0komaez.us-east-1.rds.amazonaws.com"
    port = 3306
    db = "brp"

    db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4"
    engine = create_engine(db_url)
    return engine


# def get_connection():
#     return pymysql.connect(
#         host="192.168.0.40",
#         user="SKN13_2nd_2Team",
#         password="1111",
#         db="brp",        # ← 사용하는 DB명 확인 필요!
#         port=3306,
#         charset="utf8mb4",
#         cursorclass=pymysql.cursors.DictCursor
#     )