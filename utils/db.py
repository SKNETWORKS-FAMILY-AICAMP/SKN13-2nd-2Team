
import pymysql


def get_connection():
    return pymysql.connect(
        host="database-1.cqv4s0komaez.us-east-1.rds.amazonaws.com",
        user="admin",
        password="13221322",
        db="brp",        # ← 사용하는 DB명 확인 필요!
        port=3306,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
