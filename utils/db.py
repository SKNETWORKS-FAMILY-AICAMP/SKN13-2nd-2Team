
import pymysql

def get_connection():
    return pymysql.connect(
        host="192.168.0.40",
        user="SKN13_2nd_2Team",
        password="1111",  # 실제 비밀번호로 대체해!
        db="brp",
        port=3306,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor  # dict 형태로 row 받기
    )